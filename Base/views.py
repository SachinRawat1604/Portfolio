from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Contact
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'projects': projects})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        # Save to database
        contact = Contact(name=name, email=email, number=number, message=message)
        contact.save()

        # Email sending
        full_message = f"""
        You have a new contact form submission:

        Name: {name}
        Email: {email}
        Phone: {number}

        Message:
        {message}
        """

        try:
            send_mail(
                subject=f"Portfolio Contact: {name}",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['sachinrawat4666@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        
        except Exception as e:
            print(f"Email sending failed: {e}")
            messages.error(request, "There was an error sending your message.")
            
        return redirect('home')
    
    return redirect('home')
