from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



CAMPUS = (
    ('LA', 'Los Angeles'),
    ('HTX', 'Houston'),
    ('NY', 'New York')
)


class Professor(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('professor-detail', kwargs={'pk': self.id})


class Course(models.Model):
    name = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    professors = models.ManyToManyField(Professor)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'course_id': self.id})
    


class Location(models.Model):
    campus = models.CharField(max_length=3,
        choices=CAMPUS,
        default=CAMPUS[0][0]
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_campus_display()}"



