# Generated by Django 3.1.7 on 2021-03-29 16:28

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('visitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(choices=[('WAIT', 'WAITING FOR APPROVAL'), ('APRV', 'APPROVED'), ('REJC', 'REJECTED')], max_length=4, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None)),
                ('datetime_entry', models.DateTimeField(null=True)),
                ('datetime_exit', models.DateTimeField(null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.resident')),
            ],
        ),
    ]
