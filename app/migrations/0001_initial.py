# Generated by Django 3.1.2 on 2020-10-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=500)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=360)),
                ('release_date', models.DateField()),
                ('author', models.ManyToManyField(to='app.Author')),
            ],
        ),
    ]