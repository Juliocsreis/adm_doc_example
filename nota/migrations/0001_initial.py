# Generated by Django 4.2.3 on 2023-07-21 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('recipient', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'draft'), ('APPR', 'approved'), ('SENT', 'sent'), ('PAID', 'paid')], default='DRAFT', max_length=5)),
                ('invoice_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('paid_date', models.DateTimeField(blank=True, null=True)),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NotaLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_description', models.CharField(max_length=250)),
                ('service_unitary_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nota.nota')),
            ],
        ),
    ]
