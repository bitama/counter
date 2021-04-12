from django.shortcuts import render,redirect,HttpResponse



def count(request):
    if "counter" not in request.session:
        request.session["counter"] =0
    request.session["counter"] =+1
    return render(request,"counter.html")


def delete_session(request):
    del request.session["counter"]
    return redirect("/")

def add_2(request):
    request.session["counter"] += 1
    return redirect("/")

