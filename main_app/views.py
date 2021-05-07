from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from .models import Idea, Photo, Employee

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'idea-hub-bucket'

# Create your views here.
def home(request):
  return render(request, 'home.html')

@login_required
def ideas_detail(request, idea_id):
  idea = Idea.objects.get(id=idea_id)
  return render(request, 'ideas/detail.html', {'idea': idea})

def public_list(request):
  idea = Idea.objects.filter(is_public=True)
  idea = idea.exclude(user=request.user)
  return render(request, 'main_app/public_list.html', {'idea': idea})

def make_public(request, idea_id):
  idea = Idea.objects.get(id=idea_id)
  idea.is_public = True
  idea.save()
  return redirect('detail', idea_id=idea_id)

def make_private(request, idea_id):
  idea = Idea.objects.get(id=idea_id)
  idea.is_public = False
  idea.save()
  return redirect('detail', idea_id=idea_id)


def delete_photo(request, photo_id, idea_id):
  Photo.objects.get(id=photo_id).delete()
  return redirect('detail', idea_id=idea_id)


def add_photo(request, idea_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, idea_id=idea_id)
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('detail', idea_id=idea_id)


def add_logo(request, idea_id):
  # get the idea, remove the old URL, replace it.
  idea = Idea.objects.get(id=idea_id)
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      idea.logo_url = url
      idea.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('detail', idea_id=idea_id)  


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

