from django.shortcuts import render
from .models import Registerfirst, Course, Project, Workshop, Feedback, Contact, Callme, Photos, About,Carousal

# Create your views here.

def index(request):
    registerfirst = Registerfirst.objects.all()
    course = Course.objects.all()
    project = Project.objects.all()
    workshop = Workshop.objects.all()
    feedback = Feedback.objects.all()
    callme = Callme.objects.all()
    contact = Contact.objects.all()
    photos = Photos.objects.all()
    about = About.objects.all()
    carousal = Carousal.objects.all()
    
    # courses = request.GET.get('course')
    # if courses == None:
    #     course = Course.objects.all()
    # else:
    #     course = Course.objects.filter(course__name=courses)

    # course = Course.objects.all()
    if request.method == 'POST':
        rname = request.POST.get('rname')
        remail = request.POST.get('remail')
        rphone = request.POST.get('rphone')
        rqualification = request.POST.get('rqualification')

        if Registerfirst.objects.filter(remail = remail):
            print('email already exists')
            return render(request, 'iapp/index.html')
        else:
            print('success')
            data2 = Registerfirst.objects.create(rname=rname, remail=remail, rphone=rphone, rqualification=rqualification)



    if request.method == 'POST':
        name1 = request.POST.get('name1')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        interest = request.POST.get('interest')
        if Callme.objects.filter(email = email):
            print('email already exists')
            return render(request, 'iapp/index.html')
        else:
            data = Callme.objects.create(name1=name1, phone=phone, email=email, interested=interest)
            print('success')

        
            

    

    if request.method == 'POST':
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        message = request.POST.get('cmessage')
        if Contact.objects.filter(email = email):
            print('email already exists')
            return render(request, 'iapp/index.html')
        else:
            print('success')
            data1 = Contact.objects.create(name=name, email=email, message=message)



            

    
        
    print(request.POST)
    
        



    return render(request, 'iapp/index.html', {'course':course, 'project':project, 'workshop':workshop, 'feedback':feedback, 'photos':photos, 'about':about, 'carousal':carousal})



def viewPhoto(request, pk):

    # course = Course.objects.all(id=pk)
    photo = Photos.objects.get(id=pk)

    return render(request, 'iapp/details.html', {'photo': photo})


# def reg(request):
#     if request.method == 'POST':
#         rname = request.POST.get('rname')
#         remail = request.POST.get('remail')
#         rphone = request.POST.get('rphone')
#         data2 = Registerfirst.objects.create(rname=rname, remail=remail, rphone=rphone)
#         data2.save()
#         print(request.POST)
#     return render(request, 'iapp/index.html')
