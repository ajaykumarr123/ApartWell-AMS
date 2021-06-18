# Generated by Django 3.1.7 on 2021-03-29 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('CRE', 'Created'), ('PRG', 'In Progress'), ('CMP', 'Completed')], default='CRE', max_length=3)),
                ('content', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.resident')),
            ],
        ),
    ]