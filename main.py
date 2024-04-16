import os
import random
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from auto_metamask_amit import *
from random import randint

if __name__ == '__main__':
    while True:
        try:
            while True:
                metamask_path = downloadMetamask(
                    'https://github.com/MetaMask/metamask-extension/releases/download/v10.34.0/metamask-chrome-10.34.0.zip')
                driver = setupWebdriver(metamask_path, None, None, './chromedriver')
                # Test account, please do not use for production environment
                try:
                    # setupMetamask(
                    #     'whip squirrel shine cabin access spell arrow review spread code fire marine', 'testtest')
                    phrase_most = 'track virtual team symptom lamp soul cousin element garden plug flower print'
                    phrase_1 = 'prize lion churn pig oppose exercise cat kitten worry faculty need region'
                    phrase = 'open purpose beyond genius ladder alarm top real chase quarter life mixture'
                    setupMetamask(phrase, 'dream123')
                    break
                except Exception as e:
                    driver.quit()
                    print("trying again")
                    print(e)
            driver.switch_to.new_window()
            driver.get('https://test.entangle.fi/')

            # Wait 20s for the page to load, and click the 'Connect' button
            wait = WebDriverWait(driver, 20, 1)
            wait_f = WebDriverWait(driver, 5, 1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Get Testnet Tokens')]"))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[text() = 'Connect Wallet']"))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//p[text() = 'Metamask']"))).click()
            # MetaMask will pop up a window, complete the connection
            connect()
            # time.sleep(10)
            # Click the 'Request Permissions' button
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Add Entangle Network')]"))).click()
            # MetaMask will pop up a window
            approve()

            time.sleep(2)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Claim Testnet tokens')]"))).click()
            time.sleep(2)
            # MetaMask will pop up a window
            # connect()
            while True:
                try:
                    if driver.find_element(By.XPATH, "//div[contains(text(),'Transaction in processing')]"):
                        time.sleep(2)
                    else:
                        break
                except:
                    break

            # wait.until(EC.element_to_be_clickable(
            #     (By.XPATH, "//button[contains(text(),'Claim more')]")))

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Add')]"))).click()

            confirm()
            while True:
                try:
                    dumm = randint(2,28)
                    driver.get('https://test.entangle.fi/stake/pancakeswap/NGL/entangle')
                    wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//input[@id='usdc-amount-input']"))).send_keys(dumm)
                    time.sleep(4)
                    # element_hover = driver.find_element(By.XPATH, "//button[text() = 'Approve']")
                    # hover = ActionChains(driver).move_to_element(element_hover)
                    # hover.perform()
                    try:
                        wait_f.until(EC.element_to_be_clickable(
                            (By.XPATH, "//button[text() = 'Approve']"))).click()
                        time.sleep(7)
                    except:
                        wait_f.until(EC.element_to_be_clickable(
                            (By.XPATH, "//button[text() = 'Stake']"))).click()
                        time.sleep(7)
                    approve()
                    time.sleep(2)
                    driver.get('https://test.entangle.fi/delegate')
                    wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[contains(text(),'Select Validator')]"))).click()

                    wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[@class='styles_dropWrapper__HkkQ1']//div[2]"))).click()

                    wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[contains(text(),'25%')]"))).click()

                    wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//button//p[text() = 'Delegate']"))).click()
                    time.sleep(7)
                    confirm()
                    confirm()

                    while True:
                        try:
                            if driver.find_element(By.XPATH, "//div[contains(text(),'Transaction in processing')]"):
                                time.sleep(2)
                            else:
                                break
                        except:
                            break
                except:
                    print("erorr in while loop, starting again from begining")
                    break
        except:
            print("last error")
            if driver:
                driver.quit()