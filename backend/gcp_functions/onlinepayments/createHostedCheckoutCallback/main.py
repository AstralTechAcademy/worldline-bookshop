import functions_framework

OK_HTML = '<!DOCTYPE html> \
<html lang="en"> \
<head> \
    <meta charset="UTF-8" /> \
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /> \
    <title>Purchase Successful</title> \
    <style> \
        body { \
            font-family: Arial, sans-serif;\
            display: flex; \
            flex-direction: column; \
            align-items: center; \
            justify-content: center; \
            height: 100vh; \
            margin: 0; \
            background-color: #ffffff; /* Fondo totalmente blanco */ \
        }\
        .container { \
            text-align: center; \
            padding: 20px;\
            background-color: #ffffff; /* Fondo del contenedor también blanco */\
            border-radius: 10px;\
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);\
        }\
        h1 {\
            color: #4CAF50;\
            margin-top: 20px;\
            font-size: 1.5em;\
        }\
        p {\
            margin-top: 15px;\
            font-size: 1.1em;\
            color: #333;\
        }\
    </style>\
</head>\
<body>\
    <div class="container">\
        <h1>Your purchase was successful!</h1>\
        <p>Please check your email inbox for the receipt.</p>\
    </div>\
</body>\
</html>'

@functions_framework.http
def main(request):
    res_code = request.args.get('res_code')
    return (OK_HTML, 200)
