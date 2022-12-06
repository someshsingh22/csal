# Generated by Django 4.1.3 on 2022-12-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0005_survey_pastuse_brands_survey_produse_brands"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="newuse_brands",
            field=models.ManyToManyField(related_name="newuse", to="form.brand"),
        ),
        migrations.AlterField(
            model_name="survey",
            name="pastuse_brands",
            field=models.ManyToManyField(related_name="pastuse", to="form.brand"),
        ),
        migrations.AlterField(
            model_name="survey",
            name="produse_brands",
            field=models.ManyToManyField(related_name="produse", to="form.brand"),
        ),
        migrations.AlterField(
            model_name="survey",
            name="seen_brands",
            field=models.ManyToManyField(related_name="seen", to="form.brand"),
        ),
    ]