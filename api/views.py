from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .Feistel import CryptRound, Feistel, FeistelFunction1, FeistelFunction2, reverse_miroire
from .DES import DES_ALGORITHME
from .aes import AES
# Create your views here.


def handleAES(text, key, bloc_size):

    return AES(text, key, bloc_size)


def handleDES(text, key):
    return DES_ALGORITHME(text, key)


def handleFeistel(text):
    return CryptRound(text, [FeistelFunction1, FeistelFunction2])


def handleFeistel1(text, func):
    result = Feistel(text, func)
    return result


@csrf_exempt
def main(request):
    if(request.method == 'POST'):
        x = json.loads(request.body.decode('utf-8'))
        response_data_success = {}
        response_data_error = {}
        response_data_error['response'] = 'error'
        response_data_error['errors'] = ['something went wrong !']

        # print(x['text'])
        if(x['text'] and len(x['text']) > 0):
            if(x['algoId'] == 1):
                res = handleFeistel1(text=x['text'], func=reverse_miroire)
                print("res===> "+res)
                response_data_success["response"] = "success"
                response_data_success["data"] = res
                return JsonResponse(response_data_success)
            elif x['algoId'] == 2:
                response_data_success['response'] = "success"
                response_data_success['data'] = handleFeistel(text=x['text'])
                return JsonResponse(response_data_success)
            elif x['algoId'] == 3:

                res = handleDES(text=x['text'], key=x['key'])
                response_data_success["response"] = "success"
                response_data_success["data"] = res
                return JsonResponse(response_data_success)
            elif x['algoId'] == 4:
                size_ = int(x['bloc_size'])/8

                res = handleAES(
                    text=x['text'], key=x['key'], bloc_size=size_)

                response_data_success["response"] = "success"
                response_data_success["data"] = res
                return JsonResponse(response_data_success)
            else:
                return JsonResponse(response_data_error)
        return JsonResponse(response_data_error)
    else:
        return render(request, 'index.html')
