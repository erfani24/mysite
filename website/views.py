from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import ContactForm,NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
             form.save()
             messages.add_message(request, messages.SUCCESS, 'Your message has been sent.')
         else:
             messages.add_message(request, messages.ERROR, 'Your message has been not sent.')
    else:
        form = ContactForm()
       
        
    context = {'form': form}
    return render(request, 'website/contact.html',context)

def test_view(request):
    if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
             form.save()
             return JsonResponse({'success': True})
             
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request,'website/test.html',context)

def newsletter_view(request):
    if request.method == 'POST':
         form = NewsletterForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/')
             
    else:
        form = NewsletterForm()
        
    context = {'form': form}
    return HttpResponseRedirect('/',context)

