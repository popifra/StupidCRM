from django.db import models

# Create your models here.
class anagrafica(models.Model):
    Nome =  models.CharField(max_length=50)
    Indirizzo = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.Nome
    class Meta:
        verbose_name_plural = "Anagrafica"

class esiti(models.Model):
    Nome_e=models.ForeignKey(anagrafica, on_delete=models.CASCADE)
    Esito=models.CharField(max_length=20)
    Utente=models.ForeignKey('auth.User')
    Contact_Date= models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.Nome_e

    class Meta:
        verbose_name_plural = "Esiti"
