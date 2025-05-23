import functions_framework
import json

@functions_framework.http
def book(request):

  isbn = request.args.get('isbn')

  if not isbn:
    return json.dumps({'error': 'Se requiere el parámetro isbn'}), 400
   
  file = open("database.json", "r")
  books = json.load(file)
  found_books = [book for book in books if book['isbn'] == isbn] 

  return json.dumps(found_books)
