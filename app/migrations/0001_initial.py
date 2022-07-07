# Generated by Django 4.0.5 on 2022-07-01 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CLEANINGPRICE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of cleaning price object', max_length=254, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price of cleaning', max_digits=100, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='COMPANY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of company', max_length=254, verbose_name='Name')),
                ('address', models.CharField(help_text='Address of company', max_length=254, verbose_name='Address')),
                ('vat', models.CharField(help_text='VAT of company', max_length=254, verbose_name='VAT')),
                ('phone', models.CharField(help_text='Phone of company', max_length=254, verbose_name='Phone')),
                ('email', models.EmailField(help_text='Email of company', max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='PROGRAMME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of programme', max_length=254, verbose_name='Name')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Amount of programme', max_digits=256, verbose_name='Amount')),
                ('description', models.TextField(blank=True, help_text='Description of programme', null=True, verbose_name='Description')),
                ('cleaningprice', models.ForeignKey(help_text='Cleaning Budget', on_delete=django.db.models.deletion.CASCADE, to='app.cleaningprice', verbose_name='Clean Price')),
            ],
        ),
        migrations.CreateModel(
            name='CARVAN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Type of car (trailer/car)', max_length=256, verbose_name='Type')),
                ('model', models.IntegerField(help_text='Model of car', verbose_name='Model')),
                ('ev_number', models.IntegerField(help_text='EV number', verbose_name='EV number')),
                ('note', models.TextField(blank=True, help_text='Note', null=True, verbose_name='Note')),
                ('cleanguynote', models.TextField(blank=True, help_text='Enter note for cleaning guy', null=True, verbose_name='Clean Guy Note')),
                ('washingguynote', models.TextField(blank=True, help_text='Enter note for washing guy', null=True, verbose_name='Washing Guy Note')),
                ('added', models.ForeignKey(help_text='Who Added This Carvan?', limit_choices_to={'is_superuser': True, 'type': 'Manager'}, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL, verbose_name='Added By')),
                ('cleanguy', models.ForeignKey(help_text='Select any clean guy', limit_choices_to={'is_emp': True, 'is_self': True, 'type': 'Cleaner'}, on_delete=django.db.models.deletion.CASCADE, related_name='cleaner', to=settings.AUTH_USER_MODEL, verbose_name='Clean Guy')),
                ('company', models.ForeignKey(help_text='Select any company', on_delete=django.db.models.deletion.CASCADE, to='app.company', verbose_name='Company')),
                ('programme', models.ForeignKey(help_text='Programme Type', on_delete=django.db.models.deletion.CASCADE, to='app.programme', verbose_name='Programme num')),
                ('washingguy', models.ForeignKey(help_text='Select any washing guy', limit_choices_to={'is_emp': True, 'is_self': True, 'type': 'Washer'}, on_delete=django.db.models.deletion.CASCADE, related_name='washer', to=settings.AUTH_USER_MODEL, verbose_name='Washing Guy')),
            ],
        ),
    ]
