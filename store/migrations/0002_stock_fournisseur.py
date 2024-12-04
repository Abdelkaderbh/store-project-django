# Generated by Django 5.1.4 on 2024-12-04 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='store.fournisseur'),
        ),
    ]
