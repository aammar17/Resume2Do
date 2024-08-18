from django import forms
from .models import Profile

class ProfilePostForm(forms.ModelForm):

    class Meta:
        model = Profile
        #fields = "__all__" 
        fields = ('first_name', 'last_name', 'profile_image', 'address', 'phone_number', 'email', 'linkedin', 'summary', 'skill1', 'skill2', 'skill3', 'skill4', 'skill4', 'skill6', 'designation', 'to_date', 'from_date', 'company_name', 'country', 'job_role1', 'job_role2', 'job_role3', 'job_role4', 'job_role5', 'language1', 'language2', 'language3', 'hobbies1', 'hobbies2', 'hobbies3', 'hobbies4', 'degree', 'subject', 'institute_name', 'passing_year', 'country_name', 'certificate_name1', 'course1', 'certificate_name2', 'course2')


