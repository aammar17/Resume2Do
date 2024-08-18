from django.urls import path
from . import views

urlpatterns = [
    path('jobhire/', views.hirepost, name="hirepost"),
    path('createcircular/', views.createcircular, name="createcircular"),
    path('jobapply/', views.jobapply, name="jobapply"),
    path('jobcircular/', views.jobcircular, name="jobcircular"),
    path('job/', views.job, name="job"),
    path('jobinterset/', views.jobinterset, name="jobinterset"),
    path('joblist/', views.joblist, name="joblist"),
    path('jobrequest/', views.jobrequest, name="jobrequest"),
]
