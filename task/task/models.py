__author__ = 'alex'
from django.db import models
import type
'''
def create_model(name, attrs={}, meta_attrs={}, module_path='django.db.models'):
    attrs['__module__'] = module_path

    class Meta: pass

    Meta.__dict__.update(meta_attrs, __module__=module_path)
    attrs['Meta'] = Meta
    return type(name, (models.Model,), attrs)


class Animal(models.Model):
    name = models.CharField(max_length=32)


attrs = {
    'name': models.CharField(max_length=32),
    '__module__': 'myapp.models'
}
Animal = type("Animal", (models.Model,), attrs)
'''

dct = {
    "__module__": "task.models",
    "title": models.CharField(max_length=255),
    "content": models.TextField()
}
Post = type('Post', (models.Model,), dct)


def install(model):
    from django.core.management import sql, color
    from django.db import connection

    style = color.no_style()

    cursor = connection.cursor()
    statements, pending = sql.sql_model_create(model, style)
    for sql in statements:
        cursor.execute(sql)

install(Post)