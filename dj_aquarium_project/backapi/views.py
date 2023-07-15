
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.mixins import *
from rest_framework import generics, status
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from rest_framework.exceptions import APIException 
from rest_framework.validators import UniqueValidator
from rest_framework.parsers import FileUploadParser

# from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import bad_request
from django.db.models import Prefetch
from django.contrib.auth.tokens import default_token_generator

import datetime
from django.template import Context
from django.template.loader import get_template

# Для загрузки файлов
import mimetypes
import os
import sys
from django.http.response import HttpResponse

# from .forms import *
from django.http import HttpResponseRedirect
import numpy as np

from io import StringIO
import xlsxwriter
from django.http import HttpResponse


sys.path.append('/home/frizik/projects/Aquarium_logistics/neuralnetworks')

from price_predict import *
# reg = joblib.load("/home/frizik/projects/Aquarium_logistics/neuralnetworks/RFECV[DecisionTrees].joblib")


class TicketOrderView(APIView):
    # permission_classes = [IsAuthenticated]
    #API that allows to view single participant by pk
    def get(felf, request):
        
        # pk = Token.objects.get(key = request.META.get('HTTP_AUTHORIZATION').lstrip('Token ')).user_id   
        queryset = TicketOrder.objects.all()
        serializer = TicketOrderSerializer(queryset, many=True)
        # print(serializer.data)
        return Response(serializer.data)



class TicketOrderCreate(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        order = TicketOrderCreateSerializer(data=request.data)
        if order.is_valid(raise_exception=True  ):
            order.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetConfFile(APIView):
    # np_vector = np.array([1, 0, 1, 0, 1, 1591.4, 868.1, 0.0]).reshape(1, -1)
    classes = [['П/3Б ', 'П/3Э ', 'Л/1Э ', 'К/2К ', 'Л/1У ', 'К/2У ', 'Л/1Л ']]
    # print(reg.predict(np_vector))
    def get(self, request):
        data = request.GET
        # номер поезда (0)x, месяц(1)v, станция(0 адлер)v, станция(1 москва)v, класс обслуживания(0)v, кол-во билетов(1)v, цена(v), цена(v), цена(v), расстояние
        if data.get('Class') == 's1':
            theclass = 1
        elif data.get('Class') == 's2':
            theclass = 3
        elif data.get('Class') == 's3':
            theclass = 6
        thedate = int(data.get('date').split('-')[1].strip())
        # print('WJLRBGFAWOURGFIOwabrgfi\n', thedate)
        # номер поезда (0)x, месяц(1)v, станция(0 адлер)v, станция(1 москва)v, класс обслуживания(0)v, кол-во билетов(1)v, цена(v), цена(v), цена(v), расстояние    
        # np_vector = np.array([thedate, 0, 1, theclass, int(data.get('count')), 1591.4, 868.1, 0.0]).reshape(1, -1)
        result = mypredict([thedate, 0, 1, theclass, int(data.get('count')), 1591.4, 868.1, 0.0])
        # print(result)
        # print(int(data.get('date').split('-')[1]))
        # print(data.get('Class'))
        
        return Response(round(float(result)*int(data.get('count')), 2), status=status.HTTP_200_OK)


# class FileUploadView(APIView):
#     parser_classes = (FileUploadParser,)
#     def put(self, request, filename ,format=None):
#         file_obj = request.FILES['file']
#         # do some stuff with uploaded file
#         return Response(status=204)

class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request):
        file = request.data.get('file', None)

        if file is not None:
            return Response(f'File: {file.name} successfully uploaded!', status=HTTP_200_OK)
        else:
            return Response(f'File not found!', status=HTTP_400_BAD_REQUEST)


class GetByMonth(APIView):
    def get(self, request):
        queryset = TicketOrder.objects.filter(departureDate__year='2022')
        dataByMonth = []
        for i in range(1, 12):
            dataByMonth.append(TicketOrderSerializer(queryset.filter(departureDate__month="{:02d}".format(i)), many=True).data)
        print(dataByMonth)
        return Response(dataByMonth)




def download_data(request):
    queryset = TicketOrder.objects.all()
    serializer = TicketOrderSerializer(queryset, many = True)

    # Создание excel файла
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'tables.xlsx'
    filepath = BASE_DIR + '/files/' + filename
    
    size = 'A1:J'+str(len(serializer.data) + 1)
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()
    worksheet.add_table(size, {'autofilter': False, 'columns': 
                                         [{'header': 'Класс'},
                                          {'header': 'Дата отправления'},
                                          {'header': 'Место прибытия'},
                                          {'header': 'Место отправления'},
                                          {'header': 'Расстояние'},
                                          {'header': 'Количество билетов'},
                                          {'header': 'Номер поезда'},
                                          {'header': 'Стоимость билета'},
                                          {'header': 'Стоимость плацкарты'},
                                          {'header': 'Стоимость услуг'},
                                          ]})


    # Настройка размеров отображения таблицы
    cell_format = workbook.add_format()
    cell_format.set_text_wrap()
    worksheet.set_column('A:J', 30)

    # Запись в Excel файл
    row,col = 1,0

    # Добавить сюда код чтобы всё было норм
    for item in serializer.data:
        worksheet.write(row, col, item['serviceClass'],cell_format)
        worksheet.write(row, col + 1, item['departureDate'],cell_format)
        worksheet.write(row, col + 2, item['departureStation'],cell_format)
        worksheet.write(row, col + 3, item['arrivalStation'],cell_format)
        worksheet.write(row, col + 4, item['totalDistance'],cell_format)
        worksheet.write(row, col + 5, item['seatNumber'],cell_format)
        worksheet.write(row, col + 6, item['trainNumber'],cell_format)
        worksheet.write(row, col + 7, item['costTicket'],cell_format)
        worksheet.write(row, col + 8, item['costPlatzcard'],cell_format)
        worksheet.write(row, col + 9, item['costService'],cell_format)
        row += 1
    workbook.close()

    # Отправляем сформированный документ
    if os.path.exists(filepath):
        with open(filepath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'attachment; filename=tickets.xlsx'
            return response

