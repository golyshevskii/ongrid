# Generated by Django 4.1.3 on 2022-11-16 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customeuser_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeuser',
            name='username',
        ),
    ]
