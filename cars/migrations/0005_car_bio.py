# Generated by Django 5.1 on 2024-08-31 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0004_carinventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
