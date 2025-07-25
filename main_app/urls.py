from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name ='about'),
    path('courses/', views.course_index, name='course-index'),
    path('courses/<int:course_id>/', views.course_detail, name='course-detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='course-create'),
    path('course/<int:pk>/update/', views.CourseUpdate.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDelete.as_view(), name='course-delete'),
    path('course/<int:course_id>/add-location/', views.add_location, name='add-location'),
    path('professors/create/', views.ProfessorCreate.as_view(), name='professor-create'),
    path('professors/<int:pk>/', views.ProfessorDetail.as_view(), name='professor-detail'),
    path('professors/', views.ProfessorList.as_view(), name='professor-index'),
    path('professors/<int:pk>/update/', views.ProfessorUpdate.as_view(), name='professor-update'),
    path('professors/<int:pk>/delete/', views.ProfessorDelete.as_view(), name='professor-delete'),
    path('courses/<int:course_id>/associate-professor/<int:professor_id>/', views.associate_professor, name='associate-professor'),
    path('courses/<int:course_id>/remove-professor/<int:professor_id>/', views.remove_professor, name='remove-professor'),
    path('accounts/signup/', views.signup, name='signup'),

]
