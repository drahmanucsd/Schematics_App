from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from search_app.serializers import SearchSerializer
from search_app.models import Data

def filtersearch(search_data):
    drawing_number = search_data.get('drawing_number')
    descr = search_data.get('descr')
    # Define your filter conditions based on the fields in search_data
    qq = Data.objects.all()
    if drawing_number:
        print(drawing_number)
        qq = qq.filter(drawing_number=drawing_number)
    return qq[:20]


@csrf_exempt
def searchApi(request,id=0):
    if request.method=='GET':
        return JsonResponse({'error': 'POST method is not supported for this endpoint'}, status=405)
    elif request.method=='POST':
        search_data=JSONParser().parse(request)
        search_serializer=SearchSerializer(data=search_data)
        search_results = filtersearch(search_data)
        search_serializer=SearchSerializer(search_results,many=True)
        return JsonResponse(search_serializer.data,safe=False)

    elif request.method=='PUT':
        return JsonResponse({'error': 'PUT method is not supported for this endpoint'}, status=405)
    elif request.method=='DELETE': 
        return JsonResponse({'error': 'DEL method is not supported for this endpoint'}, status=405)   

