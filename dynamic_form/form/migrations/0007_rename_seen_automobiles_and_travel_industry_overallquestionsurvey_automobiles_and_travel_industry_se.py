# Generated by Django 4.1.3 on 2022-12-08 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "form",
            "0006_rename_automobiles and travel industry_seen_overallquestionsurvey_seen_automobiles_and_travel_indust",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Automobiles_and_Travel_Industry",
            new_name="Automobiles_and_Travel_Industry_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Clothing_and_Apparel",
            new_name="Clothing_and_Apparel_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Cosmetics",
            new_name="Cosmetics_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Defence",
            new_name="Defence_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Education",
            new_name="Education_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Electronics",
            new_name="Electronics_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Energy",
            new_name="Energy_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Finance_and_Banking",
            new_name="Finance_and_Banking_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Food_and_Beverages",
            new_name="Food_and_Beverages_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Healthcare_and_Pharmaceutical",
            new_name="Healthcare_and_Pharmaceutical_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Software_Industry",
            new_name="Software_Industry_seen",
        ),
        migrations.RenameField(
            model_name="overallquestionsurvey",
            old_name="seen_Telecom",
            new_name="Telecom_seen",
        ),
    ]