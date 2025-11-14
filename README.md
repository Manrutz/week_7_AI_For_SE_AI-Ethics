🌍⚖️ AI Ethics Assignment — Designing Responsible and Fair AI Systems
Student: Remmy Kipruto Tumo
Theme: Ethical, Transparent & Accountable AI Development
📌 Project Overview

This repository contains the full submission for the AI Ethics Assignment under the theme:
“Designing Responsible and Fair AI Systems.”

The project explores ethical challenges in AI development, focusing on:

Algorithmic Bias

Fairness Metrics

Transparency vs Explainability

Responsible Data Use

AI Governance

Ethical Deployment in Sensitive Domains (e.g., Healthcare, Policing)

The assignment is divided into four parts:

Theoretical Questions

Case Study Analysis

Practical Fairness Audit (COMPAS Dataset)

Ethical Reflection

Bonus Task: Healthcare AI Policy Proposal

🗂️ Repository Structure
AI-Ethics-Project/
│
├── notebooks/
│   └── fairness_audit.ipynb          # AIF360-based COMPAS fairness audit
│
├── src/
│   └── fairness_audit.py             # Script version of the notebook
│
├── reports/
│   ├── Part1_Theory.pdf              # Short-answer responses
│   ├── Part2_Case_Study.pdf          # Hiring & Policing case analysis
│   ├── Part3_Compas_Audit_Report.pdf # 300-word fairness audit summary
│   └── Bonus_Healthcare_Policy.pdf   # 1-page policy proposal
│
├── data/
│   └── compas.csv                    # Dataset (ProPublica)
│
└── README.md                         # You are here

🎯 Learning Objectives

By completing this project, I have gained competencies in:

✔ Ethical Principles

Transparency

Fairness

Autonomy

Justice

Non-maleficence

Sustainability

✔ Technical Fairness Auditing

Using AIF360 to detect racial bias

Measuring fairness metrics:

Statistical Parity Difference

Equal Opportunity Difference

Disparate Impact

Average Odds Difference

False Positive Rate Disparity

✔ Bias Mitigation Techniques

Reweighing (pre-processing)

Feature masking

Balanced sampling

Human-in-the-loop design

✔ Policy & Governance

GDPR impact

Healthcare AI guidelines

AI regulatory best practices

🧠 Part 1: Theoretical Understanding

Covers short-answer responses on:

Algorithmic Bias

Transparency vs Explainability

GDPR and AI

Matching ethical principles (Justice, Autonomy, Sustainability, Non-maleficence)

These answers lay the ethical foundation for the technical work.

🔍 Part 2: Case Studies
Case 1: Amazon’s Biased Hiring Tool

Identifies gender bias sources

Proposes mitigation (data balancing, fairness constraints, audits)

Recommends fairness evaluation metrics

Case 2: Facial Recognition in Policing

Ethical risks: wrongful arrests, privacy violations

Responsible deployment policies

Human oversight & accountability

🧪 Part 3: Practical Audit — COMPAS Dataset

A full fairness audit implemented using:

IBM AIF360,

Pandas,

Matplotlib,

Scikit-learn.

Includes:

Dataset loading

Baseline model

Fairness metrics

Bias visualization (e.g., False Positive Rate differences)

Reweighing mitigation

300-word technical report

📝 Part 4: Ethical Reflection

A 300-word reflection on:

How to build ethically aligned AI projects

Data responsibility

Fairness audits

Transparency

Human oversight

Alignment to EU Trustworthy AI Guidelines

🏥 Bonus Task: Healthcare AI Policy Proposal

A one-page professional guideline covering:

Patient consent

Bias mitigation

Transparency & explainability

Accountability in medical AI systems

A downloadable PDF version is included in the /reports folder.

⚙️ How to Run the Fairness Audit
1. Install dependencies
pip install aif360 pandas scikit-learn matplotlib seaborn

2. Launch the notebook
jupyter notebook notebooks/fairness_audit.ipynb

3. Run the audit

Loads COMPAS dataset

Computes fairness metrics

Visualizes bias

Runs mitigation algorithms

🧑‍⚖️ Ethical & Legal Frameworks Referenced

EU Guidelines for Trustworthy AI

GDPR Articles 13–22

ACM Code of Ethics

ProPublica COMPAS investigation

🧑‍🎓 Student Credits

Developed by:

Remmy Kipruto Tumo

AI Ethics & Responsible AI Researcher in Training

📄 License

This project is for academic and educational use only.
Fairness audit results must not be used for real-world judiciary or policing decisions.
