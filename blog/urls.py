from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        # ブログ詳細ページのURLは'blog-detail/レコードのID/
        'blog-detail/<int:pk>/',
        views.BlogDetail.as_view(),
        name='detail_blog'
    )
]