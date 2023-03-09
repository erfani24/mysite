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
            messages.success(request, "Message sent." )
        else:
            messages.error(request, "Error. Message not sent.")
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
             messages.success(request, "Done." )
             return HttpResponseRedirect('/')
         else:
             messages.error(request, "Error. Email not valid.")
             
    else:
        form = NewsletterForm()
        
    context = {'form': form}
    return HttpResponseRedirect('/',context)

