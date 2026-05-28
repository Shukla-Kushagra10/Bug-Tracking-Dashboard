import sys
import os
import pandas as pd
import requests
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db_manager import engine

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL", "")

def get_bug_data():
    """Fetches combined bug and test data into a Pandas DataFrame."""
    query = """
        SELECT b.bug_id, b.severity, b.status, b.developer, b.sprint, b.resolution_time_days, 
               t.module, t.run_timestamp 
        FROM bugs b
        JOIN test_runs t ON b.test_case_id = t.test_case_id
    """
    return pd.read_sql(query, engine)

def generate_weekly_report():
    """Python script generates weekly PDF/Excel reports of bug metrics."""
    df = get_bug_data()
    if df.empty:
        print("No bug data available for report.")
        return
    
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    report_path = os.path.join(os.path.dirname(__file__), f"Bug_Report_{datetime.now().strftime('%Y%m%d')}.xlsx")
    
    # Export options: CSV/Excel for bug data [cite: 11]
    df.to_excel(report_path, index=False)
    print(f"📊 Weekly Report generated: {report_path}")

def send_slack_alert(message):
    """Sends webhook alerts."""
    if SLACK_WEBHOOK:
        try:
            requests.post(SLACK_WEBHOOK, json={"text": message})
        except Exception as e:
            print(f"Failed to send alert: {e}")
    else:
        print(f"Alert Generated (No Webhook Configured): {message}")

if __name__ == "__main__":
    generate_weekly_report()