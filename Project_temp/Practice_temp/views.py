from django.shortcuts import render
from django.http import HttpResponse 

from Practice_temp.models import Topic,Webpage,AccessRecord


# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'Practice_temp/index.html', context=date_dict)

def help(request):
    my_dict1= {'help_me':'HELP ME page'}
    return render(request, 'help.html', context=my_dict1)