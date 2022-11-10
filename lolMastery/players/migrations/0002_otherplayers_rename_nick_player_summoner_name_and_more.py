# Generated by Django 4.1.1 on 2022-10-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otherplayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summoner_name', models.CharField(max_length=200)),
                ('summoner_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='player',
            old_name='nick',
            new_name='summoner_name',
        ),
        migrations.AddField(
            model_name='player',
            name='summoner_id',
            field=models.IntegerField(null=True),
        ),
    ]
