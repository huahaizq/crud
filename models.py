from django.db import models

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    deptno = models.IntegerField()
# Create your models here.
