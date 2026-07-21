from django.contrib import admin

from .models import Author, Book, Review


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author',)
    list_filter = ('publication_date', 'author',)
    search_fields = ('title', 'author__first_name', 'author__last_name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating',)

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     """Регистрация кастомной модели пользователя в админке"""
#
#     # Поля, которые будут отображаться в списке
#     list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
#
#     # Поля для поиска
#     search_fields = ('username', 'email', 'first_name', 'last_name')
#
#     # Фильтры
#     list_filter = ('is_staff', 'is_active', 'is_superuser')
#
#     # Поля, которые можно редактировать прямо в списке
#     list_editable = ('is_staff', 'is_active')
#
#     # Порядок сортировки
#     ordering = ('username',)
#
#     # Поля, которые отображаются при создании/редактировании
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#
#     # Поля при создании нового пользователя
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2'),
#         }),
#     )
