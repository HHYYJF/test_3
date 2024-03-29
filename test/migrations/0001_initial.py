# Generated by Django 4.2.9 on 2024-01-31 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay', models.CharField(choices=[('card', 'Карта'), ('account', 'Платежный счет')], max_length=12, verbose_name='Способы оплаты')),
                ('account', models.CharField(max_length=50, verbose_name='Счет')),
                ('owner', models.CharField(max_length=100, verbose_name='ФИО ладелеца')),
                ('number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('limit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='лимит')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID заявки')),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('status', models.CharField(choices=[('pending', 'Ожидает оплаты'), ('yes', 'Оплачена'), ('no', 'Отменена')], max_length=10, verbose_name='Статус')),
                ('req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.requisite', verbose_name='Реквизиты')),
            ],
        ),
    ]
