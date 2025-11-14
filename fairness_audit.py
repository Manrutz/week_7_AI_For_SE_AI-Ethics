import pandas as pd
import numpy as np
from aif360.datasets import StandardDataset
from aif360.metrics import ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_data(path="compas.csv"):
    df = pd.read_csv(path)
    dataset = StandardDataset(
        df,
        label_name="two_year_recid",
        favorable_label=0,
        protected_attribute_names=["race"],
        privileged_classes=[["Caucasian"]],
        features_to_drop=[]
    )
    return dataset

def run_audit():
    dataset = load_data()
    
    # Split
    train, test = dataset.split([0.7], shuffle=True)
    
    X_train, y_train = train.features, train.labels.ravel()
    X_test, y_test = test.features, test.labels.ravel()
    
    # Baseline model
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # Wrap predictions
    test_pred = test.copy()
    test_pred.labels = y_pred.reshape(-1,1)

    metric = ClassificationMetric(
        test, test_pred,
        privileged_groups=[{"race": "Caucasian"}],
        unprivileged_groups=[{"race": "African-American"}]
    )
    
    print("\n=== BASELINE MODEL ===")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Statistical Parity Difference:", metric.statistical_parity_difference())
    print("Disparate Impact:", metric.disparate_impact())
    print("Equal Opportunity Difference:", metric.equal_opportunity_difference())

    # Reweighing mitigation
    rw = Reweighing(
        privileged_groups=[{"race": "Caucasian"}],
        unprivileged_groups=[{"race": "African-American"}]
    )
    rw.fit(train)
    train_rw = rw.transform(train)

    clf2 = LogisticRegression(max_iter=1000)
    clf2.fit(train_rw.features, train_rw.labels.ravel(), sample_weight=train_rw.instance_weights)

    y_pred_rw = clf2.predict(X_test)
    test_pred_rw = test.copy()
    test_pred_rw.labels = y_pred_rw.reshape(-1,1)

    metric_rw = ClassificationMetric(
        test, test_pred_rw,
        privileged_groups=[{"race": "Caucasian"}],
        unprivileged_groups=[{"race": "African-American"}]
    )
    
    print("\n=== AFTER REWEIGHING MITIGATION ===")
    print("Statistical Parity Difference:", metric_rw.statistical_parity_difference())
    print("Disparate Impact:", metric_rw.disparate_impact())
    print("Equal Opportunity Difference:", metric_rw.equal_opportunity_difference())

if __name__ == "__main__":
    run_audit()
