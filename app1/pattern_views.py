from django.shortcuts import render
import random # 加入 random 套件

def dice(request):
    no=random.randint(1,6)  # 1~6
    return render(request,"dice.html",{"no":no})

def dice2(request):
    no1=random.randint(1,6)  # 1~6
    no2=random.randint(1,6)  # 1~6
    no3=random.randint(1,6)  # 1~6
    # 使用 locals() 傳遞所有的區域變數
    return render(request,"dice2.html",locals())

# 寫在 app1/pattern_views.py 的最下面

times=0
def dice3(request):
    global times       # 宣告 global 變數
    times = times + 1
    local_times=times  # 指派給 區域變數 local_times
    username="David"
    dict_no={"no":random.randint(1,6)}  # 1~6
    return render(request,"dice3.html",locals())


#def dice3(request):
    # 臨時測試用，之後可以改寫你的邏輯
    #return render(request, "dice2.html", locals())

#def show(request):
    #from django.http import HttpResponse
    #return HttpResponse("Show 測試畫面")

def show(request):
    person1={"name":"Amy", "phone":"049-1234567", "age":20}
    person2={"name":"Jack", "phone":"02-4455666", "age":25}
    person3={"name":"Nacy", "phone":"04-9876543", "age":17}
    persons=[person1, person2, person3]
    #persons.reverse()
    return render(request, "show.html", locals())

#def filter(request):
    #from django.http import HttpResponse
    #return HttpResponse("Filter 測試畫面")
    
def filter(request):
    value=4
    list1=[1,2,3]
    pw="芝麻開門"
    
    html="<h1>Hello</h1>"
    value2=False
    return render(request,"filter.html",locals())
