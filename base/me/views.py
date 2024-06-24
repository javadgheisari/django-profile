from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Blog, Keyword

class MeView(View):
    template_name = 'me.html'

    def get(self, request):
        return render(request, self.template_name)


# class ResumeView(View):
#     template_name = 'resume.html'

#     def get(self, request):
#         return render(request, self.template_name)


class BlogView(ListView):
    template_name = 'blog.html'
    items_per_page = 10
    model = Blog

    def get(self, request, keyword=None):
        blogs = Blog.objects.all().order_by('-created')
        keywords = Keyword.objects.all()

        keyword_filter = False
        if keyword:
            blogs = blogs.filter(keywords__name=keyword)
            keyword_filter = True

        paginator = Paginator(blogs, self.items_per_page)
        page_number = request.GET.get('page')
        page_objs = paginator.get_page(page_number)
        # for blog in blogs:
        #     blog.description = blog.description_content()
        #     blog.save()

        return render(request, self.template_name, {'blogs': page_objs, 'keywords':keywords, 'keyword_filter':keyword_filter, 'keyword_name': keyword})


class ArticleٰView(View):
    template_name = 'article.html'

    def get(self, request, article_id):
        article = Blog.objects.get(id=article_id)

        return render(request, self.template_name, {'article': article})