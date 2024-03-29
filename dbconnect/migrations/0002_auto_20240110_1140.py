# Generated by Django 3.2.12 on 2024-01-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('connected', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='DatabaseConnection',
        ),
    ]
