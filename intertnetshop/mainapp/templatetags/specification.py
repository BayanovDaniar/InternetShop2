from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TABLE_HEAD = """

            """

TABLE_TAIL = """


            """
TABLE_CONTENT = """
                <div class="lower-features">
                <div class="column">{name}</div>
                <div class="value">{value}</div>
                </div>
                """

PRODUCT_SPECT = {
    "notebook": {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge'
    },
    "smartphone": {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'Разрешение экрана': 'resolution',
        'Заряд аккумулятор': 'accum_volume',
        'Оперативная память' : 'ram',
        'Наличие слота для SD карты' : 'sd',
        'Максимальный объем SD карты' : 'sd_volume_max',
        'Камера (МП)': 'main_cam_mp',
        'Фронтальная камера (МП)': 'front_cam_mp'
    },
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPECT[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value = getattr(product,value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(get_product_spec(product, model_name))
