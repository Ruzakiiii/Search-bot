# Generated by Django 4.0.5 on 2023-01-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_page', '0002_alter_get_user_info_one_string_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get_user_info_one',
            name='string_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
