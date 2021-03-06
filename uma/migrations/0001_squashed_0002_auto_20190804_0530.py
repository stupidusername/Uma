# Generated by Django 2.2.3 on 2019-08-04 05:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'verbose_name_plural': 'room categories',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'article categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='articles')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='uma.ArticleCategory')),
                ('public', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticlePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('ARS', 'Argentine Peso')], default='ARS', editable=False, max_length=3)),
                ('price', djmoney.models.fields.MoneyField(decimal_places=2, max_digits=10, validators=[djmoney.models.validators.MinMoneyValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='uma.Article')),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='ArticleComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_article_components', to='uma.Article')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_article_components', to='uma.Article')),
            ],
            options={
                'unique_together': {('parent', 'child')},
            },
        ),
        migrations.AddField(
            model_name='article',
            name='components',
            field=models.ManyToManyField(through='uma.ArticleComponent', to='uma.Article'),
        ),
        migrations.CreateModel(
            name='DayType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('date', models.DateField(unique=True)),
                ('day_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uma.DayType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StayRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('ARS', 'Argentine Peso')], default='ARS', editable=False, max_length=3)),
                ('price', djmoney.models.fields.MoneyField(decimal_places=2, max_digits=10, validators=[djmoney.models.validators.MinMoneyValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NonEditableStayRate',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('uma.stayrate', models.Model),
        ),
        migrations.CreateModel(
            name='CategoryStay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uma.RoomCategory')),
                ('stay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uma.Stay')),
                ('deleted_not_null', models.BigIntegerField(default=0, editable=False)),
            ],
            options={
                'abstract': False,
                'unique_together': {('category', 'stay', 'deleted_not_null')},
            },
        ),
        migrations.AddField(
            model_name='roomcategory',
            name='stays',
            field=models.ManyToManyField(through='uma.CategoryStay', to='uma.Stay'),
        ),
        migrations.AddField(
            model_name='stayrate',
            name='category_stay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='uma.CategoryStay'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='uma.RoomCategory')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('mode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='uma.RoomMode')),
            ],
        ),
    ]
