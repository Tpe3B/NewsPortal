from django.urls import path
from django.urls import path


from .views import PostsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe

urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('article/create/', PostCreate.as_view(), name='article_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='article_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

]
