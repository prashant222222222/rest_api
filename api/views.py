# # from django.shortcuts import render
# # from django.shortcuts import HttpResponse
# # # Create your views here.
# # import json
#
# from api import models
# from rest_framework.decorators import api_view
# # converts any request coming to the function as json api request
#
# # after applying the decorator @api_view the request which is form http gets concerted to the below request
# # from rest_framework.request import Request
# from rest_framework.response import Response
# from api import serializers
#
# import json
#
#
# class Student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks
#
#
# # @api_view()
# # def usersApi(request):
# #     # also can be fetched from db
# #     # users = [
# #     #     {
# #     #         "name": "prashant",
# #     #         "language": "python"
# #     #     },
# #     #     {
# #     #         "name": "pratik",
# #     #         "language": "c++"
# #     #     }
# #     # ]
# #
# #     # return Response(json.dumps(users))
# #     return Response(users)
# #     # dumps will take any python object and willtry to serialize into json string
#
# @api_view()
# def usersApi(request):
#     student1 = Student("prahsnbt", 34, 3)
#     student2 = Student("prahst", 34, 3)
#     student3 = Student("pranbt", 34, 3)
#     student4 = Student("hsnbt", 34, 3)
#     response = serializers.StudentSerializer([student1,
#                                               student2,
#                                               student3,
#                                               student4], many=True)
#     return Response(response.data)
#     # return Response(student)  # Object of type Student is not JSON serializable
#     # serializers are the functions which convert python object to json object that can be transported through the network
#
#
# @api_view()
# def articleApi(request):
#     articles = models.Article.objects.all()
#     response = serializers.ArticleSerializer(articles, many=True)
#     return Response(response.data)
#
#
# # 5 -> the user will thy to send backend data to the server and the backend server will try to create the article
# # frontend application will send the request with POST  raw body containg json
# @api_view(['POST'])
# def createArticleApi(request):
#     body = json.loads(request.body)
#     # print(body)
#     response = serializers.ArticleSerializer(data=body)
#     if response.is_valid():
#         inst = response.save()  # we can save to database
#         # print(inst)
#         response = serializers.ArticleSerializer(inst)
#         return Response(response.data)
#     # return Response({"message": "hello"})
#     return Response(response.errors)

# class based view

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView)

from api import serializers, models


# class ArticleListView(ListAPIView):
#     # which queryset to look into to retrieve data
#     queryset = models.Article.objects.all()
#     serializer_class = serializers.ArticleSerializer

# get detail of a single article  similar to detailview


class ArticleDetailView(RetrieveUpdateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    # RetrieveAPIView does not override  post mathod in base api view
    # so use RetrieveUpdateAPIView helps in both get and post and updation
    # for updation in postman send patch request

    def post(self, request, pk):
        return Response(request. body)


class ArticleListView(ListCreateAPIView):
    # used for both get and post (to retrieve and  create article)
    #queryset = models.Article.objects.all()

    serializer_class = serializers.ArticleSerializer

    # how to update queryset
    def get_queryset(self):
        query = {}
        # http://127.0.0.1:8000/api/articles1/?title=python mania
        for key, value in self.request.GET.items():
            query["{}__icontains".format(key)] = value
        return models.Article.objects.filter(**query)
