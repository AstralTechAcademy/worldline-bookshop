import functions_framework
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.domain.create_hosted_checkout_request import CreateHostedCheckoutRequest
from onlinepayments.sdk.domain.create_hosted_checkout_response import CreateHostedCheckoutResponse
from onlinepayments.sdk.domain.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.order import Order

@functions_framework.http
def main(request):

    origin = request.headers.get('Origin', '*')

    if request.method == 'OPTIONS':
        # Configurar cabeceras para la respuesta preflight
        headers = {
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': origin
    }

    yourAPIkey = ""
    yourAPISecret = ""
    yourCompanyName = "Worldline Bookshop"

    # Create a URI for our TEST/LIVE environment
    apiEndpoint = "https://payment.preprod.direct.worldline-solutions.com"

    communicator_configuration = CommunicatorConfiguration(
        api_endpoint=apiEndpoint,
        api_key_id=yourAPIkey,
        secret_api_key=yourAPISecret,
        authorization_type="v1HMAC",
        integrator=yourCompanyName,
        connect_timeout=5000,
        socket_timeout=10000,
        max_connections=10
    )

    communicator = Factory.create_communicator_from_configuration(communicator_configuration)

    client = Factory.create_client_from_communicator(communicator)
    # ...

    amount = request.args.get('amount')

    # Initiate fields for createHostedCheckoutRequest
    createHostedCheckoutRequest = CreateHostedCheckoutRequest()
    amountOfMoney = AmountOfMoney()
    amountOfMoney.amount = amount
    amountOfMoney.currency_code = "EUR"

    order = Order()
    order.amount_of_money = amountOfMoney

    hostedCheckoutSpecificInput = HostedCheckoutSpecificInput()
    hostedCheckoutSpecificInput.return_url = "https://worldline.com"

    createHostedCheckoutRequest.order = order
    createHostedCheckoutRequest.hosted_checkout_specific_input = hostedCheckoutSpecificInput

    # ...

    # Send the request to your PSPID on our platform and receive it via an instance of CreateHostedCheckoutResponse
    createHostedCheckoutResponse: CreateHostedCheckoutResponse = client.merchant("Wordlline1").hosted_checkout().create_hosted_checkout(
        createHostedCheckoutRequest)

    print(createHostedCheckoutResponse.redirect_url)
    return (createHostedCheckoutResponse.redirect_url, 200, headers)