# Generated by Django 4.1.3 on 2022-12-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0002_rename_brand_automobiles_0_survey_brand_automobiles_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="overallquestionsurvey",
            name="Automobiles_seen",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="overallquestionsurvey",
            name="Clothing and Apparel_seen",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="overallquestionsurvey",
            name="Cosmetics_seen",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="overallquestionsurvey",
            name="Electronics_seen",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="overallquestionsurvey",
            name="Food_seen",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="overallquestionsurvey",
            name="Healthcare_seen",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="overallquestionsurvey",
            name="Telecom_seen",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]