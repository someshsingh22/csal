# Generated by Django 4.1.3 on 2022-12-06 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0003_remove_survey_yt_sub1_survey_nouse_brands"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="survey",
            name="nouse_brands",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="pastuse_brands",
        ),
        migrations.RemoveField(
            model_name="survey",
            name="produse_brands",
        ),
    ]