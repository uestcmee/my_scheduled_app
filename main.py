import schedule
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()
# 设置python exe运行时不显示窗口
import win32api, win32gui
ct = win32api.GetConsoleTitle()
hd = win32gui.FindWindow(0,ct)
win32gui.ShowWindow(hd,0)



def show_notifier( title, text=':)'):
    toaster.show_toast(title,text,
                        # icon_path="涨跌.ico",
                        duration=5)
    return 0

def bond_deal_crawler():
    from bond_deal import fetch_bond_info
    show_notifier('债券成交','开始运行')
    fetch_bond_info()
    show_notifier('债券成交','获取完成')

def cobalt_price_crawler():
    from cobalt_price import main_func
    show_notifier('钴价格爬虫','开始运行')
    main_func()
    show_notifier('钴价格爬虫','获取完成')



if __name__ == '__main__':
    show_notifier('定期启动程序', '已开始运行')
    schedule.every().day.at("21:30").do(bond_deal_crawler)
    schedule.every().day.at("21:32").do(cobalt_price_crawler)

    while True:
        schedule.run_pending()
        time.sleep(1)