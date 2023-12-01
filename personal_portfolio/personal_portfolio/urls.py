from django.urls import path
from portfolio import views

#app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
  #  path('', views.all_blogs, name='all_blogs'),
  #  path('<int:blog_id>/', views.detail, name='detail'),
]