# Generated by Django 4.1.4 on 2022-12-30 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events_App', '0002_alter_event_info_date_alter_event_info_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=500)),
                ('Email', models.EmailField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Pincode', models.BigIntegerField()),
                ('No_Of_Mems', models.IntegerField()),
                ('Contact_No', models.BigIntegerField()),
                ('Party_Id', models.IntegerField()),
            ],
        ),
    ]
