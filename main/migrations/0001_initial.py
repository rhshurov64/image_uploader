# Generated by Django 4.2.2 on 2023-08-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('image', models.ImageField(max_length=250, upload_to='uploads/')),
            ],
        ),
    ]
