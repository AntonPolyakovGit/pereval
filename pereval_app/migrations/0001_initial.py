# Generated by Django 4.2.7 on 2023-11-24 19:14

from django.db import migrations, models
import django.db.models.deletion
import pereval_app.func


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(blank=True, max_length=2000, null=True, upload_to=pereval_app.func.get_path_upload_photos, verbose_name='Изображение')),
                ('title', models.TextField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.TextField(blank=True, null=True, verbose_name='Зима')),
                ('summer', models.TextField(blank=True, null=True, verbose_name='Лето')),
                ('autumn', models.TextField(blank=True, null=True, verbose_name='Осень')),
                ('spring', models.TextField(blank=True, null=True, verbose_name='Весна')),
            ],
            options={
                'verbose_name': 'Уровень сложности',
                'verbose_name_plural': 'Уровни сложности',
            },
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(choices=[('new', 'новый'), ('pending', 'в работе'), ('accepted', 'принят'), ('rejected', 'отклонен')])),
                ('beauty_title', models.TextField(blank=True, null=True, verbose_name='Основное название вершины')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Название вершины')),
                ('other_titles', models.TextField(blank=True, null=True, verbose_name='Другое название')),
                ('connect', models.TextField(blank=True, null=True, verbose_name='Связывает')),
                ('add_time', models.TimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'pereval_added',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fam', models.TextField(max_length=255, verbose_name='Фамилия')),
                ('name', models.TextField(max_length=255, verbose_name='Имя')),
                ('otc', models.TextField(max_length=255, verbose_name='Отчество')),
                ('phone', models.TextField(max_length=255, verbose_name='Контактный телефон')),
            ],
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('email',), name='user_unique'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='coords',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pereval_app.coords'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval_app.level'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval_app.user'),
        ),
        migrations.AddField(
            model_name='image',
            name='pereval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval_app.pereval'),
        ),
    ]
