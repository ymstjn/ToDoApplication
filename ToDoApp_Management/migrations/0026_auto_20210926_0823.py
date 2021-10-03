# Generated by Django 3.1.7 on 2021-09-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp_Management', '0025_auto_20210926_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='progress',
            field=models.CharField(choices=[('start', 0), ('quarter', 25), ('half', 50), ('thrquarter', 75), ('finish', 100)], default=0, max_length=20),
        ),
    ]