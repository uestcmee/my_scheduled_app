import schedule
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()
# 设置python exe运行时不显示窗口
import win32api, win32gui
ct = win32api.GetConsoleTitle()
hd = win32gui.FindWindow(0,ct)
win32gui.ShowWindow(hd,0)
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print (func.__name__)    # 输出 函数名
        show_notifier('开始运行',func.__doc__)
        return func(*args, **kwargs)
    return with_logging


def show_notifier( title, text=':)'):
    toaster.show_toast(title,text,duration=5)# icon_path="涨跌.ico",)
    return 0

@logged
def bond_deal_crawler():
    """
    同业交易中心债券成交爬虫
    """
    from bond_deal import fetch_bond_info
    fetch_bond_info()

@logged
def cobalt_price_crawler():
    """
    钴等商品价格爬虫
    """
    from cobalt_price import main_func
    main_func()



if __name__ == '__main__':
    show_notifier('定期启动程序', '已开始运行')
    # # 一个愚蠢的方式来工作日启动
    # schedule.every().monday.at("21:30").do(bond_deal_crawler)
    # schedule.every().tuesday.at("21:30").do(bond_deal_crawler)
    # schedule.every().wednesday.at("21:30").do(bond_deal_crawler)
    # schedule.every().thursday.at("21:30").do(bond_deal_crawler)
    # schedule.every().friday.at("21:30").do(bond_deal_crawler)

    schedule.every().day.at("21:30").do(bond_deal_crawler)
    schedule.every().day.at("21:30:30").do(cobalt_price_crawler)

    while True:
        schedule.run_pending()
        time.sleep(1)