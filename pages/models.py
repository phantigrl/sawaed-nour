from django.db import models

class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('hotel_staffing', 'توفير عمالة فندقية'),
        ('training_programs', 'برامج تدريبية'),
        ('consulting', 'استشارات وحلول'),
        ('partnership', 'شراكة وتعاون'),
        ('other', 'أخرى'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"
    

class Application(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.FileField(upload_to='cvs/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"