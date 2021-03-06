# Generated by Django 4.0.6 on 2022-07-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_customuser_is_emp_remove_customuser_is_self_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(blank=True, choices=[('Manager', 'Manager'), ('Cleaner', 'Cleaner'), ('Washer', 'Washer')], help_text='Which type of this user is?', max_length=254, null=True, verbose_name='Type'),
        ),
    ]
