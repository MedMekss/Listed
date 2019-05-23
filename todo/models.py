from django.db import models

import datetime


class Category(models.Model):
    category_name = models.CharField(max_length=32)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.category_name


class CheckList(models.Model):
    title = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.category.category_name + ' | ' + self.title


class Item(models.Model):
    title = models.CharField(max_length=32, unique=True)
    completed = models.BooleanField(default=False)
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)

    def __str__(self):
        return self.checklist.title + ' | ' + self.title
