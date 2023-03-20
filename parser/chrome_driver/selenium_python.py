import time
from selenium import webdriver

url = "https://kino-mall.ru/schedule/?date=20.03.2023"
driver = webdriver.Chrome(executable_path="D:\job_agregator_project\parser\chrome_driver\chromedriver.exe")

try:

    print("Processing...")
    while True:
        driver.get(url)
        driver.refresh()
        time.sleep(10)
        if driver.current_url != url:
            print("Ссылка изменилась!")
            break
        print("Processing...")
except Exception as e:
    print("Произошла ошибка: ", e)

finally:
    driver.close()
    driver.quit()
