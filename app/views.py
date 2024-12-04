from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, MessageFilterForm  # Import the custom forms
from .models import Message, Ticket
import qrcode
import uuid

# View for the user's dashboard
@login_required  
def dashboard(request):
    return render(request, 'dashboard.html')

# View for listing and filtering messages
@login_required
def messages_list(request):
    form = MessageFilterForm(request.GET or None)  # Include the MessageFilterForm
    messages = Message.objects.filter(user=request.user)
    
    if form.is_valid():
        message_type = form.cleaned_data.get('message_type')
        search = form.cleaned_data.get('search')
        
        if message_type:
            messages = messages.filter(message_type=message_type)
        if search:
            messages = messages.filter(subject__icontains=search)
    
    unread_count = messages.filter(is_read=False).count()
    
    context = {
        'messages': messages,
        'unread_count': unread_count,
        'form': form,  # Pass the form to the template
    }
    return render(request, 'dashboard/messages_list.html', context)

# View for the user's dashboard
@login_required  
def dashboard(request):
    # Fetch all tickets for the logged-in user
    tickets = Ticket.objects.all()  # Assuming you want to filter tickets by user

    context = {
        'tickets': tickets,  # Add tickets to the context
    }
    
    return render(request, 'dashboard.html', context)

# View for displaying a specific message and marking it as read
@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id, user=request.user)
    if not message.is_read:
        message.is_read = True
        message.save()
    
    return render(request, 'dashboard/message_detail.html', {'message': message})

# View for booking a bus ticket
@login_required
def book_bus(request):
    if request.method == 'POST':
        # Process payment submission and create a new Ticket instance
        ticket = Ticket(user=request.user, ticket_number='TKT-' + str(uuid.uuid4()))
        ticket.save()

        # Generate QR code for the ticket
        qr_code_img = qrcode.make(ticket.ticket_number)
        ticket.qr_code.save('qr_code.png', qr_code_img)

        return redirect('success')
    return render(request, 'book_bus.html')

# Success page after booking a ticket
def success(request):
    return render(request, 'success.html')

# Payment success page with a unique QR code
def payment_success(request):
    unique_qr_code_text = str(uuid.uuid4())
    return render(request, "payment_success.html", {"unique_qr_code_text": unique_qr_code_text})

# About page
def about(request):
    return render(request, 'about.html')

# Home page
def home(request):
    return render(request, 'home.html')

# Sign-in view
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

# Sign-up view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate the user after successful sign-up
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success')
            else:
                form.add_error(None, "Failed to authenticate newly created user.")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})