# Generated by Django 3.2.5 on 2021-12-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_products_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Product_ID',
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]