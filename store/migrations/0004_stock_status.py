# Generated by Django 5.1.4 on 2024-12-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_categorie_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
