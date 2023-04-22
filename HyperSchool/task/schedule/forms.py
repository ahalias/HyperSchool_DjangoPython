from django import forms
from schedule.models import Course



class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=True, label="Search",
        widget=forms.TextInput(attrs={'placeholder': 'Enter course name'}))

class AddStudentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter student's name"}))
    surname = forms.CharField(max_length=100, required=True, label="Surname",
        widget=forms.TextInput(attrs={'placeholder': "Enter student's surname"}))
    age = forms.IntegerField(required=True, label="Age")
    course = forms.ModelChoiceField(queryset=Course.objects.all())




