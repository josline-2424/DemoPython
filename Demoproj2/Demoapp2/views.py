from django.shortcuts import render

# Create your views here.
def operationhandling(request):
    return render(request, "operationhandling.html")

def add(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
#    a = int(request.GET['num3'])
#    b = int(request.GET['num4'])
#    c = int(request.GET['num5'])
#    d = int(request.GET['num6'])
#    e = int(request.GET['num7'])
#    f = int(request.GET['num8'])
    resadd = x + y
    ressub = x - y
    resmul = x * y
    if y==0:
        resdiv = 'Zero Error'
    else:
        resdiv = x / y
        #{'resadd':resadd, 'ressub':ressub, 'resmul':resmul, 'resdiv':resdiv}
    return render(request, "add.html", {'resadd':resadd, 'ressub':ressub, 'resmul':resmul, 'resdiv':resdiv})

   #def sub(request):
#    x = int(request.GET['num3'])
#    y = int(request.GET['num4'])
#    res = x - y
##    return render(request, "sub.html")
#def mul(request):
 #   x = int(request.GET['num5'])
 #   y = int(request.GET['num6'])
 #   res = x - y
 #   return render(request, "mul.html", {'result': res})
#def div(request):
#    x = int(request.GET['num7'])
#    y = int(request.GET['num8'])
#    res = x / y
#    return render(request, "div.html", {'result': res})