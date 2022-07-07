# Generated by Django 4.0.5 on 2022-07-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_is_emp_alter_customuser_is_self'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_emp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_self',
        ),
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Self', 'Self')], default='', help_text='Is this user self or employee?', max_length=254, verbose_name='Status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(blank=True, choices=[('Cleaner', 'Cleaner'), ('Washer', 'Washer')], help_text='Which type of this user is?', max_length=254, null=True, verbose_name='Type'),
        ),
    ]
