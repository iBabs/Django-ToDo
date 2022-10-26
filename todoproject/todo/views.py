from msilib.schema import SelfReg
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView, DeleteView, FormView
from .models import Mytodos
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class SignInTask(LoginView):
    template_name= "Login.html"
    field = "__all__"
    redirect_authenticated_user= True

    def get_success_url(self):
        return reverse_lazy("Task List")


class RegisterUser(FormView):
    template_name = 'Singup.html'
    form_class= UserCreationForm
    redirect_authenticated_user = True
    success_url= "/tasklist"
# this function is to keep the newly created user logged in
    def form_valid(self, form):

        owner = form.save()
        if owner is not None:
            login(self.request, owner)
        return super(RegisterUser, self).form_valid(form)
    




class MyTodoApView(LoginRequiredMixin,CreateView):
    model = Mytodos
    fields=[
        'task', "details", "complete"
    ]
    template_name = "todos.html"
    success_url= "/tasklist"
# this function is to set the task ownerautomatically
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# def alltoDo(request):
#     return render("todos.html", {})
#   the above is a functon based view while the earlier is class based
# # Create your views here.

class TaskList(LoginRequiredMixin,ListView):
    model= Mytodos
    template_name= "list.html"

# to make the owners of tasks see only the tasks they created
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["object_list"] =  context["object_list"].filter(owner=self.request.user)
        context["count"] =  context["object_list"].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['object_list'] =  context['object_list'].filter(
                task__icontains = search_input
            )

        context['search_input'] = search_input

        return context

class MyTodoDetail(LoginRequiredMixin, DetailView):
    model= Mytodos
    template_name= "detail.html"

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Mytodos
    fields=[
        'task', "details", "complete"
    ]
    template_name= "update.html"
    success_url= "/tasklist"

class DeleteTask(LoginRequiredMixin, DeleteView):
    model= Mytodos
    template_name= "delete.html"
    success_url= "/tasklist"