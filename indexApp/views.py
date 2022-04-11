from django.shortcuts import render

# Create your views here.

from .models import slider, whatido, whatidoitem, about, aboutbrief, aboutprojects, aboutskill, work, workimg, experience, experiencelist, contacttitle, contactaddr, contactform

def home(request):
    sliderData = slider.objects.all()[0]
    whatidoData = whatido.objects.all()[0]
    whatidoitemData = whatidoitem.objects.all()
    aboutData = about.objects.all()[0]
    aboutbriefData = aboutbrief.objects.all()[0]
    aboutprojectsData = aboutprojects.objects.all()
    aboutskillData = aboutskill.objects.all() 
    workData = work.objects.all()[0]
    workimgData = workimg.objects.all()
    experienceData = experience.objects.all()[0]
    experiencelistData = experiencelist.objects.all()
    contacttitleData = contacttitle.objects.all()[0]
    contactaddrData = contactaddr.objects.all()[0]

    index_dict = {
        'slider':sliderData,
        'whatido':whatidoData,
        'whatidoitem':whatidoitemData,
        'about':aboutData,
        'aboutbrief':aboutbriefData,
        'aboutprojects':aboutprojectsData,
        'aboutskill':aboutskillData,
        'work':workData,
        'workimg':workimgData,
        'experience':experienceData,
        'experiencelist':experiencelistData,
        'contacttitle':contacttitleData,
        'contactaddr':contactaddrData,
    }

    if request.method=='POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contactformdata = contactform(name=name, mail=mail, phone=phone, messages=message)
        contactformdata.save()

        return render(request, 'index.html', index_dict)

    return render(request, 'index.html', index_dict)
