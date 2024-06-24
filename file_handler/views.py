from django.conf import settings
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import csv
import os
from math import ceil  # Correct import statement for ceil function
import subprocess

PAGE_SIZE = 500

def get_csrf_token_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

class FileUploadView(View):
    def post(self, request):
        uploaded_file = request.FILES['file']
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        file_path = os.path.join(upload_dir, uploaded_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return JsonResponse({'message': 'Dosya başariyla yuklendi'}, status=200)




import os
from django.conf import settings
from django.http import JsonResponse
from math import ceil
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt

PAGE_SIZE = 500  # Her sayfada döndürülecek veri sayısı
UPLOADS_DIR = os.path.join(settings.MEDIA_ROOT, 'uploads')
CSV_FILE = os.path.join(UPLOADS_DIR, 'data2.csv')

def get_total_pages():
    with open(CSV_FILE, newline='') as csvfile:
        total_records = sum(1 for line in csvfile)
    total_pages = ceil(total_records / PAGE_SIZE)
    return total_pages

@csrf_exempt
def get_data_top10(request):
    global CSV_FILE
    page = int(request.GET.get('page', 1))
    total_pages = get_total_pages()

    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE

    data = []
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if start_index <= i < end_index and row['filter_2182'] == 'true':
                data.append(row)

    response_data = {
        'total_pages': total_pages,
        'data': data[:10]
    }

    pprint(data[:5])  # İlk 5 veriyi yazdır
    return JsonResponse(response_data)

@csrf_exempt
def get_data(request):
    global CSV_FILE
    page = int(request.GET.get('page', 1))
    total_pages = get_total_pages()

    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE

    data = []
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if start_index <= i < end_index:
                data.append(row)

    response_data = {
        'total_pages': total_pages,
        'data': data
    }

    pprint(data[:5])  # İlk 5 veriyi yazdır
    return JsonResponse(response_data)

@csrf_exempt
def get_data_two(request):
    global CSV_FILE
    page = int(request.GET.get('page', 1))
    total_pages = get_total_pages()

    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE

    data = []
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if start_index <= i < end_index and row['filter_2182'] == 'true':
                data.append(row)

    response_data = {
        'total_pages': total_pages,
        'data': data
    }

    pprint(data[:5])  # İlk 5 veriyi yazdır
    return JsonResponse(response_data)

@csrf_exempt
def get_data_three(request):
    global CSV_FILE
    page = int(request.GET.get('page', 1))
    total_pages = get_total_pages()

    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE

    data = []
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if start_index <= i < end_index and row['filter_2182'] == 'false':
                data.append(row)

    response_data = {
        'total_pages': total_pages,
        'data': data
    }

    pprint(data[:5])  # İlk 5 veriyi yazdır
    return JsonResponse(response_data)

@csrf_exempt
def get_labels(request):
    global CSV_FILE
    labels = []
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            labels.extend(row['Label'].split(','))
    unique_labels = list(set(labels))  # Tekrarlayan etiketleri kaldır
    return JsonResponse({"labels": unique_labels})

@csrf_exempt
def list_files(request):
    files = os.listdir(os.path.join(settings.BASE_DIR, 'uploads'))
    return JsonResponse({"files": files})

@csrf_exempt
def select_file(request):
    global CSV_FILE
    selected_file = request.POST.get('filename')
    CSV_FILE = os.path.join('uploads', selected_file)
    return JsonResponse({"message": f"File selected: {selected_file}"})
