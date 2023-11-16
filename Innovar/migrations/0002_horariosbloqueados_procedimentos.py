# Generated by Django 4.2.7 on 2023-11-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Innovar", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HorariosBloqueados",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("Horario", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Procedimentos",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
    ]