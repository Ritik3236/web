# Generated by Django 3.2.3 on 2021-05-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('type', models.CharField(choices=[('ques', 'Question Paper'), ('notes', 'Notes'), ('solution', 'Solution')], default='ques', max_length=10)),
                ('document', models.FileField(upload_to='userUploaded/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuotesApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anonymous', max_length=20)),
                ('author_img', models.ImageField(blank=True, null=True, upload_to='quote/')),
                ('quote_type', models.CharField(blank=True, max_length=20)),
                ('source', models.CharField(blank=True, default='Reddit', max_length=20)),
                ('quote', models.TextField(max_length=200)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
