from django.contrib import admin
from base.models import Place,Restrictions,Comment, User
# Register your models here.

admin.site.register(User)
admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(Restrictions)


