from django.db import models
from django.contrib.auth.models import User

TAX_PAYER = 'tax_payer'
TAX_OFFICIAL = 'tax_official'
USER_TYPE_CHOICES = (
    ('tax_payer', 'Tax Payer'),
    ('tax_official', 'Tax Official')
)


class UserProfile(User):
    role = models.TextField(max_length=20, choices=USER_TYPE_CHOICES)
