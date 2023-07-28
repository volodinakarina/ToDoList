from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from social_django.models import Association, Nonce

# from goals.models import BoardParticipant

from .models import User


# class BoardInline(admin.TabularInline):
#     model = BoardParticipant
#     fields = ('board', 'role', 'created', 'updated')
#     readonly_fields = ('created', 'updated', 'board')
#     ordering = ('role', 'board', 'created')
#     show_change_link = True
#     extra = 0
#     can_delete = False


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'updated',
    ]
    list_filter = ['is_staff', 'is_active']
    list_editable = ['is_staff', 'is_active']
    readonly_fields = ('date_joined', 'last_login', 'updated')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'updated')}),
    )
    # inlines = [BoardInline]


admin.site.unregister(Group)
admin.site.unregister(Association)
admin.site.unregister(Nonce)
