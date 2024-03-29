# Generated by Django 4.2.3 on 2024-03-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='reports/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
