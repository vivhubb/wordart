"""wordart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.urls import path

urlpatterns = [
    path('', views.About.as_view(template_name='about.html'), name='about'),
    path('wordart/', views.WordartList.as_view(), name='wordart'),
    path('add/', views.add_wordart, name='add_wordart'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/post_update', views.edit_wordart, name='post_update'),
    path('<slug:slug>/post_delete', views.delete_wordart, name='post_delete'),
    path('like/<slug:slug>', views.LikeUnlike.as_view(), name='like_unlike'),
    path(
        '<slug:slug>-<int:pk>/comment_update',
        views.edit_comment,
        name='comment_update'
        ),
    path(
        '<int:pk>/comment_delete',
        views.delete_comment,
        name='comment_delete'
        ),
]
