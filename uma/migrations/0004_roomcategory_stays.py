# Generated by Django 2.2.3 on 2019-07-28 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uma', '0003_categorystay'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomcategory',
            name='stays',
            field=models.ManyToManyField(through='uma.CategoryStay', to='uma.Stay'),
        ),
    ]
