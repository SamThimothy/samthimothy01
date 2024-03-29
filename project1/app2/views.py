from django.shortcuts import render,redirect
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin

import datetime

# LogIn and SignUp
class CustomLoginView(LoginView):
    template_name='app2/login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')
    


class SignupPage(FormView):
    template_name = 'app2/signup.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)
        return super(SignupPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(SignupPage, self).get(*args, **kwargs)


# CRUD Operations
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        date=datetime.datetime.now() 
        msg='Good ' 
        h=int(date.strftime('%H')) 
        if h<12: 
            msg +='Morning!' 
        elif h<16: 
            msg +='AfterNoon!' 
        elif h<21: 
            msg +='Evening!' 
        else: 
            msg='Welcome! '

        context['wish']=msg

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input']= search_input

        return context





class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name ='task'
    success_url =reverse_lazy('tasks')


#Dynamic content
    
