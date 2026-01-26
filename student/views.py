from django.shortcuts import render
from .models import Student

def student_form(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            number=request.POST['number'],
            degree=request.POST['degree'],
            query=request.POST['query']
        )
    return render(request, 'student_form.html')
