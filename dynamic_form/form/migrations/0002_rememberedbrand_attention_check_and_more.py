# Generated by Django 4.0.6 on 2022-12-11 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rememberedbrand",
            name="attention_check",
            field=models.CharField(default="Default", max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="rememberedbrand",
            name="attention_check_answer",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
