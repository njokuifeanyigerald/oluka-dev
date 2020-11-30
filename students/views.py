from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Student, Guardian, StudentMessages, Admission, WAEC
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *


def isValid(values):
    valid = True
    for value in values:
        if value == '':
            valid = False
    return valid

# Create your views here.


def load_student(request, title):

    try:
        student_data = Student.objects.get(student_email=request.user.email)
    except:
        student_data = False
    try:
        notification = student_data.studentmessages_set.all()
        notification_size = len(notification)
        # notification = StudentMessages.objects.filter(
        #     to__student_email=request.user.email)
    except:
        notification = False
        notification_size = False
    try:
        # admission = student_data.admission_set.get(student=student_data)
        admission = Admission.objects.get(
            student__student_email=request.user.email)
    except:
        admission = False


    context = {
        'title': title,
        'student': student_data,
        'notifications': notification,        
        'notifications_size': notification_size,
        'admission': admission,
    }

    return context


@login_required
def dashboard_view(request):
    context = load_student(request, 'Dashboard')
    print(context)
    return render(request, 'students/base.html', context)

@login_required
def crash_course_view(request):
    if request.method == 'POST':
        student_fname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone_number = request.POST.get('phoneNumber')
        level_of_edu = request.POST.get('levelOfEducation')
        inputStateOrigin = request.POST.get('inputStateOrigin')
        inputState = request.POST.get('inputState')
        gridCheck = request.POST.get('gridCheck')
        gridCheck = True if gridCheck else False
        dateOfBirth = request.POST.get('dateOfBirth')
        inputCourse = request.POST.get('inputCourse')
        inputAddress = request.POST.get('inputAddress')
        inputCity = request.POST.get('inputCity')
        levelOfEmployment = request.POST.get('levelOfEmployment')
        crash_course = "Crash Course"
        Coupon = request.POST.get('Coupon')
        EmployerName = request.POST.get('EmployerName')
        passport = request.POST.get('Passport')

        # if isValid([student_fname,gender,email, phone_number,level_of_edu,levelOfCourse1,levelOfCourse2,
        #         dateOfBirth,inputAddress,inputCity,nextOfKinFullName,
    #    nextOfKinEmail,nextOfKinPhoneNumber,nextOfKinAddress,nextOfKinRelationship]):
        student = Student(user=request.user, student_fname=student_fname, gender=gender, student_email=email, student_address=inputAddress,
                          student_phone=phone_number, highest_level_of_education=level_of_edu, dob=dateOfBirth, disability=gridCheck, state_of_origin=inputStateOrigin,
                          state_of_residence=inputState, city=inputCity, course_plan=crash_course, desired_course=inputCourse, employer_name=EmployerName,
                          employment_status=levelOfEmployment, referal_code=Coupon, image=passport
                          )
        student.save()
        return redirect('dashboard')

    context = load_student(request, 'Crash Course')

    return render(request, 'students/enroll-crash-course.html', context)

@login_required
def full_course_view(request):
    if request.method == 'POST':
        student_fname = request.POST.get('fullname')
        gender = request.POST.get("gender")
        email = request.POST.get('email')
        phone_number = request.POST.get('phoneNumber')
        level_of_edu = request.POST.get('levelOfEducation')
        inputStateOrigin = request.POST.get('inputStateOrigin')
        inputState = request.POST.get('inputState')
        levelOfCourse1 = request.POST.get('levelOfCourse1')
        levelOfCourse2 = request.POST.get('levelOfCourse2')
        gridCheck = request.POST.get('gridCheck')
        gridCheck = True if gridCheck else False
        dateOfBirth = request.POST.get('dateOfBirth')
        inputAddress = request.POST.get('inputAddress')
        inputCity = request.POST.get('inputCity')
        coursePlan = request.POST.get('coursePlan')
        passport = request.POST.get('Passport')
        # next of kin
        nextOfKinFullName = request.POST.get('nextOfKinFullName')
        nextOfKinEmail = request.POST.get('nextOfKinEmail')
        nextOfKinPhoneNumber = request.POST.get('nextOfKinPhoneNumber')
        nextOfKinAddress = request.POST.get('nextOfKinAddress')
        nextOfKinRelationship = request.POST.get('nextOfKinRelationship')

        if isValid([student_fname, gender, email, phone_number, level_of_edu, levelOfCourse1, levelOfCourse2,
                    dateOfBirth, inputAddress, inputCity, coursePlan, nextOfKinFullName,
                    nextOfKinEmail, nextOfKinPhoneNumber, nextOfKinAddress, nextOfKinRelationship]):
            student = Student(user=request.user, student_fname=student_fname, gender=gender, student_email=email, student_address=inputAddress,
                              student_phone=phone_number, highest_level_of_education=level_of_edu, dob=dateOfBirth, disability=gridCheck, state_of_origin=inputStateOrigin,
                              state_of_residence=inputState, city=inputCity, course_of_choice=levelOfCourse1, course_of_choice2=levelOfCourse2, course_plan=coursePlan,
                              nextOfKinFullName=nextOfKinFullName, nextOfKinEmail=nextOfKinEmail, nextOfKinAddress=nextOfKinAddress, nextOfKinPhone=nextOfKinPhoneNumber,
                              nextOfKinRelationship=nextOfKinRelationship, image=passport
                              )
            student.save()
            return redirect('upload_waec')

    context = {
        'title': 'Full Course'
    }
    return render(request, 'students/enroll-full-course.html', context)

@login_required
def enroll_view(request):
    context = load_student(request, 'Enroll')

    return render(request, 'students/enroll.html', context)

@login_required
def student_profile_view(request):
    context = load_student(request, 'Student Profile')

    return render(request, 'students/student/student-profile.html', context)

@login_required
def upload_waec_view(request):

    context = load_student(request, 'Uplaod WAEC')

    # if request.method == 'POST':
    #     waec = request.POST.get('WAEC')

    #     if isValid([waec]):
    #         student = WAEC(user=request.user, waec=waec)
    #         messages.success(request,f"{context['student'].student_fname} Your WAEC result was uploaded successsfully. Uplaod your JAMB")
    #         student.save()
    #         return redirect('upload_jamb')
    if request.method == 'POST':
        form = WAECForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # messages.success(
            #     request, f"{context['student'].student_fname} Your WAEC result was uploaded successsfully. Uplaod your JAMB")
            return render(request, 'students/student/upload-jamb.html', context)
    else:
        form = WAECForm()

    context['form'] = form

    return render(request, 'students/student/upload-waec.html', context)

@login_required
def upload_jamb_view(request):
    context = load_student(request, 'Uplaod JAMB')

    return render(request, 'students/student/upload-jamb.html', context)

@login_required
def upload_guardian_view(request):
    context = load_student(request, 'Guardian')
    return render(request, 'students/student/upload-guardian.html', context)

@login_required
def grade_view(request):
    context = load_student(request, 'Grade')

    return render(request, 'students/student/credentials/grade.html', context)


def profile_view(request):
    context = load_student(request, 'Profile')

    return render(request, 'students/student/credentials/update-profile.html', context)


# def login_view(request):
#     context = {
#         'title': 'Login'
#     }
#     return render(request, 'registration/login.html', context)


# def logout_view(request):
#     context = {
#         'title': 'Logout'
#     }
#     return render(request, 'students/logout.html', context)


# def register_view(request):
#     context = {
#         'title': 'Register'
#     }
#     return render(request, 'registration/register.html', context)
