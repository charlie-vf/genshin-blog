from . import views
from django.urls import path


urlpatterns = [
    # url for index.html template view
    path('', views.PostList.as_view(), name='home'),
    # url for post_details.html template to view full post info
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
