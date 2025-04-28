import functions_framework
import json

@functions_framework.http
def foo(request):
  file = open("database.json", "r")
  data = json.load(file)

  return data