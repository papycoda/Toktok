# Generated by Django 2.2.7 on 2022-12-02 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221201_2330'),
        ('toks', '0003_auto_20221202_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokcomment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to='users.User'),
        ),
        migrations.AddField(
            model_name='tokcomment',
            name='retoks',
            field=models.ManyToManyField(blank=True, related_name='comment_retoks', to='users.User'),
        ),
        migrations.CreateModel(
            name='TokCommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toks.TokComment')),
                ('replied_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]