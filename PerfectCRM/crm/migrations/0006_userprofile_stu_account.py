# Generated by Django 2.0.6 on 2018-07-14 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20180713_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='stu_account',
            field=models.ForeignKey(blank=True, help_text='只有学员报名后方可为其创建账号', null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Student', verbose_name='关联学员账号'),
        ),
    ]
