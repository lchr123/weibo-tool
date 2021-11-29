import auto_delete_blogs

blog_list = auto_delete_blogs.read_txt('blogs.txt')
print(len(blog_list))