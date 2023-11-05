from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.

@api_view(['GET', 'POST'])#must select what HTTP methods the function can support
def books(request):#must use "api_view()" decorator and "Response" from "rest_framework.response", to get the API endpoint lay out
    return Response('list of the books', status=status.HTTP_200_OK)


#BookList Class API view provides methods for listing and filtering and creating books
class BookList(APIView):#must pass APIView as an argument
    def get(self, request): # 2 parameters
        author = request.GET.get('author') # retrieves the value of auther  query parameter from the URL
        if(author): # if author parameter is present
            return Response({"message":"list of the books by " + author}, status.HTTP_200_OK)
            # return response that includes  JSON message with the authors name, the response has a 200_OK status code
   
        return Response({"message":"list of the books"},status.HTTP_200_OK)
    
    #you can add methods with HTTP functionality with out updating the urls.py file(app level)
    def post(self, request): # 2 parameters
        return Response({"title":request.data.get('title')}, status.HTTP_201_CREATED)
        #when POST request is made, creates a JSON response from the request data and sets the status code to 201_CREATED
    

#Book API view can retrieve books with thier primary key and update the title
class Book(APIView):
    def get(self, request, pk): # 3 parameters
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
        #returns JSON response that includes the "pk" "Book ID", sets status code to 200_OK
    
    def put(self, request, pk): # must include "pk" as an argument when defining the function
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
        #when put request is made the code updates the books title with the value of the requested data, sets status code to 200_OK
        #in this case it more or less creates data

    
    # get = read only
    # post = create data
    # put = update data

