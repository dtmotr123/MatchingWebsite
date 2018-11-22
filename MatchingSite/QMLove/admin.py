from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Hobby


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

# Only display the fields from the fieldsets
# in the admin interface
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Personal info', {'fields': ('username', 'password', 'first_name', 'last_name')}),
    )
    inlines = (ProfileInline,)

class HobbyAdmin(admin.ModelAdmin):
    model = Hobby
    can_delete = False
    verbose_name_plural = 'Hobbies'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Hobby, HobbyAdmin)
