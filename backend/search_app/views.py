from rest_framework import generics, viewsets

from .models import Data
from .serializers import DataSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

def search(request):
    # Extract multiple query parameters
    field1_value = request.GET.get('field1')
    field2_value = request.GET.get('field2')
    # Perform search logic using the parameters, for example:
    results = YourModel.objects.filter(field1__icontains=field1_value, field2__icontains=field2_value)
    # Serialize the results if necessary
    serialized_results = [{'id': obj.id, 'name': obj.name} for obj in results]
    return JsonResponse(serialized_results, safe=False)



# from rest_framework import generics
# from .models import Data
# from .serializers import DataSerializer

# class DataListView(generics.ListAPIView):
#     serializer_class = DataSerializer

#     def get_queryset(self):
#         queryset = Data.objects.all()
#         search_term = self.request.query_params.get('search', None)

#         if search_term:
#             queryset = queryset.filter(
#                 Q(descr__icontains=search_term) | Q(drawn_by__icontains=search_term)
#             )

#         return queryset
