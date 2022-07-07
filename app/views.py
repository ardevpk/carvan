from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import CARVAN, CARVANSTATUS
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect



class HomeView(LoginRequiredMixin, View):
    


    # model = CARVANSTATUS
    # paginate_by = 10
    # template_admin = 'app/admin/dashboard.html'
    # template_manager = 'app/manager/dashboard.html'
    # template_cleaner = 'app/cleaner/dashboard.html'
    # template_washer = 'app/washer/dashboard.html'
    # template_employee = 'app/employee/dashboard.html'
    # template_self = 'app/self/dashboard.html'
    # template_permission = 'app/permisssion_denied.html'
    # template_index = 'app/index.html'
    # def get_template_names(self):
    #     if self.request.user.is_superuser:
    #         return self.template_admin
    #     elif self.request.user.type == 'Cleaner':
    #         return self.template_cleaner
    #     elif self.request.user.type == 'Washer':
    #         return self.template_washer
    #     elif self.request.user.type == 'Manager':
    #         return self.template_manager
    #     elif self.request.user.status == 'Employee':
    #         return self.template_employee
    #     elif self.request.user.status == 'Self':
    #         return self.template_self
    #     else:
    #         return self.template_permission

    # def get_queryset(self):
    #     queryset = self.model.objects.all()
    #     if self.request.user.is_superuser:
    #         return queryset
    #     return queryset.filter(Q(carvan__cleaningguy=self.request.user)
    #     |Q(carvan__washingguy=self.request.user), complete=False).order_by('-id')
    def get(self, request, *args, **kwargs):
        # import threading
        # from .thread import dbChangeThread

        # thread = threading.Thread(target=dbChangeThread)
        # thread.setDaemon(True)
        # thread.start()
        return redirect('/admin/')
        # from .models import IMAGE
        # image = IMAGE.objects.last().image.url
        # return HttpResponse(
        #     '<img src="{image}"></img>'.format(image)
        # )























# @receiver(post_save, sender=CARVAN)
# def create_carvan_status(sender, **kwargs):
#     if kwargs.get('created'):
#         CARVANSTATUS.objects.create(carvan=kwargs.get('instance'))