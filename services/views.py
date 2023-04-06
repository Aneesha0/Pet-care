# from django.shortcuts import get_object_or_404, render, redirect
# from .models import Service
# from .models import Book
# from .forms import Submit
# from django.urls import reverse
# from django.views import generic
# from django.views.generic import TemplateView
# from django.http import HttpResponseRedirect, HttpResponse
# from .models import Status

# class index(generic.ListView):
#     template_name=''
#     template_name='services/index.html'
#     context_object_name = 'services_list'
#     def get_queryset(self):
#         return Service.objects.all()[:]

# def Booking(request,Service_id):
#     template_name='services/book.html'
#     if request!='POST':
#         form = Submit(initial={'statuses':Status.objects.all()[0],'services':Service.objects.all()[Service_id-1]})
#         cost_=Service.objects.all()[Service_id-1].cost
#         service=Service.objects.all()[Service_id-1]
#         context = {
#             'form': form,
#             'cost_': cost_,
#             'service':service
#         }
        
#         return render(request, template_name, context)

#     if request=='POST':
#         form = Submit(request.POST)
#         if form.is_valid():
#             post=form.save(commit=False)   
#             post.owners=request.user
#             post.save()
#             form=Submit(initial={'statuses':Status.objects.all()[0],'services':Service.objects.all()[Service_id-1]})
#             return redirect('book')
#         return render(request,template_name,{'form':form})



from django.shortcuts import get_object_or_404, render, redirect
from .models import Service
from .models import Book
from .forms import Submit
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from .models import Status

class index(generic.ListView):
    template_name=''
    template_name='services/index.html'
    context_object_name = 'services_list'
    def get_queryset(self):
        return Service.objects.order_by('services_name')[:]

class Booking(TemplateView):
    template_name='services/book.html'
    def get(self,request):
        form = Submit(initial={'statuses':Status.objects.all()[0]})
        cost=Service
        context = {
            'form': form,
            'cost': cost
        }
        
        return render(request, self.template_name, context)

    def post(self,request):
        form = Submit(request.POST)
        if form.is_valid():
            post=form.save(commit=False)   
            post.owners=request.user
            post.save()
            form=Submit(initial={'statuses':Status.objects.all()[0]})
            return redirect('book')
        return render(request,self.template_name,{'form':form})


        # if request.method == 'POST':
        #     # create a form instance and populate it with data from the request:
        #     form = Submit(request.POST)
        #     # check whether it's valid:
        #     if form.is_valid():
        #         # process the data in form.cleaned_data as required
        #         # ...
        #         # redirect to a new URL:
        #         form.save()
        #         return HttpResponseRedirect(reverse('services')) 
        # else:
        #     # if this is a POST request we need to process the form data
        #     services_list=Service.objects.order_by('services_name')[:]
        #     username=request.user.username
        #     form = Submit()
        #     context = {
        #     'services_list': services_list,
        #     'service_id':service_id,
        #     'username':username,
        #     'form': form
        #     }
        #     return render(request, 'services/book.html', context)
        
            # create a form instance and populate it with data from the request:

            # check whether it's valid:
            
                # process the data in form.cleaned_data as required
                # a=form.save(commit=False)
                # a.user=request.user
                
                # redirect to a new URL:
            