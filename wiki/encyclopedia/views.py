import markdown2
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from . import util
from random import randint


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def goto(request,entry):
    page=util.get_entry(entry)
    if(page):
        return render(request,"encyclopedia/entry.html",{
        "content":markdown2.markdown(page),"title":entry
        })
    return render(request,"encyclopedia/error.html",{
        "error_msg":"Page doesnt exist"
    })
def search(request):
    query=request.POST.get("q")
    if(util.get_entry(query)): #if the page is in our enteries
        return HttpResponseRedirect(reverse("main:page",args=[query]))
    else:
        query_list=util.list_entries()
        result=[]
        for q in query_list:
            sub=str(query).lower()
            item=str(q).lower()
            if item.find(sub)!=-1:
                result.append(q)

    return render(request,"encyclopedia/search.html",{
        "result_list":result
        })     
def new_page(request):
    return render(request,"encyclopedia/newpage.html")

def create(request):
    title=request.POST.get("title")
    body=request.POST.get("body")
    if(util.get_entry(title)):
        return render(request,"encyclopedia/error.html",{
            "error_msg":"Page already exists"
        })
    else:
        title=title.capitalize()
        content="# "+title+"\n" +body
        util.save_entry(title,content)
        return HttpResponseRedirect(reverse("main:page",args=[title]))

def redirect(request,title):
    body=util.get_entry(title)  
    return render(request,"encyclopedia/edit.html",{
        "title":title,"body":body
    })
def edit(request):
    title=request.POST.get("title")
    content=request.POST.get("body")
    util.save_entry(title,content)
    return HttpResponseRedirect(reverse("main:page",args=[title]))
def random_page(request):
    entries=util.list_entries()
    num=randint(0,len(entries)-1) 
    title=entries[num]
    return HttpResponseRedirect(reverse("main:page",args=[title]))

    

    
    

