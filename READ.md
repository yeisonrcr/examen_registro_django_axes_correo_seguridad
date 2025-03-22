# Configuración de Django-Allauth con Autenticación Social

Este documento explica cómo configurar `django-allauth` para habilitar autenticación social (por ejemplo, Google o Facebook), incluyendo redirecciones después de iniciar/cerrar sesión.

---

## **1. Instalación de Django-Allauth**
Asegúrate de que `django-allauth` esté instalado en tu proyecto. Si no lo has hecho, instálalo usando pip:

```bash
pip install django-allauth


INSTALLED_APPS = [
    ...
    'django.contrib.sites',  # Necesario para django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  # Para autenticación social
    'allauth.socialaccount.providers.google',  # Ejemplo para Google
    'allauth.socialaccount.providers.facebook',  # Ejemplo para Facebook
]


python manage.py migrate


Configuración de SITE_ID
Define el sitio actual que estás utilizando. Esto debe coincidir con el ID registrado en django_site:
SITE_ID = 1  # Cambia según tu tabla django_site

LOGIN_REDIRECT_URL = '/'  # URL después de iniciar sesión
LOGOUT_REDIRECT_URL = '/'  # URL después de cerrar sesión

ACCOUNT_SIGNUP_REDIRECT_URL = '/bienvenido/'  # Redirección después de registrarse
LOGIN_URL = '/accounts/login/'  # Página de inicio de sesión obligatoria
ACCOUNT_LOGOUT_ON_GET = True  # Permite cerrar sesión con solo acceder a la URL


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Rutas de django-allauth
    path('', include('empresas.urls')),  # Rutas de tu aplicación
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




Registro de aplicaciones sociales en el Admin

Para habilitar la autenticación social con Google o Facebook:

    Accede al admin de Django (/admin).

    Ve a la sección Social applications en socialaccount.

    Haz clic en Add Social Application y completa:

        Provider: Selecciona el proveedor (Google, Facebook, etc.).

        Name: Dale un nombre descriptivo (por ejemplo, "Google Login").

        Client ID: Agrega el ID proporcionado por Google/Facebook.

        Secret Key: Agrega la clave secreta.

        Sites: Asocia el sitio correspondiente (por ejemplo, example.com).


Configuración de proveedores de autenticación social
Google

    Ve a la Google cloude console
    Crea un proyecto nuevo y habilita la API de OAuth 2.0.

    Configura una credencial de tipo OAuth 2.0:

        URI de redirección: https://tudominio.com/accounts/google/login/callback/
    Copia el Client ID y el Client Secret proporcionados.


Facebook

    Ve al Facebook dev portal
    Registra tu aplicación.

    Configura una credencial:

        URI de redirección: https://tudominio.com/accounts/facebook/login/callback/
        
    Copia el Client ID y el Client Secret proporcionados.






Pruebas y Verificación

    Accede a /accounts/login/ en tu aplicación.

    Verifica que aparezcan las opciones de inicio de sesión con Google/Facebook (si las configuraste correctamente).

    Inicia sesión y asegúrate de que:

        La autenticación funciona correctamente.

        La redirección posterior al inicio/cierre de sesión lleva al usuario a la URL definida en LOGIN_REDIRECT_URL o LOGOUT_REDIRECT_URL.



Asegúrate de que tu SITE_ID = 1: Esto confirma que Django está utilizando el registro de la tabla django_site con ID 1 (tu dominio principal). No necesitas configurar otro sitio.

Configura Google como proveedor en el admin de Django:

    Ve a /admin/socialaccount/socialapp/.

    Agrega un nuevo registro de "Social Application":

        Provider: Selecciona "Google".

        Name: Un nombre descriptivo, como "Google Login".

        Client ID: El ID de cliente proporcionado por Google.

        Secret Key: La clave secreta proporcionada por Google.

        Sites: Selecciona tu sitio (probablemente sea el único disponible, con el dominio correspondiente al SITE_ID = 1).


URI de redirección de Google:

    Durante la configuración en la 









Aquí estás configurando dos cachés:

    default: Almacena datos de caché general del proyecto utilizando Redis (base de datos 0).

    axes: Utiliza una base de datos separada (1) de Redis para manejar datos relacionados con intentos fallidos de inicio de sesión que django-axes utiliza para proteger tu aplicación.

Redis es un sistema de almacenamiento en memoria que permite mejorar la velocidad al almacenar datos frecuentemente accedidos.




