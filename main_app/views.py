from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from .models import Idea, Photo, Employee

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

# Create your views here.
def home(request):
  return render(request, 'home.html')

@login_required
def ideas_detail(request, idea_id):
  idea = Idea.objects.get(id=idea_id)
  return render(request, 'ideas/detail.html', {'idea': idea})

def public_list(request):
  idea = Idea.objects.all()
  return render(request, 'main_app/public_list.html', {'idea': idea})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Create your CBV's here.
class IdeaCreate(LoginRequiredMixin, CreateView):
  model = Idea
  fields = ['name', 'description', 'industry', 'is_public']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class IdeaList(LoginRequiredMixin, ListView):
  model = Idea

class IdeaDelete(LoginRequiredMixin, DeleteView):
  model = Idea
  success_url = '/ideas/'

class IdeaUpdate(LoginRequiredMixin, UpdateView):
  model = Idea
  fields = ['name', 'description', 'industry', 'is_public']

