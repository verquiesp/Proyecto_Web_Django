from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, LineaPedido
from carro.carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/autenticacion/loguear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido

        ))

    LineaPedido.objects.bulk_create(lineas_pedido) # Procesar en lote

    enviar_mail(pedido = pedido,
                lineas_pedido = lineas_pedido,
                nombreusuario = request.user.username,
                emailusuario = request.user.email
            )

    messages.success(request, "El pedido se ha realizado correctamente")

    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto = "Pedido realizado"
    mensaje = render_to_string("emails/pedido.html", {

        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario"),
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "xxxxxxxxxxxxxxx" # Completar con el email de la tienda
    to = kwargs.get("emailusuario")
    # to ="xxxxxxxxxxxxxxxxxxxxxx" Comentamos la línea 50 y descomentamos esta especificando un correo para probar que todo funcione

    send_mail(asunto, mensaje_texto, from_email, [to], html_message = mensaje)