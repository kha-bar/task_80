from django import template

register = template.Library()

ABUSIVE_WORDS = [
    'сосиска',
    'редиска',
    'морковка',
]

# Регистрируем наш фильтр под именем abusive, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.


@register.filter()
def abusive(value):
    value = value.lower()
    for word in ABUSIVE_WORDS:
        value = value.replace(word, word[0] + '*' * (len(word) - 1))
    return value













