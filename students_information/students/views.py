from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.exceptions import MethodNotAllowed

from .models import UniversityModel, CollegeModel, StudentModel


def login(request):
    '''Shows a login form.'''

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username is not None and password is not None:
            user = auth.authenticate(username=username, password=password)
        else:
            error_message = "Username or Password is missing."
            return redirect(error, error_message)

        if user is not None and user.is_active:
            auth.login(request, user)
            success_message = "Login successful!"
            return redirect(success, success_message)
        else:
            error_message = "Invalid Login, Username or Password is missing."
            return redirect(error, error_message)

    # if not POST then return login form
    return render(request, "index.html")


def error(request, error_message):
    """
    Method to display error messages.
    :param request:
    :param error_message:
    :return:
    """
    return render(request, 'error.html', {'error_message': error_message})


def success(request, success_message):
    """
    Method to display success message.
    :param request:
    :param success_message:
    :return:
    """
    return render(request, 'success.html', {'success_message': success_message})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def create_university_form(request):
    """
    Method to display Create/Update form
    """
    return render(request, 'create_university.html')


def create_university(request):
    """
    Method to create university details.
    :param request:
    :return:
    """
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        university_qs = None

        if name is None:
            return HttpResponse(status=400, content="name is required.")
        username = name.replace(" ", "")

        if address is None:
            return HttpResponse(status=400, content="address is required.")

        if district is None:
            return HttpResponse(status=400, content="district is required.")

        if state is None:
            return HttpResponse(status=400, content="state is required.")

        if pincode is None:
            return HttpResponse(status=400, content="pincode is required.")

        try:
            university_qs = UniversityModel.objects.get(name=name)
        except UniversityModel.DoesNotExist:
            pass

        university_qs = UniversityModel(name=str(name),
                    district=str(district),
                    address=str(address),
                    state=str(state),
                    pincode=str(pincode)).save()

        print(university_qs)

        success_message = "University created successfully."
        return redirect(success, success_message)
        # return HttpResponse(status=200, content="University created successfully.",)

    raise MethodNotAllowed


def fetch_univesity_list(request):
    """
    Method to get list of universities
    :param request:
    :return:
    """

    university_qs = None
    total_university_count = 0
    search_university_qs = None
    name = None

    name = request.GET.get('name')
    if request.method == "POST":
        name = request.POST.get("name")

    print(name)

    if name is not None:
        university_qs = UniversityModel.objects.filter(name__icontains=name).order_by('id')
    else:
        university_qs = UniversityModel.objects.all().order_by('id')

    if university_qs is not None and university_qs.exists:
        total_university_count = university_qs.count()

    page_size = 5
    page = request.GET.get('page', 1)
    if page is not None:
        current_page = int(page)

    paginator = Paginator(university_qs, page_size)
    try:
        universities = paginator.page(page)
    except PageNotAnInteger:
        universities = paginator.page(1)
    except EmptyPage:
        universities = paginator.page(paginator.num_pages)

    print(paginator.num_pages)
    start_index = (current_page - 1) * page_size + 1
    last_index = current_page * page_size
    if current_page == paginator.num_pages:
        last_index = total_university_count

    context = {
        'universities': universities,
        'total_university_count': total_university_count,
        'name': name,
        'start_index': start_index,
        'last_index': last_index,
    }

    return render(request, 'university.html', context)


def fetch_college_list(request):
    """
    Method to get list of colleges
    :param request:
    :return:
    """

    college_qs = None
    total_college_count = 0
    search_college_qs = None
    name = None
    id = None

    id = request.GET.get(id)
    if request.method == "POST":
        name = request.POST.get("name")

    

    if name is not None:
        college_qs = CollegeModel.objects.filter(name__contains=name).order_by('id')
    else:
        college_qs = CollegeModel.objects.all().order_by('id')

    if college_qs is not None and college_qs.exists:
        total_college_count = college_qs.count()

    print(college_qs)

    page_size = 5
    page = request.GET.get('page', 1)
    if page is not None:
        current_page = int(page)
    page = request.GET.get('page', 1)

    paginator = Paginator(college_qs, page_size)
    try:
        colleges = paginator.page(page)
    except PageNotAnInteger:
        colleges = paginator.page(1)
    except EmptyPage:
        colleges = paginator.page(paginator.num_pages)

    print(paginator.num_pages)
    start_index = (current_page - 1) * page_size + 1
    last_index = current_page * page_size
    if current_page == paginator.num_pages:
        last_index = total_college_count

    context = {
        'colleges': colleges,
        'total_university_count': total_college_count,
        'start_index': start_index,
        'last_index': last_index,

    }

    return render(request, 'college.html', context)


def fetch_student_list(request):
    """
    Method to get list of students
    :param request:
    :return:
    """

    student_qs = None
    total_student_count = 0
    search_student_qs = None
    name = None
    if request.method == "POST":
        name = request.POST.get("name")

    if name is not None:
        student_qs = StudentModel.objects.filter(name__contains=name).order_by('id')
    else:
        student_qs = StudentModel.objects.all().order_by('id')

    if student_qs is not None and student_qs.exists:
        total_college_count = student_qs.count()

    print(student_qs)

    page_size = 5
    page = request.GET.get('page', 1)
    if page is not None:
        current_page = int(page)
    page = request.GET.get('page', 1)

    paginator = Paginator(student_qs, page_size)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    print(paginator.num_pages)
    start_index = (current_page - 1) * page_size + 1
    last_index = current_page * page_size
    if current_page == paginator.num_pages:
        last_index = total_student_count

    context = {
        'students': students,
        'total_student_count': total_student_count,
        'start_index': start_index,
        'last_index': last_index,

    }

    return render(request, 'student.html', context)














