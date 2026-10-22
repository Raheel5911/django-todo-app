from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        Todo.objects.create(user=request.user, title=request.POST['title'])
        return redirect('home')
    todos = Todo.objects.filter(user=request.user )
    return render(request, 'home.html', {'todos':todos})

def toggle(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')


def delete(request, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('home')

def signup(request):
    if request.method =='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html',{'form':form} )