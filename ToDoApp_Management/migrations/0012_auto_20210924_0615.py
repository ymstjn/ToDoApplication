# Generated by Django 3.1.7 on 2021-09-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp_Management', '0011_auto_20210924_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]