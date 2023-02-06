from django.urls import path

from . import views

urlpatterns = [
    path('', views.MeView.as_view(), name='me'),
    # path('resume/', views.ResumeView.as_view(), name='resume'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<int:article_id>/', views.ArticleٰView.as_view(), name='article'),
]