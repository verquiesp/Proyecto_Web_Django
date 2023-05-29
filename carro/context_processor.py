from .carro import Carro

# Hemos creado una variable globa para nuestra web

def importe_total_carro(request):
    carro = Carro(request)
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + (float(value["precio"]))
    else:
        total = "Debes iniciar sesión: 0"

    return {"importe_total_carro": total}

