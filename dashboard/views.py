from django.shortcuts import render,redirect
from .models import Profile,Resource
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def addProfile(request):
    if request.user.is_authenticated == False:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Login to Access the URL')
        return redirect('/') 
    if request.method=="POST":
        uploads=request.FILES
        profile = uploads['profile']
        profession=request.POST["profession"]
        location = request.POST['location']
        mobile=request.POST["mobile"]
        Profile.objects.create(profile_image=profile,profession=profession,location=location,mobile=mobile,user=request.user)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Profile Added')
        return redirect('/dashboard') 
    if Profile.objects.filter(user=request.user).exists():
        return redirect('/dashboard/updateProfile')
    return render(request,"addProfile.html")

def updateProfile(request):
    if request.user.is_authenticated == False:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Login to Access the URL')
        return redirect('/') 
    if request.method=="POST":
        uploads=request.FILES
        profile = uploads['profile']
        profession=request.POST["profession"]
        location = request.POST['location']
        obj = Profile.objects.get(user=request.user)
        obj.profile_image=profile
        obj.profession=profession
        obj.location=location
        obj.save()
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Profile Updated Successfully')
        return redirect('/dashboard') 
    obj = Profile.objects.get(user=request.user)
    return render(request,"updateProfile.html",{'obj':obj})

def addResource(request):
    if request.method=="POST":
        title = request.POST["title"]
        uploads=request.FILES
        doc = uploads['upload']
        description = request.POST["description"]
        branch = request.POST["branch"]
        year = request.POST["year"]
        Resource.objects.create(user=request.user,title=title,upload=doc,description=description,branch=branch,year=year)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Resource Added Successfully')
        return redirect('/dashboard')
    obj = Resource.objects.filter(user=request.user) 
    return render(request,"addResource.html",{'obj':obj})

def viewResource(request):
    branch = request.GET.get('branch')
    year = request.GET.get('year')
    if branch is None and year is None:
        obj = Resource.objects.all()
        return render(request,"viewResource.html",{'obj':obj})
    else:
        if branch=="ALL":
            if year=="ANY":
                obj = Resource.objects.all()
                return render(request,"viewResource.html",{'obj':obj})
            else:
                obj = Resource.objects.filter(year=year)
                return render(request,"viewResource.html",{'obj':obj})
        else:
            if year=="ANY":
                obj = Resource.objects.filter(branch=branch)
                return render(request,"viewResource.html",{'obj':obj})
            else:
                obj = Resource.objects.filter(branch=branch,year=year)
                return render(request,"viewResource.html",{'obj':obj})