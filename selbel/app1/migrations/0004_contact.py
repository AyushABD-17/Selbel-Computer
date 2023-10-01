# Generated by Django 4.2.3 on 2023-08-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_team_fee_team_title_alter_team_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
