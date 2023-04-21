##Django Level three 

134. Django forms : 
-----------------
1. cd D:\work related\Shivani\Django\Django level three>
2. django-admin startproject basicforms 
3. cd basicforms
4. django-admin startapp basicapp
5. create folder in templates "Django level three\basicforms"
6. create basicapp folder templates
7. create index.html in templates/basicapp/
8. create form_page.html in templates/basicapp/
9. add some basic content index.html and form_page.html
10. edit basicforms/settings.py like do changes for adding template dir , and add basicapp in INSTALLED_APPS
11. create basicapp/forms.py and add below content :
`
       from django import forms
       
       class FormName(forms.Form):
       	name = forms.CharField()
       	email = forms.EmailField()
       	text = forms.CharField(widget=forms.Textarea)
`

12. edit basicapp/views.py 
`
        from django.shortcuts import render
        from . import forms
        
        # Create your views here.
        
        def index(request):
        	return render(request, 'basicapp/index.html')
        
        def form_name_view(request):
           form = forms.FormName()
           
           if request.method == 'POST':
              form = forms.FormName(request.POST)

           if form.is_valid() : 
                #DO SOMETHING 
                print("VALIDATION SUCCESS!")
                print("NAME:" + form.cleaned_data['name'])
                print("EMAIL:" + form.cleaned_data['email'])
                print("TEXT:" + form.cleaned_data['text'])
        
           return render(request, 'basicapp/form_page.html',{'form': form})

`

13. edit basicforms/urls.py : 
`
        from django.contrib import admin
        from django.urls import path
        from basicapp import views
        
        
        urlpatterns = [
        	path("",views.index, name='index'),
        	path("admin/", admin.site.urls),
        	path("formpage/", views.form_name_view , name='form_name')
        ]

`
14. add link tag in  templates/basicapp/form_page.html , index.html 

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

15. add changes form_page.html 

`
<body>
        <h1>Fill out the form!</h1>
        <div class="container">
            <form method="POST">
                {{ form.as_p }}
                {% csrf_token %}
                <input type="submit" class="btn btn-primary" value="Submit">
            </form>
        </div>
    </body>
`
16. whe you submit it by enetering the detail in http://127.0.0.1:8000/formpage/ , you will get the below detail in terminal ( not in browser) : 
VALIDATION SUCCESS!
NAME:sf
EMAIL:as@test.com
TEXT:lkdf


######

136. Form Validation : 

To be continued with above 135 steps : 

1. edit forms.py 

`
from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
`


After doing the changes , I loaded the page , and while inspecting the elemets from the webpage , i couldn;t see 
`<input id='id_botcatcher' name='botcatcher' type='hidden' ` line. 

If it's available, we can add value tag at last i.e., 
`<input id='id_botcatcher' name='botcatcher' type='hidden' value='Hello' `, 

after editing and submit the data , in web page it will below text 


2. for email validation edit forms.py as below : 

`
from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure Emails match!")
`
'Hiden field bitcatcher, ensure the value has atmost 0 characters (It has 6)'



-------
138 . Model Forms Execise : 

Copy 'ProTWo' to Django level three folder and do edits in it . 

1. add below line in index.html and users.html of templates/appTwo/

`<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"> `

2. create forms.py in appTwo
`
from django import forms
from appTwo.models import Users

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Users
        field = '__all__'
`
3. edit appTwo/views.py : 

`
from django.shortcuts import render

from appTwo.models import Users
from appTwo.forms import NewUserForm

def index(request):
    return render(request, 'appTwo/index.html')


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else :
            print('Error form Invalid')

    return render(request, 'appTwo/users.html', {'form': form})


4. edit templates/appTwo/users.html

"
<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8">
        <title>Users</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <h1>Please sign up here !</h1>
            <form method="POST">
                {{form.as_p}}
                {% csrf_token %}
                <input type="submit" class="btn btn-primary" value="submit">
            </form>
        </div>
        
          
    </body>
</html>
"

-> also do some changes in users.html by adding some form and button related tag 
