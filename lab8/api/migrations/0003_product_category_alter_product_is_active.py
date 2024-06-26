# Generated by Django 5.0.3 on 2024-03-31 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]
