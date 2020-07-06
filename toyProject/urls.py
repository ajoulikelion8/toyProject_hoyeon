from django.contrib import admin
from django.urls import path
import account.views
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.home, name='home'),
    path('account/signup/', account.views.signup, name='signup'),
    path('account/login/', account.views.login, name='login'),
    path('account/logout/', account.views.logout, name='logout'),
    path('crud/newblog/', crud.views.create, name='newblog'),
    path('crud/update/<int:pk>', crud.views.update, name='update'),
    path('crud/delete/<int:pk>', crud.views.delete, name='delete'),
    
]
