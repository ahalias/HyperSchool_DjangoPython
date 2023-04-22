from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from schedule.forms import SearchForm, AddStudentForm
from schedule.models import Course, Teacher, Student


class LogInView(LoginView):
    template_name = 'schedule/login.html'
    success_url = reverse_lazy('course_list') # replace 'home' with the name of your homepage URL

    def get_success_url(self):
        return self.success_url


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "schedule/signup.html"
    success_url = reverse_lazy("course_list")


class AddCourseView(View):

    def get(self, request):
        form = AddStudentForm()
        return render(request, "schedule/add_course.html", {'form': form})

    def post(self, request):
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student = Student(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                age=form.cleaned_data['age'],
            )
            student.save()
            courses = [form.cleaned_data['course']]
            student.course.set(courses)
        return render(request, "schedule/add_course.html", {'form': form})


class CourseView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        student_list = Student.objects.filter(course=course)
        return render(request, "schedule/course.html", {"course": course, "students": student_list})

class TeacherView(View):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        return render(request, "schedule/teacher.html", {"teacher": teacher})



# Create your views here.
class CourseListView(View):

    def get(self, request):
        form = SearchForm()
        search_query = request.GET.get('q')
        course_list = Course.objects.filter(title__contains=search_query) if search_query else Course.objects.all()
        return render(request, 'schedule/index.html', {'form': form, "course_list": course_list})





