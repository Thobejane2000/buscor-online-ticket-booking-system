from django.urls import path
from . import views

urlpatterns = [
    # Home, Authentication, and General Views
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('success/', views.success, name='success'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('about/', views.about, name='about'),
    path('book-bus/', views.book_bus, name='book_bus'),

    # Messages Views
    path('messages/', views.messages_list, name='messages_list'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),
]
