from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    path('courses/', views.course_index, name='course-index'),
    path('courses/<int:course_id>/', views.course_detail, name='course-detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='course-create'),
    path('course/<int:pk>/update/', views.CourseUpdate.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDelete.as_view(), name='course-delete'),
    path('course/<int:course_id>/add-location/', views.add_location, name='add-location'),
]
