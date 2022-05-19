from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_log import GetLogger
import time
from selenium.webdriver.common.keys import Keys

log = GetLogger.get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info('初始化driver{}'.format(driver))
        self.driver = driver
        self.action = ActionChains(self.driver)

    # 查找元素方法 (提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info('正在查找元素:{}'.format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # # 二次定位(用于下拉框)
    # def base_twice_find_element(self, loc, loc_son):
    #     return self.base_find_element(loc).base_find_element(loc_son)

    # 点击方法
    def base_click(self, loc):
        log.info('正在点击元素:{}'.format(loc))
        self.base_find_element(loc).click()

    # 键盘向下加回车方法
    def base_keys(self, loc):
        log.info('正在向下')
        self.base_find_element(loc).send_keys(Keys.DOWN)
        log.info('正在回车')
        self.base_find_element(loc).send_keys(Keys.ENTER)

    # # 下拉框点击
    # def base_twice_click(self, loc, loc_son):
    #     log.info('正在点击元素:{}的{}'.format(loc, loc_son))
    #     self.base_twice_find_element(loc, loc_son).click()

    # 输入方法
    def base_input(self, loc, value):
        log.info('准备给元素{}输入内容:{}'.format(loc, value))
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        log.info('正在给元素{}清空'.format(loc))
        # 输入
        el.send_keys(value)
        log.info('正在给元素{}输入内容:{}'.format(loc, value))

    # # 弹出框输入方法
    # def base_twice_input(self, loc, loc_son, value):
    #     log.info('准备给元素{}输入内容:{}'.format(loc_son, value))
    #     el = self.base_twice_find_element(loc, loc_son)
    #     # 清空
    #     el.clear()
    #     log.info('正在给元素{}清空'.format(loc_son))
    #     # 输入
    #     el.send_keys(value)
    #     log.info('正在给元素{}输入内容:{}'.format(loc_son, value))

    # 获取文本方法
    def base_get_text(self, loc):
        # 注意：一定要返回元素的文本信息
        log.info('正在获取元素{}的文本'.format(loc))
        return self.base_find_element(loc, timeout=3).text

    # 获取输入框内文本方法
    def base_get_value(self, loc):
        # 注意：一定要返回元素的文本信息
        log.info('正在获取元素{}的value值'.format(loc))
        return self.base_find_element(loc, timeout=3).get_attribute('value')

    # 截图方法
    def base_get_image(self):
        log.info('正在截图')
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 封装判断元素是否存在
    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info('判断元素{}存在'.format(loc))
            # 找到元素  aseertTrue
            return True
        except:
            # 没找到元素
            return False

    # 鼠标操作-元素右击
    def base_context_click(self, loc):
        log.info('正在右击元素:{}'.format(loc))
        self.action.context_click(self.base_find_element(loc)).perform()

    # 鼠标操作-元素双击
    def base_double_click(self, loc):
        log.info('正在右击元素:{}'.format(loc))
        self.action.double_click(self.base_find_element(loc)).perform()

    # 鼠标操作-元素拖动
    def base_drag_and_drop(self, loc_source, loc_target):
        log.info('正在从元素:{}拖动到元素:{}上'.format(loc_source, loc_target))
        self.action.drag_and_drop(self.base_find_element(loc_source), self.base_find_element(loc_target)).perform()

    # 鼠标操作-元素悬挺
    def base_move(self, loc):
        log.info('正在把鼠标悬停在元素:{}之上'.format(loc))
        self.action.move_to_element(self.base_find_element(loc)).perform()
