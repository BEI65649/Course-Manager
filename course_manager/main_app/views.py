from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Course, Location
from .forms import LocationForm




# class Course:
#       def __init__(self, name, term, description, year):
#         self.name = name
#         self.term = term
#         self.description = description
#         self.year = year

# courses = [
#     Course('English101', 'Summer', 'Intro to Literature.', 2025),
#     Course('Programming101', 'Spring', 'Intro to Programming in Python.', 2026),
#     Course('Mathmatics201', 'Winter', 'Intermediate Geometry.', 2025),
#     Course('Physics101', 'Fall', 'Intro to Physics.', 2025)
# ]        

def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

def course_index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    location_form = LocationForm()
    return render(request, 'courses/detail.html', {'course': course, 'location_form' : location_form })

class CourseCreate(CreateView):
    model = Course
    fields = '__all__'

class CourseUpdate(UpdateView):
    model = Course
    fields = ['term', 'description', 'year']

class CourseDelete(DeleteView):
    model = Course
    success_url = '/courses/'

   
def add_location(request, course_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.course_id = course_id
        new_location.save()
    return redirect('course-detail', course_id=course_id)
