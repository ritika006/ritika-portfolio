from django.shortcuts import render
from .models import ContactMessage

def contact_view(request):
    success = False

    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        success = True

    return render(request, 'contact/contact.html', {
        'success': success
    })
