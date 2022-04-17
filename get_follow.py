import requests
import json

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; UOR=,,cn.bing.com; SSOLoginState=1648640805; XSRF-TOKEN=ooMFmUMncyeUWBrV2DwnEldx; _s_tentry=weibo.com; Apache=5108247916641.18.1648641123152; ULV=1648641123238:22:3:1:5108247916641.18.1648641123152:1647493451102; YF-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWH6mYRKSjVCzzl0UpTaRS65JpX5KMhUgL.FoMpeo2pS02pehz2dJLoI0YLxKqL12eLBKnLxKqLB-qL12BLxKqLB-BLB-2LxKML1K2L1--LxK-LB--L1h.LxKqLBK5LB.eLxKML1K2L1--t; ALF=1681221836; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97YksnAWHy8W0s_NYb1Rjk9SZzIXvE30GRSzZfFf9cCgsvU.; SUB=_2A25PUEUfDeRhGeFP6VMQ9y_Nyz6IHXVsJDHXrDV8PUNbmtAfLU_3kW9NQSTheUbrXlZIpuxnl0RGAnGS_JHbDuEC; WBPSESS=-0P3q-N8qU2s6SBRYEQ7f63bM52czQzID_DFq2DoCDCM32wbzzL6misytcfv5JMwhsGiAnJsfOM8Ik7lDw4pKaLyTLwA1LovTBMJgmlcKAymky45PiD2KpyJS7JCCxg-Brcnh3GdsUxq55rILcF6xw=="
}

def get_follow_pages():
    content = requests.get("https://weibo.com/ajax/profile/followContent?sortType=all",
                           headers=headers).text
    content_json = json.loads(content)
    total_follow = content_json['data']['total_number']
    return int(int(total_follow) / 50) + 1

def get_follow_list(pages):
    content = requests.get("https://weibo.com/ajax/profile/followContent?page=" + str(pages) + "&next_cursor=50",
                           headers = headers).text
    content_json = json.loads(content)
    return content_json

def write_txt(content):
    with open('follow.txt','w') as file:
        file.write(str(content))
    return 1


if __name__ == '__main__':
    total_pages = get_follow_pages()
    follow_id_list = []
    for i in range(1,total_pages+1):
        page_data = get_follow_list(i)
        users_number = len(page_data['data']['follows']['users'])
        for j in range(0,users_number):
            follow_id_list.append(page_data['data']['follows']['users'][j]['id'])
    write_txt(follow_id_list)

