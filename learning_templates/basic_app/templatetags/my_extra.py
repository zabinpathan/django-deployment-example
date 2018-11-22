from django import template

register=template.Library()
@register.filter(name='cut')
def cut(value,arg):
    #cut agr from value parameter
    return value.replace(arg,'')

#register.filter('cut',cut)