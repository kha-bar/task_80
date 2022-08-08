# from django_filters import FilterSet, ModelChoiceFilter
import django_filters
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.


class PostFilter(django_filters.FilterSet):
    class Meta:
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'post_title': ['contains'],
            'post_text': ['contains'],
            'post_creation': ['gt'],
            'post_type': ['contains'],
        }



