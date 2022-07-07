from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from .models import *
from django import forms

from django import forms
from accounts.models import CustomUser
from django.db.models import Q



class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" width="100" height="100" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))









class CARVANAdminForm(forms.ModelForm):
    class Meta:
        model = CARVAN
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CARVANAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            # self.fields['cleaningguy'].queryset = CustomUser.objects.filter(Q(type='Cleaner')|Q(status='Employee')|Q(status='Self'))
            self.fields['added'].queryset = CustomUser.objects.filter(Q(is_superuser=True)|Q(type='Manager'))
    # form = CARVANAdminForm





class CARVAInline(admin.StackedInline):
    model = CARVANSTATUS
    fields = ['cleaning_required', 'washing_required']
    min_num = 1
    max_num = 1
    extra = 0
    can_delete = False




class CARVANAdmin(admin.ModelAdmin):
    list_display = ('added', 'type', 'model', 'ev_number', 'programme', 'company', 'cleaningguy', 'washingguy')
    list_filter = ('added', 'programme', 'company', 'cleaningguy', 'washingguy')
    inlines = [
        CARVAInline,
    ]
    form = CARVANAdminForm
    # def get_list_filter(self, request):
    #     qs =  super().get_list_filter(request)
    #     if request.user.type == 'Manager':
    #         return ['cleaning', 'washing', 'complete']
    #     elif request.user.is_superuser:
    #         return qs
    #     else:
    #         return []
    # search_fields = ('added', 'type', 'model', 'ev_number', 'programme')
    # ordering = ('-id',)



class PROGRAMMEAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'cleaningprice', 'description')


class CLEANINGPRICELISTAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class COMPANYAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'vat', 'phone', 'email')




class IMAGESInline(admin.TabularInline):
    model = IMAGE
    max = 5
    extra = 0
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }

class EXTRAAdmin(admin.ModelAdmin):
    list_display = ('carvan', 'cost')
    inlines = [IMAGESInline]

# class IMAGEAdmin(admin.ModelAdmin):
#     list_display = ('extra', 'image')




class CARVANSTATUSAdmin(admin.ModelAdmin):
    model = CARVANSTATUS

    def get_readonly_fields(self, request, obj):
        qs = super().get_readonly_fields(request, obj)
        if request.user.type == 'Cleaner':
            return ['get_cleaning_note']
        elif request.user.type == 'Washer':
            return ['get_washing_note']
        return qs

    # def get_fieldsets(self, request, obj):
    #     qs =  super().get_fieldsets(request, obj)
    #     print(qs[0][1]['fields'])
    #     if request.user.type == 'Cleaner':
    #         qs[0][1]['fields'].append('get_cleaning_note')
    #     elif request.user.type == 'Washer':
    #         qs[0][1]['fields'].append('get_washing_note')
    #     return qs

    @admin.display(description='Note')
    def get_cleaning_note(self, obj):
        return obj.carvan.cleaningguynote

    @admin.display(description='Note')
    def get_washing_note(self, obj):
        return obj.carvan.washingguynote

    list_display = ('carvan', 'cleaning_required', 'cleaning', "washing_required", 'washing', 'complete')
    list_filter = ('carvan__cleaningguy', 'carvan__washingguy', "complete")
    
    # def get_note(self, obj):
    #     return obj.carvan.cleaningguynote
    # get_note.admin_order_field  = 'carvan'
    # get_note.short_description = 'Note'

    # def get_note2(self, obj):
    #     return obj.carvan.washingguynote
    # get_note2.admin_order_field  = 'carvan'
    # get_note2.short_description = 'Note'

    def get_list_display(self, request):
        qs =  super().get_list_display(request)
        if request.user.is_superuser:
            return qs
        elif request.user.type == 'Cleaner':
            return ['carvan', 'cleaning_required', 'cleaning']
            # return ['carvan', 'cleaning_required', 'cleaning', "get_note"]
        elif request.user.type == 'Washer':
            return ['carvan', 'washing_required', 'washing']
            # return ['carvan', 'washing_required', 'washing', "get_note2"]
        elif request.user.type == 'Manager':
            return qs

    def get_queryset(self, request):
        qs = super(CARVANSTATUSAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.type == 'Cleaner':
            return qs.filter(carvan__cleaningguy=request.user)
        elif request.user.type == 'Washer':
            return qs.filter(carvan__washingguy=request.user)
        elif request.user.type == 'Manager':
            # return qs
            return qs.filter(carvan__washingguy=request.user).filter(carvan__cleaningguy=request.user)
        else:
            return qs.none()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            if request.user.type == 'Cleaner':
                form.base_fields['washing'].widget = forms.HiddenInput()
                form.base_fields['washing_required'].widget = forms.HiddenInput()
                form.base_fields['cleaning_required'].disabled = True
            elif request.user.type == 'Washer':
                form.base_fields['cleaning'].widget = forms.HiddenInput()
                form.base_fields['cleaning_required'].widget = forms.HiddenInput()
                form.base_fields['washing_required'].disabled = True
            
            form.base_fields['carvan'].widget = forms.HiddenInput()
            form.base_fields['complete'].widget = forms.HiddenInput()
        return form


    def get_list_filter(self, request):
        qs =  super().get_list_filter(request)
        if request.user.is_superuser:
            return qs
        elif request.user.type == 'Cleaner':
            return ['cleaning']
        elif request.user.type == 'Washer':
            return ['washing']
        elif request.user.type == 'Manager':
            return ['cleaning', 'washing', 'complete']




admin.site.site_header = "Carvan"
admin.site.site_title = "Carvan Title"
admin.site.index_title = "Welcome To Carvan Dashboard"
admin.site.register(CARVAN, CARVANAdmin)
admin.site.register(PROGRAMME, PROGRAMMEAdmin)
admin.site.register(CLEANINGPRICE, CLEANINGPRICELISTAdmin)
admin.site.register(COMPANY, COMPANYAdmin)
admin.site.register(CARVANSTATUS, CARVANSTATUSAdmin)
admin.site.unregister(Group)
admin.site.register(EXTRA, EXTRAAdmin)
# admin.site.register(IMAGE, IMAGEAdmin)
