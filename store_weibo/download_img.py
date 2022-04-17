import requests

def download_img(path, url, weibo_id):
    file_name = weibo_id + '.jpg'
    img = requests.get(url)
    with open(path + file_name, mode='wb') as f:
        f.write(img.content)

# path = 'D:\\testDownload\\'
# img = requests.get("https://wx1.sinaimg.cn/large/65aefdccly1h136330hctj20n08xo7wh.jpg")
# file_name = 'test.jpg'
#
# with open(path + file_name, mode='wb') as f:
#     f.write(img.content)

