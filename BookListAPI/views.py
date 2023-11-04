from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.

@api_view(['GET', 'POST'])#must select what HTTP methods the function can support
def books(request):
    #must use "api_view()" decorator and "Response" from "rest_framework.response"
    #to get the API endpoint lay out
    return Response('list of the books', status=status.HTTP_200_OK)

class Orders():
    @staticmethod #this  is required to define the function as something that belongs to the class, and not any instace of the class
    @api_view(['GET'])#must select what HTTP methods the function can support
    def listOrders(request): #define the function
        return Response({'message':'list of orders'}, 200)
        #^^ returns DRF respsonse, which is the key vaue pair, plus the http request


# class BookView(APIView):
#     def get(self, request, pk):
#         return Response({"message":"single book with id" + str(pk)}, status.HTTP_200_OK)
#     def put(self, request, pk):
#         return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
    
class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({"message":"All books"}, status.HTTP_200_OK)
    def create(self, request):
        return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
    