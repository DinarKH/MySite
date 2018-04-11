# Generated by Django 2.0.3 on 2018-04-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('winner', models.IntegerField()),
            ],
        ),
    ]