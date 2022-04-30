import datetime

from django.shortcuts import render

from blog.models import Blog,Category


def Index(req):
    return render(req,'index.html',
                  {
                   "blogs":Blog.objects.all(),
                   "sehirler":["diyarbakır","istanbul","ankara","izmir"],
                    "date": datetime.datetime.now()
                   })

