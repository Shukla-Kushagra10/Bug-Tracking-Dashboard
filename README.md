# 🐞 Bug Tracking & Reporting Dashboard

An end-to-end QA Automation and Defect Tracking pipeline that bridges the gap between automated test execution and real-time project management metrics. This system runs automated Selenium test suites, intercepts execution failures, logs granular bug details to a relational SQL database, aggregates analytical data via Pandas, and visualizes live insights through an interactive Plotly Dash dashboard.

---

## 🏗️ System Workflow & Architecture

To help developers, QA managers, and stakeholders understand the application lifecycle, the pipeline follows a structured, automated workflow:

```text
[ Code Push / Schedule ] ──> 1. GitHub Actions (CI/CD)
                                     │
                                     ▼
                        2. Selenium Automation Layer
                                     │
                 ┌───────────────────┴───────────────────┐
                 ▼ (If Test Passes)                      ▼ (If Test Fails)
          [ Log Test Run ]                       [ Log Test Run & Details ]
                 │                                       │
                 │                                       ▼
                 │                             3. SQL Database (SQLAlchemy)
                 │                                       │
                 ▼                                       ├────────────────────────┐
       [ Complete Pipeline ]                             ▼                        ▼
                                                 [ Live Dashboard ]      4. Slack Webhook Alert
                                                    (Plotly Dash)         (Critical Failures)
                                                         │
                                                         ▼
                                               5. Reporting Engine
                                                (Pandas Excel/CSV)
