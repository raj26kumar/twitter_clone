# Generated by Django 3.0.8 on 2020-07-05 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='mysite.Account'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.Account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Account'),
        ),
    ]
