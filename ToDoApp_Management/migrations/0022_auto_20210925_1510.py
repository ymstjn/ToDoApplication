# Generated by Django 3.1.7 on 2021-09-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp_Management', '0021_auto_20210925_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order',
            field=models.CharField(choices=[('asc', '期限遅い順'), ('desc', '期限早い順'), ('ctg_asc', '期限遅い順（カテゴリー毎）'), ('ctg_desc', '期限早い順（カテゴリー毎）')], default='期限昇順', max_length=10),
        ),
    ]