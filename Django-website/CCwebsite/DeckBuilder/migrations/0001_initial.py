# Generated by Django 3.2.5 on 2022-04-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeckStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=30, verbose_name='Slot1_name')),
                ('slot2', models.CharField(max_length=30, verbose_name='Slot2_name')),
                ('slot3', models.CharField(max_length=30, verbose_name='Slot3_name')),
                ('slot4', models.CharField(max_length=30, verbose_name='Slot4_name')),
                ('slot5', models.CharField(max_length=30, verbose_name='Slot5_name')),
                ('slot6', models.CharField(max_length=30, verbose_name='Slot6_name')),
                ('slot7', models.CharField(max_length=30, verbose_name='Slot7_name')),
                ('slot8', models.CharField(max_length=30, verbose_name='Slot8_name')),
                ('slot9', models.CharField(max_length=30, verbose_name='Slot9_name')),
                ('slot10', models.CharField(max_length=30, verbose_name='Slot10_name')),
                ('slot11', models.CharField(max_length=30, verbose_name='Slot11_name')),
                ('slot12', models.CharField(max_length=30, verbose_name='Slot12_name')),
                ('slot13', models.CharField(max_length=30, verbose_name='Slot13_name')),
                ('slot14', models.CharField(max_length=30, verbose_name='Slot14_name')),
                ('slot15', models.CharField(max_length=30, verbose_name='Slot15_name')),
                ('slot16', models.CharField(max_length=30, verbose_name='Slot16_name')),
                ('slot17', models.CharField(max_length=30, verbose_name='Slot17_name')),
                ('slot18', models.CharField(max_length=30, verbose_name='Slot18_name')),
                ('slot19', models.CharField(max_length=30, verbose_name='Slot19_name')),
                ('slot20', models.CharField(max_length=30, verbose_name='Slot20_name')),
                ('slot21', models.CharField(max_length=30, verbose_name='Slot21_name')),
                ('slot22', models.CharField(max_length=30, verbose_name='Slot22_name')),
                ('slot23', models.CharField(max_length=30, verbose_name='Slot23_name')),
                ('slot24', models.CharField(max_length=30, verbose_name='Slot24_name')),
                ('maket_name', models.CharField(max_length=30, verbose_name='Maket_name')),
            ],
        ),
    ]