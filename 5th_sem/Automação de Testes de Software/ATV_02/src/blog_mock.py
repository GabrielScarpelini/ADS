from blog import Blog

class BlogMock(Blog):

    def __init__(self):
        self.fullData = Blog.posts()
        self.byUser = Blog.post_by_user_id("6")

    def alldata(Blog):
        return Blog.posts()
    
    def getPostByUserId(var):
        return var.post_by_user_id("6")


byID = BlogMock.getPostByUserId(Blog)
data = BlogMock.alldata(Blog)

print(len(byID))
print(len(data))