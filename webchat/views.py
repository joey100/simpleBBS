from django.shortcuts import render,HttpResponse
import json,time,queue
from webchat import models
from django.core.cache import cache
import os
# Create your views here.

GLOBAL_MSG_QUEUES = {}

def sendMsg(request):
    print(request.POST)
    msgData = request.POST.get('data')
    if msgData:
        msgData = json.loads(msgData)
        msgData['timestamp'] = time.time()
        if msgData['type'] == 'single':
            if not GLOBAL_MSG_QUEUES.get(int(msgData['to'])): #如果没有接收者的queue,创建一个以接收者ID为key 的queue
                GLOBAL_MSG_QUEUES[int(msgData['to'])] = queue.Queue()
            GLOBAL_MSG_QUEUES[int(msgData['to'])].put(msgData)  #将发送的消息塞到接收者的queue里
        else:#group
            groupObj = models.WebGroup.objects.get(id=msgData['to'])
            members = groupObj.members.select_related()
            for member in members:
                if not GLOBAL_MSG_QUEUES.get(member.id):
                    GLOBAL_MSG_QUEUES[member.id]=queue.Queue()
                if member.id != request.user.userprofile.id:
                    GLOBAL_MSG_QUEUES[member.id].put(msgData)
    print(GLOBAL_MSG_QUEUES)
    return HttpResponse('----------msg received------')

def getNewMsgs(request):

    queueId = request.user.userprofile.id
    if queueId not in GLOBAL_MSG_QUEUES:
        print("no queue for user [%s]" %queueId,request.user)
        GLOBAL_MSG_QUEUES[queueId]=queue.Queue()
    qObj = GLOBAL_MSG_QUEUES[queueId]
    msgCount = qObj.qsize()
    msgList = []
    if msgCount > 0:
        for msg in range(msgCount):
            msgList.append(qObj.get())
        print("new msgs:",msgList)
    else:#没有消息，挂起
        print("no new msg for ",queueId,request.user)
        try:
            msgList.append(qObj.get(timeout=60)) #超时60s
        except queue.Empty:
            print("\033[41;1mno msg for [%s][%s] ,timeout\033[0m" %(request.user.userprofile.id,request.user))
    return HttpResponse(json.dumps(msgList))


def fileUpload(request):
    print(request.POST,request.FILES)
    fileObj = request.FILES.get('file')
    #print("----------file upload name:",fileObj.name)
    userHomeDir = "uploads/%s" %request.user.userprofile.id
    if not os.path.isdir(userHomeDir):
        os.mkdir(userHomeDir)
    newFileName = "%s/%s" % (userHomeDir,fileObj.name)
    recvSize = 0
    with open(newFileName, "wb") as newFileObj:
        for chunk in fileObj.chunks():
            newFileObj.write(chunk)
            recvSize += len(chunk)
            cache.set(fileObj.name,recvSize)

        return HttpResponse("---upload success----")

def fileUploadProgress(request):
    filename = request.GET.get('filename')
    #print("----file upload progress filename:", filename)
    progress = cache.get(filename)
    print("%s upload progress: %s" %(filename,progress))
    return HttpResponse(json.dumps({'recvSize':progress}))

def deleteCacheKey(request):
    cacheKey = request.GET.get("cacheKey")
    cache.delete(cacheKey)
    return HttpResponse("cache key %s has been deleted." % cacheKey)



def dashboard(request):


    return render(request, 'webchat/dashboard.html')