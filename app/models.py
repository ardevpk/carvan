from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL




class CLEANINGPRICE(models.Model):
    name = models.CharField(max_length=254, verbose_name='Name', help_text='Name of cleaning price object')
    price = models.DecimalField(verbose_name='Price', help_text='Price of cleaning',max_digits=100, decimal_places=2)
    def __str__(self):
        return self.name




class PROGRAMME(models.Model):
    name = models.CharField(max_length=254, verbose_name='Name', help_text='Name of programme')
    amount = models.DecimalField(verbose_name='Amount', help_text='Amount of programme', max_digits=256, decimal_places=2)
    cleaningprice = models.ForeignKey(to=CLEANINGPRICE, on_delete=models.CASCADE, verbose_name='Clean Price', help_text='Cleaning Budget')
    description = models.TextField(verbose_name='Description', help_text='Description of programme', null=True, blank=True)
    def __str__(self):
        return self.name






class COMPANY(models.Model):
    name = models.CharField(max_length=254, verbose_name='Name', help_text='Name of company')
    address = models.CharField(max_length=254, verbose_name='Address', help_text='Address of company')
    vat = models.CharField(max_length=254, verbose_name='VAT', help_text='VAT of company')
    phone = models.CharField(max_length=254, verbose_name='Phone', help_text='Phone of company')
    email = models.EmailField(verbose_name='Email', help_text='Email of company')
    def __str__(self):
        return self.name




class CARVAN(models.Model):
    added = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Added By', help_text='Who Added This Carvan?', limit_choices_to={'is_staff': True}, related_name='staff')

    type = models.CharField(max_length=256, verbose_name='Type', help_text='Type of car (trailer/car)')

    model = models.IntegerField(verbose_name='Model', help_text='Model of car')

    ev_number = models.IntegerField(verbose_name='EV number', help_text='EV number')

    programme = models.ForeignKey(to=PROGRAMME, verbose_name='Programme num', help_text='Programme Type', on_delete=models.CASCADE)

    company = models.ForeignKey(to=COMPANY, verbose_name='Company', help_text='Select any company', on_delete=models.CASCADE)

    note = models.TextField(verbose_name='Note', help_text='Note', null=True, blank=True)

    cleaningguy = models.ForeignKey(to=User, verbose_name='Cleaning Guy', help_text='Select any clean guy', on_delete=models.CASCADE, limit_choices_to={'is_superuser': False}, related_name='cleaner', null=True, blank=True)

    cleaningguynote = models.TextField(verbose_name='Clean Guy Note', help_text='Enter note for cleaning guy', null=True, blank=True)

    washingguy = models.ForeignKey(to=User, verbose_name='Washing Guy', help_text='Select any washing guy', on_delete=models.CASCADE, limit_choices_to={'is_superuser': False}, related_name='washer', null=True, blank=True)
    
    washingguynote = models.TextField(verbose_name='Washing Guy Note', help_text='Enter note for washing guy', null=True, blank=True)
    def __str__(self):
        return f"{self.type} || {self.model} || {self.ev_number}"




class CARVANSTATUS(models.Model):
    carvan = models.OneToOneField(to=CARVAN, on_delete=models.CASCADE, verbose_name='Carvan', help_text='Select any carvan')

    cleaning_required = models.BooleanField(verbose_name='Cleaning Required', help_text='Is cleaning required?', default=False)
    cleaning = models.BooleanField(verbose_name='Cleaning done', help_text='Cleaning Status', default=False)

    washing_required = models.BooleanField(verbose_name='Washing Required', help_text='Is washing required?', default=False)
    washing = models.BooleanField(verbose_name='Washing done', help_text='Washing Status', default=False)

    complete = models.BooleanField(verbose_name='Complete done', help_text='Complete Status', default=False)

    def __str__(self):
        return f"{self.carvan.type} || {self.carvan.model} || {self.carvan.ev_number}"






class EXTRA(models.Model):
    carvan = models.ForeignKey(to=CARVANSTATUS, on_delete=models.CASCADE, verbose_name='Carvan', help_text='Select any carvan')

    cost = models.DecimalField(verbose_name='Cost', help_text='Cost of extra', max_digits=256, decimal_places=2)

    note = models.TextField(verbose_name='Note', help_text='Note', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.carvan.carvan.type} || {self.carvan.carvan.model} || {self.carvan.carvan.ev_number}"




class IMAGE(models.Model):
    extra = models.ForeignKey(to=EXTRA, on_delete=models.CASCADE, verbose_name='Extra', help_text='Select any extra')

    image = models.ImageField(verbose_name='Image', help_text='Image of damage', upload_to='images/')