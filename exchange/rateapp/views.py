from django.shortcuts import render

def japan(request):
    return render(request,'jpn.html')

def china(request):
    return render(request,'cny.html')

def usa(request):
    return render(request,'usd.html')

def about(request):
    return render(request,'about.html')

def result(request):

    jpnexchange = 0
    cnyexchange = 0
    usdexchange = 0
    ls = [None,]*3


    if request.GET.get('fulltext1') != None:
        ls[0] = request.GET.get('fulltext1')
        jpnexchange = round(int(ls[0])*0.099, 3)
    elif request.GET.get('fulltext2') != None:
        ls[1] = request.GET.get('fulltext2')
        cnyexchange = round(int(ls[1])*0.0059, 3)
    elif request.GET.get('fulltext3') != None:
        ls[2] = request.GET.get('fulltext3')
        usdexchange = round(int(ls[2])*0.00089, 3)
    
    return render(request,'result.html', {'fulltext1': ls[0] ,'fulltext2' : ls[1], 'fulltext3' : ls[2], 
    'jpn' : jpnexchange, 'cny' : cnyexchange, 'usd' : usdexchange})

  