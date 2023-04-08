# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .forms import Save,UpdateUserForm,UpdateStatus
from django.shortcuts import get_object_or_404, render, redirect
from .models import Default_value
from django.contrib import messages
from services.models import Book,Status,Service


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class Update(TemplateView):
    template_name='accounts/default.html'
    def get(self,request):
        if (Default_value.objects.filter(owners_id=request.user).values_list('name')[:]) and (Default_value.objects.filter(owners_id=request.user).values_list('pet_name')[:]):
            form=Save(initial={'name':Default_value.objects.filter(owners_id=request.user).values_list('name')[0][0],
                               'pet_name':Default_value.objects.filter(owners_id=request.user).values_list('pet_name')[0][0]})
        else:
            form=Save()
        user_form = UpdateUserForm(instance=request.user)
        return render(request, self.template_name, {'user_form': user_form, 'form':form})

    def post(self,request):

        if (Default_value.objects.filter(owners_id=request.user).values_list('name')[:]) and (Default_value.objects.filter(owners_id=request.user).values_list('pet_name')[:]):
            name = request.POST['name']
            pet_name = request.POST['pet_name']
            user_form = UpdateUserForm(request.POST, instance=request.user)
            form=Save(request.POST)
            if form.is_valid() and user_form.is_valid():
                user_form.save()
                text=Default_value.objects.get(owners_id=request.user)
                text.name=name
                text.pet_name=pet_name
                text.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect('accounts:default')
            return render(request,self.template_name,{'user_form': user_form,'form':form})

        else:
            form=Save(request.POST)
            user_form = UpdateUserForm(request.POST, instance=request.user)
            if form.is_valid() and user_form.is_valid():
                user_form.save()
                post=form.save(commit=False)   
                post.owners=request.user
                post.save()
                form=Save(initial={'name':Default_value.objects.filter(owners_id=request.user).values_list('name')[0][0],
                                   'pet_name':Default_value.objects.filter(owners_id=request.user).values_list('pet_name')[0][0]})
                messages.success(request, 'Your profile is updated successfully')
                return redirect('accounts:default')
            return render(request,self.template_name,{'user_form': user_form, 'form':form})    
        
class account(generic.TemplateView):
    template_name="accounts/index.html"        
    def get(self, request):
        return render(request, self.template_name)
    
class Display(TemplateView):
    template_name = 'accounts/past.html'
    def get(self,request):
        book=Book.objects.filter(owners_id=request.user).values().order_by('-time')
        s=Status.objects.all()
        service=Service.objects.all()
        return render(request, self.template_name,{'book':book})

class Cancel(TemplateView):
    def post(self,request,**kwargs):
        b=Book.objects.filter(owners_id=request.user).order_by('-time')[kwargs['counter']-1]
        b.statuses=Status.objects.all()[2]
        b.save()
        return redirect('accounts:display')
        