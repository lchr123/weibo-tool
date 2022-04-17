import time
import urllib.parse
import requests
import auto_follow

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; UOR=,,cn.bing.com; XSRF-TOKEN=lB8tRN5ZDezhe5PLmPIxfKvx; _s_tentry=weibo.com; appkey=; Apache=6050953275296.765.1638077646480; ULV=1638077646487:17:3:1:6050953275296.765.1638077646480:1636902796228; login_sid_t=4bbec7502b4370f3ad6d1d53bf44822e; cross_origin_proto=SSL; SSOLoginState=1638102818; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWH6mYRKSjVCzzl0UpTaRS65JpX5KMhUgL.FoMpeo2pS02pehz2dJLoI0YLxKqL12eLBKnLxKqLB-qL12BLxKqLB-BLB-2LxKML1K2L1--LxK-LB--L1h.LxKqLBK5LB.eLxKML1K2L1--t; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97YksHi65NClGbHpeh4PqWSp5QZMmF8pYVJZc5DIcXwMI5o.; SUB=_2A25MolUEDeRhGeFP6VMQ9y_Nyz6IHXVv1sHMrDV8PUNbmtAKLRLWkW9NQSTheStoJyzdPALk4KQ7cylBM4p3W9Xf; ALF=1669814483; WBPSESS=Dt2hbAUaXfkVprjyrAZT_HzclRMfRfYY8hTuytsVIpPd4mVuR19BuCCsXzwK9npuPqdCAIJSXIe1RfRBwh48hCH9gFj-x7CJ0kSNunvF_QxMzFnkZYoQhFgJ6nxCltuTFV5YHTxpxTlFTM0SyAOZbPXR8Z9ap5VGYx8kHlxznXUfPHYXet04kCOiGCDC87nxcEFYshQKYFsrb09WkcpHuw==",
    "Referer": "https://api.weibo.com/chat/",
    "accept":"application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload_json = {
    # mail content
    "text": "",
    "uid": 0,
    "extensions": {"clientid":"3tvqundjdbk3li99ydvokm1194hf4"},
    "is_encoded": 0,
    "decodetime": 1,
    "source": 209678993
}

payload = ""

def handle_payload(uid):
    # mail content
    payload_json["uid"] = int(uid)
    return urllib.parse.urlencode(payload_json)

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