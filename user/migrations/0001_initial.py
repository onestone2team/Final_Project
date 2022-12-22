# Generated by Django 4.1.3 on 2022-12-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(error_messages={'unique': '이미 사용중인 이메일입니다'}, max_length=254, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=30, verbose_name='비밀번호')),
                ('profile', models.ImageField(default='basic_profile/guest.png', upload_to='%y/%m/', verbose_name='프로필 사진')),
                ('profilename', models.CharField(error_messages={'unique': '이미 사용중인 이름입니다'}, max_length=50, verbose_name='회원이름')),
                ('address', models.TextField(blank=True, null=True, verbose_name='배송지')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='연락처')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
