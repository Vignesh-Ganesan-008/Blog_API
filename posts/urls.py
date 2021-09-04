from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# <------------------- METHOD-1 & 2 ------------------->
# urlpatterns = [
#     path('posts/', views.postList),
#     path('post/<int:pk>', views.postDetail)
# ]

# <------------------- METHOD-3, 4 & 5 ------------------->
urlpatterns = format_suffix_patterns([
    path("", views.apiRoot),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user-detail')
])
