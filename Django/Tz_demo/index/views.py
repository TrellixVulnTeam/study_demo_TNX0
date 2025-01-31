from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .comparebar import *
from .bar import *
from .map import *
from .radar import *
from django.views.decorators.cache import cache_page
import json

def index(request):
    ## print(this is a index)
    return render(request,'index.html',locals())

@cache_page(60 * 15)
def comparebar(request):
    # 第一张图 各县局的四要素统计
    stations =['58559','58652','58568','58660','K8201','K8301','58665','58664','58667','58665']
    data ={
    'wind':[],
    'pre':[],
    'tem':[],
    'sun':[],
    }
    result = return_sql_station()#[wind,pre,tem,sun]
    data['wind'] = result[0]
    data['pre'] = result[1]
    data['tem'] = result[2]
    data['sun'] = result[3]
    # for i in stations:
    #     avg = read_sql_station(i)
    #     data['wind'].append(avg[0])
    #     data['pre'].append(avg[2])
    #     data['tem'].append(avg[1])
    #     data['sun'].append(avg[3])
#    data={
#        'wind':[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0],
#        'pre':[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8],
#        'tem':[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5],
#        'sun':[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5],
#    }
    return JsonResponse(data)

def history(request):
    # 第二张图 历史排位 历史上本月的极值
    data={
        'day':['第一', '第二', '第三', '第四', '第五', '第六'],
        'pre':[55, 60, 170, 210, 350, 550],
        'tem':[3, 13, 25, 30, 38, 44],
    }
    return JsonResponse(data)

def bar(request):
    # 月的实际要素值
    result = return_sql_bar()
    data = {
        'day':['1日','2日','3日','4日','5日','6日','7日','8日','9日','10日','11日','12日',
               '13日','14日','15日','16日','17日','18日','19日','20日','21日','22日','23日','24日',
               '25日','26日','27日','28日','29日','30日','31日'],
        'wind':result[1],
        'pre':result[3],
        'tem': result[2],
    }
    # data={
    #     'day':['1日','2日','3日','4日','5日','6日','7日','8日','9日','10日','11日','12日',
    #         '13日','14日','15日','16日','17日','18日','19日','20日','21日','22日','23日','24日',
    #         '25日','26日','27日','28日','29日','30日','31日'],
    #     'wind':[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3,
    #         2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3,
    #         2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6],
    #     'pre':[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3,
    #         2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3,
    #         2.6, 5.9, 9.0, 26.4, 28.7, 70.7],
    #     'tem':[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2,
    #         2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2,
    #         2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3],
    # }
    return JsonResponse(data)

def radar(request):
    # 计算与常年的对比
    data =return_sql_radar()


    # data={
    #     'month':[4300, 10000, 28000, 35000, 35000,50000,19000],
    #     'history':[5000, 14000, 28000, 31000, 31000,42000,21000],
    # }
    return JsonResponse(data)

def map(request):
    # 地图scatter的极大温度
    # data = return_sql_map()
    data={
        'month':[4300, 10000, 28000, 35000, 35000,50000,19000],#Ta,Tn,Tx,RR,Rn,S,Fy
        'history':[5000, 14000, 28000, 31000, 31000,42000,21000],
    }
    return JsonResponse(data,safe=False)#返回的是一个列表所有要safe=false
