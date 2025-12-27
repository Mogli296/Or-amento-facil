from django.db import models
from django.contrib.auth.models import User

class Cnpj(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,   # <-- corrigido
        unique=True,
        null=True,
        blank=True
    )
    # outros campos...
