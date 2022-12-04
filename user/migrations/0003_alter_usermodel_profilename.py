# Generated by Django 4.1.3 on 2022-12-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_usermodel_profilename"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="profilename",
            field=models.CharField(
                error_messages={"unique": "profilename 이미 사용중인 이름입니다"},
                max_length=50,
                unique=True,
                verbose_name="회원이름",
            ),
        ),
    ]