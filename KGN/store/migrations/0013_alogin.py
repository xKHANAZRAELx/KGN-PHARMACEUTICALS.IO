# Generated by Django 4.0.3 on 2022-03-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_category_id_alter_customer_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alogin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]