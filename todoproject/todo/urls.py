from django.urls import path 
from .views import MyTodoApView, TaskList, MyTodoDetail, TaskUpdate, DeleteTask, SignInTask, RegisterUser
from django.contrib.auth.views import LogoutView




urlpatterns = [
   path('Singup/', RegisterUser.as_view(), name = "Signup-page"),
   path('Login/', SignInTask.as_view(), name = "login-page"),
   path('logout/', LogoutView.as_view(next_page="login-page"), name = "logout"),
   path('', MyTodoApView.as_view(), name= "home"),
   path("tasklist/", TaskList.as_view(), name="Task List"),
   path('details/<pk>/', MyTodoDetail.as_view(), name="details"),
   path("update/<pk>/", TaskUpdate.as_view(), name="update"),
   path("delete/<pk>/", DeleteTask.as_view(),name="delete")
]
