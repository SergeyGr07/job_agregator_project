import time
from selenium import webdriver

# Устанавливаем ссылки на страницы, которые нужно проверять
url = "https://kino-mall.ru/schedule/?date=23.03.2023"

# Инициализируем драйвер браузера
driver = webdriver.Chrome(executable_path="D:\job_agregator_project\parser\chrome_driver\chromedriver.exe")

try:
    # Открываем страницу
    print("Opening page...")
    driver.get(url)

    while True:
        # Обновляем страницу
        print("Checking page...")
        driver.refresh()
        print("Processing...")
        # Ждем 1(3600) час
        time.sleep(10)
        print("Checking the page...Please wait...")
        # Проверяем, изменилась ли ссылка на страницу
        if driver.current_url == url:
            print("Ссылка изменилась!")
            break

except Exception as e:
    # Обрабатываем ошибки
    print("Произошла ошибка: ", e)

finally:
    # Закрываем браузер
    driver.close()
    driver.quit()
