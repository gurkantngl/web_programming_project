import os
from google.cloud import language_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account-file.json"
client = language_v1.LanguageServiceClient()

text = "Google Cloud is great!"
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
response = client.analyze_sentiment(request={'document': document})
print("Metnin Duygu Puanı: ", response.document_sentiment.score)
print("Metnin Duygu Büyüklüğü: ", response.document_sentiment.magnitude)
