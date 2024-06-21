from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog-detail/<int:pk>/',
          views.BlogDetail.as_view(), name='detail_blog'),
    path('tech-list/',
         views.TechView.as_view(), name='tech_list'),
    path('dailylife-list/',
         views.DailylifeView.as_view(), name='dailylife_list'),
    path('hobby_list/',
         views.HobbyView.as_view(), name='hobby_list'),
]