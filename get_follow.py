import requests
import json

# login manually and get cookie
headers = {
    'cookie': "SINAGLOBAL=5477873140407.266.1619794197463; SCF=AqnMqOeCgx9gVwLuH3wjVHTfnmRwFZzehL2z2Wim97YkNrT8K04BHScpbM-UsZhOMUqxMH4ofbmSsXcEGa_m_Zg.; UOR=,,cn.bing.com; XSRF-TOKEN=lB8tRN5ZDezhe5PLmPIxfKvx; _s_tentry=weibo.com; appkey=; Apache=6050953275296.765.1638077646480; ULV=1638077646487:17:3:1:6050953275296.765.1638077646480:1636902796228; login_sid_t=4bbec7502b4370f3ad6d1d53bf44822e; cross_origin_proto=SSL; wb_view_log=1536*8641.25; SUB=_2A25MpwYIDeRhGeFK7FYY9CrMyT-IHXVv1XDArDV8PUNbmtB-LRjVkW9NQx_G1n_V_MSKomEQh6ocNc2Jl_shKzD4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFmI8PcMP4hClh2U3GB48gl5JpX5KzhUgL.FoMXS0B4ShB7eoe2dJLoIEXLxKqL12eLBKnLxKqLB-qL12BLxK-LB--L1h.LxKqLBK5LB.eLxKML1K2L1--t; ALF=1669638615; SSOLoginState=1638102616; WBPSESS=Dt2hbAUaXfkVprjyrAZT_Aoi3G1lruQBkPEQjpwojSxqAlfLl2RZGJpnbmtc_lCcHxtdVUXvs1PXRFZ0HSVXIVtRJxXHMdsLYzHJFBj22DXlv8ruSCrTAWo0emQ_NZ0U0DpiNdJqizJHz8ouiYJcQlLMc5G_i0aqt2PkKZnNSo8z_z87-tcKnHchPAzx0rKjs6iEMBA8d1S13mQyHNsjgg=="
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

