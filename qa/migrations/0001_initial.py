# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('creation_date', models.DateTimeField()),
                ('last_activity_date', models.DateTimeField()),
                ('rating', models.IntegerField()),
                ('body', models.TextField()),
                ('comment_count', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnswerComment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('creation_date', models.DateTimeField()),
                ('rating', models.IntegerField()),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('creation_date', models.DateTimeField()),
                ('last_activity_date', models.DateTimeField()),
                ('rating', models.IntegerField()),
                ('body', models.TextField()),
                ('comment_count', models.PositiveIntegerField()),
                ('answer_count', models.PositiveIntegerField()),
                ('tags_string', models.TextField()),
                ('title', models.CharField(max_length=1024)),
                ('favorite_count', models.PositiveIntegerField()),
                ('view_count', models.PositiveIntegerField()),
                ('last_edit_date', models.DateTimeField(null=True, blank=True)),
                ('accepted_answer', models.ForeignKey(null=True, related_name='accepted_for', to='qa.Answer', blank=True, on_delete=models.DO_NOTHING)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('creation_date', models.DateTimeField()),
                ('rating', models.IntegerField()),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('email', models.CharField(max_length=200)),
                ('date_joined', models.DateTimeField()),
                ('display_name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=400)),
                ('location', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('views', models.PositiveIntegerField()),
                ('votes_up', models.PositiveIntegerField()),
                ('votes_down', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='owner',
            field=models.ForeignKey(to='qa.User', on_delete=models.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='post',
            field=models.ForeignKey(related_name='comment_set', to='qa.Question', on_delete=models.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='question',
            name='last_editor',
            field=models.ForeignKey(null=True, related_name='last_edited_questions', to='qa.User', blank=True, on_delete=models.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='question',
            name='owner',
            field=models.ForeignKey(to='qa.User', on_delete=models.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='owner',
            field=models.ForeignKey(to='qa.User', on_delete=models.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='post',
            field=models.ForeignKey(related_name='comment_set', to='qa.Answer', on_delete=models.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='answer',
            name='owner',
            field=models.ForeignKey(to='qa.User', on_delete=models.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='qa.Question', on_delete=models.DO_NOTHING),
        ),
    ]
