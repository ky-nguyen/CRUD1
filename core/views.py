from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *
# Create your views here.


class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html',
                      {'stu_data': stu_data}
                      )
        
class Add_Student(View):
     def get(self, request):
         fm = AddStudentForm()
         return render(request, 'core/add_student.html',
                       {'fm': fm}
                       );  
         
     def post(self, request):
         fm = AddStudentForm(request.POST)   
         if fm.is_valid():
             fm.save()
             return redirect('/')
         else:
             return render(request, 'core/add_student.html',
                       {'fm': fm}
                       );  

class Delete_Student(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')
        
class Edit_Student(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'core/edit-student.html',
                      {'fm': fm}
                      )
        
    def post(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')