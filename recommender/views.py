from rest_framework import generics, serializers, views, status
from rest_framework.response import Response

from .serializers import RecommenderSerializer
from .recommender import getRecommendations


class RecommenderAPIView(generics.GenericAPIView):
    serializer_class = RecommenderSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            link = serializer.data.get('link')
            product_count = serializer.data.get('product_count')

            indices, distances, recommendations = getRecommendations(link, product_count)

            return Response({'link': link, 'product_count': product_count, 'recommendations': recommendations, 'indices': indices, 'distances': distances}, status=status.HTTP_200_OK)
        return Response({'Bad Request': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
