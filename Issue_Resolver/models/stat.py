from django.db import models

class Stat(models.Model):
    statname=models.CharField(max_length=20,default='PENDING')

   
    @staticmethod
    def get_all_types():
        return Stat.objects.all()

    @staticmethod
    def find_stat_no_by_name(statname):
        return Stat.objects.get(statname=statname)
        # return statname.id 

    # @staticmethod
    # def find_name_by_id(id):
    #     statname=Stat.objects.get(id=id)
    #     return statname.statname
    


    def __str__(self):
        return  self.statname


