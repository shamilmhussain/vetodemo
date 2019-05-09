from django.shortcuts import render,loader,HttpResponse
from vetodemo import models

# Create your views here.

def home_view(request):
    template = loader.get_template('main/home.html')
    items=models.Popular_videos.objects.filter(category__category_name='PSC')
    return HttpResponse(template.render({'items':items}, request))

def home2_view(request):
    template = loader.get_template('main/home2.html')
    items=models.Popular_videos.objects.filter(category__category_name='PSC')
    return HttpResponse(template.render({'items':items}, request))

def admin_dashboard(request):
    template=loader.get_template('admin panel/dashboard.html')
    return HttpResponse(template.render({},request))

def admin_manage(request):
    template=loader.get_template('admin panel/manage_employee.html')
    category = models.Category.objects.all()
    level = models.Levels.objects.all()
    exam = models.Exams.objects.all()
    module = models.Modules.objects.all()
    sub_module = models.Sub_modules.objects.all()
    module_type = models.Module_Type.objects.all()
    return HttpResponse(template.render({'category':category,'level':level,'exam':exam, 'module':module,'sub_module':sub_module,'module_type':module_type},request))

def treeview_test(request):
    template=loader.get_template('treeview_test.html')
    category = models.Category.objects.all()
    level = models.Levels.objects.all()
    exam = models.Exams.objects.all()
    module = models.Modules.objects.all()
    sub_module = models.Sub_modules.objects.all()
    module_type = models.Module_Type.objects.all()
    return HttpResponse(template.render({'category':category,'level':level,'exam':exam, 'module':module,'sub_module':sub_module,'module_type':module_type},request))

def adminbase(request):
    template=loader.get_template('main/admin_base.html')
    return HttpResponse(template.render({},request))

def manage(request):
    template = loader.get_template('main/treeview.html')
    category = models.Category.objects.all()
    level = models.Levels.objects.all()
    exam = models.Exams.objects.all()
    module = models.Modules.objects.all()
    sub_module = models.Sub_modules.objects.all()
    module_type = models.Module_Type.objects.all()
    return HttpResponse(template.render({'category':category,'level':level,'exam':exam, 'module':module,'sub_module':sub_module}, request))

def tableview(request):
    template=loader.get_template('main/tableview.html')
    return HttpResponse(template.render({},request))

def sub_module_view(request,category,level,exam,module,sub_module,type):
    template = loader.get_template('main/tableview.html')
    category=category
    level=level
    exam=exam
    module=module
    sub_module=sub_module
    a=''
    b=''
    c=len(models.Main_model.objects.filter(category__category_name=category,level__level_name=level,exam__exam_name=exam,module__module_name=module,sub_module__sub_module_name=sub_module,module_type__module_type_name="Audio"))
    d=len(models.Main_model.objects.filter(category__category_name=category,level__level_name=level,exam__exam_name=exam,module__module_name=module,sub_module__sub_module_name=sub_module,module_type__module_type_name="Video"))
    if type=="Audio":
        a="active"
    elif type=="Video":
        b="active"
    filter_db = models.Main_model.objects.filter(category__category_name=category,level__level_name=level,exam__exam_name=exam,module__module_name=module,sub_module__sub_module_name=sub_module,module_type__module_type_name=type)
    return HttpResponse(template.render({'db':filter_db,'category':category,'level':level,'exam':exam, 'module':module,'sub_module':sub_module,'a':a,'b':b,'c':c,'d':d},request))

# def video_view(request,category,level,exam,module,sub_module,type):
#     template=loader.get_template('main/video.html')
#     category = category
#     level = level
#     exam = exam
#     module = module
#     sub_module = sub_module
#     filter_db = models.Main_model.objects.filter(category__category_name=category, level__level_name=level,
#                                                  exam__exam_name=exam, module__module_name=module,
#                                                  sub_module__sub_module_name=sub_module,module_type__module_type_name=type)
#     return HttpResponse(template.render({'db': filter_db,'category':category,'level':level,'exam':exam, 'module':module,'sub_module':sub_module}, request))


