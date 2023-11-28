from django.db import models

# Create your models here.


class Order(models.Model):
    # 定義 order 表格的欄位
    id = models.AutoField(primary_key=True)
    drink = models.CharField(max_length=255, default='default_value')
    ice = models.CharField(max_length=50)
    suger = models.CharField(max_length=50)
    add = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    uid = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}"
