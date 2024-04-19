from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def home(request):
    return render(request,'home.html')


def word(request):
    search = request.GET.get('search') 
    dictionary=PyDictionary() 
    meaning=dictionary.meaning(search) 
    synonyms=dictionary.synonym(search) 
    antonyms=dictionary.antonym(search)
    context = {
        'meaning': meaning['Noun'][0],
        'synonym': synonyms,
        'antonym': antonyms,
    }

    return render(request,'word.html',context)