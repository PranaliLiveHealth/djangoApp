from django.shortcuts import render_to_response, render
from renderJSONResponse import JSONResponse

def index(request):
    try:
        return render(request,'viewPage.html')
    except :
        return JSONResponse({'code':500})
