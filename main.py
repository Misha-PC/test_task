from news_parser import Firefox

driver = r"C:\Program Files\Driver\geckodriver.exe"

if __name__ == '__main__':

    firefox = Firefox(driver)                   # init object
    res = firefox.get_last_news_yandex()        # get last news
    print(res)
    print(len(res))
    del firefox
