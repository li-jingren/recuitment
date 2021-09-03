from django.db import models

# Create your models here.

JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类"),
]


Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳"),
]


class Job(models.Model):

    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位列表")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(choices=Cities, blank=False)
    job_responsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    creator = models.CharField(max_length=200, verbose_name="创建者")
