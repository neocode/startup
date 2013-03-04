import datetime
from django import forms
#from django.forms.fields import DateField, ChoiceField, MultipleChoiceField, CharField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
#from django.contrib.auth.forms import UserCreationForm
#from captcha.fields import CaptchaField

class PersonalInformation(forms.Form):
    #required_css_class = 'gridtable'
    year_start = datetime.date.today().year - 60
    year_finish = datetime.date.today().year - 18
    name = forms.CharField(label = "Name*", max_length=100)
    surname = forms.EmailField(label = "Surname*", required=False)
    birth_year = forms.DateField(label = "Birth Year*", widget = SelectDateWidget(years=range(year_start, year_finish)))
    address = forms.CharField(label = "Address", max_length=200)
    phone = forms.CharField(label = "Phone*", max_length=100)
    #select = forms.ChoiceField(widget = forms.Select(), choices = ([('1','1'), ('2','2'),('3','3'), ]), initial='3', required = True,)

class Education_part1(forms.Form):
    name_edu_inst = forms.CharField(label = "Name of the educational institution*", max_length=300)

class Education_part2(forms.Form):
    year_start = datetime.date.today().year - 60
    year_finish = datetime.date.today().year
    choices1 = [(u'', u'Start year')]
    choices1.extend([(unicode(year), unicode(year)) for year in range(year_start, year_finish)])
    graduation_start = forms.ChoiceField(choices=choices1)
    choices2 = [(u'', u'Finish year')]
    choices2.extend([(unicode(year), unicode(year)) for year in range(year_start, year_finish)])
    graduation_finish = forms.ChoiceField(choices=choices2)

class Education_part3(forms.Form):
    basic_specialty = forms.CharField(label = "Basic specialty*:", max_length=300)
    optional_specialty = forms.CharField(label = "Optional specialty:", max_length=300)
    desired_vacancy = forms.CharField(label = "Desired vacancy*:", max_length=300)

class Experience(forms.Form):
    year_start = datetime.date.today().year - 60
    year_finish = datetime.date.today().year
    name_of_the_company = forms.CharField(label = "Name of the company*:", max_length=300)
    sphere_of_activities = forms.CharField(label = "Sphere of activities:", max_length=300)
    job_start = forms.DateField(label = "Start date*:", widget = SelectDateWidget(years=range(year_start, year_finish)))
    till_now = forms.BooleanField(label="Until now", widget=forms.CheckboxInput(attrs={'onclick': 'check_tillnow(this);'}), required=False)
    job_finish = forms.DateField(label = "Finish date*:", widget = SelectDateWidget(years=range(year_start, year_finish)))
    position = forms.CharField(label = "Position*:", max_length=300)
    additional_duties = forms.CharField(label = "Additional duties:", max_length=300)

class Earnings(forms.Form):
    old_wage = forms.CharField(label = "Salary for the last job, $:", max_length=8)
    want_wage = forms.CharField(label = "You want to earn, $:", max_length=8)

class Skills(forms.Form):
    skills = forms.CharField(label = "Enter your skills here*:", widget=forms.Textarea, max_length=5000)
    realized_projects = forms.CharField(label = "Enter the projects in which you took a part:", widget=forms.Textarea, max_length=5000)

class LangSkills(forms.Form):
    language = [('Language','Language:'), ('English','English'), ('Deutch','Deutch'), ('French','French'), ('Spanish','Spanish'),
                ('Italian','Italian'), ('Russian','Russian'), ('Ukrainian','Ukrainian'),]
    level = [('Level','Level:'), ('Starter','Starter'), ('Elementary','Elementary'), ('Pre-Intermediate','Pre-Intermediate'),
             ('Intermediate','Intermediate'), ('Upper-Intermediate','Upper-Intermediate'),
             ('Advanced','Advanced'), ('Proficiency','Proficiency'),]
    select_lang1 = forms.ChoiceField(widget = forms.Select(), choices = (language), initial='English', required = True,)
    select_level1 = forms.ChoiceField(widget = forms.Select(), choices = (level), initial='Starter', required = True,)
    #select_lang2 = forms.ChoiceField(widget = forms.Select(attrs={'style': 'display:none;'}),  choices = (language), initial='English', required = True,)
    #select_level2 = forms.ChoiceField(widget = forms.Select(attrs={'style': 'display:none;'}), choices = (level), initial='Starter', required = True,)
    select_lang2 = forms.ChoiceField(widget = forms.Select(),  choices = (language), initial='Language', required = False,)
    select_level2 = forms.ChoiceField(widget = forms.Select(), choices = (level), initial='Level', required = False,)
    select_lang3 = forms.ChoiceField(widget = forms.Select(),  choices = (language), initial='Language', required = False,)
    select_level3 = forms.ChoiceField(widget = forms.Select(), choices = (level), initial='Level', required = False,)
    select_lang4 = forms.ChoiceField(widget = forms.Select(),  choices = (language), initial='Language', required = False,)
    select_level4 = forms.ChoiceField(widget = forms.Select(), choices = (level), initial='Level', required = False,)
    select_lang5 = forms.ChoiceField(widget = forms.Select(),  choices = (language), initial='Language', required = False,)
    select_level5 = forms.ChoiceField(widget = forms.Select(), choices = (level), initial='Level', required = False,)
    select_lang6 = forms.ChoiceField(widget = forms.Select(),  choices = (language), initial='Language', required = False,)
    select_level6 = forms.ChoiceField(widget = forms.Select(), choices = (level), initial='Level', required = False,)
    select_lang7 = forms.ChoiceField(widget = forms.Select(),  choices = (language), initial='Language', required = False,)
    select_level7 = forms.ChoiceField(widget = forms.Select(), choices = (level), initial='Level', required = False,)
    select_lang8 = forms.ChoiceField(widget = forms.Select(),  choices = (language), initial='Language', required = False,)
    select_level8 = forms.ChoiceField(widget = forms.Select(), choices = (level), initial='Level', required = False,)

class AddInfo(forms.Form):
    add_info = forms.CharField(label = "Enter any useful information about you:", widget=forms.Textarea, max_length=5000, required = False,)

#class Captcha(forms.Form):
#    captcha = CaptchaField('Are you human?')