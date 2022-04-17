import requests
import time

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; UOR=,,cn.bing.com; WBPSESS=Dt2hbAUaXfkVprjyrAZT_Aoi3G1lruQBkPEQjpwojSxwwHZj0Ohwmf4qiZphphdMa1exOyEo6d_IvWbdYUdpXXHegvdyrEhy-RUuPzmuTF9oezokRIeKjACkPrkimQ28K-v36sWRDGSy7zwUQyAX3Cheh_AFS5LwGDwPCocmGoWVWNfr82Bl8UH8yw6sQcuI-rhQqeJCMzWGPH28-CBokQ==; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QKGY.ZSlyJeFeLp2xXz405JpX5KMhUgL.FoMNSK2cSoqfS022dJLoIEXLxKqL12eLBKnLxKqLB-qL12BLxKqLBoeLBo5LxKnL1h5L12eLxK-LB.-L1KMt; ALF=1681351338; SSOLoginState=1649815339; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97Yk0ylnlQoxmzHR_7JltObtybRFW3tVy7rZUT4gYqIwVvY.; SUB=_2A25PUl98DeRhGeFJ7lMX9ijJzD2IHXVsJje0rDV8PUNbmtAfLXjZkW9Nf75k41Gq2Rdp14zExGadNZXQ5lF40yWh; XSRF-TOKEN=brd-5FqEesllSTHoS6hfFq8s; _s_tentry=weibo.com; Apache=6251158385578.943.1649818566759; ULV=1649818566813:23:1:1:6251158385578.943.1649818566759:1648641123238",
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