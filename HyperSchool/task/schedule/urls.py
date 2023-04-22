from django.urls import path

from schedule.views import CourseListView, CourseView, TeacherView, AddCourseView, SignUpView, LogInView


urlpatterns = [
    path('schedule/course_details/<int:id>', CourseView.as_view(), name='course_url'),
    path('schedule/teacher_details/<int:id>', TeacherView.as_view(), name='teacher_url'),
    path('schedule/main/', CourseListView.as_view(), name='course_list'),
    path('schedule/add_course/', AddCourseView.as_view(), name='add_course'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
]

