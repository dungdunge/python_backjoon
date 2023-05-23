from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# from rembg import remove
# Create your views here.
def upload(request):
    
    up_image = request.GET.get('up_image')
    return render(request, 'image.html')

#test

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        return HttpResponse('Upload Success!')
    return render(request, 'image.html')




# def nukki(request):
#     input_path = request.GET.get('up_image')
#     output_path = 'output_' + input_path # output 경로를 지정할 때도 파일 확장자를 포함하여 정확하게 지정해야 합니다.

#     with open(input_path,'rb')as i:
#         with open(output_path,'wb')as o:  # 파일 포인터 변수의 이름도 정확하게 지정해야 합니다.
#             input_data = i.read()
#             output_data = remove(input_data)
#             o.write(output_data)

#     return FileResponse(open(output_path,"rb"))
