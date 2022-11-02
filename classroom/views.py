from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from classroom.models import Course, Category, Grade,Schedule,Attendance

from classroom.forms import NewCourseForm,NewScheduleForm,NewAttendanceForm


# Create your views here.

@login_required
def index(request):
	user = request.user
	courses = Course.objects.filter(enrolled=user)
	teacher_mode = False
	if user.groups.filter(name='Teacher'):
		teacher_mode = True
		return redirect('my-courses')
	context = {
		'courses': courses,
		'teacher_mode':teacher_mode,
	}
	return render(request, 'index.html', context)

def Categories(request):
	user = request.user
	teacher_mode = False
	categories = Category.objects.all()
	if user.groups.filter(name='Teacher'):
		teacher_mode = True
	context = {
		'categories': categories,
		'teacher_mode':teacher_mode,
	}
	return render(request, 'classroom/categories.html', context)

def CategoryCourses(request, category_slug):
	user = request.user
	teacher_mode = False
	category = get_object_or_404(Category, slug=category_slug)
	courses = Course.objects.filter(category=category)
	if user.groups.filter(name='Teacher'):
		teacher_mode = True

	context = {
		'category': category,
		'courses': courses,
		'teacher_mode':teacher_mode,
	}
	return render(request, 'classroom/categorycourses.html', context)

@login_required
def NewCourse(request):
	user = request.user
	teacher_mode = False
	if user.groups.filter(name='Teacher'):
		teacher_mode = True
	if request.method == 'POST':
		form = NewCourseForm(request.POST, request.FILES)
		if form.is_valid():
			picture = form.cleaned_data.get('picture')
			title = form.cleaned_data.get('title')
			description = form.cleaned_data.get('description')
			category = form.cleaned_data.get('category')
			syllabus = form.cleaned_data.get('syllabus')
			Course.objects.create(picture=picture, title=title, description=description, category=category, syllabus=syllabus, user=user)
			return redirect('my-courses')
	else:
		form = NewCourseForm()

	context = {
		'form': form,
		'teacher_mode':teacher_mode,
	}

	return render(request, 'classroom/newcourse.html', context)

@login_required
def CourseDetail(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	teacher_mode = False

	if user.groups.filter(name='Teacher'):
		teacher_mode = True

	context = {
		'course': course,
		'teacher_mode': teacher_mode,
	}

	return render(request, 'classroom/course.html', context)



@login_required
def Enroll(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	course.enrolled.add(user)
	return redirect('index')

@login_required
def DeleteCourse(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)

	if user != course.user:
		return HttpResponseForbidden()
	else:
		course.delete()
	return redirect('my-courses')


@login_required
def EditCourse(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)

	if user != course.user:
		return HttpResponseForbidden()

	else:
		if request.method == 'POST':
			form = NewCourseForm(request.POST, request.FILES, instance=course)
			if form.is_valid():
				course.picture = form.cleaned_data.get('picture')
				course.title = form.cleaned_data.get('title')
				course.description = form.cleaned_data.get('description')
				course.category = form.cleaned_data.get('category')
				course.syllabus = form.cleaned_data.get('syllabus')
				course.save()
				return redirect('my-courses')
		else:
			form = NewCourseForm(instance=course)

	context = {
		'form': form,
		'course': course
	}

	return render(request, 'classroom/editcourse.html', context)


def MyCourses(request):
	user = request.user
	courses = Course.objects.filter(user=user)
	teacher_mode = False
	if user.groups.filter(name='Teacher'):
		teacher_mode = True

	context = {
		'courses': courses,
		'teacher_mode': teacher_mode,
	}

	return render(request, 'classroom/mycourses.html', context)


def Submissions(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	grades = Grade.objects.filter(course=course, submission__user=user)
	teacher_mode = False
	if user.groups.filter(name='Teacher'):
		teacher_mode = True
	context = {
		'grades': grades,
		'course': course,
		'teacher_mode': teacher_mode,
	}
	return render(request, 'classroom/submissions.html', context)

def StudentSubmissions(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	if user != course.user:
		return HttpResponseForbidden()
	else:
		grades = Grade.objects.filter(course=course)
		context = {
			'course': course,
			'grades': grades,
		}
	return render(request,'classroom/studentgrades.html', context)

def StudentSchedules(request, course_id):
	user = request.user
	course = get_object_or_404(Course,id=course_id)
	teacher_mode = False
	if user.groups.filter(name='Teacher'):
		teacher_mode = True
	if user !=course.user:
		return HttpResponseForbidden()
	else:
		schedules = Schedule.objects.filter(course=course)
		context = {
			'course': course,
			'schedules': schedules,
			'teacher_mode': teacher_mode,
		}
	return render(request,'classroom/studentschedules.html', context)

def NewSchedule(request, course_id,):
	user = request.user
	course = get_object_or_404(Course, id=course_id)

	if user != course.user:
		return HttpResponseForbidden()
	else:
		if request.method == 'POST':
			form = NewScheduleForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data.get('title')
				date = form.cleaned_data.get('date')
				start_time = form.cleaned_data.get('start_time')
				end_time = form.cleaned_data.get('end_time')
				m = Schedule.objects.create(course=course, title=title, adviser=user,date=date,start_time=start_time,end_time=end_time)
				m.save()
				return redirect('student-schedules', course_id=course_id)
		else:
			form = NewScheduleForm()

	context = {
		'form': form,
		'course':course
	}

	return render(request, 'classroom/newschedule.html', context)

def EditSchedule(request, course_id, schedule_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	schedule = get_object_or_404(Schedule, id=schedule_id)

	if user != course.user:
		return HttpResponseForbidden()
	else:
		if request.method == 'POST':
			form = NewScheduleForm(request.POST, instance=schedule)
			if form.is_valid():
				schedule.title = form.cleaned_data.get('title')
				schedule.date = form.cleaned_data.get('date')
				schedule.start_time = form.cleaned_data.get('start_time')
				schedule.end_time = form.cleaned_data.get('end_time')
				schedule.save()
				return redirect('student-schedules', course_id=course_id)
		else:
			form = NewScheduleForm(instance=schedule)

	context = {
		'form': form,
		'course':course,
		'schedule':schedule
	}

	return render(request, 'classroom/editschedule.html', context)

def Attendee(request,course_id,schedule_id):
	
	students = Course.objects.get(id=course_id)
	course = get_object_or_404(Course, id=course_id)
	schedules = get_object_or_404(Schedule,id=schedule_id)
	list = Attendance.objects.filter(schedule_id=schedule_id,course_id=course_id)
	marked = []
	for att in list:
		im = att.person.id
		marked.append(im)
	
	context = {
		'course':course,
		'students':students,
		'schedules':schedules,
		'marked':marked,
	}
	return render(request,'classroom/attendee.html',context)

def TakeAttendance(request,course_id,schedule_id,person_id):
	user = request.user
	students = Course.objects.get(id=course_id)
	course = get_object_or_404(Course, id=course_id)
	schedules = get_object_or_404(Schedule,id=schedule_id)
	person = get_object_or_404(User,id=person_id)
	if user != course.user:
		return HttpResponseForbidden()
	else:
		if request.method == 'POST':
			form = NewAttendanceForm(request.POST)
			if form.is_valid():
				status = form.cleaned_data.get('status')
				m = Attendance.objects.create(course=course,schedule=schedules,person=person,status=status)
				m.save()
				return redirect('attendee',course_id=course.id,schedule_id=schedule_id)
		else:
			form = NewAttendanceForm()
	context = {
		'course':course,
		'students':students,
		'schedules':schedules,
		'person':person,
		'form':form,
	}
	return render(request,'classroom/takeattendance.html',context)

def EditAttendance(request,course_id,schedule_id,person_id):
	user = request.user
	students = Course.objects.get(id=course_id)
	course = get_object_or_404(Course, id=course_id)
	schedules = get_object_or_404(Schedule,id=schedule_id)
	person = get_object_or_404(User,id=person_id)
	attendance = Attendance.objects.filter(course_id=course_id,schedule_id=schedule_id,person_id=person_id).first()
	if user != course.user:
		return HttpResponseForbidden()
	else:
		if request.method == 'POST':
			form = NewAttendanceForm(request.POST,instance=attendance)
			if form.is_valid():
				attendance.course = course
				attendance.schedule = schedules
				attendance.person = person
				attendance.status = form.cleaned_data.get('status')
				attendance.save()
				return redirect('attendee',course_id=course.id,schedule_id=schedule_id)
		else:
			form = NewAttendanceForm(instance=attendance)
	context = {
		'course':course,
		'students':students,
		'schedules':schedules,
		'person':person,
		'form':form,
		'attendance':attendance,
	}
	return render(request,'classroom/editattendance.html',context)
	
def GradeSubmission(request, course_id, grade_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	grade = get_object_or_404(Grade, id=grade_id)

	if user != course.user:
		return HttpResponseForbidden()
	else:
		if request.method == 'POST':
			points = request.POST.get('points')
			grade.points = points
			grade.status = 'graded'
			grade.graded_by = user
			grade.save()
			return redirect('student-submissions', course_id=course_id)
	context = {
		'course': course,
		'grade': grade,
	}

	return render(request, 'classroom/gradesubmission.html', context)
	
def StudentCourse(request):
	user = request.user
	courses = Course.objects.filter(enrolled=user)
	teacher_mode = False
	if user.groups.filter(name='Teacher'):
		teacher_mode = True
		return redirect('my-courses')
	context = {
		'courses': courses,
		'teacher_mode':teacher_mode,
	}
	return render(request, 'classroom/studentcourse.html', context)
