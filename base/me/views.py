from django.shortcuts import render
from django.views import View
from .models import Blog

class MeView(View):
    template_name = 'me.html'

    def get(self, request):
        return render(request, self.template_name)


# class ResumeView(View):
#     template_name = 'resume.html'

#     def get(self, request):
#         return render(request, self.template_name)


class BlogView(View):
    template_name = 'blog.html'

    def get(self, request):
        blogs = Blog.objects.all()
        # for blog in blogs:
        #     blog.description = blog.description_content()
        #     blog.save()

        return render(request, self.template_name, {'blogs': blogs})


class ArticleٰView(View):
    template_name = 'article.html'

    def get(self, request, article_id):
        article = Blog.objects.get(id=article_id)

        return render(request, self.template_name, {'article': article})