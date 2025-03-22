from django import forms
from django.core.validators import RegexValidator
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError


class CustomSignupForm(SignupForm):
    # Validaciones personalizadas
    nombre = forms.CharField(
        max_length=50, 
        required=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', 
                message='El nombre solo puede contener letras y espacios'
            )
        ]
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres")
        return nombre

    def save(self, request):
        # Lógica personalizada de registro
        user = super().save(request)
        user.first_name = self.cleaned_data['nombre']
        user.save()
        return user

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        # Validaciones de complejidad de contraseña
        if len(password1) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres")
        
        # Verificar que la contraseña no sea solo numérica
        if password1.isdigit():
            raise ValidationError("La contraseña no puede ser solo numérica")
        
        # Verificar que contenga al menos un número y una letra mayúscula
        if not any(char.isdigit() for char in password1):
            raise ValidationError("La contraseña debe contener al menos un número")
        
        if not any(char.isupper() for char in password1):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula")
        
        return password1
    
    