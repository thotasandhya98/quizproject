from django.contrib import admin

from .models import User, Questions, Options, Answers, Test

admin.site.register(User)
admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(Answers)
admin.site.register(Test)



# Register your models here.
