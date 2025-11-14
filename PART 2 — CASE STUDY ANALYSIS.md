Case 1: Biased Hiring Tool
Scenario: Amazon’s AI recruiting tool penalized female candidates.
1. Identify the Source of Bias

The bias came from historical training data and feature encoding:

a) Biased Training Data

The model was trained on 10 years of CVs where men dominated technical roles.

AI learned that male-associated patterns = “good candidates”.

Words like “women’s chess club” or “women’s coding bootcamp” were downgraded.

b) Proxy Features & Model Design

Certain terms correlated with gender were learned as “undesirable”.

The model was not designed to detect or mitigate gender correlations.

No fairness constraints were embedded in the architecture.

c) Lack of Bias Audits

System wasn't monitored for adverse impact across gender groups.

No human-in-the-loop oversight during automated scoring.

2. Propose Three Fixes to Make the Tool Fairer
Fix 1: Balanced & Representative Training Data

Rebuild dataset with gender-balanced examples.

Remove historical bias by re-sampling or reweighing training examples.

Use debiasing preprocessing (e.g., AIF360 Reweighing).

Fix 2: Remove or Mask Gender-Proxies

Remove features like:

Gender-coded words (“women’s”)

Demographic attributes

Gender-correlated activities

Use adversarial debiasing to suppress gender signals.

Fix 3: Add Fairness Constraints in the Model

Enforce Equal Opportunity or Demographic Parity thresholds.

Use Explainability tools (SHAP/LIME) to inspect feature influence.

Include a human reviewer to verify final decisions.

Optional Fixes:

Conduct regular fairness audits

Introduce transparent scoring rules

Maintain a model card documenting risks

3. Suggest Metrics to Evaluate Fairness After Correction

Use group fairness and individual fairness metrics:

Group Fairness Metrics

Disparate Impact Ratio (DIR)

Should be between 0.8 and 1.25.

Statistical Parity Difference

Equal Opportunity Difference (TPR parity for men vs women)

Average Odds Difference

Performance Metrics

Overall accuracy, precision, recall

Per-gender accuracy (to ensure equal treatment)

Explainability Metrics

SHAP feature parity across genders

Transparency on what drives decisions

Case 2: Facial Recognition in Policing
Scenario: Misidentifies minorities at higher rates.
1. Ethical Risks
a) Wrongful Arrests

Higher false positives for Black and minority individuals.

Leads to unjust detentions and legal consequences.

b) Privacy Violations

Surveillance without consent.

Tracking individuals in public spaces.

Violates GDPR’s principles of proportionality and necessity.

c) Discrimination & Social Harm

Reinforces racial profiling.

Reduces public trust in law enforcement.

Disproportionately impacts marginalized communities.

d) Accountability Gap

Black-box AI decisions → difficult to challenge or appeal.

Lack of transparency in vendor algorithms.

e) Inaccuracy Under Real-World Conditions

Poor performance under low light, occlusions, different angles.

2. Recommend Policies for Responsible Deployment
Policy 1: Mandatory Accuracy & Fairness Benchmarks

Require minimum thresholds for all demographic groups.

Independent fairness audits before deployment.

Public model cards and performance reports.

Policy 2: Human-in-the-Loop Enforcement

AI should never be the sole basis for arrest.

Officers must verify matches manually.

AI should provide confidence scores, not binary outputs.

Policy 3: Strict Data Governance & Consent

Limit use to specific, high-necessity scenarios.

Limit retention of images/data.

Require public notice and opt-out mechanisms.

Policy 4: Transparency & Accountability

Publish algorithms’ evaluation reports.

Provide appeal mechanisms for misidentification victims.

Third-party oversight boards to monitor use.

Policy 5: Regular Retraining & Monitoring

Update datasets periodically.

Re-evaluate fairness metrics quarterly.

Ban usage if demographic disparity exceeds set thresholds.