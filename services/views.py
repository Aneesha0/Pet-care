from django.shortcuts import render, redirect
from .models import Service
from .forms import Submit
from django.views import generic
from django.views.generic import TemplateView
from .models import Status
from accounts.models import Default_value

class Index(TemplateView):
    template_name='services/index.html'
    char=''
    services_list=Service.objects.all()[:]
    context={
        'services_list':services_list,
        'char':char
        
    }
    def get(self,request):
        return render(request, self.template_name, self.context)

class Booking(TemplateView):
    template_name='services/book.html'
    def get(self,request,**kwargs):
        if(Default_value.objects.filter(owners_id=request.user).values_list('name')[:]) and (Default_value.objects.filter(owners_id=request.user).values_list('name')[:]):
            form = Submit(initial={'owner':Default_value.objects.filter(owners_id=request.user).values_list('name')[0][0],
                                   'pet_name':Default_value.objects.filter(owners_id=request.user).values_list('pet_name')[0][0],
                                   'statuses':Status.objects.all()[0],
                                   'services':Service.objects.all()[kwargs['service_id']-1]})
        else:
            form = Submit(initial={'owner':request.user.username,
                                   'statuses':Status.objects.all()[0],
                                   'services':Service.objects.all()[kwargs['service_id']-1]})
        cost_=Service.objects.all()[kwargs['service_id']-1].cost
        service=Service.objects.all()[kwargs['service_id']-1]
        context = {
            'form': form,
            'cost_': cost_,
            'service':service
        }
        
        return render(request, self.template_name, context)

    def post(self,request,**kwargs):
        form = Submit(request.POST)
        cost_=Service.objects.all()[kwargs['service_id']-1].cost
        service=Service.objects.all()[kwargs['service_id']-1]
        if form.is_valid():
            post=form.save(commit=False)   
            post.owners=request.user
            post.save()
            if(Default_value.objects.filter(owners_id=request.user).values_list('name')[:]) and (Default_value.objects.filter(owners_id=request.user).values_list('name')[:]):
                form = Submit(initial={'owner':Default_value.objects.filter(owners_id=request.user).values_list('name')[0][0],
                                    'pet_name':Default_value.objects.filter(owners_id=request.user).values_list('pet_name')[0][0],
                                    'statuses':Status.objects.all()[0],
                                    'services':Service.objects.all()[kwargs['service_id']-1]})
            else:
                form = Submit(initial={'owner':request.user.username,
                                    'statuses':Status.objects.all()[0],
                                    'services':Service.objects.all()[kwargs['service_id']-1]})
            return redirect('home')
        return render(request,self.template_name,{'form': form,'cost_': cost_,'service':service})
         