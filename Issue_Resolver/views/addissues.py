import http
from django.views import View
from django.db import models
from unicodedata import category
from django.shortcuts import render,redirect
from Issue_Resolver.models.issue import Issue
from Issue_Resolver.models.category import Category
from Issue_Resolver.models.plumber import Plumber
from Issue_Resolver.models.type import Type
from Issue_Resolver.models.stat import Stat
from Issue_Resolver.models.student import Student

 
class Addissues(View):
    def get(self,request):
       categories = Category.get_all_categories()
       types=Type.get_all_types()
       return render(request , 'addissues.html'  , {'categories' : categories,'types' : types})
      

 
    def post(self,request):
        name=request.POST.get('description')
        category_name=request.POST.get('category')
        type_name=request.POST.get('type')
        
        category= Category.get_category_id_by_name(category_name)
        type= Type.get_type_id_by_name(type_name)

        print(category)

        

        description=request.POST.get('description')

         
        student = request.session.get('student')
      
        issue=Issue(description=description,category=Category(id=category),
                        type=Type(id=type),
                        student=Student(id=student))

        issue.save()


        if category_name == 'PLUMBER':
            date = models.DateTimeField(auto_now_add=True)

            stat=Stat.find_stat_no_by_name('PENDING')

            room_no=Student.find_room_no_by_id(student)

            # statname=Stat.find_name_by_id(stat)

            plumber=Plumber(description=description,room=room_no,date=date,stat=stat)
            
            plumber.save()


        return redirect('homepage')

    
    

 
    
    

 