# Generated by Django 4.2 on 2023-05-06 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date',)},
        ),
    ]
