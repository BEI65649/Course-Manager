from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Course, Professor
from .forms import LocationForm, UserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




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
      

class Home(LoginView):
    template_name = 'home.html'


def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

@login_required
def course_index(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'courses/index.html', {'courses': courses,})

@login_required
def course_detail(request, course_id):
    try:
        course = Course.objects.get(user=request.user, id=course_id)
    except Course.DoesNotExist:
        return redirect('course_create')
    professors = Professor.objects.all() 
    professors_course_doesnt_have = Professor.objects.exclude(id__in = course.professors.all().values_list('id')) # Fetch all toys
    location_form = LocationForm()
    return render(request, 'courses/detail.html', {
        # include the cat and feeding_form in the context
        'course': course, 'location_form': location_form,
        'professors': professors_course_doesnt_have  # send those toys
    })

class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['name', 'term', 'description', 'year']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)


class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['term', 'description', 'year']

class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = '/courses/'

@login_required   
def add_location(request, course_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.course_id = course_id
        new_location.save()
    return redirect('course-detail', course_id=course_id)

class ProfessorCreate(LoginRequiredMixin, CreateView):
    model = Professor
    fields = '__all__'

class ProfessorList(LoginRequiredMixin, ListView):
    model = Professor

class ProfessorDetail(LoginRequiredMixin, DetailView):
    model = Professor

class ProfessorUpdate(LoginRequiredMixin, UpdateView):
    model = Professor
    fields = ['name', 'bio']

class ProfessorDelete(LoginRequiredMixin, DeleteView):
    model = Professor
    success_url = '/professors/'

@login_required
def associate_professor(request, course_id, professor_id):
    course = Course.objects.get(id=course_id)
    professor = Professor.objects.get(id=professor_id)
    course.professors.add(professor)
    return redirect('course-detail', course_id=course_id)

# def associate_professor(request, course_id, professor_id):
#     Course.objects.get(id=course_id).professors.add(professor_id)
#     return redirect('course-detail', course_id=course_id)

@login_required
def remove_professor(request, course_id, professor_id):
    Course.objects.get(id=course_id).professors.remove(professor_id)
    return redirect('course-detail', course_id=course_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
 
