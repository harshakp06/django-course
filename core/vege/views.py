from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum
# Create your views here.

@login_required(login_url='/login')
def receipes(request):
    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get("receipe_image")
        # receipe_image = data.get("receipe_image")

        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        # print(receipe_name)
        # print(receipe_description)
        # print(receipe_image)

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description
        )

        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))



    context = {'receipes': queryset}
    
    return render(request, 'receipes.html' , context)



@login_required(login_url='/login')
def delete_receipe(request,id):
    # print(id)
    # return  HttpResponse(f"The ID {id} is deleted")
    
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

@login_required(login_url='/login')
def update_receipe(request, id):

    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get("receipe_image")
        # receipe_image = data.get("receipe_image")

        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        queryset.receipe_name =receipe_name
        queryset.receipe_description =receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')

    context = {'receipe': queryset}
    

    return render(request, 'update_receipes.html', context)


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login')
        
        else:
            login(request, user)
            return redirect('/receipes/')
        

        



    return render(request, "login.html")

@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')


def register(request):  # sourcery skip: last-if-guard

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request,"Username already taken")
            return redirect('/register/')



        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Sucessfully ')
        
        return redirect('/register/')


    return render(request, "register.html")



def get_students(request):
    queryset = Student.objects.all()

    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
    
    for rank in ranks:
        print(rank.marks)

    if request.GET.get("search"):
        serach = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains=serach) |
            Q(department__department__icontains=serach) |
            Q(student_id__student_id__icontains=serach) |
            Q(student_email__icontains=serach) 
            )

    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)



    return render(request,'report/students.html' ,{'queryset': page_obj})




def see_marks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    # print(queryset.)
    # print(queryset.student)

    # current_rank = next(
    #     (i for rank in ranks if student_id == rank.student_id.student_id), -1
    # )

    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i=1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            current_rank =i
            break
        i+=1

    # name = Student.objects.get(student_id=student_id)
    # print(name)
    return render(request, 'report/see_marks.html',{'queryset': queryset,'total_marks':total_marks,'current_rank':current_rank})
