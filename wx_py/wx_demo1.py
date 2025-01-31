from wxpy import *

import time,datetime

from threading import Thread 
bot=Bot(cache_path=True)


####　　　　　　　　测试代码
###################################################################################


# 机器人账号自身
myself = bot.self

print("机器人自身：",myself)

allfriends = bot.friends()

print("机器人的所有好友：",allfriends)

allgroups = bot.chats(update=False)
## 打印的是所有的微信的聊天对象
print("机器人的聊天对象：",allgroups)



#####################################################################################






friend = bot.friends().search('liyuan')[0]
print(friend)

message = '这是message消息'
# 功能一 ：自动回复微信消息
@bot.register() # 接收从指定好友发来的消息，发送者即recv_msg.sender为指定好友girl_friend
def recv_send_msg(recv_msg):
    #业务逻辑代码
    # 附加功能：增加消息记录的功能
    print('收到的消息：',recv_msg.text) # recv_msg.text取得文本
    if recv_msg.text == '1':
        return '1111111111111'
    elif recv_msg.text == '2':
        return '22222222222'
    return '您好，一个微信机器人，按1，按2试试'


# 功能二 ：主动推送消息给一些人
def putmsg(friend,message):
    friend.send(message)

# 功能三 ：定时的自动向目标群(好友)推送消息
def run(h,m):
    while True:
        now  = datetime.datetime.now()
        print(now.hour,now.minute)
        if now.hour in h and now.minute in m:
            putmsg(friend,message)
        time.sleep(60)

# run函数为定时启动的函数
# run(23,m=[24])
# 开辟一个新的进程对新的
#p = Process(target = run,kwargs = {'h':22,'m':[50,51,52]})
p = Thread(target = run,kwargs = {'h':[23],'m':[8,9,10,11,12]})
p.start()
#p.join()
# 功能三：主动推送消息给一些人


# 阻塞等待微信机器人的消息

bot.join()