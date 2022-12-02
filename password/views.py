import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .utils import generate_secure_password

# Create your views here.
@csrf_exempt
def password_generator(request):

    context = {}
    
    if request.method == "POST":

        # Get data from form
        lower = request.POST.get("lower")
        upper = request.POST.get("upper")
        numbers = request.POST.get("numbers")
        symbols = request.POST.get("symbols")
        length = request.POST.get("length")

        if(lower == upper == numbers == symbols == length == None):

            data = json.loads(request.body)

            lower = data.get("lower")
            upper = data.get("upper")
            numbers = data.get("numbers")
            symbols = data.get("symbols")
            length = data.get("length")

        print("Hola Mundo: ", lower, upper, numbers, symbols, length)
        
        # Generates a secure password
        password = generate_secure_password(lower, upper, numbers, symbols, length)
        
        data = {'result': 'Success', 'message': 'Password generated successfully', 'password': password}
        return JsonResponse(data)

    elif request.method != "GET":
        context["error"] = "Request method should be POST or GET."
    
    return render(request, "password/generate_password.html", context)