from django import forms
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
        else:
            try:
                data.readline(50).decode('utf-8')
            except:
                self.add_error('principal_file', "El formato de archivo no es un CSV valido.")    
            data.seek(0)

        return data

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
                'tabindex': 1,
                'list' : 'columnoptions',
            })


    def clean(self):
        cleaned_data = super().clean()
        non_repeating_data = set(cleaned_data.values())

        if len(non_repeating_data) != len(self.fields):
            self.add_error('__all__', 'Los nombres de columnas se repiten entre sí, y esto no es correcto.')
  
class AddStockOptional(ModelForm):
    class Meta:
        model = Stock
        fields = ('category_column', 'added_date_column', 'updated_date_column')
        labels = {
            'category_column' : 'Columna categorias',
            'added_date_column' : 'Columna de fecha-añadido',
            'updated_date_column' : 'Columna de fecha-renovado'
        }

    @staticmethod
    def generate_placeholder(label):
        label = label.replace("Columna de ", "")
        label = label.replace("-", " de ")
        return label.capitalize()

    def __init__(self, *args, **kwargs):
        super(AddStockOptional, self).__init__(*args, **kwargs)

        for tabindex, field in enumerate(self.fields, 7):
            self.fields[field].widget.attrs.update({
                'placeholder': self.generate_placeholder(self.fields[field].label),
                'tabindex': 1,
                'list' : 'columnoptions',
            })

    def clean(self):
        cleaned_data = super().clean()
        non_blank_data = [value for value in cleaned_data.values() if value != ""]
        non_repeating_data = set(non_blank_data)

        if len(non_repeating_data) != len(non_blank_data):
            self.add_error('__all__', 'Los nombres de columnas se repiten entre sí, y esto no es correcto.')

class DeleteStock(forms.Form):
    password = forms.CharField(
                                required=True,
                                label = "Contraseña de Usuario",
                                widget=forms.PasswordInput(
                                    attrs={'type':'password', 'name': 'password','placeholder':'Contraseña de Usuario', 'tabindex' : '1'}
                                    )
                                )

class EditFaceStock(ModelForm):
    name = forms.CharField(
                            required=False,
                            label = "Nombre de Stock",
                            widget = forms.TextInput(
                                attrs = {
                                    'tabindex' : '1',
                                    'placeholder' : 'Nombre de Stock'
                                }))
    image = forms.ImageField(required=False)
    class Meta:
        model = Stock
        fields = ('name', 'image')
        labels = {
            'name' : 'Nombre de Stock',
            'image' : 'Imagen de Stock',
        }

    def __init__(self, *args, **kwargs):
        super(EditFaceStock, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update({'onchange' :'uploadFilePutNameNoId(this)'})
    
    def clean_image(self):
        data = self.cleaned_data['image']
        if data:
            if data.size >  (10 * (1024**2)): #10 MB
                raise ValidationError(f"La imagen tiene un tamaño mayor al soportado.")

        return data
