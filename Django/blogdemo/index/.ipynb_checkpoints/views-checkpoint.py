from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
import numpy as np
from django.core.urlresolvers import reverse_lazy
from matplotlib.figure import Figure  
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import random
import datetime
import base64
from io import BytesIO
# Create your views here.
def index(request):
    tag = Tag.objects.all()
    post = Post.objects.raw('select * from index_post')
    auther = Auther.objects.raw('select id,auther_name from index_auther')
    return render(request,'index.html',locals())

def plot(request):
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    FigureCanvasAgg(fig)
    buf = BytesIO()
    fig.savefig(buf, format='png')
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    return HttpResponse(f"<img src='data:image/png;base64,{data}'/>")

class Listviews(ListView):
    # 定义查询数据的数据表
    model = Post
    # queryset = Post.objects.all()
    # list的翻页功能
    paginate_by = 5
    # 对应查找的querset对象的名称
    context_object_name = 'post'
    # 模板的名称
    template_name = 'list.html'
    # 定义返回数据的querset的数据结构和内容
    def get_queryset(self):
        return Post.objects.all()

class Detailviews(ListView):
    # 定义查询数据的数据表
    model = Post
    # queryset = Post.objects.all()
    # list的翻页功能
    # paginate_by = 5
    # 对应查找的querset对象的名称
    context_object_name = 'post'
    # 模板的名称
    template_name = 'detail.html'
    # 定义返回数据的querset的数据结构和内容
    def get_queryset(self):
        return Post.objects.all()

class MainList(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'post'

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy('main')
    fields = ['id', 'time','post_name', 'auther', 'tag','content']
    template_name = 'Post_form.html'

class PostCreate(CreateView):
    model = Post
    # 成功后的url
    success_url = reverse_lazy('main')
    fields = ['id', 'time','post_name', 'auther', 'tag','content']
    template_name = 'Post_form.html'
    # def add(request):
    #     form = Post(request.POST or None)
    #     if form.is_valid():
    #         instance.save()
    #     context = {
    #         'form': form,
    #     }
    #     #如果没有有效提交，则仍留在原来页面
    #     return render(request, 'main.html',  context)
def funcpost(request):
    if request.method == 'GET':
        return render(request, 'funcpost.html')
    else:
        post_name = request.POST.get('post_name')
        time = request.POST.get('time')
        auther = request.POST.get('auther')
        tag = request.POST.get('tag')
        content = request.POST.get('content')

        return HttpResponse('获取请求数据成功')
