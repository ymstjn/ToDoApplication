# Generated by Django 3.1.7 on 2021-09-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp_Management', '0024_auto_20210926_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
