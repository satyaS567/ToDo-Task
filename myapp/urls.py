
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('signup',views.signup,name='signup'),
    path('addtask',views.addtask,name='addtask'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
]