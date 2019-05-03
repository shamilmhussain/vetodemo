from django.shortcuts import render,HttpResponse,loader,HttpResponseRedirect
from . import models
from django.db.models import Q

def index_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def add_category(request):
    template = loader.get_template('category.html')


    if request.method=="POST" and 'category' in request.POST:
        db = models.Category()
        db.category_name=request.POST.get('category')
        db.save()
    if request.method=="POST" and 'level' in request.POST:
        db = models.Levels()
        db.level_name=request.POST.get('level')
        db.save()
    if request.method=="POST" and 'exam' in request.POST:
        db = models.Exams()
        db.exam_name=request.POST.get('exam')
        db.save()
    if request.method=="POST" and 'module' in request.POST:
        db = models.Modules()
        db.module_name=request.POST.get('module')
        db.save()
    if request.method=="POST" and 'sub-module' in request.POST:
        db = models.Sub_modules()
        db.sub_module_name=request.POST.get('sub-module')
        db.save()
    if request.method=="POST" and 'module_type' in request.POST:
        db = models.Module_Type()
        db.module_type_name=request.POST.get('module_type')
        db.save()

    check=models.Main_model.objects.filter(level__level_name='10 th level')
    print('cccccccccccccccccccccc',check,)
    for i in check:
        print('hmmmmmmmmmmmm',i.level.level_name)
    return HttpResponse(template.render({}, request))

def edit_view(request):
    some = ''
    filter_set=''
    template = loader.get_template('view_or_edit.html')
    category = models.Category.objects.all()
    level = models.Levels.objects.all()
    exam = models.Exams.objects.all()
    module = models.Modules.objects.all()
    sub_module = models.Sub_modules.objects.all()
    module_type=models.Module_Type.objects.all()
    c=''
    l=''
    e=''
    m=''
    sm=''
    mt=''


    if request.method=="POST" and 'btn-main' in request.POST:
        db = models.Main_model()
        db.category=models.Category.objects.get(category_name=request.POST.get('md_category'))
        db.level = models.Levels.objects.get(level_name=request.POST.get('md_level'))
        db.exam = models.Exams.objects.get(exam_name=request.POST.get('md_exam'))
        db.module = models.Modules.objects.get(module_name=request.POST.get('md_module'))
        db.sub_module = models.Sub_modules.objects.get(sub_module_name=request.POST.get('md_sub_module'))
        db.module_type = models.Module_Type.objects.get(module_type_name=request.POST.get('md_module_type'))
        db.name=request.POST.get('md_name')
        db.link=request.POST.get('md_link')
        db.save()
        c = request.POST.get('md_category')
        l = request.POST.get('md_level')
        e = request.POST.get('md_exam')
        m = request.POST.get('md_module')
        sm = request.POST.get('md_sub_module')
        mt = request.POST.get('md_module_type')
        filter_list = [Q(category__category_name=c), Q(level__level_name=l),
                       Q(exam__exam_name=e), Q(module__module_name=m),
                       Q(sub_module__sub_module_name=sm),
                       Q(module_type__module_type_name=mt)]
        for i in filter_list:
            if filter_set != '':
                filter_set = filter_set & i
            else:
                filter_set = i
        some = models.Main_model.objects.filter(filter_set)
    if request.method == 'POST' and 'dltbtn' in request.POST:
        db=models.Main_model.objects.get(id=request.POST.get('dltbtn'))
        db.delete()
        c=request.POST.get('c')
        l=request.POST.get('l')
        e=request.POST.get('e')
        m=request.POST.get('m')
        sm=request.POST.get('sm')
        mt=request.POST.get('mt')
        filter_list = [Q(category__category_name=c), Q(level__level_name=l),
                       Q(exam__exam_name=e), Q(module__module_name=m),
                       Q(sub_module__sub_module_name=sm),
                       Q(module_type__module_type_name=mt)]
        for i in filter_list:
            if filter_set != '':
                filter_set = filter_set & i
            else:
                filter_set = i
        some = models.Main_model.objects.filter(filter_set)
        msg = 'deleted'
    if request.method == "POST" and 'btn-sel' in request.POST:
        category_name = request.POST.get('bcategory')
        level_name = request.POST.get('blevel')
        exam_name = request.POST.get('bexam')
        module_name = request.POST.get('bmodule')
        sub_module_name = request.POST.get('bsub_module')
        module_type_name = request.POST.get('bmodule_type')
        filter_list = [Q(category__category_name=category_name), Q(level__level_name=level_name), Q(exam__exam_name=exam_name),Q(module__module_name=module_name),Q(sub_module__sub_module_name=sub_module_name),Q(module_type__module_type_name=module_type_name)]
        c=category_name
        l=level_name
        e=exam_name
        m=module_name
        sm=sub_module_name
        mt = module_type_name
        for i in filter_list:
            if filter_set != '':
                filter_set = filter_set & i
            else:
                filter_set = i
        some = models.Main_model.objects.filter(filter_set)
    if request.method == "POST" and 'btn-update' in request.POST:
        print('doneeeeeeeeeeeeeeeeeeeeeeeee',request.POST.get('md_id'))
        db=models.Main_model.objects.get(id=request.POST.get('md_id'))
        db.name = request.POST.get('md_name')
        db.link = request.POST.get('md_link')
        db.save()
        c = request.POST.get('md_category')
        l = request.POST.get('md_level')
        e = request.POST.get('md_exam')
        m = request.POST.get('md_module')
        sm = request.POST.get('md_sub_module')
        mt = request.POST.get('md_module_type')
        filter_list = [Q(category__category_name=c), Q(level__level_name=l),
                       Q(exam__exam_name=e), Q(module__module_name=m),
                       Q(sub_module__sub_module_name=sm),
                       Q(module_type__module_type_name=mt)]
        for i in filter_list:
            if filter_set != '':
                filter_set = filter_set & i
            else:
                filter_set = i
        some = models.Main_model.objects.filter(filter_set)
    return HttpResponse(template.render({'category':category,'level':level,'exam':exam,'module':module,'sub_module':sub_module,'module_type':module_type,'filter_set':some,'c':c,'l':l,'e':e,'m':m,'sm':sm,'mt':mt}, request))

def test(request):
    template = loader.get_template('test.html')
    category = models.Category.objects.all()
    level=''
    exam=''
    if request.method == 'POST' and 'bcategory' in request.POST:
        level=models.Levels.objects.filter(category__category_name=request.POST.get('bcategory'))
    if request.method == 'POST' and 'blevel' in request.POST:
        exam=models.Exams.objects.filter(category__category_name=request.POST.get('bcategory'),level__level_name=request.POST.get('blevel'))
    # level = models.Levels.objects.all()
    # exam = models.Exams.objects.all()
    # module = models.Modules.objects.all()
    # sub_module = models.Sub_modules.objects.all()
    # module_type = models.Module_Type.objects.all()
    return HttpResponse(template.render({'category':category,'level':level,'exam':exam},request))

def addpopular(request):
    template=loader.get_template('addpopular.html')
    category = models.Category.objects.all()
    c=''
    some=''
    if request.method == "POST" and 'btn-sel' in request.POST:
        category_name = request.POST.get('bcategory')
        c=category_name
        some = models.Popular_videos.objects.filter(category__category_name=category_name)
    if request.method=="POST" and 'btn-main' in request.POST:
        db = models.Popular_videos()
        db.category=models.Category.objects.get(category_name=request.POST.get('md_category'))
        db.name=request.POST.get('md_name')
        db.link=request.POST.get('md_link')
        db.save()
        c = request.POST.get('md_category')
        some = models.Popular_videos.objects.filter(category__category_name=c)
    if request.method == 'POST' and 'dltbtn' in request.POST:
        db=models.Popular_videos.objects.get(id=request.POST.get('dltbtn'))
        db.delete()
        c=request.POST.get('c')
        some = models.Popular_videos.objects.filter(category__category_name=c)
    if request.method == "POST" and 'btn-update' in request.POST:
        db=models.Popular_videos.objects.get(id=request.POST.get('md_id'))
        db.name = request.POST.get('md_name')
        db.link = request.POST.get('md_link')
        db.save()
        c = request.POST.get('md_category')
        some = models.Popular_videos.objects.filter(category__category_name=c)
    return HttpResponse(template.render({'category':category,'some':some,'c':c},request))