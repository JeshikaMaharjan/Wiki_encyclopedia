from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import random 


from . import util
import markdown2


def index(request):    
    return render(request, "encyclopedia/wiki.html", {
        "entries": util.list_entries()
    })

def show(request, name):
    entry = util.get_entry(name)
    if entry != None:
        page = markdown2.markdown(entry) #conversion of md file to html using markdown2 library.
        return render(request,"encyclopedia/show.html", {
            "entries": page, "title" : name
        })
    else:
        return render(request,"encyclopedia/error.html")

def search(request):
        search_item = str(request.GET['q']) #request.GET is the dictionary of the 'GET' variables in the http request made to server 
        entry = util.get_entry(search_item)
        if entry != None:
            page = markdown2.markdown(entry) #conversion of md file to html using markdown2 library.
            return render(request,"encyclopedia/show.html", {
                "entries": page, "title" : search_item
            })
        else:
            entries = util.list_entries()
            substring = []            
            for entry in entries:
                if int(entry.casefold().find(search_item.casefold())) != -1: #casefold removes all case distinctions in strings.(and makes entry case insensitive)
                    substring.append(entry)
                    check = True
                    break
                else:
                    check = False
            if check == True:
                return render(request,"encyclopedia/search.html", {
                            "entries": substring , "title" : search_item
                        })    
            else:
                return render(request,"encyclopedia/error.html")

def newentry(request):
    if request.method == "POST":
        entry = util.get_entry(request.POST['title'])
        if entry == None:
            util.save_entry(request.POST['title'], request.POST['content'])
            return HttpResponseRedirect(reverse("index"), {
                "entries": util.list_entries()
            }) 
        else:
            return HttpResponse("Entry already exists.") 
    return render(request, "encyclopedia/newentry.html")


def editentry(request,name):
    content = util.get_entry(name)      
    if request.method == "POST":
        util.save_entry(request.POST['title'],request.POST['content'])
        page = markdown2.markdown(request.POST['content']) #conversion of md file to html using markdown2 library.
        return render(request,"encyclopedia/show.html", {
            "entries": page, "title" : request.POST['title']
        })

    
    return render(request,"encyclopedia/editentry.html", {
                    "title" : name, "entries" : content
                }) 
  

def randome(request):
    entry = random.choice(util.list_entries())
    page = markdown2.markdown(util.get_entry(entry)) 
    return render(request,"encyclopedia/show.html", {
        "entries": page, "title" : entry
    })



   
    
    