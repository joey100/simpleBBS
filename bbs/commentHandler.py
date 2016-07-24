




def addNode(treeDic,comment):
    if comment.parent_comment is None:
        treeDic[comment]={}
    else:
        for k,v in treeDic.items():
            if k == comment.parent_comment:
                treeDic[comment.parent_comment][comment]={}
            else:
                addNode(v,comment)




def buildTree(commentObj):
    treeDic = {}
    for comment in commentObj:
        addNode(treeDic,comment)
    for k,v in treeDic.items():
        print(k,v)
    return treeDic




def renderCommentNode(treeDic,margin):
    html = ''
    for k,v in treeDic.items():
        ele = "<div class='comment-node' style='margin-left:%spx'>" % margin + k.comment  + "<span style='margin-left:20px'>%s </span>"%k.date \
              + "<span style='margin-left:20px'>%s</span>" %k.user.name \
              + '<span comment-id="%s" '%k.id + 'style="margin-left:20px" class="glyphicon glyphicon-comment add-comment" aria-hidden="true"></span>'\
              +"</div>"
        html += ele
        html += renderCommentNode(v,margin+20)
    return html

def renderCommentTree(treeDic):
    html = ''
    for k,v in treeDic.items():
        ele = "<div class='root-comment'>" + k.comment + "<span style='margin-left:20px'>%s </span>"%k.date \
              + "<span style='margin-left:20px'>%s</span>" %k.user.name \
              + '<span comment-id="%s"' %k.id + ' style="margin-left:20px" class="glyphicon glyphicon-comment add-comment" aria-hidden="true"></span>'\
              + "</div>"
        html += ele
        html += renderCommentNode(v,10)
    return html
    pass



