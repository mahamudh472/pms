# Generated by Django 4.2 on 2023-04-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='', max_length=30)),
                ('total_amount', models.IntegerField(default='')),
                ('available', models.IntegerField()),
                ('on_order', models.IntegerField()),
            ],
        ),
    ]
