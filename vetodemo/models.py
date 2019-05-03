from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        self.category_name

class Levels(models.Model):
    level_name = models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        self.level_name

class Exams(models.Model):
    exam_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level=models.ForeignKey(Levels,on_delete=models.CASCADE)
    def __str__(self):
        self.exam_name

class Modules(models.Model):
    module_name = models.CharField(max_length=50)
    exam=models.ForeignKey(Exams,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)

    def __str__(self):
        self.module_name

class Sub_modules(models.Model):
    sub_module_name = models.CharField(max_length=50)
    module=models.ForeignKey(Modules,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)

    def __str__(self):
        self.sub_module_name

class Module_Type(models.Model):
    module_type_name = models.CharField(max_length=50)
    sub_module=models.ForeignKey(Sub_modules,on_delete=models.CASCADE)
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)

    def __str__(self):
        self.module_type_name

class Main_model(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    level = models.ForeignKey(Levels,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exams,on_delete=models.CASCADE)
    module = models.ForeignKey(Modules,on_delete=models.CASCADE)
    sub_module = models.ForeignKey(Sub_modules,on_delete=models.CASCADE)
    module_type = models.ForeignKey(Module_Type,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    link=models.CharField(max_length=100)

class Popular_videos(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    link=models.CharField(max_length=100)
