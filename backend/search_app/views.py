from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from search_app.serializers import SearchSerializer
from search_app.models import Data

def filtersearch(search_data):
    drawing_number = search_data.get('drawing_number')
    descr = search_data.get('descr')
    date_drawn = search_data.get('date_drawn')
    operator_type = search_data.get('operator_type')
    ght = search_data.get('ght')
    latching_feature = search_data.get('latching_feature')
    # Define your filter conditions based on the fields in search_data
    qq = Data.objects.all()
    if drawing_number:
        qq = qq.filter(drawing_number__icontains=drawing_number)
    if operator_type:
        qq = qq.filter(operator_type__icontains=operator_type)
    if descr:
        print(descr)
        qq = qq.filter(descr__icontains =descr)
    if date_drawn:
        qq = qq.filter(date_drawn=date_drawn[2:10])
    if ght:
        if latching_feature:
            qq = qq.filter(aa="Y")
        qq = qq.filter(e_d='Y')
    return qq[:100],len(qq)


@csrf_exempt
def searchApi(request,id=0):
    if request.method=='GET':
        return JsonResponse({'error': 'POST method is not supported for this endpoint'}, status=405)
    elif request.method=='POST':
        search_data=JSONParser().parse(request)
        search_serializer=SearchSerializer(data=search_data)
        search_results = filtersearch(search_data)
        search_serializer=SearchSerializer(search_results[0],many=True)
        data_to_send = {
            'search_results': search_serializer.data,
            'total_results':search_results[1]
        }
        return JsonResponse(data_to_send,safe=False)

    elif request.method=='PUT':
        return JsonResponse({'error': 'PUT method is not supported for this endpoint'}, status=405)
    elif request.method=='DELETE': 
        return JsonResponse({'error': 'DEL method is not supported for this endpoint'}, status=405)   

