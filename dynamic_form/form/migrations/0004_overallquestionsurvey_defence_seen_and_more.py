# Generated by Django 4.1.3 on 2022-12-08 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0003_overallquestionsurvey_automobiles_seen_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="overallquestionsurvey",
            name="Defence_seen",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="survey",
            name="brand_Defence",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]