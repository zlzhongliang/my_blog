import datetime

from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.




# 上传图片的地址
def user_avatar_path(instance, filename):
    """自定义用户头像保存路径和文件名"""
    # 获取源文件名的后缀
    ext = filename.split('.')[-1]
    # 通过当前时间字符串作为文件名
    file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # 拼接文件名和后缀
    file = 'blog/article/icon/'+file_name + '.' + ext
    # 使用当前用户id为路径
    return file


class PictureModel(models.Model):
    name = models.CharField(max_length=20,verbose_name='图片名称')
    picture = models.ImageField(upload_to=user_avatar_path, verbose_name='图片')
    issuedate = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    is_Show = models.BooleanField(default=True,verbose_name='是否显示')
    is_Delete = models.BooleanField(default=True,verbose_name='是否删除')

    def __str__(self):
        return self.name


    @classmethod
    def create_picture(cls, name,picture):
        picture = cls(name=name,picture=picture)
        return picture


class NavModel(models.Model):
    nav_name = models.CharField(max_length=20,verbose_name='类别')
    nav_picture = models.ForeignKey(PictureModel,default=1,on_delete=models.CASCADE,verbose_name='图片')
    issuedate = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    is_Show = models.BooleanField(default=True,verbose_name='是否显示')
    is_Delete = models.BooleanField(default=True,verbose_name='是否删除')
    Nav_root = models.ForeignKey('self',related_name='root_nav',null=True,on_delete=models.DO_NOTHING,blank=True,verbose_name='根')

    def __str__(self):
        return self.nav_name


    @classmethod
    def create_nav(cls, nav_name, nav_root):
        nav = cls(Nav_name=nav_name, Nav_root=nav_root)
        return nav


class ArticleModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    author = models.CharField(max_length=10, verbose_name="作者")
    article_picture = models.ForeignKey(PictureModel,related_name='图片',default=1,on_delete=models.CASCADE,verbose_name='图片')
    video = models.CharField(max_length=500,verbose_name='视频地址')
    # content = RichTextUploadingField()
    content = models.TextField(verbose_name="内容")
    nav1 = models.ForeignKey(NavModel,related_name='nav1',default=1,on_delete=models.CASCADE,verbose_name='一级类别')
    nav2 = models.ForeignKey(NavModel,related_name='nav2',default=1, on_delete=models.CASCADE, verbose_name='二级类别')
    issuedate = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    alterdate = models.DateTimeField(auto_now=True,verbose_name='最近修改')
    sort = models.IntegerField(default=0,verbose_name='排序')
    browse_count = models.IntegerField(default=0, verbose_name="浏览次数")
    praise = models.IntegerField(default=0, verbose_name='点赞')
    is_Delete = models.BooleanField(default=True,verbose_name='是否删除')
    is_show = models.BooleanField(default=True,verbose_name='是否显示')

    def __str__(self):
        return self.title

    @classmethod
    def createArticle(cls,author, title, video,content,nav1,nav2,is_show,article_picture):
        article = cls(author=author,title=title, video=video, content=content,nav1=nav1,nav2=nav2,is_show=is_show,article_picture=article_picture)
        return article
