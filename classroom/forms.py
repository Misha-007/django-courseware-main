from dataclasses import field
from django import forms
from ckeditor.widgets import CKEditorWidget

from classroom.models import ATTENDANCE_CHOICES, Course, Category,Schedule,Attendance

class NewCourseForm(forms.ModelForm):
	picture = forms.ImageField(required=True)
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	description = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	category = forms.ModelChoiceField(queryset=Category.objects.all())
	syllabus = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Course
		fields = ('picture', 'title', 'description', 'category', 'syllabus')

class NewScheduleForm(forms.ModelForm):
	title = forms.CharField(required=True,max_length=200)
	date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}),required=True)
	start_time = forms.TimeField(widget=forms.widgets.DateInput(attrs={'type': 'time','class':'timepicker'}),required=True)
	end_time = forms.TimeField(widget=forms.widgets.DateInput(attrs={'type': 'time'}),required=True)
	
	class Meta:
		model = Schedule
		fields = ('title','date','start_time','end_time')

class NewAttendanceForm(forms.ModelForm):
	status = forms.ChoiceField(required=True,choices=ATTENDANCE_CHOICES)
	class Meta:
		model = Attendance
		fields = ('status',)
