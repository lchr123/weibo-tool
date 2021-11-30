import requests
import time

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; UOR=,,cn.bing.com; XSRF-TOKEN=lB8tRN5ZDezhe5PLmPIxfKvx; _s_tentry=weibo.com; appkey=; Apache=6050953275296.765.1638077646480; ULV=1638077646487:17:3:1:6050953275296.765.1638077646480:1636902796228; login_sid_t=4bbec7502b4370f3ad6d1d53bf44822e; cross_origin_proto=SSL; SSOLoginState=1638102818; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWH6mYRKSjVCzzl0UpTaRS65JpX5KMhUgL.FoMpeo2pS02pehz2dJLoI0YLxKqL12eLBKnLxKqLB-qL12BLxKqLB-BLB-2LxKML1K2L1--LxK-LB--L1h.LxKqLBK5LB.eLxKML1K2L1--t; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97YksHi65NClGbHpeh4PqWSp5QZMmF8pYVJZc5DIcXwMI5o.; SUB=_2A25MolUEDeRhGeFP6VMQ9y_Nyz6IHXVv1sHMrDV8PUNbmtAKLRLWkW9NQSTheStoJyzdPALk4KQ7cylBM4p3W9Xf; ALF=1669814483; WBPSESS=Dt2hbAUaXfkVprjyrAZT_HzclRMfRfYY8hTuytsVIpPd4mVuR19BuCCsXzwK9npuPqdCAIJSXIe1RfRBwh48hCH9gFj-x7CJ0kSNunvF_QzJZuGeN9doBb1r4rJ39V-4e21r4z4QNB6-2Ce9gpwLcRn9nk-_dqUPZjy5b2wJxKTcFQx3feDeT3PMmdQLtSI6UMCiYrptFums2jzWUVRhnA==",
    'x-xsrf-token': "",
    "accept":"application/json, text/plain, */*"
}

payload = {
    "friend_uid":"6079157125",
    "page":"profile",
    "lpage":"profile"
}

def write_xsrf_from_cookie(cookie):
    c_list = cookie.split(';')
    for i in range(len(c_list)):
        if(c_list[i].find('XSRF') != -1):
            headers['x-xsrf-token'] = c_list[i].split('=')[-1]
            return 'SUCCESS'
    return 'NO XSRF TOKEN! WRONG!'

def post_follow_list():
    return requests.post("https://weibo.com/ajax/friendships/create",
                         json = payload,
                         headers = headers).text

def read_txt(file):
    with open(file,'r') as f:
        follow_list = list(eval(f.read()))
    return follow_list

if __name__ == '__main__':
    write_xsrf_from_cookie(headers['cookie'])
    follow_list = read_txt('D://projects//weibo-tool//follow.txt')
    for i in range(len(follow_list)):
        time.sleep(5)
        payload['friend_uid'] = str(follow_list[i])
        print(post_follow_list())