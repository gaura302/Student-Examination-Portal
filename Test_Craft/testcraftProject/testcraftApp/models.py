from django.db import models
class Questions(models.Model):
    qno = models.IntegerField(primary_key=True)
    qtext = models.CharField(max_length=200)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    subject = models.CharField(max_length=60)
    ans = models.CharField(max_length=200)
    class Meta :
        db_table = 'question'

class UserData(models.Model):
    username = models.CharField(max_length=30 , primary_key=True)
    password = models.CharField(max_length=250)
    mobno = models.BigIntegerField()
    class Meta :
        db_table = 'userdata'

class Result(models.Model):
    username = models.ForeignKey( UserData,  on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    score = models.IntegerField()
    class Meta:
        db_table = 'result'