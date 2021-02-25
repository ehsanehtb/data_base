from django.db import models

# Create your models here.
class Blood_TC(models.Model):
    branch_ID = models.IntegerField(primary_key=True)
    branch_name = models.CharField(max_length=30)
    branch_kind = models.CharField(max_length=30)
    established = models.DateField(blank=True)
    capacity = models.IntegerField(blank=True)
    postcode = models.BigIntegerField()
    province = models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=30,blank=True)
    district = models.CharField(max_length=30,blank=True)
    street = models.CharField(max_length=30,blank=True)
    alley = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.branch_name

class Employee(models.Model):
    employee_ID = models.IntegerField(primary_key=True)
    branch_ID = models.ForeignKey(Blood_TC,related_name='employees',on_delete=models.CASCADE,default=0)
    blo_branch_ID = models.ForeignKey(Blood_TC,related_name='employees1',on_delete=models.CASCADE,default=0)
    national_ID = models.BigIntegerField()
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True)
    hiring_date = models.DateField(blank=True)
    work_place = models.CharField(max_length=60,blank=True)
    post = models.CharField(max_length=30)
    phone_num = models.IntegerField(blank=True)
    province = models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=30,blank=True)
    district = models.CharField(max_length=30,blank=True)
    street = models.CharField(max_length=30,blank=True)
    alley = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    employee_ID = models.ForeignKey(Employee,related_name='doctors',on_delete=models.CASCADE,default=0)
    med_sys_ID = models.IntegerField(primary_key=True)
    specialist = models.CharField(max_length=30,blank=True)
    hospital_name = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.specialist




class Donator(models.Model):
    employee_ID = models.ForeignKey(Employee,related_name='don_em',on_delete=models.CASCADE,default=0)
    med_sys_ID = models.ForeignKey(Doctor,related_name='don_doc',on_delete=models.CASCADE,default=0)
    donator_num = models.IntegerField(primary_key=True)
    national_ID = models.IntegerField()
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    birth_date = models.DateField()
    blood_type = models.CharField(max_length=30)
    deseas_rec = models.CharField(max_length=100)
    vital_signs = models.CharField(max_length=100)
    gender = models.BooleanField()
    wieght = models.IntegerField()
    phone_num = models.IntegerField()
    postcode = models.IntegerField()
    consent = models.BooleanField()
    province = models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=30,blank=True)
    district = models.CharField(max_length=30,blank=True)
    street = models.CharField(max_length=30,blank=True)
    alley = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.name

class Blood(models.Model):
    employee_ID = models.ForeignKey(Employee,related_name='blood_em',on_delete=models.CASCADE,default=0)
    med_sys_ID = models.ForeignKey(Doctor,related_name='blood_doc',on_delete=models.CASCADE,default=0)
    donator_num = models.ForeignKey(Donator,related_name='blood_don',on_delete=models.CASCADE,default=0)
    bar_code = models.IntegerField(primary_key=True)
    branch_ID = models.ForeignKey(Blood_TC,related_name='blood_btc',on_delete=models.CASCADE,default=0)
    blood_type = models.CharField(max_length=20)
    donation_date = models.DateField()
    hemoglobin_lvl = models.IntegerField()
    health_status = models.CharField(max_length=100)

    def __str__(self):
        return self.blood_type
