from django.shortcuts import render
import os
from google.cloud import language_v1

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')


def nlp_analysis(text):
    # Hizmet hesabı anahtarınızın yolunu belirtin
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account-file.json"

    # Natural Language API istemcisini oluşturun
    client = language_v1.LanguageServiceClient()

    # Metin belgesi oluşturun
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Metin duygu analizini yapın
    response = client.analyze_sentiment(request={'document': document})

    string = "Metnin Duygu Puanı: ", response.document_sentiment.score
    string += "Metnin Duygu Büyüklüğü: ", response.document_sentiment.magnitude

    return string
    