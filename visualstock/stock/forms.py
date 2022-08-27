from django.forms import ModelForm, ValidationError
from .models import Stock

class AddStockStepOne(ModelForm):
    class Meta:
        model = Stock
        fields = ('name', 'image', 'principal_file')
        labels = {
            'name' : 'Nombre de Stock',
            'image' : 'Imagen de Stock',
            'principal_file' : 'Archivo fuente .csv'
        }

    def __init__(self, *args, **kwargs):
        super(AddStockStepOne, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': self.fields[field].label
            })

        self.fields['name'].widget.attrs.update({
                                                    'autofocus': True,
                                                    'tabindex': 1
                                                })        
        self.fields['principal_file'].widget.attrs.update({
                                                            'accept': '.csv',
                                                            'onchange' :'uploadFilePutName(this)'
                                                          })
        self.fields['image'].widget.attrs.update({'onchange' :'uploadFilePutName(this)'})

    def clean_image(self):
        data = self.cleaned_data['image']

        if data.size >  (10 * (1024**2)): #10 MB
            raise ValidationError(f"La imagen tiene un tamaño mayor al soportado.")

        return data

    def clean_principal_file(self):
        data = self.cleaned_data['principal_file']

        if not data.name.endswith('.csv'):
            self.add_error('principal_file', f"No es un archivo CSV: {data.name}")

        elif data.size >  (5 * (1024**2)): #5 MB
            self.add_error('principal_file', "El archivo CSV tiene un tamaño mayor al soportado.")

            try:
                data.readline(50).decode('utf-8')
            except:
                self.add_error('principal_file', "El formato de archivo no es un CSV valido.")
            
            data.seek(0)

        return data


class EditFaceStock(ModelForm):
    class Meta:
        model = Stock
        fields = ('name', 'image')
        labels = {
            'name' : 'Nombre de Stock',
            'image' : 'Imagen de Stock',
        }

    def __init__(self, *args, **kwargs):
        super(AddStockStepOne, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': self.fields[field].label
            })

class AddStockStepTwo(ModelForm):
    class Meta:
        model = Stock
        fields = ('name_column', 'price_column', 'quantity_column')
        labels = {
            'name_column' : 'Columna de nombre-producto',
            'price_column' : 'Columna de precio-producto',
            'quantity_column' : 'Columna de cantidad-productos'
        }

    @staticmethod
    def generate_placeholder(label):
        label = label.replace("Columna de ", "")
        label = label.replace("-", " de ")
        return label.capitalize()


    def __init__(self, *args, **kwargs):
        super(AddStockStepTwo, self).__init__(*args, **kwargs)

        for tabindex, field in enumerate(self.fields, 4):
            self.fields[field].widget.attrs.update({
                'placeholder': self.generate_placeholder(self.fields[field].label),
                'tabindex': tabindex,
                'list' : 'columnoptions',
            })


    def clean(self):
        cleaned_data = super().clean()
        non_repeating_data = set(cleaned_data.values())

        if len(non_repeating_data) != len(self.fields):
            self.add_error('__all__', 'Los nombres de columnas se repiten entre sí, y esto no es correcto.')

# #Archivo para crear y gestionar formularios.
# from django import forms

# #from django.contrib.auth.models import User
# from users.models import User

# class RegisterForm(forms.Form):
#     username = forms.CharField(required=True, min_length=4, max_length=50,
#                                widget=forms.TextInput(attrs={
#                                 'class': 'form-control',
#                                 'id': 'username'
#                                 }))
#     email = forms.EmailField(required=True,
#                              widget=forms.EmailInput(attrs={
#                                 'class': 'form-control',
#                                 'id': 'email',
#                                 'placeholder': 'example@correin.com'
#                              }))
#     password = forms.CharField(required=True,
#                                widget=forms.PasswordInput(attrs={
#                                 'class': 'form-control'
#                                }))

#     password2 = forms.CharField(label='Confirmar password',
#                                 required=True,
#                                 widget=forms.PasswordInput(attrs={
#                                     'class': 'form-control'
#                                 }))

#     #Al usar el prefijo clean_
#     #le indicamos a Django que vamos a realizar una validación sobre el
#     #campo que le sigue a _
#     def clean_username(self):
#         username = self.cleaned_data.get('username')

#         #Verificamos si el usuario ya existia previamente.
#         if User.objects.filter(username=username).exists():
#             #Lanzamos un error
#             raise forms.ValidationError('El username ya se encuentra en uso!!')

#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get('email')

#         #Verificamos si el usuario ya existia previamente.
#         if User.objects.filter(email=email).exists():
#             #Lanzamos un error
#             raise forms.ValidationError('El email ya ha sido registrado :c')

#         return email

#     #Sobreescribimos el metodo clean.
#     #Hacemos esto, si hay dependemcia de campos.
#     def clean(self):
#         #Extraemos los datos de la clase padre.
#         cleaned_data = super().clean()

#         #Los comparamos.
#         if cleaned_data.get('password2') != cleaned_data.get('password'):
#             #Mandamos un error a password2, si no son iguales.
#             self.add_error('password2', 'El password no coincide')

#     #Metodo para persistir usuarios, y ahorrar codigo.
#     def save(self):
#         return User.objects.create_user(
#             self.cleaned_data.get('username'), #dict
#             self.cleaned_data.get('email'),
#             self.cleaned_data.get('password')
#         )

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

# from django.forms import ModelForm
# from .models import ShippingAddress

# #Formulario de modelo.
# class ShippingAddressForm(ModelForm):
#     class Meta:
#         model = ShippingAddress
#         #Campos de interes.
#         fields = [
#             'line1', 'line2', 'city', 'state', 'country', 'postal_code', 'reference'
#         ]

#         #Como se visualizan los nombres de los campos en html.
#         labels = {
#             'line1': 'Calle 1',
#             'line2': 'Calle 2',
#             'city': 'Ciudad',
#             'state': 'Estado',
#             'country': 'País',
#             'postal_code': 'Código postal',
#             'reference': 'Referencias'
#         }

#     #Para gestionar el diseño de los campos.
#     #resscribimos el constructor __init__
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         #Campo a campo le actualizamos el estilo.
#         #Por medio de la clase.
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#             })  # dict

#         #colocamos un placeholder particular a postal_code
#         self.fields['postal_code'].widget.attrs.update({
#             'placeholder': '0000'
#         })

################################################################################################
################################################################################################
################################################################################################
################################################################################################
