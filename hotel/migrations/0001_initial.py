# Generated by Django 5.2 on 2025-04-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("location", models.CharField(max_length=255)),
                ("availability", models.BooleanField(default=True)),
            ],
        ),
    ]
