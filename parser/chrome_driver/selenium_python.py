import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Устанавливаем ссылки на страницы, которые нужно проверять
url = "https://kino-mall.ru/schedule/?date=23.03.2023"

# options
options = webdriver.ChromeOptions()

# headless mode
options.add_argument("--headless")


# Инициализируем драйвер браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


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
