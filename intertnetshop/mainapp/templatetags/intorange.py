from django import template

register = template.Library()

# В этом файле блять ничего не менять !
# Нужен доп функционал, пиши фильтр сам !

@register.filter(name='range')
def times(products, args):
    arg_list = [int(arg) for arg in args.split(',')]
    result = []
    differ = arg_list[1]-arg_list[0]
    # print(products)
    for i in range(arg_list[0], arg_list[1]):

        result.append(products[i])
    try:
        return result
    except:
        return []
