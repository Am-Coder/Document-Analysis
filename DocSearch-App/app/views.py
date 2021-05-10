from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .recommend_utils.PredictPaper import PredictPaper, Graph, DataHandler
from .recommend_utils.KeywordExtractor import KeywordExtractor
import mimetypes

DATA_PATH = "Data.xlsx"
GRAPH_PATH = "output2k"


# Create your views here.
def index(request):
    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    context = {
        'papers': ['paper1', 'paper2'],
    }
    return render(request, 'Research.html', context)


def recommend_keywords(request):
    inp = request.POST.get('keyword_list')
    input_list = inp.split(';')
    final_list = [s.strip() for s in input_list]
    print(final_list)
    predPap = PredictPaper(DATA_PATH, GRAPH_PATH)
    commonWords = 3
    result = predPap.predict(final_list, commonWords)
    context = {
        'papers': result,
    }
    return render(request, 'Research.html', context)


def recommend_abstract(request):
    inp = request.POST.get('abstract')
    abstract = inp.strip()
    # print(abstract)
    key_extractor = KeywordExtractor()
    ext_list = key_extractor.rakealgo(abstract)
    final_list = []
    for key in ext_list:
        for word in key:
            remove_special_chars = word.translate({ord(c): " " for c in "”!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
            word = remove_special_chars.strip()
            final_list.append(word.strip())
    print(final_list)
    predPap = PredictPaper(DATA_PATH, GRAPH_PATH)
    commonWords = 3
    result = predPap.predict(final_list, commonWords)
    context = {
        'papers': result,
    }
    return render(request, 'Research.html', context)


def download_file(request, filepath):
    # fill these variables with real values
    print(filepath)
    fl_path = '/file/path'
    filename = 'downloaded_file_name.extension'
    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
