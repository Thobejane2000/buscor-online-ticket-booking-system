from django.db import models
from django.contrib.auth.models import User

# Message Model
class Message(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('booking', 'Booking Confirmation'),
        ('promotion', 'Promotional Offer'),
        ('service', 'Service Alert'),
        ('support', 'Customer Support'),
        ('feedback', 'Feedback Request'),
        ('general', 'General Announcement'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    subject = models.CharField(max_length=200)
    body = models.TextField()
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPE_CHOICES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-created_at']

# Ticket Model
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    ticket_number = models.CharField(max_length=20, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    destination = models.CharField(max_length=50)
    pickup = models.CharField(max_length=50)
    distance = models.FloatField(null=True, blank=True)  # Added distance field
    rate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if self.distance is not None:  # Ensure distance is provided
            rate_per_unit_distance = 10  # Rate per unit distance
            self.rate = self.distance * rate_per_unit_distance
        else:
            self.rate = 0  # Default rate if distance is not provided
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_number


# Rate Model
class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
    rate_type = models.CharField(max_length=50)  # e.g. 'economy', 'business', etc.
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.rate_type} - {self.amount}"
