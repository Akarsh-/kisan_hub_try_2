# Generated by Django 2.0 on 2017-12-14 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0004_auto_20171214_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountriesTempMeanValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uMonthId', models.IntegerField()),
                ('uTempValue', models.DecimalField(decimal_places=2, max_digits=6)),
                ('uCountryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloworld.Country')),
            ],
        ),
        migrations.CreateModel(
            name='CountriesTempMinValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uMonthId', models.IntegerField()),
                ('uTempValue', models.DecimalField(decimal_places=2, max_digits=6)),
                ('uCountryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloworld.Country')),
            ],
        ),
    ]
