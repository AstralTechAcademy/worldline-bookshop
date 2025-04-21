import functions_framework
import json
import time

@functions_framework.http
def hello_http(request):

    # Test Astro island dinamyc load
    time.sleep(5)
    
    return json.dumps({"description": "Orán. Años 20, siglo xx. En esta ciudad africana de origen árabe, pulso español y administración francesa desembarca una joven con el falso nombre de Cecilia Belmonte. En apariencia, ha cruzado el Mediterráneo para escapar de la miseria, como tantos compatriotas. Su razón, sin embargo, es más turbia."})
