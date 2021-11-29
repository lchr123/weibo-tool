import requests
import time

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97YkNrT8K04BHScpbM-UsZhOMUqxMH4ofbmSsXcEGa_m_Zg.; UOR=,,cn.bing.com; XSRF-TOKEN=lB8tRN5ZDezhe5PLmPIxfKvx; _s_tentry=weibo.com; appkey=; Apache=6050953275296.765.1638077646480; ULV=1638077646487:17:3:1:6050953275296.765.1638077646480:1636902796228; login_sid_t=4bbec7502b4370f3ad6d1d53bf44822e; cross_origin_proto=SSL; wb_view_log=1536*8641.25; SSOLoginState=1638096525; SUB=_2A25MpxDaDeRhGeFP6VMQ9y_Nyz6IHXVv1QUSrDV8PUNbmtAKLVjCkW9NQSTheQ85eHfwe4kCF5yLbMkeZXifvmRj; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWH6mYRKSjVCzzl0UpTaRS65JpX5KzhUgL.FoMpeo2pS02pehz2dJLoI0iWMr9DdbH8SCHWSF-RxbH8SCHWSF-4BEH81C-4xF-41CH8SCHFxCHWxCH8SC-RSE-R1Btt; ALF=1669633033; WBPSESS=Dt2hbAUaXfkVprjyrAZT_HzclRMfRfYY8hTuytsVIpPd4mVuR19BuCCsXzwK9npuPqdCAIJSXIe1RfRBwh48hCH9gFj-x7CJ0kSNunvF_QzrGECj2Go-JvDFKTvuMw7lo-HG5RapMTBsg4FRLcFZDcYcoomumGQMj1KaZl5-2sYr7PSygRQs-Vir-7iiLyHG7_ZGNxL2OS1Z8iLHkBZG1A==",
    'x-xsrf-token': "",
    "accept":"application/json, text/plain, */*"
}

payload = {
    "uid": ""
}

def post_blog_list():
    return requests.post("https://weibo.com/ajax/profile/destroyFollowers",
                         json = payload,
                         headers = headers).text

def write_xsrf_from_cookie(cookie):
    c_list = cookie.split(';')
    for i in range(len(c_list)):
        if(c_list[i].find('XSRF') != -1):
            headers['x-xsrf-token'] = c_list[i].split('=')[-1]
            return 'SUCCESS'
    return 'NO XSRF TOKEN! WRONG!'

def read_txt(file):
    with open(file,'r') as f:
        follow_list = list(eval(f.read()))
    return follow_list

if __name__ == '__main__':
    write_xsrf_from_cookie(headers['cookie'])
    blog_list = read_txt('fans.txt')
    for i in range(len(blog_list)):
        time.sleep(2)
        payload['uid'] = str(blog_list[i])
        print(post_blog_list())