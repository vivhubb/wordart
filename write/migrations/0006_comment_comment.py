# Generated by Django 3.2.16 on 2023-01-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0005_auto_20230116_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=''),
        ),
    ]
