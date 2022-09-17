from email.mime import image
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from django.views import  View
from django.core.files.storage import FileSystemStorage
from Issue_Resolver.models.issue import  Issue


 

class Myissues(View):
    def get(self ,request):
        student=request.session.get('student')
        issues = Issue.get_issues_by_student_id(student)
        return render(request , 'myissues.html' , {'issues' : issues} )

    def post(self ,request):
          issue_id=request.POST.get('issue')
          Issue.delete_issue_by_id(issue_id)
          student=request.session.get('student')
          issues = Issue.get_issues_by_student_id(student)
          return render(request , 'myissues.html' , {'issues' : issues} )


     
         
   

     