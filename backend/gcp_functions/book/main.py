import functions_framework
import json

@functions_framework.http
def book(request):

  isbn = request.args.get('isbn')

  if not isbn:
    return json.dumps({'error': 'Se requiere el parámetro isbn'}), 400
   
  books = list()
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299591", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299593", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299594", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299595", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299596", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299597", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299598", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299599", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})

  found_books = [book for book in books if book['isbn'] == isbn] 

  return json.dumps(found_books)
