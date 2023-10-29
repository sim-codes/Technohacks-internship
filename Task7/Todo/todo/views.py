from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import TodoForm, UserRegistrationForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Todo


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'pages/todo_detail.html'

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ('title', 'description', 'status')
    template_name = 'pages/todo_edit.html'

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_create_list')
    template_name = 'pages/todo_delete.html'


@login_required
def todo_create_list(request):
    """Page to handle both Todo creation and listing depending on the request"""
    todos = Todo.objects.filter(author=request.user)

    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        # Checking form validity and adding get current user as the author
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            form.save()
        # Redirect user to the page to load all todos
        return redirect('todo_create_list')
    
    create_form = TodoForm() # Send an empty form when request is not post
    
    return render(request, 'pages/todo.html', {'create_form': create_form, 'todos': todos})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})