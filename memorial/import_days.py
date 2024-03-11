import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memorial.settings')
django.setup()

import csv
from alldays.models import Year23 

def import_days(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Year23.objects.create(
                filename=row['filename'],
                author=row['author'],
                description=row['description'],
                inst=row['inst']
            )

if __name__ == '__main__':
    csv_file_path = '/Users/masha/Desktop/CODE/chislennichek memorial/memorial-git/memorial/Year23sheet.csv'
    import_days(csv_file_path)