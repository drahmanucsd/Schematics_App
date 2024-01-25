from rest_framework import generics

from .models import Data
from .serializers import DataSerializer

class DataViewSet(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


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
