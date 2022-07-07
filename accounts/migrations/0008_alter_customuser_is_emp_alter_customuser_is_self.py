# Generated by Django 4.0.5 on 2022-07-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_emp',
            field=models.BooleanField(help_text='Is this user an employee?', verbose_name='Employee'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_self',
            field=models.BooleanField(help_text='Is this user self employee?', verbose_name='Self Employee'),
        ),
    ]
