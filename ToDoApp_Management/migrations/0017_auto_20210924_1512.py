# Generated by Django 3.1.7 on 2021-09-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp_Management', '0016_auto_20210924_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='category',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='content',
            field=models.CharField(max_length=40),
        ),
    ]