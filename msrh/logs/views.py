#log/views.py
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from msrh_user.models import HR,HOD,SUPERVISOR,EMPLOYEE, Training, DEPARTMENT
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating

check = "false"
y = HOD.objects.all()
k = HR.objects.all()
a = SUPERVISOR.objects.all()
u = EMPLOYEE.objects.all()
l = DEPARTMENT.objects.all()
r = Training.objects.all()

@login_required(login_url="login/")
def home(request):
    z = 0
    for x in y :
        if(x.Eid == request.user.username):
            z=1
            return render(request,"hod_home.html")
    if z == 0:
        for x in k :
            if(x.Eid == request.user.username):
                z=1
                return render(request,"hr_home.html")
    if z == 0:
        for x in a:
            if (x.Eid == request.user.username):
                z = 1
                return render(request, "supervisor_home.html")
    if z == 0:
            return render(request, "login.html")

@login_required(login_url="login/")
def test(request):
    return render(request, "test.html", {'accept': u})

@login_required(login_url="login/")
def maketraining(request):
    return render(request, "maketraining.html", {'dept':l})


def make(request):
    if request.method == "POST":
        train = Training()
        dept = DEPARTMENT()
        train.name = request.POST['tname']
        train.venue = request.POST['tvenue']
        train.date = request.POST['tdate']
        train.time = request.POST['ttime']
        dept.name = request.POST['tdept']
        train.department = dept
        train.topic = request.POST['ttopic']
        train.head_of_program = request.POST['thead']
        train.save()
        check = "true"
        return render(request, "maketraining.html",{'check': check, 'dept':l})

def shows(request):
    return render(request, "show.html", {'train':r})