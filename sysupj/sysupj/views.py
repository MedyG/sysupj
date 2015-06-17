#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from sysupj.models import Student,Course,Teacher,Discussion,Followings,Material,Rating,Teachings

import sysupj.models
def home(request):
    return render_to_response("Home.html")

def comment_submit(request):
    html = """
	        <html>
            <head>
            <title>Comment</title>
            </head>
            <body>
            <form action="/comments/" method="post">
                <input type="text" name="q"/>
                <input type="submit" value="Comment"/>
            </form>
            </body>
            </html>"""
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))