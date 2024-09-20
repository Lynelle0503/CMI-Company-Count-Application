from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from tablib import Dataset
from .models import CompanyData
from .resources import CompanyDataResource
from django.contrib import messages
from django.http import HttpResponse
import csv, io

# Create your views here.

def uploadFile(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            ca_res = CompanyDataResource
            csv_file = request.FILES['csv_file']
            dataset = Dataset()
            
            if not csv_file.name.endswith('csv'):
                messages.info(request, 'Please upload a CSV file only')
                form = CSVUploadForm()
                return render(request, 'uploadPage.html', {'form': form})
            else:
                messages.info(request, 'Uploading File...')
            imported_data = dataset.load(csv_file.read().decode('utf-8'), format='csv')
            #dataset = csv_file.read().decode('utf-8')
            #io_string = io.StringIO(dataset)
            #next(io_string)
            #for c in csv.reader(io_string, delimiter=',', quotechar="|" ):
            for data in imported_data.dict:
                '''
                ['5872184', 'ibm', 'ibm.com', '1911.0', 'information technology and services', 
                '10001+', '"new york', ' new york', ' united states"', 'united states', 
                'linkedin.com/company/ibm', '274047', '716906']
                
                	name	domain	year founded	industry	size range	locality	
                 country	linkedin url	current employee estimate	total employee estimate
                '''
                CompanyData.objects.update_or_create(
                    name = data['name'],
                    domain = data['domain'],
                    founded_year = data['year founded'][:-2],
                    industry = data['industry'],
                    size_range = data['size range'][:-1],
                    locality = data['locality'],
                    country = data['country'],
                    linkedin_url = data['linkedin url'],
                    curr_emp_estimate =  data['current employee estimate'],
                    total_emp_estimate =  data['total employee estimate'],
                )
            messages.info(request, 'File is done uploading!')
            
            return render(request, "uploadPage.html", {'form': form})
        
    else:
        form = CSVUploadForm()
    return render(request, "uploadPage.html", {'form': form})

    

def qbPage(request):
    return render(request, "QBuildPage.html")
    