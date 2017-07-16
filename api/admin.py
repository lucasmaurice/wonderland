from django.contrib import admin

# Register your models here.
from .models import Entity, Human, Object, Door, Room, AccessPoint

admin.site.register(Entity)
admin.site.register(Human)
admin.site.register(Object)
admin.site.register(Door)
admin.site.register(AccessPoint)
admin.site.register(Room)
