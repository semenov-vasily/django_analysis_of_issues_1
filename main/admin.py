from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


from main.models import Category, Post, Tag, PostTag


class PostTagInlineFormSet(BaseInlineFormSet):  # своя логика для формы (BaseInlineFormSet-набор форм) взаимодействует с формой PostTagInline
    def clean(self):  # метод для валидации данных, которые внесены в форму
        count = 0  # счетчик, подсчитывающий количество тегов is_main(основной тег)
        for form in self.forms:  # проходимся по формам
            if form.cleaned_data.get("is_main"):  # из формы получаем из словаря cleaned_data (в нем поля формы) поле is_main
                count += 1
            if count > 1:
                raise ValidationError("ошибка, только один тег основной")
        if count == 0:
            raise ValidationError("ошибка, должен быть один тег основным")
        return super().clean()  # завершение метода clean и продолжение кода (запись данных формы в таблицу)


class PostTagInline(admin.TabularInline):  # дополнительная форма заполнения для основной (теги в постах)
    model = PostTag
    fields = ["tag", "is_main"]  # заполняемые поля
    extra = 3  # количество строк (тегов) для заполнения
    formset = PostTagInlineFormSet  # применяется логика класса PostTagInlineFormSet к этой форме


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostTagInline]
    list_display = ["title", "category", "created_at"]  # отображение полей в админке
    list_filter = ["category"]  # фильтрация по категориям
    search_fields = ["title"]  # поиск указанных слов(части слов) в данном поле и вывод записей(постов)


# категории в админке
admin.site.register(Category)
# теги в админке
# admin.site.register(Tag)
# равнозначно
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass



# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostTagInline]
#
# admin.site.register(Post, PostAdmin)

# равнозначно
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostTagInline]