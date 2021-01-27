# 定期获取数据，定时模块单独封装
# 后期可以使用mainloop文件进行定时
import datetime

import sqlite3

# 获取债券数据
def fetch_bond_info():
    """
    获取债券数据的文件，如果文件已经存在，则跳过
    :return:
    """
    date_time = datetime.datetime.today()
    date = date_time.date()

    def GetTables(db_file="main.db"):
        try:
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            cur.execute(
                "select name from sqlite_master where type='table' order by name"
            )
            return cur.fetchall()
        except Exception as e:
            print(e)
            return []

    """不做存在检测，每日运行一次"""
    # exist_list = [x[0] for x in GetTables('债券成交.db')]
    # exist_flag = (str(date) in exist_list)
    # exist_flag=False
    # if exist_flag: # 已经存在
    #     print('今日结果已经存在')
    #     # time.sleep(300)# 延时五分钟
    #     return 0
    # else:
    print("获取今日成交")
    if "ak" not in locals():  # 避免重复import
        import akshare as ak
    bond_df_raw = ak.bond_spot_deal()

    """
    上一句中的bond_spot_deal中源码写错了，修改源码，可获取交易量数据
    # "dmiPrvsClsngContraRate",
    "dmiTtlTradedAmntLabel",
    """
    """
    将结果保存到数据库中
    """
    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///债券成交.db")
    bond_df_raw.to_sql(str(date), engine, if_exists="replace")

    print("成交获取完成")
    return 0


if __name__ == "__main__":
    # print('成交数据每日爬虫')
    # 工作日获取债券信息
    # 8点结束交易，但是8:30-9:30才有成交量数据，之前的一直没有获取到成交量数据
    # Timing(title='债券成交爬虫',rule='weekday<5 and tim>"21:10:00"').main_loop(func=fetch_bond_info,wait_time=5)
    fetch_bond_info()
