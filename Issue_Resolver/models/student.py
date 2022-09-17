from statistics import mode
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    hostel_name=models.CharField(max_length=50)
    room_no=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    
    def register(self):
        self.save()

    @staticmethod
    def get_student_by_email(email):
        try:
          return Student.objects.get(email=email)
        except:
            return False

    @staticmethod
    def find_room_no_by_id(id):
        try:
          return Student.objects.get(id=id)
        except:
            return False
            
    
    def isExists(self):
        if Student.objects.filter(email=self.email):
            return True
        
        return False