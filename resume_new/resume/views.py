from django.core.mail import send_mail
from django.shortcuts import render_to_response
from forms import PersonalInformation, Education_part1, Education_part2, Education_part3, Experience, Earnings, Skills, LangSkills, AddInfo
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime
import core

def contact(request):
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            cd = form1.cleaned_data
            '''
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
            '''
            return render_to_response('contact_form.html', {'result': core.swap(cd['message']), 'form1': form1,}, context_instance=RequestContext(request))
    else:
        form1 = PersonalInformation()
        form2_1 = Education_part1()
        form2_2 = Education_part2()
        form2_3 = Education_part3()
        form3 = Experience()
        form4 = Earnings()
        form5 = Skills()
        form6 = LangSkills()
        form7 = AddInfo()
        #form8 = Captcha()

    return render_to_response('contact_form.html', {'form1': form1, 'form2_1': form2_1, 'form2_2': form2_2,
                              'form2_3': form2_3, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                              'form7': form7,},
                              context_instance=RequestContext(request))