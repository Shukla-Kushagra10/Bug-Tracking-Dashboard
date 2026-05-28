import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from db.db_manager import log_test_result, log_bug
from reports.data_processor import send_slack_alert

def setup_driver():
    options = Options()
    options.add_argument('--headless') # Crucial for CI/CD environments
    return webdriver.Chrome(options=options)

def test_checkout_flow():
    test_id = "TC-102"
    module = "Checkout"
    driver = setup_driver()
    
    try:
        driver.get("https://example.com")
        # Simulating a failure by searching for an element that doesn't exist
        driver.find_element(By.ID, "checkout-button").click()
        
        log_test_result(test_id, module, "Pass")
        print(f"✅ {test_id} Passed")
        
    except Exception as e:
        error_msg = str(e)[:200]
        # Store failed test case details automatically in SQL [cite: 3]
        log_test_result(test_id, module, "Fail", error_msg)
        log_bug(test_id, severity="High", priority="P1")
        
        # Send automated Slack notifications for critical bugs [cite: 10]
        send_slack_alert(f"🚨 Critical Bug Logged! {test_id} failed in {module}. Error: {error_msg}")
        print(f"❌ {test_id} Failed - Bug Logged")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_checkout_flow()