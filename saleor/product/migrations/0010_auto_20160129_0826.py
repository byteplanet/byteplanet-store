# Generated by Django 1.9.1 on 2016-01-29 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("product", "0009_discount_categories")]

    operations = [
        migrations.RemoveField(model_name="discount", name="categories"),
        migrations.RemoveField(model_name="discount", name="products"),
        migrations.DeleteModel(name="Discount"),
    ]
