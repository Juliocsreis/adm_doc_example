from django.db import models


class Client(models.Model):
    owner = models.ForeignKey('doctor.Doctor', related_name='owner', null=False, blank=False, on_delete=models.CASCADE)
    cpf = models.CharField(null=True, blank=True, max_length=14)
    cnpj = models.CharField(null=True, blank=True, max_length=14)
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.CharField(max_length=250, null=False, blank=False)
    address = models.ForeignKey('address.Address', related_name='address', null=False, blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
