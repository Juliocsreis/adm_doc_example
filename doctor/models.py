from django.db import models
from core.models import User


class Doctor(User):
    # TODO add doctor fields and methods

    def __str__(self):
        return str(self.pk)

