# Generated by Django 3.1.7 on 2021-09-24 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp_Management', '0010_auto_20210924_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ToDoApp_Management.categorymodel'),
        ),
    ]