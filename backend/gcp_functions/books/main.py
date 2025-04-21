import functions_framework
import locale
import json
import time

@functions_framework.http
def foo(request):
  locale.setlocale(locale.LC_TIME, "es_ES")
  cors = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "Content-Type",
  }

  books = list()
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})
  books.append({"title": "POR SI UN DÍA VOLVEMOS", "pages": "100", "author": "Maria Dueñas", "isbn": "9788408299592", "price": "20,00 €", "img": "https://imagessl2.casadellibro.com/a/l/s7/92/9788408299592.webp"})

  return json.dumps(books)