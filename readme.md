# 微博炸号解决方案

随便买个新号就可以开搞了。所有工具使用前需要手动获取并修改登录用户的cookie。

## 账号处理脚本

### 关注者

get_follow.py自动获取当前账号关注者id，写入follow.txt。

auto_follow.py自动关注follow.txt中的关注者。

auto_unfollow.py自动取关follow.txt中的关注者。

### 粉丝

get_fans.py自动获取当前账号粉丝id，写入fans.txt。

auto_delete_fans.py自动移除fans.txt中的粉丝。

### 博文

get_all_blogs.py自动获取当前账号所有博文id，写入blogs.txt。

auto_delete_blogs.py自动删除blogs.txt中的博文。

## 下载博文（文本、图片、视频）

被删前留存敏感博文，防夹。

store_weibo/store_weibo.py，path为想要下载到的本地文件夹，weibo_url为博文链接。

ps：这里使用selenium包截图，需要下一个chrome驱动到chrome的文件夹里（版本需要对应）。
