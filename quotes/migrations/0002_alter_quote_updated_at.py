# Generated by Django 4.1.2 on 2022-10-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]