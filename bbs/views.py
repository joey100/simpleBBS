#_*_ coding:utf-8 _*_
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from bbs import models
from bbs import commentHandler
from bbs import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import time,datetime
import json
# Create your views here.


category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
def index(request):
    category_obj = models.Category.objects.get(position_index=1)
    article_list = models.Article.objects.filter(status='published')
    latestId = models.Article.objects.order_by('-id')[0].id
    return render(request,'bbs/index.html',{'category_list':category_list,
                                             'article_list':article_list,
                                            'category_obj':category_obj,
                                            'latestId':latestId,
                                            })

def category(request,id):
    category_obj = models.Category.objects.get(id = id)
    latestId = models.Article.objects.order_by('-id')[0].id
    if category_obj.position_index == 1:
        article_list = models.Article.objects.filter(status='published')
    else:
        article_list = models.Article.objects.filter(category_id = category_obj.id, status='published')
    return render(request, 'bbs/index.html', {'category_obj': category_obj,
                                              'category_list':category_list,
                                              'article_list':article_list,
                                              'latestId':latestId,})

def accountLogin(request):
    if request.method == 'POST':
        #print(request.POST)
        user = authenticate(username = request.POST.get('username'),
                            password = request.POST.get('password'))
        #print(user)
        if user is not None:
            login(request,user)
            #print(request.GET.get('next'))
            return redirect(request.GET.get('next') or '/bbs/')
        else:
            loginError = "username or password is incorrect"
            return render(request,'login.html',{'loginError':loginError})
    return render(request,'login.html')

def accountLogout(request):
    logout(request)
    return redirect('/bbs/')


def articleDetail(request,articleId):
    articleObj = models.Article.objects.get(id=articleId)
    commentTree = commentHandler.buildTree(articleObj.comment_set.select_related())
    return render(request, 'bbs/articleDetail.html', {'category_list':category_list,
                                                      'articleObj':articleObj})


def postComments(request):
    if request.method  == 'POST':
        newCommentObj = models.Comment(
            article_id = request.POST.get('article_id'),
            parent_comment_id = request.POST.get('parent_comment_id') or None,
            comment_type = request.POST.get("comment_type"),
            user_id = request.user.userprofile.id,
            comment = request.POST.get('comment')
        )
        newCommentObj.save()
    return HttpResponse(request.POST.get('parent_comment_id'))

def getComments(request,articleId):
    articleObj = models.Article.objects.get(id=articleId)
    commentTree = commentHandler.buildTree(articleObj.comment_set.select_related())
    treeHtml = commentHandler.renderCommentTree(commentTree)
    return HttpResponse(treeHtml)

def inputArticle(request):
    if request.method == 'GET':
        articleForm = forms.articleModelForm()
    elif request.method == 'POST':
        print(request.POST)
        print('前端要上传的文件, --->', request.FILES)
        articleForm = forms.articleModelForm(request.POST,request.FILES)
        if articleForm.is_valid():
            data = articleForm.cleaned_data
            data['author_id'] = request.user.userprofile.id
            articleObj = models.Article(**data)
            articleObj.save()
            articleObj1 = models.Article.objects.filter(title = request.POST.get('title')) #maybe there are same title articles
            print('article --- >',articleObj)
            print('pub date, --->',datetime.datetime.now())
            return redirect('/bbs/articleDetail/%s'% articleObj1[0].id )
        else:
            return render(request, 'bbs/inputArticle.html',{'articleForm':articleForm})
    return render(request, 'bbs/inputArticle.html',{'articleForm':articleForm})


def postArticle(request):

    return redirect('/bbs')
    pass

def fileUpload(request):
    print(request.FILES)
    fileObj = request.FILES.get('filename')
    with open('uploads/%s' %fileObj.name, 'wb+') as destination:
        for chunk in fileObj.chunks():
            destination.write(chunk)
    return render(request,'bbs/inputArticle.html')



def getLatestArticleCount(request):
    # print(request.GET.get('latestId'))
    latestArticleId = request.GET.get('latestId')
    if latestArticleId:
        newArticleCount = models.Article.objects.filter(id__gt = latestArticleId).count()
    else:
        newArticleCount = 0
    return HttpResponse(json.dumps({'newArticleCount':newArticleCount}))
