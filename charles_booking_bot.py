import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, WebDriverException
import re
import time

def run_selenium_script(email, password):
    # Create a placeholder for the log messages
    log_placeholder = st.empty()

    def log_message(message):
        # Update the placeholder with a new message
        log_placeholder.markdown(message)

    # Initialize the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)


    try:
        log_message(":earth_americas: Navigating to the webpage...")
        driver.get("https://resy.com/cities/new-york-ny/venues/westville-east")
        driver.implicitly_wait(5)
        
        log_message(":busts_in_silhouette: Selecting party size...")
        select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'party_size')))
        select = Select(select_element)
        select.select_by_value('4')
        
        log_message(":calendar: Clicking date picker button...")
        button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'DropdownGroup__selector--date')))
        button_element.click()
        selected_date = []
        
        log_message(":date: Selecting specific date...")
        for i in range(1, 6):  # Assuming the date picker has up to 6 rows
            try:
                date_xpath = f"//*[@id='DayPicker']/div[3]/div/div/table/tbody/tr[{i}]/td[6]/button"
                date_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", date_element)
                try:
                    date_string = date_element.get_attribute('aria-label')
                    match = re.search(r'(\d{1,2})(?=, \d{4})', date_string)

                    if match:
                        selected_date.append(match.group(1))
                        date_element.click()
                        log_message(f":calendar_spiral: Selected date: **{match.group(1)}**")
                        break
                    
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", date_element)
            except TimeoutException:
                pass
        
        log_message(":clock1: Selecting time...")
        select_element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'time')))
        select1 = Select(select_element1)
        
        available_times = [option.get_attribute('value') for option in select1.options]
        
        if '1900' in available_times and '1930' in available_times and '2000' in available_times and '2030' in available_times and '2100' in available_times:
            time_values = ['1900', '1915', '1930', '1945', '2000', '2015', '2030', '2045', '2100']
            time_value_selects = ['1900', '1930', '2000', '2030', '2100']
            for time_value_select in time_value_selects:
                for time_value in time_values:
                    select1.select_by_value(time_value_select)
                    button_element_xpath = f'//*[@id="rgs://resy/75127/2392369/2/2024-05-{selected_date[0]}/2024-05-{selected_date[0]}/{time_value[:2]}:{time_value[2:]}:00/4/Patio"]'
                    try:
                        button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_element_xpath)))
                        driver.execute_script("arguments[0].scrollIntoView(true);", button_element)
                        button_element.click()
                        
                        log_message(":arrow_forward: Clicking book now button...")
                        iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='Resy - Book Now']")))
                        driver.switch_to.frame(iframe)
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "page-wrapper")))
                        
                        reserve_button_xpath = '/html/body/div[1]/div/summary-page/div/div[2]/div[4]/div[1]/button'
                        reserve_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, reserve_button_xpath)))
                        driver.execute_script("arguments[0].scrollIntoView(true);", reserve_button)
                        
                        try:
                            driver.execute_script("arguments[0].click();", reserve_button)
                        except ElementClickInterceptedException:
                            driver.execute_script("arguments[0].click();", reserve_button)
                        
                        log_message(":lock: Filling in the login form...")
                        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
                        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
                        email_input.send_keys(email)
                        password_input.send_keys(password)
                        
                        log_message(":arrow_forward: Clicking continue button...")
                        for _ in range(3):
                            try:
                                continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div/resy-auth/div/div[2]/div[2]/div/form/div/button')))
                                continue_button.click()
                                done_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div/confirmation-page/div/div[2]/div[3]/button')))
                                done_button.click()
                                st.success(":tada: Congratulations, seat reserved!")
                                return True
                            except ElementClickInterceptedException:
                                pass
                        
                        break

                    except TimeoutException:
                        pass
                    except ElementClickInterceptedException:
                        pass

        else:
            log_message(":warning: Desired time values not found in available options.")
        
    except WebDriverException as e:
        log_message(f":exclamation: An error occurred: **{str(e).split('n')[0]}**. Retrying...")
    finally:
        driver.quit()

    return False


def main():
    st.title("Reservation Script")

    # Initialize the state variables if they do not exist
    if 'running' not in st.session_state:
        st.session_state.running = False

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Start Reservation"):
        if email and password:
            st.session_state.running = True  # Set the running flag to True
            st.info("reservation is in process...")
            retry_limit = 3
            retry_count = 0
            success = False
            while retry_count < retry_limit and not success:
                if not st.session_state.running:  # Check if the stop button has been clicked
                    st.warning("Reservation process stopped.")
                    break
                try:
                    success = run_selenium_script(email, password)
                    if success:
                        break
                except WebDriverException:
                    retry_count += 1
                    time.sleep(10)  # Wait for 10 seconds before retrying
            if not success and st.session_state.running:
                st.error("Failed to make a reservation after multiple attempts.")
            st.session_state.running = False  # Reset the running flag
        else:
            st.error("Please enter both email and password")

    if st.button("Stop Reservation"):
        st.session_state.running = False  # Set the running flag to False


if __name__ == "__main__":
    main()
