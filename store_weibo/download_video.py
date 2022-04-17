import requests

def download_video(path, url, weibo_id):
    file_name = weibo_id + '.mp4'
    video = requests.get(url)
    with open(path + file_name, mode='wb') as f:
        f.write(video.content)

# path = 'D:\\testDownload\\'
# file_name = 'test.mp4'
# video = requests.get("https://f.video.weibocdn.com/o0/PXhj9g50lx07V7FDR6VG01041200o7C90E010.mp4?label=mp4_1080p&template=1080x2160.24.0&media_id=4756098775974065&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=4&ot=v&ps=3lckmu&uid=7LVHUq&ab=3915-g1,7397-g1,6377-g0,1192-g0,1191-g0,1046-g2,1258-g0,3601-g19&Expires=1649480064&ssig=AD4GPVNIKo&KID=unistore,video")
#
# with open(path + file_name, mode='wb') as f:
#     f.write(video.content)

