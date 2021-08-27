from User import views
from django.urls import path
urlpatterns =[
    path('',views.index,name='signup'),
    path('login/',views.User_login,name='login'),
    path('post/',views.post,name='post'),
    path('logout/',views.user_logout,name='logout'),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('edit/',views.editPost,name='edit'),
    path('delete/',views.del_user, name='delete'),
    ]