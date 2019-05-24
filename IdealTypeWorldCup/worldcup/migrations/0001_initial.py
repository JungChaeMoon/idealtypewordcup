# Generated by Django 2.2.1 on 2019-05-22 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worldcup_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldcup.Contest')),
            ],
        ),
    ]
