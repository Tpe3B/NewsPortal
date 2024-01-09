from django import template

register = template.Library()

SWEAR_WORDS = ['редиска', 'дурак', 'козел']

@register.filter()
def censor(value):
    text = str(value)
    for word in SWEAR_WORDS:
        text = text.replace(word[1:], "*" * (len(word)-1))
    return text