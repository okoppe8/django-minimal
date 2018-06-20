# Generated by Django 2.0.6 on 2018-06-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample', models.CharField(max_length=20, verbose_name='サンプル')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
            ],
            options={
                'verbose_name': 'アイテム',
                'verbose_name_plural': 'アイテム',
            },
        ),
    ]
