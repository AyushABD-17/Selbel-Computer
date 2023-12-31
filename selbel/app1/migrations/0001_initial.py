# Generated by Django 4.2.3 on 2023-08-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('desc', models.TextField(max_length=200)),
                ('duration', models.TextField(max_length=20)),
                ('fee', models.TextField(max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='ser')),
            ],
        ),
    ]
