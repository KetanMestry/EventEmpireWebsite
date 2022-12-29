from django.db import migrations, models

class Migration(migrations.Migration):
    
    initial = True
    
    dependencies = [
    ]
    
    operations = [ 
        migrations.CreateModel(
            name= 'Event_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Party_Name',  models.CharField(max_length=300)),
                ('Location', models.CharField(max_length=300)),
                ('Date', models.CharField(max_length=300)),
                ('Time', models.CharField(max_length=300)),
                ('Age_Criteria', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Event_Details', models.CharField(max_length=1600)),
                ('Venue', models.CharField(max_length=300)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Party_Type', models.IntegerField()),
                ('Image', models.CharField(max_length=1000))
            ],
        ),
    ]