from django.contrib import admin
from scoreboard import models


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


class ScoreAdmin(admin.ModelAdmin):
    pass


class SizeAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Score, ScoreAdmin)
admin.site.register(models.Size, SizeAdmin)
