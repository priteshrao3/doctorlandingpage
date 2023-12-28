from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models import RegistrationForm, MainContent, DocterDetails, Awarded_By, Framework_Steps, How_Will_This, Get_Bonuses, Who_Attend, About_Your_Health_Coach, Your_Health_Coach_Awarded, FAQs, How_Does_This

# Create your views here.
def landingpage(request):

    maincontent = MainContent.objects.latest('created_at')
    doctor_details = DocterDetails.objects.latest('created_at')
    awarded = Awarded_By.objects.all()
    framework_steps = Framework_Steps.objects.all().reverse()

    framestep1 = framework_steps[0]
    framestep2 = framework_steps[1]
    framestep3 = framework_steps[2]
    framestep4 = framework_steps[3]
    framestep5 = framework_steps[4]
    framestep6 = framework_steps[5]
    framestep7 = framework_steps[6]
    framestep8 = framework_steps[7]
    framestep9 = framework_steps[8]

    how_will_this = How_Will_This.objects.latest('created_at')

    get_bonuses = Get_Bonuses.objects.all().reverse()
    bonuses1 = get_bonuses[0]
    bonuses2 = get_bonuses[1]
    bonuses3 = get_bonuses[2]
    bonuses4 = get_bonuses[3]
    bonuses5 = get_bonuses[4]
    bonuses6 = get_bonuses[5]

    who_attend = Who_Attend.objects.all().reverse() 
    attend1 = who_attend[0]
    attend2 = who_attend[1]
    attend3 = who_attend[2]
    attend4 = who_attend[3]
    attend5 = who_attend[4]
    attend6 = who_attend[5]


    health_coach = About_Your_Health_Coach.objects.latest('created_at')
    health_coach_awarded = Your_Health_Coach_Awarded.objects.all()
    faqs = FAQs.objects.all()
    how_does_this = How_Does_This.objects.latest('created_at')

    return render(request, 'landingpage.html', {'maincontent':maincontent, 'doctor_details':doctor_details, 'awarded':awarded, 
        'framework_steps':framework_steps, 'how_will_this':how_will_this, 'get_bonuses':get_bonuses,
        'health_coach':health_coach, 'health_coach_awarded':health_coach_awarded, 'faqs':faqs, 
        'how_does_this':how_does_this, 'framestep1':framestep1, 'framestep2':framestep2, 'framestep3':framestep3,
        'framestep4':framestep4, 'framestep5':framestep5, 'framestep6':framestep6, 'framestep7':framestep7, 'framestep8':framestep8,
        'framestep9':framestep9, 'bonuses1':bonuses1, 'bonuses2':bonuses2, 'bonuses3':bonuses3, 'bonuses4':bonuses4,
        'bonuses5':bonuses5, 'bonuses6':bonuses6, 'attend1':attend1, 'attend2':attend2, 'attend3':attend3,
        'attend4':attend4, 'attend5':attend5, 'attend6':attend6})


def registrationform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        location = request.POST.get('location')

        reg = RegistrationForm(name=name, mobile=mobile, location=location)
        reg.save()
        return HttpResponseRedirect('https://rzp.io/l/vaG2Fit')
    else:
        return render(request, 'registrationform.html')