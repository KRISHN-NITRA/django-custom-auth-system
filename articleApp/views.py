from .models import ArticleModel
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ArticleDispay(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        try:
            if id is not None:
                artiadta = ArticleModel.objects.get(id=id)
                serializer = ArticleSerializer(artiadta)
                return Response(serializer.data)

            artiadta = ArticleModel.objects.all()
            serializer = ArticleSerializer(artiadta, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error":f"{pk} id not in database"}, status=status.HTTP_204_NO_CONTENT)

class ArticleInsetUpdate(APIView):
    # def get(self, request, pk=None, format=None):
        # id = pk
        # try:
        #     if id is not None:
        #         artiadta = ArticleModel.objects.get(id=id)
        #         serializer = ArticleSerializer(artiadta)
        #         return Response(serializer.data)
        #
        #     artiadta = ArticleModel.objects.all()
        #     serializer = ArticleSerializer(artiadta, many=True)
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # except:
        #     return Response({"error":f"{pk} id not in database"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None, format=None):
        permission_classes = [IsAuthenticated]
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data inserted"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        permission_classes = [IsAuthenticated]
        id = pk
        try:
            artiadta = ArticleModel.objects.get(id=id)
            serializer = ArticleSerializer(artiadta, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "update successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": f"{pk} id not in database"}, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk=None, format=None):
        permission_classes = [IsAuthenticated]
        try:
            id = pk
            artiadta = ArticleModel.objects.get(id=id)
            serializer = ArticleSerializer(artiadta, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "partial update successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": f"{pk} id not in database"}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk=None, format=None):
        permission_classes = [IsAuthenticated]
        try:
            id = pk
            artiadta = ArticleModel.objects.get(id=id)
            artiadta.delete()
            return Response({"msg": "delete successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": f"{pk} id not in database"}, status=status.HTTP_204_NO_CONTENT)


