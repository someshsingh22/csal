# Generated by Django 4.1.3 on 2022-12-07 06:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0007_apprisemethod_remove_survey_newuse_brands_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="brand_Automobiles_0",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Automobiles_1",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Automobiles_2",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Clothing and Apparel_0",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Clothing and Apparel_1",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Clothing and Apparel_2",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Cosmetics_0",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Cosmetics_1",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Cosmetics_2",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Electronics_0",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Electronics_1",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Electronics_2",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Food_0",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Food_1",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Food_2",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Healthcare_0",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Healthcare_1",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Healthcare_2",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Telecom_0",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Telecom_1",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Telecom_2",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="survey",
            name="gpa",
            field=models.FloatField(
                default=5.12,
                validators=[
                    django.core.validators.MinValueValidator(4.0),
                    django.core.validators.MaxValueValidator(10.0),
                ],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Automobiles_0",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Automobiles_1",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Automobiles_2",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Clothing and Apparel_0",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Clothing and Apparel_1",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Clothing and Apparel_2",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Cosmetics_0",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Cosmetics_1",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Cosmetics_2",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Electronics_0",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Electronics_1",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Electronics_2",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Food_0",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Food_1",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Food_2",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Healthcare_0",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Healthcare_1",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Healthcare_2",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Telecom_0",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Telecom_1",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="product_Telecom_2",
            field=models.CharField(default="tesla", max_length=255),
            preserve_default=False,
        ),
    ]
