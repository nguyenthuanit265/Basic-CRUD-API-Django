from django.shortcuts import render, redirect
from user.form import UserForm
from user.models import User


# Create your views here.
def show(requsest):
    users = User.objects.all();
    return render(requsest, 'show.html', {'users': users})


def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/my-admin/user/show')
            except:
                pass
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'edit.html', {'user': user})


def update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect("/my-admin/user/show")
    return render(request, 'edit.html', {'user': user})


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/my-admin/user/show")
