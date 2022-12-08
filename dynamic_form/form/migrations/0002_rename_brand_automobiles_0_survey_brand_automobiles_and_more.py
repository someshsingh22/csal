# Generated by Django 4.1.3 on 2022-12-08 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="survey",
            old_name="brand_Automobiles_0",
            new_name="brand_Automobiles",
        ),
        migrations.RenameField(
            model_name="survey",
            old_name="brand_Automobiles_1",
            new_name="brand_Clothing and Apparel",
        ),
        migrations.RenameField(
            model_name="survey",
            old_name="brand_Automobiles_2",
            new_name="brand_Cosmetics",
        ),
        migrations.RenameField(
            model_name="survey",
            old_name="brand_Clothing and Apparel_0",
            new_name="brand_Electronics",
        ),
        migrations.RenameField(
            model_name="survey",
            old_name="brand_Clothing and Apparel_1",
            new_name="brand_Food",
        ),
        migrations.RenameField(
            model_name="survey",
            old_name="brand_Clothing and Apparel_2",
            new_name="brand_Healthcare",
        ),
        migrations.RenameField(
            model_name="survey",
            old_name="brand_Cosmetics_0",
            new_name="brand_Telecom",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Cosmetics_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Cosmetics_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Electronics_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Electronics_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Electronics_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Food_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Food_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Food_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Healthcare_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Healthcare_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Healthcare_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Telecom_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Telecom_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="brand_Telecom_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Automobiles_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Automobiles_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Automobiles_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Clothing and Apparel_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Clothing and Apparel_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Clothing and Apparel_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Cosmetics_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Cosmetics_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Cosmetics_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Electronics_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Electronics_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Electronics_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Food_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Food_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Food_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Healthcare_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Healthcare_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Healthcare_2",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Telecom_0",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Telecom_1",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="product_Telecom_2",
        ),
    ]
