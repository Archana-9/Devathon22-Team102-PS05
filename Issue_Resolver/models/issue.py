from unicodedata import category
from django.db import models
from Issue_Resolver.models.student import Student
from .category import Category
from .type import Type

# Create your models here.
class Issue(models.Model):
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,default=1)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    @staticmethod
    def get_all_issues():
        return Issue.objects.all()

    @staticmethod
    def get_issues_by_id(ids):
        return Issue.objects.filter(id__in=ids)

    
    @staticmethod
    def get_all_issues_by_category_id(category_id):
        if category_id:
            return Issue.objects.filter(category=category_id)
        else:
            return Issue.get_all_products();

        
    
    def get_all_issues_by_type_id(type_id):
        if type_id:
            return Issue.objects.filter(type=type_id)
        # else:
        #     return Issue.get_all_products();

      
    @staticmethod
    def delete_issue_by_id(issue_id):
        Issue.objects.filter(id=issue_id).delete()




    # @staticmethod
    # def get_all_issues():
    #     return Product.objects.all()

    # @staticmethod
    # def get_all_issues_by_type(issue_type):
    #     if category_id:
    #         return Issue.objects.filter(category=category_id)
    #     else:
    #         return Issue.get_all_products();

    # @staticmethod
    # def get_all_issues_by_category_id(category_id):
    #     if category_id:
    #         return Issue.objects.filter(category=category_id)
    #     else:
    #         return Issue.get_all_products();


    # @staticmethod
    # def get_issue_by_id(product):
    #         return Issue.objects.get(id=product)

    #  @staticmethod
    #  issue_type="PUBLIC"
    # def get_issue_by_type():
    #         return Issue.objects.get(id=product)
   
    
    @staticmethod
    def get_issues_by_student_id(student):
        return Issue.objects.filter(student=student)


   
            
