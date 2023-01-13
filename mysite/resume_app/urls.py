from django.contrib import admin
from django.urls import include, path


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/download/<int:id>/',
         views.download_resume, name='download_resume'),
    path('resume/<int:id>/', views.single_resume, name='single_resume'),
    path('resume/', views.create_resume, name='create_resume'),
    path('resumes/', views.resumes_list, name='resumes_list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.create_resume, name='create_resume'),
]
