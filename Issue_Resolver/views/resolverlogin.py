from django.shortcuts import render,redirect,HttpResponseRedirect
from Issue_Resolver.models.student import Student
from django.contrib.auth.hashers import check_password
from django.views import View


class Resolverlogin(View):
    return_url=None
    def get(self,request):
        return render(request,'resolverlogin.html')
        
  


 