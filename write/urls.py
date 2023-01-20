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
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.LikeUnlike.as_view(), name='like_unlike'),
    path('add/', views.PostWordArt.as_view(
        template_name='add_wordart.html'), name='add_wordart')
]
