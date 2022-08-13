from django.urls import path

from .views import AppListView, AppDetailView, PostListView, PostDetailView

urlpatterns = [
    path('', AppListView.as_view(), name='app_list'),
    path('<int:pk>/', AppDetailView.as_view(), name='app_detail'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]