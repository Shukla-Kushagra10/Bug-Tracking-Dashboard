# 🐞 Bug Tracking & Reporting Dashboard

[cite_start]Building an end-to-end QA Automation and Bug Tracking pipeline demonstrates a deep understanding of the entire software development life cycle, not just test execution[cite: 16, 63]. [cite_start]This project is a complete, modular, and production-ready architecture[cite: 17]. [cite_start]It runs Selenium tests, automatically logs failures to a SQL database, and visualizes defect metrics via Plotly Dash[cite: 82]. 

---

## 🚀 Key Features

* [cite_start]**Automation Layer:** Uses Python and Selenium to run automated test cases like login, checkout, and API calls[cite: 1, 34]. 
* [cite_start]**Detailed Captures:** Records test results including Test Case ID, Status (Pass/Fail), Error Message, and Timestamp[cite: 2, 35].
* [cite_start]**Automated Bug Logging:** Stores failed test case details automatically into a SQL database[cite: 3, 36].
* [cite_start]**Comprehensive Database Tracking:** The bug table logs BugID, TestCaseID, Severity, Priority, Timestamp, and Status[cite: 4, 37].
* [cite_start]**Data Processing:** Uses Python and Pandas to aggregate bug data daily or weekly[cite: 5, 38]. 
* [cite_start]**Interactive Dashboard Visualization:** Built using Plotly Dash, featuring a pie chart for bug severity, a line graph for defect trends, a bar chart for average resolution time, and a table comparing open vs closed bugs[cite: 6, 7, 39, 40].
* [cite_start]**Advanced Filters:** Filter dashboard metrics by module, severity, sprint, or developer[cite: 11, 44].
* [cite_start]**Reporting & Alerts:** A Python script generates weekly PDF or Excel reports for bug metrics[cite: 9, 43]. 
* [cite_start]**Automated Notifications:** Sends automated Slack or email notifications for critical bugs[cite: 10, 44].
* [cite_start]**CI/CD Integration:** Integrated with GitHub Actions so that test runs trigger automatically on code push, updating the bug database seamlessly[cite: 7, 8, 41, 42].

---

## 🛠️ Technology Stack

* **Language:** Python
* [cite_start]**Testing:** Selenium [cite: 1, 34]
* [cite_start]**Database:** SQLAlchemy (Database-agnostic, supporting PostgreSQL, MySQL, and SQLite) [cite: 18, 19, 72]
* [cite_start]**Data Analysis:** Pandas [cite: 5, 38]
* [cite_start]**Visualization:** Plotly Dash [cite: 6, 39]
* [cite_start]**CI/CD Pipeline:** GitHub Actions [cite: 14, 41]

---

## 📁 Project Structure

* [cite_start]`database/schema.sql` - Contains the SQL schema designed for PostgreSQL and MySQL[cite: 20].
* [cite_start]`src/db_manager.py` - Handles database connections and inserts using SQLAlchemy[cite: 21].
* [cite_start]`src/test_runner.py` - A Selenium script that runs tests, captures failures, and automatically logs them to the database[cite: 22].
* [cite_start]`src/data_processor.py` - Handles Pandas aggregations, Excel report generation, and Slack alerting[cite: 23].
* [cite_start]`src/app.py` - The complete Plotly Dash application containing interactive filters and requested graphs[cite: 24].
* [cite_start]`.github/workflows/ci-cd.yml` - The GitHub Actions pipeline that triggers Selenium tests automatically on a push to main[cite: 25, 26].
* [cite_start]`README.md` - Documentation explaining project setup, execution, and features[cite: 14, 83, 105].

---

## ⚙️ Setup Instructions

**1. Clone the repository**
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd bug-tracking-dashboard
