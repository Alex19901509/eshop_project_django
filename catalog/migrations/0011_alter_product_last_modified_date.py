# Generated by Django 4.2.3 on 2023-08-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_product_date_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
    ]
