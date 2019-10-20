
import json
from renderJSONResponse import JSONResponse

def getAPI(request):
    data=[]
    try:
        with open('data.json', 'r+') as json_file:
            data = json.load(json_file)
        return JSONResponse({'code': 200, 'file_data':data})
    except:
        return JSONResponse({'code': 500})
