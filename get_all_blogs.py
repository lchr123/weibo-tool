import json
import time

import requests

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97YkNrT8K04BHScpbM-UsZhOMUqxMH4ofbmSsXcEGa_m_Zg.; UOR=,,cn.bing.com; XSRF-TOKEN=lB8tRN5ZDezhe5PLmPIxfKvx; _s_tentry=weibo.com; appkey=; Apache=6050953275296.765.1638077646480; ULV=1638077646487:17:3:1:6050953275296.765.1638077646480:1636902796228; login_sid_t=4bbec7502b4370f3ad6d1d53bf44822e; cross_origin_proto=SSL; wb_view_log=1536*8641.25; SUB=_2A25MpwdyDeRhGeFP6VMQ9y_Nyz6IHXVv1X-6rDV8PUNbmtAKLRXQkW9NQSTheS04_O9G3t6aEma_DotoEqnjdB9e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWH6mYRKSjVCzzl0UpTaRS65JpX5KzhUgL.FoMpeo2pS02pehz2dJLoI0iWMr9DdbH8SCHWSF-RxbH8SCHWSF-4BEH81C-4xF-41CH8SCHFxCHWxCH8SC-RSE-R1Btt; ALF=1669638817; SSOLoginState=1638102818; WBPSESS=Dt2hbAUaXfkVprjyrAZT_HzclRMfRfYY8hTuytsVIpPd4mVuR19BuCCsXzwK9npuPqdCAIJSXIe1RfRBwh48hCH9gFj-x7CJ0kSNunvF_QzJZuGeN9doBb1r4rJ39V-4jBVIYZVdghzPs8wg6OEWo4z6PcNNQPwa0Ri3pZehemIUcwbE-vzBlx9NiVYfCLhBs4qtPjmyEANk1CZ4ESibrQ=="
}

def get_blog_list(page):
    content = requests.get("https://weibo.com/ajax/statuses/mymblog?uid=7121171102&page=" + str(page) + "&feature=0",
                           headers = headers).text
    content_json = json.loads(content)
    return content_json

def write_txt(content):
    with open('blogs.txt','w') as file:
        file.write(str(content))
    return 1

if __name__ == '__main__':
    blog_id_list = []
    for i in range(1, 100):
        time.sleep(5)
        page_data = get_blog_list(i)
        page_size = len(page_data['data']['list'])
        for j in range(page_size):
            blog_id_list.append(page_data['data']['list'][j]['id'])
    write_txt(blog_id_list)