# Generated by Django 4.2.4 on 2023-09-06 09:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chatbot", "0003_alter_chathistory_updated_on_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chathistory",
            options={"ordering": ("created_on",)},
        ),
    ]
