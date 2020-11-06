from django.db import models

# Create your models here.


class UniversityModel(models.Model):
    """
    University Model contains id, name, address,
    district, state, pincode.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=False)
    address = models.TextField(null=False)
    district = models.CharField(max_length=256, null=False, db_index=True)
    state = models.CharField(max_length=256, null=False, db_index=True)
    pincode = models.CharField(max_length=128)

    def __int__(self):
        return self.id


class CollegeModel(models.Model):
    """
    College Model contains id, university, name, address,
    district, state, pincode.
    """
    id = models.AutoField(primary_key=True)
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=False)
    address = models.TextField(null=False)
    district = models.CharField(max_length=256, null=False, db_index=True)
    state = models.CharField(max_length=256, null=False,db_index=True)
    pincode = models.CharField(max_length=128)

    def __int__(self):
        return self.id


GENDER = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    )


class StudentModel(models.Model):
    """
    College Model contains id, university, name, address,
    district, state, pincode.
    """
    id = models.AutoField(primary_key=True)
    college = models.ForeignKey(CollegeModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=False)
    roll_number = models.CharField(max_length=128, null=False)
    gender = models.CharField(max_length=6, choices=GENDER, default="M")
    class_name = models.CharField(max_length=256, null=False,db_index=True)

    def __int__(self):
        return self.id