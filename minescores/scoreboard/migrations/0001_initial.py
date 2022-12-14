# Generated by Django 4.1.1 on 2022-09-22 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BEGINNER', 'débutant'), ('INTERMEDIATE', 'intérmédiraire'), ('EXPERT', 'expert')], max_length=30)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('count_mine', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('time', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('count_mine', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreboard.user')),
            ],
        ),
    ]
