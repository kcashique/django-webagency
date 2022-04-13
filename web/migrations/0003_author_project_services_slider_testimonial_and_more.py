# Generated by Django 4.0.3 on 2022-04-12 09:47

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_blog_points_alter_blog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('photo', versatileimagefield.fields.VersatileImageField(upload_to='')),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('advertising', 'Advertising'), ('branding', 'Branding'), ('creative', 'Creative')], default='creative', max_length=128)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('icon', versatileimagefield.fields.VersatileImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('sub_title', models.CharField(max_length=128)),
                ('btn_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=30)),
                ('profile_photo', versatileimagefield.fields.VersatileImageField(upload_to='')),
                ('feedback', models.TextField()),
                ('designation', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_one',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_two',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='points',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
