import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from download_video import download_video
from download_img import download_img

def store_weibo(path, weibo_url):
    weibo_id = weibo_url.split("com/")[1].replace("/","_")
    path = path + weibo_id
    os.mkdir(path)
    # How to match the version of chrome: https://cloud.tencent.com/developer/article/1778586
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.get(weibo_url)
        time.sleep(10)
        browser.maximize_window()
        browser.save_screenshot(path + '\\微博截图.png')
        article = browser.find_element_by_tag_name("article")
        img_srcs = []

        try:
            img_tags = article.find_elements_by_tag_name("img")
            for img_tag in img_tags:
                img_srcs.append(img_tag.get_property("src"))
            for i in range(0,len(img_srcs)):
                download_img(path, img_srcs[i], "\\图片_" + str(i))
        except(NoSuchElementException):
            print("NoSuchElementException: No img.")

        try:
            video_src = article.find_element_by_tag_name("video").get_property("src")
            download_video(path, video_src, "\\视频")
        except(NoSuchElementException):
            print("NoSuchElementException: No video.")

        weibo_text = article.find_element_by_class_name("detail_wbtext_4CRf9").text
        with open(path + "\\微博文本内容.txt", mode='w', encoding="utf-8") as f:
            f.write(weibo_text)


# store_path = 'D:\\testDownload\\'
# weibo_url = "https://weibo.com/6596961402/Lnxrc11i7"
# store_weibo(store_path, weibo_url)


