# Generated by Django 5.0.1 on 2024-07-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergieTerug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tijdstip', models.CharField(max_length=10)),
                ('Waarde', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
