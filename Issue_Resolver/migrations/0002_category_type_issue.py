# Generated by Django 4.1.1 on 2022-09-17 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Issue_Resolver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], max_length=2)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Issue_Resolver.category')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Issue_Resolver.student')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Issue_Resolver.type')),
            ],
        ),
    ]
