# Generated by Django 4.2.3 on 2023-08-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0005_accounttype_branch_district_material_user_userinfo_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='district',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='AccountType',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
