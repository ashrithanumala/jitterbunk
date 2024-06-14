from django.http import HttpResponse, HttpResponseRedirect
from bunk.models import Bunk, User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def index(request):
    bunk_list = Bunk.objects.all()
    user_list = User.objects.all()
    context = {
        "bunk_list" : bunk_list,
        "user_list" : user_list
    }
    return render(request, "bunk/index.html", context)

def personal(request, userid):
    user = get_object_or_404(User, pk=userid)
    bunked_by_name_list = Bunk.objects.filter(from_user=user)
    name_bunked_by_list = Bunk.objects.filter(to_user=user)
    bunk_options = User.objects.exclude(pk = userid)
    context = {
        "user" : user,
        "userid" : userid,
        "bunked_by_name_list" : bunked_by_name_list,
        "name_bunked_by_list" : name_bunked_by_list, 
        "bunk_options" : bunk_options
    }
    return render(request, "bunk/personal.html", context)

def addbunk(request):
    if request.method == 'POST':
        new_from_user = User.objects.get(username=request.POST.get('from_user'))
        new_to_user = User.objects.get(username=request.POST.get('to_user'))
        new_bunk = Bunk(from_user=new_from_user, to_user=new_to_user, time=timezone.now())
        new_bunk.save()
        return redirect('personal', userid=new_from_user.pk)
    
    return render(request, "bunk/personal.html")
