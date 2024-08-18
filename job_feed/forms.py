from django import forms
from .models import JobPost, JobApply

class JobPostForm(forms.ModelForm):

    class Meta:
        model = JobPost
        #fields = "__all__" 
        fields = ('name', 'type', 'title', 'description', 'fulldescription', 'work', 'email', 'address', 'sector', 'experience', 'position', 'date')

class JobApplyForm(forms.ModelForm):

    class Meta:
        model = JobApply
        fields = "__all__" 
        #fields = ('letter',)