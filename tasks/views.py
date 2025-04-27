from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm, RegisterForm
from django.db.models import Q
from datetime import date

def index(request):
    tasks = [
        {'title': 'Dars qilish', 'is_completed': True},
        {'title': 'Sport bilan shug\'ullanish', 'is_completed': False},
        {'title': 'Loyiha topshirig\'i', 'is_completed': False, 'is_important': True},
    ]
    return render(request, 'index.html', {'tasks': tasks})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email yoki parol xato.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Ro\'yxatdan o\'tishda xatolik yuz berdi.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter', 'all')
    
    tasks = Task.objects.filter(user=request.user)
    
    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    if filter_type == 'today':
        tasks = tasks.filter(due_date=date.today())
    elif filter_type == 'completed':
        tasks = tasks.filter(is_completed=True)
    elif filter_type == 'important':
        tasks = tasks.filter(is_important=True)
    
    stats = {
        'completed': Task.objects.filter(user=request.user, is_completed=True).count(),
        'pending': Task.objects.filter(user=request.user, is_completed=False).count(),
        'important': Task.objects.filter(user=request.user, is_important=True).count(),
    }
    
    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'stats': stats,
        'query': query,
        'filter_type': filter_type,
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Vazifa muvaffaqiyatli qo\'shildi.')
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'add-task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vazifa muvaffaqiyatli yangilandi.')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'add-task.html', {'form': form, 'task': task})

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('dashboard')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, 'Vazifa o\'chirildi.')
    return redirect('dashboard')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')