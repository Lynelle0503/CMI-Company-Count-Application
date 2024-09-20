from celery import shared_task
import csv
from .models import CSVFile, CompanyData
#celery task
@shared_task
def process_csv_file(csv_file_id):
    try:
        csv_file = CSVFile.objects.get(id=csv_file_id)
    
        with open(csv_file.file.path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                CompanyData.objects.create(
                    name=row['name'],
                    domain=row['domain'],
                    founded_year=row['year founded'],
                    industry=row['industry']
            )
    except Exception as e:
        # You can add logging here for better debugging
        print(f"Error processing CSV file: {e}")