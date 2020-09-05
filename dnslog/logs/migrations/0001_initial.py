# Generated by Django 3.1.1 on 2020-09-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DnsLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("host", models.TextField(verbose_name="host")),
                ("type", models.TextField(verbose_name="dns type")),
                (
                    "log_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="time loged"),
                ),
            ],
            options={"ordering": ["log_time"],},
        ),
        migrations.CreateModel(
            name="WebLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip", models.GenericIPAddressField(verbose_name="remote_addr")),
                ("path", models.TextField(verbose_name="path")),
                ("header", models.TextField(verbose_name="header")),
                ("body", models.TextField(verbose_name="body")),
                (
                    "log_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="time loged"),
                ),
            ],
            options={"ordering": ["log_time"],},
        ),
    ]