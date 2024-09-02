from rest_framework.response import Response 
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.db.models import Q
from django.shortcuts import render
import datetime

from Data.models import EnergieTerug
from .serializers import ItemSerializer

#@api_view(['GET'])
#def getData(request):
#    items = EnergieTerug.objects.all()
#    serializer = ItemSerializer(items, many=True)
#    return Response(serializer.data)

#@api_view(['GET'])
#def getData(request):
    # Get query parameters (using get() to avoid KeyErrors)
    #maand = request.GET.get('maand')
    #jaar = request.GET.get('jaar')

    # Define filter conditions based on parameters
    #filters = Q()
    #if maand:
        #filters &= Q(Maand=maand)
    #if jaar:
        #filters &= Q(Jaartal=jaar)

    # Retrieve data based on filters (or all data if no filters)
    #items = EnergieTerug.objects.filter(filters) if filters else EnergieTerug.objects.all()

    # Optional serialization if you're using a serializer class
    #if 'application/json' in request.content_type:
        #serializer = ItemSerializer(items, many=True)
        #return Response(serializer.data)

    # Return non-serialized data by default (adjust as needed)
    #return Response(items.values())  # Return dictionary of values



def chartDemo(request):
    maand = request.GET.get('maand')
    jaar = request.GET.get('jaar')
    interval = request.GET.get('interval')

    # Define filter conditions based on parameters

    totaal = {}
    if interval != 'dag':
        for card in list(EnergieTerug.objects.all().values()):
            indexName = f'{str(card["Maand"])}_{str(card["Jaartal"])}'
            if indexName in totaal:
                totaal[indexName] += int(card["Waarde"])
            else:
                totaal[indexName] = int(card["Waarde"])
        
    filters = Q()
    if maand:
            filters &= Q(Maand=maand)
    if jaar:
            filters &= Q(Jaartal=jaar)
    
    if jaar == None: 
        filters &= Q(Jaartal=datetime.date.today().year)

    if maand == None: 
        filters &= Q(Jaartal=datetime.date.today().month)


    maandentallen = {
        '1': "jan",
        '3': "mrt",
        '4': "apr",
        '5': "mei",
        '2': "feb",
        '6': "jun",
        '7': "jul",
        '8': "aug",
        '9': "sep",
        '10': "okt",
        '11': "nov",
        '12': "dec",
    }

    if totaal != {}:
        newtotaal = {}

        for i, v in totaal.items():
            datesplit = i.split('_')  # Extract month part from the key (index)
            if datesplit[0] in maandentallen:
                newtotaal[f"{maandentallen[datesplit[0]]} '{datesplit[1][-2:]}"] = v
        
        totaal = newtotaal

    # Retrieve data based on filters (or all data if no filters)
    dataLabel = []
    dataValue = []

        
    if interval == "dag":
        query = EnergieTerug.objects.filter(filters) if filters else EnergieTerug.objects.all()
        mylist = list(query.values())

        for card in mylist:
            dataLabel.append(card["Tijdstip"]) 
            dataValue.append(card["Waarde"])
    else:
        for i, v in totaal.items():
            dataLabel.append(i)
            dataValue.append(v)
    
    context = {
        'dataLabel': dataLabel,
        'dataValue': dataValue,
    } 
    
    return render(request, 'chart.html', context)

    