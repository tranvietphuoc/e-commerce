# Generated by Django 5.1.2 on 2024-10-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_option',
            field=models.CharField(choices=[('Z', 'zalopay'), ('M', 'momo')], max_length=1),
        ),
    ]
