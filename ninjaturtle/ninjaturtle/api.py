from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("/add")
def add(request):
    first = 6
    second = 2
    sum = first + second
    return 'The sum of '+str(first)+' and '+ str(second) +' is '+ str(sum)

@api.get("/divide")
def divide(request):
    first = 6
    second = 2
    quotient = first / second
    return 'The quotient of '+str(first)+' and '+ str(second) +' is '+ str(quotient)

@api.get("/subtract")
def subtract(request):
    first = 6
    second = 2
    diff = first - second
    return 'The difference of '+str(first)+' and '+ str(second) +' is '+ str(diff)

@api.get("/multiply")
def multiply(request):
    first = 6
    second = 2
    product = first * second
    return 'The product of '+str(first)+' and '+ str(second) +' is '+ str(product)