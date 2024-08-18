from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfilePostForm
from user_profile.models import Profile


def test(request):
    return render(request, template_name='profile/profile.html')

# Create your views here.
def home(request):
    return render(request, template_name='profile/home.html')

@login_required
def resume(request):
    return render(request, template_name='profile/resume.html')


def profile_dashboard(request):
    context= {}
    form = ProfilePostForm()
    if request.method == 'POST':
        fn = request.POST.get('first_name','')
        ln = request.POST.get('last_name','')
        img = request.POST.get('profile_image','')
        ads= request.POST.get('address','')
        phn = request.POST.get('phone_number','')
        em = request.POST.get('email','')
        lkd = request.POST.get('linkedin','')
        sum = request.POST.get('summary','')
        sk1 = request.POST.get('skill1','')
        sk2 = request.POST.get('skill2','')
        sk3 = request.POST.get('skill3','')
        sk4 = request.POST.get('skill4','')
        sk5 = request.POST.get('skill5','')
        sk6 = request.POST.get('skill6','')
        dgn = request.POST.get('designation','')
        fd = request.POST.get('from_date','')
        td = request.POST.get('to_date','')
        comn = request.POST.get('company_name','')
        cnty = request.POST.get('country','')
        jr1 = request.POST.get('job_role1','')
        jr2 = request.POST.get('job_role2','')
        jr3 = request.POST.get('job_role3','')
        jr4 = request.POST.get('job_role4','')
        jr5 = request.POST.get('job_role5','')
        lan1 = request.POST.get('language1','')
        lan2 = request.POST.get('language2','')
        lan3 = request.POST.get('language3','')
        hb1 = request.POST.get('hobbies1','')
        hb2 = request.POST.get('hobbies2','')
        hb3 = request.POST.get('hobbies3','')
        hb4 = request.POST.get('hobbies4','')
        dg = request.POST.get('degree','')
        sub = request.POST.get('subject','')
        inst = request.POST.get('institute_name','')
        pasy = request.POST.get('passing_year','')
        cntyn = request.POST.get('country_name','')
        cern1 = request.POST.get('certificate_name1','')
        cor1 = request.POST.get('course1','')
        cern2 = request.POST.get('certificate_name2','')
        cor2 = request.POST.get('course2','')

        pf= Profile(user=request.user,first_name=fn, last_name=ln, profile_image=img, address=ads, phone_number=phn, email=em, linkedin=lkd, summary=sum, skill1=sk1, skill2=sk2, skill3=sk3, skill4=sk4, skill5=sk5, skill6=sk6, designation=dgn, from_date=fd, to_date=td, company_name=comn, country=cnty, job_role1=jr1, job_role2=jr2, job_role3=jr3, job_role4=jr4, job_role5=jr5, language1=lan1, language2=lan2, language3=lan3, hobbies1=hb1, hobbies2=hb2, hobbies3=hb3, hobbies4=hb4, degree=dg, subject=sub, institute_name=inst, passing_year=pasy, country_name=cntyn, certificate_name1=cern1, course1=cor1, certificate_name2=cern2, course2=cor2)
       
        pf.save()
        messages.info(request, "Profile is created successfully!")
        return redirect('profile_dashboard')
    profile_data  = Profile.objects.filter(user_id = request.user.id)
    context = {
        'form': form,
        'profile': profile_data
    }
    print("asdasdasdads",profile_data)
    
    # if len(profile_data) > 0:
    #     context['profile']= profile_data[0]
    #     print("data",profile_data)
    
    return render(request, template_name='profile/profiledashboard.html', context=context)


@login_required
def user_list(request):
    return render(request, template_name='profile/userlist.html')


def sign_up(request):

    if request.method == 'POST':

        username = request.POST.get('username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email)
                user.save()
                
                return redirect('login')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('signup')
    else:
        return render(request, 'profile/signup.html')
    

def log_in(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_dashboard')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('login')

    return render(request, 'profile/login.html')


def sign_out(request):
    logout(request)
    return redirect('home')  