# Generated by Django 2.2.3 on 2019-07-20 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uma', '0005_auto_20190718_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('date', models.DateField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]