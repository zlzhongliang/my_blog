from django.shortcuts import render, redirect

# Create your views here.
from blog.models import ArticleModel, NavModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    articles = ArticleModel.objects.filter(is_show=True, is_Delete=True).order_by('sort', '-id')
    navs = NavModel.objects.filter(is_Show=True, is_Delete=True)
    right_articles = ArticleModel.objects.filter(is_show=True, is_Delete=True).order_by('sort', 'browse_count')[:5]

    paginator = Paginator(articles, 6)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)
    try:
        page_of_blogs = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger as e:
        page_of_blogs = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage as e:
        page_of_blogs = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    data = {'articles': page_of_blogs,
            'right_articles': right_articles,
            'navs': navs,
            'title': "钟亮的个人博客",
            }
    return render(request, "blog/index.html", data)


def article_list(request, nav_id):

    nav2 = NavModel.objects.get(is_Show=True, is_Delete=True, id = nav_id)
    articles = ArticleModel.objects.filter(is_show=True, is_Delete=True, nav2=nav2).order_by('sort', '-id')
    navs = NavModel.objects.filter(is_Show=True, is_Delete=True)
    right_articles = ArticleModel.objects.filter(is_show=True, is_Delete=True).order_by('sort', 'browse_count')[:5]

    paginator = Paginator(articles, 6)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)
    try:
        page_of_blogs = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger as e:
        page_of_blogs = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage as e:
        page_of_blogs = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    data = {'articles': page_of_blogs,
            'right_articles': right_articles,
            'navs': navs,
            'title': "钟亮的个人博客",
            }
    return render(request,"blog/article_list.html", data)


def article(request,article_id):
    try:
        article = ArticleModel.objects.get(is_show=True, is_Delete=True, id=article_id)
        article_class = article.nav2
        articleid = article.id
        article_next = ArticleModel.objects.filter(id__lt=articleid,is_show=True,is_Delete=True,nav2=article_class).order_by('-id').first()
        article_prev = ArticleModel.objects.filter(id__gt=articleid,is_show=True,is_Delete=True,nav2=article_class).first()
        if article_next == None:
            article_next = ArticleModel.objects.filter(id__lt=articleid, is_show=True, is_Delete=True).order_by('-id').first()
            if article_next == None:
                article_next = article
        if article_prev == None:
            article_prev = ArticleModel.objects.filter(id__gt=articleid, is_show=True, is_Delete=True).first()
            if article_prev == None:
                article_prev = article
        article.browse_count += 1
        article.save()
        navs = NavModel.objects.filter(is_Show=True, is_Delete=True)
        right_articles = ArticleModel.objects.filter(is_show=True, is_Delete=True).order_by('sort', 'browse_count')[:5]
        data = {'article': article,
                'right_articles': right_articles,
                'navs': navs,
                'title': article.title,
                'article_next': article_next,
                'article_prev': article_prev,
                }
        return render(request, "blog/article.html", data)
    except Exception as e:
        return redirect("/index")


def about(request):
    navs = NavModel.objects.filter(is_Show=True, is_Delete=True)
    right_articles = ArticleModel.objects.filter(is_show=True, is_Delete=True).order_by('sort', 'browse_count')[:5]
    data = {'right_articles': right_articles,
            'navs': navs,
            'title': "关于博主",
            }
    return render(request,"blog/about.html", data)
