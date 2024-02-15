from django.contrib import admin
from .models import Project, Task
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    # list_editable = ['title']
    search_fields = ('id', 'title', 'slug',)
    # list_filter = ['title']
    list_display_links = ['id', 'title', 'slug']
    list_per_page = 10
    # verbose_title_plural = 'Projetos'


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'slug', 'done')
    # list_editable = ['title']
    search_fields = ('id', 'title', 'project', 'slug',)
    list_filter = ['project', 'done']
    list_display_links = ['id', 'title', 'project', 'slug']
    list_per_page = 10
    # verbose_title_plural = 'Tareas'


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
