# @Author: Administrator
# @Email: 2478711969@qq.com
# @Date: 2021/2/1 19:26
# @File: urls
# @Project: tutorial
# @Desc:

from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)