from selenium import webdriver
import page


class GetDriver:
    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 设置谷歌对象
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            # 设置浏览器分辨率，opt会导致maximize最大化失败
            chrome_options.add_argument('--window-size=1920,1080')
            # 实例化浏览器
            cls.driver = webdriver.Chrome(chrome_options=chrome_options)
            # 最大化
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(page.url)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            # print("关闭之前：", cls.driver)
            cls.driver.quit()
            # print("关闭之后：", cls.driver)

            # 注意：此处有一个很大坑
            cls.driver = None
            # print("置空之后：", cls.driver)


if __name__ == '__main__':
    # 第一次获取浏览器
    print(GetDriver().get_driver())
    # 第二次获取浏览器
    print(GetDriver().get_driver())
    # 调用关闭，测试 关闭后driver是否为None
    GetDriver().quit_driver()
    # print(GetDriver().get_driver())