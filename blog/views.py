from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import BlogPost

class IndexView(ListView):
    """トップページのビュー
    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name:レンダリングするテンプレート
        context_object_name: object_listキーの別名を設定
        queryset: データベースのクエリ
    """
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # object_listの別名を定義
    context_object_name = 'Orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並び替える
    queryset = BlogPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 4

class BlogDetail(DetailView):
    """
    投稿記事の詳細を表示するのでDetailViewを継承する
    Attributes;
      template_name: レンダリングするテンプレート
      Model: モデルのクラス
    """
    # post.htmlをレンダリングする
    template_name = 'post.html'
    # クラス変数modelにBlogPostを設定
    model = BlogPost

class TechView(ListView):
    """
    技術的なこと(tech)カテゴリの記事を一覧するビュー
    """
    template_name = 'tech_list.html'
    model = BlogPost