from django import template


register = template.Library()

UNWANTED_WORDS = {
    'дурак': '***',
    'идиот': '***',
}


@register.filter(name='censor')
def replace(value, str='дурак'):
    postfix = UNWANTED_WORDS[str]
    return f'{value}{postfix}'


@register.filter(name='censor')
def replace(value, str='идиот'):
    postfix = UNWANTED_WORDS[str]
    return f'{value}{postfix}'



