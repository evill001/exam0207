# Generated by Django 5.0.6 on 2024-07-01 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_statement"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="statement",
            name="user",
        ),
    ]