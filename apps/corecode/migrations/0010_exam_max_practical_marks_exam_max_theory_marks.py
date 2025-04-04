# Generated by Django 5.1 on 2024-12-31 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0009_alter_schemes_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="exam",
            name="max_practical_marks",
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exam",
            name="max_theory_marks",
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
    ]
