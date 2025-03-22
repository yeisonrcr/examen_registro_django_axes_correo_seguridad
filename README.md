# Configuración de Autenticación Social con Django-Allauth

Este documento explica cómo configurar `django-allauth` para habilitar autenticación social (Google, Facebook, etc.), incluyendo redirecciones después de iniciar/cerrar sesión y protección contra ataques de fuerza bruta con `django-axes`.

---

## **1. Instalación de Django-Allauth**
Asegúrate de tener `django-allauth` instalado. Si no lo tienes, instálalo con:

```bash
pip install django-allauth
```

Luego, agrega las siguientes aplicaciones en `INSTALLED_APPS` dentro de `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.sites',  # Necesario para django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  # Para autenticación social
    'allauth.socialaccount.providers.google',  # Proveedor Google
    'allauth.socialaccount.providers.facebook',  # Proveedor Facebook
]
```

Ejecuta las migraciones:

```bash
python manage.py migrate
```

### **Configuración de SITE_ID**
Define el sitio que estás utilizando. Debe coincidir con el ID registrado en la tabla `django_site`:

```python
SITE_ID = 1  # Ajusta según tu base de datos
```

### **Configuraciones de Redirecciones**

```python
LOGIN_REDIRECT_URL = '/'  # URL después de iniciar sesión
LOGOUT_REDIRECT_URL = '/'  # URL después de cerrar sesión
ACCOUNT_SIGNUP_REDIRECT_URL = '/bienvenido/'  # Después de registrarse
LOGIN_URL = '/accounts/login/'  # Página de inicio de sesión
ACCOUNT_LOGOUT_ON_GET = True  # Permite cerrar sesión con solo acceder a la URL
```

### **Configuración de URLs**
En `urls.py`, agrega:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # URLs de django-allauth
    path('', include('empresas.urls')),  # URLs de tu aplicación principal
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## **2. Registro de Aplicaciones Sociales**

Para habilitar la autenticación social:

1. Accede al panel de administración de Django (`/admin`).
2. Ve a **Social applications** en `socialaccount`.
3. Haz clic en **Add Social Application** y completa:
   - **Provider**: Selecciona el proveedor (Google, Facebook, etc.).
   - **Name**: Nombre descriptivo (ej. "Google Login").
   - **Client ID**: Proporcionado por Google/Facebook.
   - **Secret Key**: Clave secreta.
   - **Sites**: Asocia el sitio correspondiente (ej. `example.com`).

### **Configuración de Proveedores**
#### **Google**
1. Accede a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un proyecto nuevo y habilita la API de OAuth 2.0.
3. Configura una credencial de tipo OAuth 2.0:
   - **URI de redirección**: `https://tudominio.com/accounts/google/login/callback/`
4. Copia el **Client ID** y el **Client Secret** proporcionados.

#### **Facebook**
1. Accede a [Facebook Developers](https://developers.facebook.com/).
2. Registra tu aplicación.
3. Configura una credencial OAuth:
   - **URI de redirección**: `https://tudominio.com/accounts/facebook/login/callback/`
4. Copia el **Client ID** y el **Client Secret** proporcionados.

---

## **3. Pruebas y Verificación**

1. Accede a `/accounts/login/` en tu aplicación.
2. Verifica que aparezcan las opciones de inicio de sesión con Google/Facebook.
3. Inicia sesión y comprueba que:
   - La autenticación funciona correctamente.
   - La redirección después de iniciar/cerrar sesión lleva al usuario a las URLs definidas en `LOGIN_REDIRECT_URL` o `LOGOUT_REDIRECT_URL`.

Asegúrate de que `SITE_ID = 1` esté correctamente configurado.

---

## **4. Configuración de Seguridad con Django Axes**

Django Axes protege contra ataques de fuerza bruta en los intentos de inicio de sesión.

### **Configuración en `settings.py`**

```python
AXES_ENABLED = True  # Activa Django Axes
AXES_FAILURE_LIMIT = 5  # Máximo de intentos fallidos permitidos
AXES_COOLOFF_TIME = 1  # Tiempo de bloqueo en horas
AXES_LOCKOUT_URL = '/locked/'  # URL de bloqueo
AXES_LOCKOUT_TEMPLATE = 'accounts/blocked/lock.html'  # Plantilla de bloqueo
AXES_RESET_ON_SUCCESS = True  # Restablece intentos fallidos tras login exitoso
AXES_LOCK_OUT_BY_USERNAME_OR_IP = True  # Bloqueo por usuario o IP
AXES_ENABLE_ADMIN = True  # Protege el admin de Django
```

### **Notas Adicionales**
- Ajusta estos parámetros según las necesidades de seguridad de tu aplicación.
- La configuración `AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP` ha sido sustituida por `AXES_LOCK_OUT_BY_USERNAME_OR_IP`, que ofrece mayor flexibilidad.

---

## **5. Configuración de Redis como Caché y para Django Axes**

Redis es un sistema de almacenamiento en memoria que mejora el rendimiento de Django y gestiona los intentos de acceso fallidos.

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'axes': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

Esto configura dos cachés:
- **default**: Para datos generales.
- **axes**: Para intentos de inicio de sesión fallidos gestionados por Django Axes.

---

Este documento te guía paso a paso en la configuración de autenticación social en Django con seguridad adicional usando Django Axes y Redis.

