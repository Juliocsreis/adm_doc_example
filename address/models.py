from django.db import models


class Address(models.Model):
    logradouro = models.CharField(max_length=500, null=False, blank=False)
    bairro = models.CharField(max_length=250, null=False, blank=False)
    number = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    localidade = models.CharField(max_length=250, null=True, blank=True)
    uf = models.CharField(max_length=250, null=False, blank=False)
    country = models.CharField(max_length=250, null=False, blank=False)
    complemento = models.CharField(max_length=250, null=True, blank=True)
    cep = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return '%s %s' % (self.pk, self.logradouro)
