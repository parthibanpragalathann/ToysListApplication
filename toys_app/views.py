from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from toys_app.serializers import ToysSerializer
from toys_app.models import ToysList


# class TOYS details view here ToysSerializer
class CreateViewToys(APIView):
    serializer_class = ToysSerializer

    def get(self, request, *args, **kwargs):
        toys_info = ToysList.objects.order_by('name')
        serializer = ToysSerializer(toys_info, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ToysSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModifyViewToys(APIView):
    serializer_class = ToysSerializer

    def get_object(self, pk):
        try:
            return ToysList.objects.get(pk=pk)
        except ToysList.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        detail = self.get_object(pk)
        serializer = ToysSerializer(detail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        toys = self.get_object(pk)
        serializer = ToysSerializer(toys, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        toys_delete = self.get_object(pk)
        toys_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ToyView(APIView):
    def get(self, request, pk, format=None):
        try:
            detail = ToysList.objects.filter(id=pk).values('name','description', 'toy_category')
            return Response(detail)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
