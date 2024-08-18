from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from job_feed.models import JobPost
from job_feed.models import JobApply
from .forms import JobPostForm
from .forms import JobApplyForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def hirepost(request):
    form = JobPostForm()

    if request.method == 'POST':
        nm = request.POST.get('name','')
        typ = request.POST.get('type','')
        tt= request.POST.get('title','')
        dsp = request.POST.get('description','')
        fdsp = request.POST.get('fulldescription','')
        wk = request.POST.get('work','')
        em = request.POST.get('email','')
        ads = request.POST.get('address','')
        sr = request.POST.get('sector','')
        exp = request.POST.get('experience','')
        pn = request.POST.get('position','')
        dt = request.POST.get('date','')

        jp = JobPost(name=nm, type=typ, title=tt, description=dsp, fulldescription=fdsp, work=wk, email=em, address=ads, sector=sr, experience=exp, position=pn, date=dt)
        
        jp.save()
        messages.info(request, "Job hiring post is created successfully!")
        return redirect('home')
    context ={
        'form': form
    }
    return render(request, 'job/jobhire.html', context)

@login_required
def createcircular(request):
    form = JobPostForm()

    if request.method == 'POST':
        nm = request.POST.get('name','')
        typ = request.POST.get('type','')
        tt= request.POST.get('title','')
        dsp = request.POST.get('description','')
        fdsp = request.POST.get('fulldescription','')
        wk = request.POST.get('work','')
        em = request.POST.get('email','')
        ads = request.POST.get('address','')
        sr = request.POST.get('sector','')
        exp = request.POST.get('experience','')
        pn = request.POST.get('position','')
        dt = request.POST.get('date','')

        jp = JobPost(name=nm, type=typ, title=tt, description=dsp, fulldescription=fdsp, work=wk, email=em, address=ads, sector=sr, experience=exp, position=pn, date=dt)
        
        jp.save()
        messages.info(request, "Job hiring post is created successfully!")
        return redirect('home')
    context ={
        'form': form
    }
    return render(request, 'job/createcircular.html', context)


@login_required
def jobapply(request):
    form = JobApplyForm()

    if request.method == 'POST':
  
        lt = request.POST.get('letter','')

        ja = JobApply(letter=lt)

        ja.save()
        messages.info(request, "Job apply post is created successfully!")
        return redirect('home')

    dict ={
        'form': form
    }
    return render(request, template_name='job/jobapply.html', context=dict)


def jobcircular(request):
    return render(request, template_name='job/jobcircular.html')

@login_required
def job(request):
    return render(request, template_name='job/myjob.html')

@login_required
def jobinterset(request):
    return render(request, template_name='job/jobinterest.html')

@login_required
def joblist(request):
    return render(request, template_name='job/joblist.html')

@login_required
def jobrequest(request):
    return render(request, template_name='job/jobrequest.html')
