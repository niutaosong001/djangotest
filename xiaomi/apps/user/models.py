from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from db.base_model import base_model as Base_Model

class User(AbstractUser,Base_Model):
    # 用户模型类什么也不写，继承
    phone=models.CharField(max_length=11,verbose_name="用户电话",default="")
    class Meta:
        db_table="df_user"
        verbose_name="用户"
        verbose_name_plural=verbose_name

class Address(Base_Model):
    user=models.ForeignKey("User",verbose_name="所属账户")
    receiver=models.CharField(max_length=20,verbose_name="收件人")
    addr=models.CharField(max_length=256,verbose_name="收件地址")
    zip_code=models.CharField(max_length=6,null=True,verbose_name="邮政编码")
    phone=models.CharField(max_length=11,verbose_name="联系电话")
    is_default=models.BooleanField(default=False,verbose_name="是否默认")

    class Meta:
        db_table="df_address"
        verbose_name="地址"
        verbose_name_plural=verbose_name





