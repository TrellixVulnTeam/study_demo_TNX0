from django.test import TestCase

# Create your tests here.
import pymssql
import pandas as pd
import time
import datetime
from datetime import  date, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



today = datetime.date.today()
last_day_of_last_month = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
first_day_of_last_month = datetime.date(last_day_of_last_month.year, last_day_of_last_month.month, 1)
print(last_day_of_last_month)
end_day_in_mouth = today.replace(day=1)

#stations =['58559','58652','58568','58660','K8201','K8301','58665','58664','58665']
def return_sql_bar():
    print("this is a read station file")
    server = "172.21.158.201"    # 连接服务器地址
    user = "down"# 连接帐号
    password = "downx"# 连接密码
    conn = pymssql.connect(server, user, password, "ZJSZDZDB")  #获取连接
    cursor = conn.cursor() # 获取光标
    cursor.execute('USE ZJSZDZDB' )
    cursor.fetchall()
    data = pd.DataFrame(list(row))
    # 计算历史降水排位
    sql = "SELECT Year(tTime) as ye, max(RR) as Rsum  FROM Tab_AWS Where RR>-1 And IIiii In ('58660') " \
          "GROUP BY YEAR(tTime) ORDER BY  Rsum desc"
    cursor.execute(sql)
    #row =
    print(data)

return_sql_bar()