
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.pagination import LimitOffsetPagination
from stackapi import StackAPI
from datetime import datetime

from stack_app.models import *
from stack_app.serializers import *
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


import requests
SITE = StackAPI('stackoverflow')
class StackQuestionsAPI(APIView, LimitOffsetPagination):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request, format=None):
        # Questions.objects.all().delete()
        query_params = request.query_params
        order = query_params.get("order","")
        sort = query_params.get("sort","")
        page = query_params.get("page","")
        pagesize = query_params.get("pagesize","")
        tagged = query_params.get("tagged","")
        fromdate = query_params.get("fromdate","")
        todate = query_params.get("todate","")
       
        questions_list = []
        try:
            if order != '' or sort != '' or page != '' or pagesize != '' or tagged != '' or fromdate != '' or todate != '':
                # a = datetime.now()
                print(" == CALLED ++++ ")
                try:
                    dates=datetime.strptime(fromdate, "%Y-%m-%d")
                    fromdate = int(dates.strftime('%Y%m%d'))
                except:
                    pass
                try:
                    dates2=datetime.strptime(todate, "%Y-%m-%d")
                    todate = int(dates2.strftime('%Y%m%d'))
                except:
                    pass
            
        
                url = 'https://api.stackexchange.com/2.3/questions?order={}&sort={}&page={}&pagesize={}&fromdate={}&todate={}&tagged={}&site=stackoverflow'.format(order,sort,page,pagesize,fromdate,todate,tagged)
                stack_question = {}
                r = requests.get(url)
                data = r.json()
                    
                for que in data['items']:
                
                    question_created, _ = Questions.objects.get_or_create(
                        question=que['title']
                    )
                    question_created.view_count = que['view_count']
                    question_created.answer_count = que['answer_count']
                    question_created.score = que['score']
                    question_created.save()
                
            question_list = Questions.objects.all()
            print("question_list = Questions.objects.all() ==",question_list.count())
            page = request.GET.get('page', 1)

            paginator = Paginator(question_list, 5)
            try:
                questions = paginator.page(page)
            except PageNotAnInteger:
                questions = paginator.page(1)
            except EmptyPage:
                questions = paginator.page(paginator.num_pages)

            results = self.paginate_queryset(question_list, request, view=self)
            serializer = QuestionsSerializer(results, many=True)
            
            return Response({'stack_question':questions},status=200)
        except Exception as e:
            print(e)
            return Response({'error':'Same issue when calling api'},status=500)
            

        # pass

    def post(self, request, format=None):
        pass