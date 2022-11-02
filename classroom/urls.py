from django.urls import path
from classroom.views import EditAttendance, EditSchedule, TakeAttendance,Attendee, Categories, CategoryCourses, NewCourse, Enroll, DeleteCourse, EditCourse, MyCourses, CourseDetail, Submissions, StudentSubmissions, GradeSubmission,StudentCourse,StudentSchedules,NewSchedule

from module.views import NewModule, CourseModules
from page.views import NewPageModule, PageDetail, MarkPageAsDone
from quiz.views import NewQuiz, NewQuestion, QuizDetail, TakeQuiz, SubmitAttempt, AttemptDetail
from assignment.views import NewAssignment, AssignmentDetail, NewSubmission
from question.views import NewStudentQuestion, Questions, QuestionDetail, MarkAsAnswer, VoteAnswer
urlpatterns = [
	#Course - Classroom Views
	path('newcourse/', NewCourse, name='newcourse'),
	path('course/',StudentCourse,name='student-course'),
	path('MyCourses/', MyCourses, name='my-courses'),
	path('categories/', Categories, name='categories'),
	path('categories/<category_slug>', CategoryCourses, name='category-courses'),
	path('<course_id>/', CourseDetail, name='course'),
	path('<course_id>/enroll', Enroll, name='enroll'),
	path('<course_id>/edit', EditCourse, name='edit-course'),
	path('<course_id>/delete', DeleteCourse, name='delete-course'),
	#Modules
	path('<course_id>/modules', CourseModules, name='modules'),
	path('<course_id>/modules/newmodule', NewModule, name='new-module'),
	#Pages
	path('<course_id>/modules/<module_id>/pages/newpage', NewPageModule, name='new-page'),
	path('<course_id>/modules/<module_id>/pages/<page_id>', PageDetail, name='page-detail'),
	path('<course_id>/modules/<module_id>/pages/<page_id>/done', MarkPageAsDone, name='mark-page-as-done'),
	#Quizzes
	path('<course_id>/modules/<module_id>/quiz/newquiz', NewQuiz, name='new-quiz'),
	path('<course_id>/modules/<module_id>/quiz/<quiz_id>/newquestion', NewQuestion, name='new-question'),
	path('<course_id>/modules/<module_id>/quiz/<quiz_id>/', QuizDetail, name='quiz-detail'),
	path('<course_id>/modules/<module_id>/quiz/<quiz_id>/take', TakeQuiz, name='take-quiz'),
	path('<course_id>/modules/<module_id>/quiz/<quiz_id>/take/submit', SubmitAttempt, name='submit-quiz'),
	path('<course_id>/modules/<module_id>/quiz/<quiz_id>/<attempt_id>/results', AttemptDetail, name='attempt-detail'),
	#Assignment
	path('<course_id>/modules/<module_id>/assignment/newassignment', NewAssignment, name='new-assignment'),
	path('<course_id>/modules/<module_id>/assignment/<assignment_id>', AssignmentDetail, name='assignment-detail'),
	path('<course_id>/modules/<module_id>/assignment/<assignment_id>/start', NewSubmission, name='start-assignment'),
	#Submissions
	path('<course_id>/submissions', Submissions, name='submissions'),
	path('<course_id>/studentsubmissions', StudentSubmissions, name='student-submissions'),
	path('<course_id>/submissions/<grade_id>/grade', GradeSubmission, name='grade-submission'),
	#Schedule
	path('<course_id>/schedules', StudentSchedules, name='student-schedules'),
	path('<course_id>/schedules/newschedules', NewSchedule, name='new-schedules'),
	path('<course_id>/schedules/<schedule_id>/attendee', Attendee, name='attendee'),
	path('<course_id>/schedules/<schedule_id>/attendance/<person_id>/takeattendance', TakeAttendance, name='take-attendance'),
	path('<course_id>/schedules/<schedule_id>/attendance/<person_id>/editattendance/', EditAttendance, name='edit-attendance'),
	path('<course_id>/schedules/<schedule_id>/editschedule', EditSchedule, name='edit-schedule'),
	#Questions
	path('<course_id>/questions', Questions, name='questions'),
	path('<course_id>/questions/newquestion', NewStudentQuestion, name='new-student-question'),
	path('<course_id>/questions/<question_id>', QuestionDetail, name='question-detail'),
	path('<course_id>/questions/<question_id>/vote', VoteAnswer, name='vote-answer'),
	path('<course_id>/questions/<question_id>/<answer_id>/markasanswer', MarkAsAnswer, name='mark-as-answer'),


]