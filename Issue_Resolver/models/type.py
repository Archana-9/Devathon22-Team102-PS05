from django.db import models

class Type(models.Model):
    typename=models.CharField(max_length=20)

   
    @staticmethod
    def get_all_types():
        return Type.objects.all()


    
    @staticmethod
    def get_type_id_by_name(typename):
        typename=Type.objects.get(typename=typename)
        return typename.id 

 

    def __str__(self):
        return  self.typename


