from . import views
from django.urls import path, include


# urlpatterns = {
#     path('', views.about, name='write-about'),
#     path('wordart/', views.wordart, name='write-wordart'),
#     path('register/', views.register, name='write-register')
# }

urlpatterns = [
    path('', views.About.as_view(template_name='about.html'), name='about'),
    path('wordart/', views.WordartList.as_view(), name='wordart'),
    path('register/', views.Register.as_view(
        template_name='register.html'), name='register'),
    path('add/', views.PostWordArt.as_view(
        template_name='add_wordart.html'), name='add-wordart')
]
