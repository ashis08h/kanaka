from django.contrib import admin

# Register your models here.
from students.models import UniversityModel, CollegeModel, StudentModel


class UniversityModelAdmin(admin.ModelAdmin):

    model = UniversityModel
    list_display = ['id', 'name', 'address', 'district', 'state', 'pincode']
    search_fields = ['name']


class CollegeModelAdmin(admin.ModelAdmin):

    model = CollegeModel
    list_display = ['id', 'name', 'address', 'university', 'district', 'state', 'pincode']
    search_fields = ['name']


class StudentModelAdmin(admin.ModelAdmin):

    model = StudentModel
    list_display = ['id', 'name', 'college', 'roll_number', 'class_name', 'gender']
    search_fields = ['name']


admin.site.register(UniversityModel, UniversityModelAdmin)
admin.site.register(CollegeModel, CollegeModelAdmin)
admin.site.register(StudentModel, StudentModelAdmin)