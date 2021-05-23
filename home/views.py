# from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import *
from home.forms import *


def sort_by_values(dic=None):
    if dic:
        return {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}


def txt_to_list(txt, spacer=' '):
    return txt.split(spacer)


def func_course_list():
    context = {}
    if Course.objects.all().exists():
        for obj in Course.objects.all().iterator():
            context.update({str(obj.id): obj.c_name})
        return sort_by_values(context).items()
    return ('1', 'No Data')


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *arg, **kwargs):
        sem_list = {'1': '1st', '2': '2nd', '3': '3rd',
                    '4': '4th', '5': '5th', '6': '6th'}
        context = {
            'course_list': func_course_list(),
            'sem_list': sem_list,
            'sub_list': txt_to_list('Plz select Course & semester 👈'),
            'ques_list': ['Plz Select Any Subject 📚 '],
        }
        return render(request, self.template_name, context)


class QuestionView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, sem_id=1, sub_name='Hindi', *args, **kwargs):

        questions = []
        ques_list = []
        sem_list = {'1': '1st', '2': '2nd', '3': '3rd',
                    '4': '4th', '5': '5th', '6': '6th'}

        if Subject.objects.filter(course_name_id__pk=kwargs['c_id']).exists():
            s = Subject.objects.get(course_name_id__pk=kwargs['c_id'])
            sub_list = list(s.sub_names.split(","))
            ques_result = QuesPaper.objects.filter(
                course_name=kwargs['c_id'], semester=sem_id, sub_name=sub_name.lower())
            for q in ques_result:
                ques_list = list(q.fl_id.split(","))
            for i in ques_list:
                try:
                    q_paper = QuesPaperMedia.objects.get(fl_id=i.lower())
                    questions.append(q_paper)
                except QuesPaperMedia.DoesNotExist:
                    q_paper = 'None'
        else:
            sub_list = txt_to_list('Sorry We Got No Subjects 😔')

        if questions == []:
            questions = [' Either Subject or Question Paper Missing 😔 ']

        context = {
            'course_list': func_course_list(),
            'id': kwargs['c_id'],
            'sem_id': sem_id,
            'sem_list': sem_list,
            'sub_list': sub_list,
            'sub_name': sub_name,
            'questions': questions,

        }

        print(questions)
        return render(request, self.template_name, context)


class TestView(TemplateView):
    template_name = 'home/test.html'

    def get(self, request, *args, **kwargs):
        context = {'form': TestForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        file_upload = FileUpload()

        form = TestForm(request.POST , request.FILES)
        files = request.FILES.getlist('document')
        if form.is_valid():
            for file in files:
                file_upload.name = form.cleaned_data['name']
                file_upload.email = form.cleaned_data['email']
                file_upload.type = form.cleaned_data['type']
                file_upload.document = file
                file_upload.description = form.cleaned_data['description']

                print(file_upload.document.name)
                file_upload.save()
            
        context = {'form': TestForm()}
        return render(request, self.template_name, context)

        data = {
            'f_name':
                'm_name'
                'l_name'
                'email'
                'dob'
                'address'
                'gender'
        }
