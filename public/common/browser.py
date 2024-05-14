"""         ==Coding: UTF-8==
**    @Project :        PublicInstitutionSystem
**    @fileName         browser.py
**    @author           Echo
**    @EditTime         2023/12/11
"""
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import globalparam
from public.common.exceptions import UnsupportedBrowserException
from utils.download_driver import download_driver


def setup_driver_options(browser):
    """
    根据浏览器类型设置WebDriver的选项。
    :param browser: 浏览器名称
    :return: WebDriver选项对象
    """
    options_map = {
        'chrome': ChromeOptions,
        'edge': EdgeOptions,
        'firefox': FirefoxOptions
    }

    if browser in options_map:
        options_class = options_map[browser]
        options = options_class()
        if browser == 'chrome':
            options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 禁用自动测试迹象
            options.add_experimental_option('useAutomationExtension', False)  # 禁用自动化扩展
            options.add_experimental_option("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,  # 禁用保存密码提示框
                'download.default_directory': globalparam.download_path,  # 设置下载路径
                'download.prompt_for_download': False,  # 不弹出下载提示框
                'download.directory_upgrade': False,  # 记录下载目录是否被更改
                'safebrowsing.enabled': False  # 禁用提示安全警告
            })

        options.add_argument('ignore-certificate-errors')  # 忽略证书错误
        return options
    else:
        raise UnsupportedBrowserException(f"不支持的浏览器: {browser}")


def create_service(browser, driver_path):
    """
    为WebDriver创建Service对象。
    :param browser: 浏览器名称
    :param driver_path: WebDriver驱动程序的路径
    :return: Service对象
    """
    if browser == 'chrome':
        service = Service(driver_path)
        return service
    else:  # 其他浏览器的驱动暂未实现
        return None


def initialize_driver(browser, options, service, system_driver):
    """
    初始化WebDriver，传入选项和浏览器驱动地址。
    :param browser: 浏览器名称
    :param options: WebDriver选项对象
    :param service: Service对象
    :param system_driver: 系统平台
    :return: WebDriver实例
    """
    try:
        driver_class = getattr(webdriver, browser.capitalize())
        driver = driver_class(options=options, service=service)
        return driver
    except Exception as e:
        print(f"初始化驱动程序时发生错误: {e}")
        download_driver(browser=browser)
        return initialize_driver(browser, options, service, system_driver)


def select_browser(browser=globalparam.browser.lower()) -> webdriver:
    """
    根据指定的浏览器和系统选择并返回WebDriver实例。
    :param browser: 浏览器名称
    :return: WebDriver实例
    """
    system_driver = sys.platform
    options = setup_driver_options(browser)
    service = create_service(browser,
                             globalparam.driver_path if system_driver == 'win32' else globalparam.linux_driver_path)

    return initialize_driver(browser, options, service, system_driver)
