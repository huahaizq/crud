# Generated by Django 5.0.1 on 2024-02-01 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("empno", models.IntegerField(primary_key=True, serialize=False)),
                ("ename", models.CharField(max_length=100)),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("deptno", models.IntegerField()),
            ],
        ),
    ]
