# Generated by Django 4.2.3 on 2023-07-21 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nota', '0003_nota_recipeient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='recipeient',
            new_name='recipient',
        ),
    ]