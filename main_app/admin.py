from django.contrib import admin
from .models import Idea, Employee, Photo, Liked, Message
# Register your models here.
admin.site.register(Idea)
admin.site.register(Employee)
admin.site.register(Photo)
admin.site.register(Liked)
admin.site.register(Message)