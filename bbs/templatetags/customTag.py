
from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def truncateUrl(imgObj):
    imgUrl = imgObj.name.split("/",maxsplit=1)[-1]
    #print(imgUrl)
    return imgUrl

@register.simple_tag
def commentsThumps(articleObj):
    queryset = articleObj.comment_set.select_related()
    commentsDic = {
        'commentsCount':queryset.filter(comment_type=1).count(),
        'thumpsCount':queryset.filter(comment_type=2).count()

    }
    return commentsDic