import uuid

from django.db import models


class Nota(models.Model):
    DRAFT = 'DRAFT'
    APPROVED = 'APPR'
    SENT = 'SENT'
    PAID = 'PAID'

    NF_STATUS = [(DRAFT, 'draft'), (APPROVED, 'approved'), (SENT, 'sent'), (PAID, 'paid')]

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey('core.User', null=False, blank=False, on_delete=models.CASCADE)
    recipient = models.ForeignKey('client.Client', null=False, blank=False, on_delete=models.CASCADE)
    recipient_static_data = models.JSONField(null=False,
                                 blank=False)  # https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.JSONField
    status = models.CharField(choices=NF_STATUS, max_length=5, default=DRAFT, null=False, blank=False)
    invoice_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    paid_date = models.DateTimeField(null=True, blank=True)
    total_value = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=20)

    def __str__(self):
        return str(self.pk)


class NotaLineItem(models.Model):
    nota = models.ForeignKey(Nota, null=False, blank=False, on_delete=models.CASCADE)
    service_description = models.CharField(max_length=250, null=False, blank=False)
    service_unitary_value = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=20)
    quantity = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=1000)

    def __str__(self):
        return str(self.pk)
