# Generated by Django 5.1.5 on 2025-01-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='department',
            field=models.ManyToManyField(null=True, to='base.department'),
        ),
    ]
