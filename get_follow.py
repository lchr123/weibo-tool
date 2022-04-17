import requests
import json

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; UOR=,,cn.bing.com; ULV=1649818566813:23:1:1:6251158385578.943.1649818566759:1648641123238; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QKGY.ZSlyJeFeLp2xXz405JpX5KMhUgL.FoMNSK2cSoqfS022dJLoIEXLxKqL12eLBKnLxKqLB-qL12BLxKqLBoeLBo5LxKnL1h5L12eLxK-LB.-L1KMt; XSRF-TOKEN=y4JFtvIWW5lmISeeg76ly02S; ALF=1681659364; SSOLoginState=1650123365; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97YkCK8fS4sUUXFYbAySRk8sSR3z__WyJloEGnSRLsTFkLw.; SUB=_2A25PXpI1DeRhGeFJ7lMX9ijJzD2IHXVsLYT9rDV8PUNbmtAfLVfkkW9Nf75k45kVLUWKmSEUJoVVor9nmuhWR0El; WBPSESS=UG2SL6FgLS_M1rKl2zG2w51uUQrCj9ieiHtKGwsT41liMZKxIXlslAwy-ZLPscsEy5lN9AW1fJcVFQNJMVxtkG4548R3lgWzeHhuZbObJ6yazBJKNjnM-VjAZRuYSWeYrXLkceA0oAzm15krovgSxg=="
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

