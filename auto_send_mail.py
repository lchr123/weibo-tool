import time

import requests
import auto_follow

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; UOR=,,cn.bing.com; _s_tentry=weibo.com; appkey=; Apache=6050953275296.765.1638077646480; ULV=1638077646487:17:3:1:6050953275296.765.1638077646480:1636902796228; login_sid_t=4bbec7502b4370f3ad6d1d53bf44822e; cross_origin_proto=SSL; SSOLoginState=1638102818; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97Yk2UOlgdPKa-Xzb-G365tACObpYEAFb08D0PoWqj_hgEE.; SUB=_2A25MoLmdDeRhGeFP6VMQ9y_Nyz6IHXVv16xVrDV8PUNbmtB-LUnykW9NQSTheSsbPu9_BKqXG3IpRwUlNX2DVoqh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWH6mYRKSjVCzzl0UpTaRS65JpX5KMhUgL.FoMpeo2pS02pehz2dJLoI0YLxKqL12eLBKnLxKqLB-qL12BLxKqLB-BLB-2LxKML1K2L1--LxK-LB--L1h.LxKqLBK5LB.eLxKML1K2L1--t; ALF=1669725516",
    "Referer": "https://api.weibo.com/chat/",
    "accept":"application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = ""

def handle_payload(uid):
    # mail content
    text = "hello!It is a test mail from BOT!"

    return "text=" + text + "&uid=" + str(uid) + "&extensions=%7B%22clientid%22%3A%223psatsdkbosc3e8ef1et9qj0v2gsxv%22%7D&is_encoded=0&decodetime=1&source=209678993"


def send_mail():
    return requests.post("https://api.weibo.com/webim/2/direct_messages/new.json",
                         data=payload,
                         headers=headers).text

if __name__ == '__main__':
    receiver_list = auto_follow.read_txt('temp.txt')
    for i in range(len(receiver_list)):
        time.sleep(5)
        payload = handle_payload(receiver_list[i])
        print(send_mail())