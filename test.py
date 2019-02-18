from selenium import webdriver

driver = webdriver.Firefox()
# driver.maximize_window()  # 最大化窗口
number = 1
while number:
    number += 1
    # 初始化一个火狐浏览器实例：driver

    driver.minimize_window()
    driver.implicitly_wait(60)

    # driver.get("https://www.baidu.com")  # 通过get()方法，打开一个url站点
    driver.get("https://blog.csdn.net/ChaoFeiLi/article/details/86595160")
    driver.get("https://blog.csdn.net/ChaoFeiLi/article/details/86591672")
    driver.implicitly_wait(60)
    driver.get("https://blog.csdn.net/ChaoFeiLi/article/details/86584958")
    driver.get("https://blog.csdn.net/ChaoFeiLi/article/details/84789949")
    driver.implicitly_wait(60)
    driver.get("https://blog.csdn.net/ChaoFeiLi/article/details/86606128")
    driver.get('https://blog.csdn.net/ChaoFeiLi/article/details/86617923')
    driver.implicitly_wait(120)

    if number % 10 == 0:
        # 关闭浏览器
        driver.quit()
        driver = webdriver.Firefox()
        driver.implicitly_wait(120)
        driver.minimize_window()

    print(number)
