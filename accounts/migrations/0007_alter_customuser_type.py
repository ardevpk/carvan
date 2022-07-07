# Generated by Django 4.0.5 on 2022-07-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('-', '-'), ('Cleaner', 'Cleaner'), ('Washer', 'Washer'), ('Manager', 'Manager')], default='-', help_text='Which type of this user is?', max_length=254, verbose_name='Type'),
        ),
    ]
