# from django.contrib import admin
#
# from goals.models import Category, Goal
#
#
# @admin.register(Category)
# class GoalCategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'created', 'updated')
#     search_fields = ('title', 'user')
#
#
# @admin.register(Goal)
# class GoalAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'created', 'updated')
#     search_fields = ('title', 'user')
from django.contrib import admin

from goals.models import GoalCategory, Goal


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


# admin.site.register(GoalCategory, GoalCategoryAdmin)
