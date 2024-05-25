import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import re
import time
from datetime import datetime
import pytz  # Import pytz for timezone handling


def run_selenium_script(email, password):
    # Initialize the WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the webpage
        driver.get("https://resy.com/cities/new-york-ny/venues/westville-east")
        
        # Wait for and select the party size dropdown
        select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'party_size')))
        select = Select(select_element)
        select.select_by_value('4')
        
        # Wait for and click the date picker button
        button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'DropdownGroup__selector--date')))
        button_element.click()
        selected_date = []
        
        # Wait for the date picker to be visible and select a specific date
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
                        break
                    
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", date_element)
            except TimeoutException:
                pass
        
        # Wait for and select the time dropdown
        select_element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'time')))
        select1 = Select(select_element1)
        
        # Get all available time options to check the correct format
        available_times = [option.get_attribute('value') for option in select1.options]
        
        # Check if the desired times are in the available options
        if '1900' in available_times and '1930' in available_times and '2000' in available_times and '2030' in available_times and '2100' in available_times:
            time_values = ['1900', '1915', '1930', '1945', '2000', '2015', '2030', '2045', '2100']
            time_value_selects = ['1900', '1930', '2000', '2030', '2100']
            for time_value_select in time_value_selects:
                for time_value in time_values:
                    select1.select_by_value(time_value_select)
                    # Create dynamic XPath for the dialog button
                    button_element_xpath = f'//*[@id="rgs://resy/75127/2392369/2/2024-05-{selected_date[0]}/2024-05-{selected_date[0]}/{time_value[:2]}:{time_value[2:]}:00/4/Patio"]'
                    try:
                        button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_element_xpath)))
                        driver.execute_script("arguments[0].scrollIntoView(true);", button_element)
                        button_element.click()
                        
                        # Debugging step: Check if dialog box appeared
                        iframe = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='Resy - Book Now']"))
                        )
                        driver.switch_to.frame(iframe)
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "page-wrapper")))
                        
                        # Wait for the dialog box to appear and the reserve button to be clickable
                        reserve_button_xpath = '/html/body/div[1]/div/summary-page/div/div[2]/div[4]/div[1]/button'
                        reserve_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, reserve_button_xpath)))
                        driver.execute_script("arguments[0].scrollIntoView(true);", reserve_button)
                        
                        try:
                            driver.execute_script("arguments[0].click();", reserve_button)
                        except ElementClickInterceptedException:
                            driver.execute_script("arguments[0].click();", reserve_button)
                        
                        # Fill in the login form
                        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
                        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
                        email_input.send_keys(email)
                        password_input.send_keys(password)
                        
                        # Click continue button with retry mechanism
                        for _ in range(3):
                            try:
                                continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div/resy-auth/div/div[2]/div[2]/div/form/div/button')))
                                continue_button.click()
                                done_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div/confirmation-page/div/div[2]/div[3]/button')))
                                done_button.click()
                                st.success("Congratulations, seat reserved!")
                                return True
                            except ElementClickInterceptedException:
                                pass
                        
                        break  # Exit the loop if reservation attempt is successful

                        
                    except TimeoutException:
                        pass
                    except ElementClickInterceptedException:
                        pass

        else:
            st.error("Desired time values not found in available options.")
        
    finally:
        # Close the WebDriver
        driver.quit()

    return False


def main():
    st.title("Reservation Script")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Start Reservation"):
        if email and password:
            st.info("Starting reservation process...")
            # while True:
            #     est = pytz.timezone('US/Eastern')
            #     current_time = datetime.now(est)
            #     if current_time.hour == 9 and (current_time.minute == 0 or current_time.minute == 30):
            #         if run_selenium_script(email, password):
            #             break
            #     time.sleep(60)  # Check every minute
            run_selenium_script(email, password)
        else:
            st.error("Please enter both email and password")


if __name__ == "__main__":
    main()
