from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Attendee)
admin.site.register(Trainer)
admin.site.register(Classroom)
admin.site.register(Attendance)
admin.site.register(ClassroomResource)
