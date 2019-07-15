# Generated by Django 2.2.3 on 2019-07-15 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='rooms', to='uma.RoomCategory'),
            preserve_default=False,
        ),
    ]