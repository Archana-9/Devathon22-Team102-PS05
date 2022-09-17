import http
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from Issue_Resolver.models.issue import Issue
from Issue_Resolver.models.category import Category
from Issue_Resolver.models.student import Student
from Issue_Resolver.models.type import Type






class Index(View):
    def post(self , request):
        issue = request.POST.get('issue')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(issue)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(issue)
                    else:
                        cart[issue]  = quantity-1
                else:
                    cart[issue]  = quantity+1

            else:
                cart[issue] = 1
        else:
            cart = {}
            cart[issue] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')


    def get(self,request):
       cart = request.session.get('cart')
       if not cart:
          request.session['cart']={}
       issues=None
       categories=Category.get_all_categories();
       catagoryID=request.GET.get('category')
       
       typename='PUBLIC'
       typeID=Type.get_type_id_by_name(typename)
       if typeID:
           issues=Issue.get_all_issues_by_type_id(typeID)
    #    else:
    #        issues=Issue.get_all_issues();



    #    if catagoryID:
    #        issues=Issue.get_all_issues_by_category_id(catagoryID)
    #    else:
    #        issues=Issue.get_all_issues();

       data={}
       data['issues']=issues
       data['categories'] = categories
    #    print(request.session.get('email'))
       return render(request,'index.html',data)


 
 
    





 

 



 
    





 

 
