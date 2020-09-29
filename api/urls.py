from django.urls import path

from api import views

urlpatterns = [
    # path('users/', views.usersApi),
    # path('articles/', views.articleApi),
    # path('createarticle/', views.createArticleApi),
    path('articles1/', views.ArticleListView.as_view()),
    path('articles1/<int:pk>', views.ArticleDetailView.as_view()),

]
