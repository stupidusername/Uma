# Generated by Django 2.2.3 on 2019-07-23 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uma', '0008_auto_20190721_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonEditableArticlePrice',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('uma.articleprice', models.Model),
        ),
        migrations.AddField(
            model_name='article',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]