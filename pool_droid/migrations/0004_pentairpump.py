# Generated by Django 3.2.4 on 2021-06-30 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool_droid', '0003_onewiretempsensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='PentairPump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('pump_address', models.CharField(choices=[(15, 'BROADCAST'), (16, 'SUNTOUCH'), (32, 'EASYTOUCH'), (33, 'REMOTE_CONTROLLER'), (34, 'REMOTE_WIRELESS_CONTROLLER'), (72, 'QUICKTOUCH'), (96, 'INTELLIFLO_PUMP_1'), (97, 'INTELLIFLO_PUMP_2'), (98, 'INTELLIFLO_PUMP_3'), (99, 'INTELLIFLO_PUMP_4'), (100, 'INTELLIFLO_PUMP_5'), (101, 'INTELLIFLO_PUMP_6'), (102, 'INTELLIFLO_PUMP_7'), (103, 'INTELLIFLO_PUMP_8'), (104, 'INTELLIFLO_PUMP_9'), (105, 'INTELLIFLO_PUMP_10'), (106, 'INTELLIFLO_PUMP_11'), (107, 'INTELLIFLO_PUMP_12'), (108, 'INTELLIFLO_PUMP_13'), (109, 'INTELLIFLO_PUMP_14'), (110, 'INTELLIFLO_PUMP_15'), (111, 'INTELLIFLO_PUMP_16')], max_length=4)),
                ('port', models.CharField(max_length=100, unique=True)),
                ('baud_rate', models.IntegerField(choices=[(50, 50), (75, 75), (110, 110), (134, 134), (150, 150), (200, 200), (300, 300), (600, 600), (1200, 1200), (1800, 1800), (2400, 2400), (4800, 4800), (9600, 9600), (19200, 19200), (38400, 38400), (57600, 57600), (115200, 115200), (230400, 230400), (460800, 460800), (500000, 500000), (576000, 576000), (921600, 921600), (1000000, 1000000), (1152000, 1152000), (1500000, 1500000), (2000000, 2000000), (2500000, 2500000), (3000000, 3000000), (3500000, 3500000), (4000000, 4000000)], default=9600)),
                ('byte_size', models.FloatField(choices=[(5, 5), (6, 6), (7, 7), (8, 8)], default=8)),
                ('parity', models.CharField(choices=[('N', 'None'), ('E', 'Even'), ('O', 'Odd'), ('M', 'Mark'), ('S', 'Space')], default='N', max_length=1)),
                ('stop_bits', models.FloatField(choices=[(1, 1), (1.5, 1.5), (2, 2)], default=1)),
            ],
        ),
    ]