from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from Data.forms import CSVForm
from Data.models import EnergieTerug
import csv
import io

# Create your views here.

@user_passes_test(lambda u: u.is_staff)
def UploadCSV(request):
    if request.method == "POST":
        form = CSVForm(request.POST, request.FILES)

        if form.is_valid():
            if not request.user.is_staff:
                return HttpResponse("Error: Page restricted to admins only.")

            #form.save() # Disabled, in principe niet nodig, alles kan in het geheugen worden uitgelezen

            #Reading the CSV file
            OutputFile = request.FILES["CSVBestand"]
            if OutputFile.name.endswith(".csv"):
                with OutputFile.open('r') as file:
                    text_file = io.TextIOWrapper(file, encoding='utf-8')
                    csvReader = csv.DictReader(text_file, delimiter=',')
    
                    next(csvReader)
                    for i, row in enumerate(csvReader):
                        extractedTijdstip = row['Tijdstip']
                        extractedWaarde = row['Waarde']
                        if extractedTijdstip is not None and extractedWaarde is not None:
                            if EnergieTerug.objects.filter(Tijdstip=extractedTijdstip).exists() == False:
                                saveNewData, created = EnergieTerug.objects.get_or_create(
                                    Tijdstip = str(extractedTijdstip),
                                    Waarde = extractedWaarde,
                                    Maand = str(extractedTijdstip).split('-')[1],
                                    Jaartal = str(extractedTijdstip).split('-')[0],
                                )

                    file.close()     
                    
                    return render(request, 'success.html')
                    
            
        else: #Form isn't valid
            context = {'form': form}
            return render(request, 'upload.html', context)

    context = {'form': CSVForm()}
    return render(request, 'upload.html', context)