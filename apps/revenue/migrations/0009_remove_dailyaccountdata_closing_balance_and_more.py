# Generated by Django 5.1 on 2024-12-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("revenue", "0008_dailyaccountdata"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dailyaccountdata",
            name="closing_balance",
        ),
        migrations.RemoveField(
            model_name="dailyaccountdata",
            name="day_expence",
        ),
        migrations.RemoveField(
            model_name="dailyaccountdata",
            name="day_income",
        ),
        migrations.AlterField(
            model_name="dailyaccountdata",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
    ]
