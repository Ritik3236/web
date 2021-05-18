from typing import Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from home.models import *


def sort_by_values(dic: Dict):
    return {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}


def txt_to_list(txt, spacer=' '):
    return(txt.split(spacer))


def fun_course():
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
        context = {
            'context': fun_course(),
            'sub_list': txt_to_list('Plz select Course & semester 👈'),
            'qes_list': ['Plz Select Any Subject 📚 '],
        }
        return render(request, self.template_name, context)


class QuestionView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, sem_id=1, sub_name='Hindi', *args, **kwargs):
        qes_list = ['Plz Select Subject']

        if Subject.objects.filter(pk=kwargs['c_id']).exists():
            s = Subject.objects.get(pk=kwargs['c_id'])
            sub_list = list(s.sub_names.split(","))

            ques_result = QuesPaper.objects.filter(
                course_name=kwargs['c_id'], semester=sem_id, sub_name=sub_name.lower())
            for q in ques_result:
                qes_list = list(q.fl_name.split(","))
            if qes_list[0] == 'Plz Select Subject':
                qes_list = [' Unfortunately We Got No Qestion Paper 😔 ']
            print(qes_list)
        else:
            sub_list = txt_to_list('Sorry We Got No Subjects 😔')
        context = {
            'context': fun_course(),
            'id': kwargs['c_id'],
            'sem': sem_id,
            'sub_list': sub_list,
            'qes_list': qes_list,
        }
        return render(request, self.template_name, context)
# lst = list(sub.sub_name.split(","))
