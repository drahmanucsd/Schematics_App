from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from search_app.serializers import SearchSerializer
from search_app.serializers import DataSerializer
from search_app.models import Data

def filtersearch(search_data):
    drawing_number = search_data.get('drawing_number')
    descr = search_data.get('descr')

    # Define your filter conditions based on the fields in search_data
    filter_conditions = Q()
    if drawing_number:
        filter_conditions &= Q(drawing_number=drawing_number)
    if descr:
        filter_conditions &= Q(descr=descr)

    return Data.objects.filter(filter_conditions)


@csrf_exempt
def searchApi(request,id=0):
    if request.method=='GET':
        search_data=JSONParser().parse(request)
        search_serializer=SearchSerializer(data=search_data)
        search_results = filtersearch(search_data)
        search_serializer=DataSerializer(search_results,many=True)
        return JsonResponse(search_serializer.data,safe=False)
    elif request.method=='POST':
        return JsonResponse({'error': 'POST method is not supported for this endpoint'}, status=405)
    elif request.method=='PUT':
        return JsonResponse({'error': 'PUT method is not supported for this endpoint'}, status=405)
    elif request.method=='DELETE': 
        return JsonResponse({'error': 'DEL method is not supported for this endpoint'}, status=405)   
    # elif request.method=='EDIT':
    #     search_data=JSONParser().parse(request)
    #     search_serializer=StudentSerializer(data=search_data)
    #     if search_serializer.is_valid():
    #         search_serializer.save()
    #         return JsonResponse("Added Successfully",safe=False)
    #     return JsonResponse("Failed to Add",safe=False)
