# Generated by Django 4.0.6 on 2022-12-17 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_hiddensurvey_prod_clear'),
    ]

    operations = [
        migrations.CreateModel(
            name='RememberedBrand_L',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenes_description', models.TextField()),
                ('audio', models.IntegerField()),
                ('usage_product', models.IntegerField()),
                ('used_brand', models.BooleanField()),
                ('ad_seen', models.BooleanField()),
                ('attention_check', models.CharField(max_length=256)),
                ('attention_check_answer', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.brand')),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.experience')),
            ],
        ),
        migrations.CreateModel(
            name='OverallQuestionSurvey_L',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.experience')),
                ('remembered_brands', models.ManyToManyField(to='form.brand')),
            ],
        ),
    ]