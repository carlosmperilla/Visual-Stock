from django import forms
from django.forms import ModelForm, ValidationError
from .models import Product

from zipfile import ZipFile, is_zipfile

class EditProduct(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'quantity', 'category',)

class ImportImages(forms.Form):
    images = forms.ImageField(required=False, widget=forms.FileInput(attrs={'multiple': True}))
    zip = forms.FileField(required=False, widget=forms.FileInput(attrs={'accept': '.zip'}))

    def clean_zip(self):
        data = self.cleaned_data['zip']
        image_types = ['jpg','bmp', 'exr', 'gif', 'jpeg', 'pbm', 'pgm', 'png', 'ppm', 'rast', 'rgb', 'tiff', 'webp', 'xbm']
        size_limit = (10 * (1024**2))
        
        if data == None:
            return data
        
        if not data.name.endswith('.zip') or not is_zipfile(data):
            raise ValidationError(f"No es un archivo zip: {data.name}")
        if data.size >  (500 * (1024**2)): # 500 MB
            raise ValidationError("El archivo zip tiene un tamaño mayor al soportado (500MB).")
        
        with ZipFile(data) as customzip:
            if customzip.testzip() != None:
                raise ValidationError(f"Archivo zip corrupto: {data.name}")
            for info_image in customzip.infolist():
                file_type = info_image.filename.split(".")[-1].lower()
                if not (file_type in image_types):
                    raise ValidationError(f"El zip contiene archivos que no son imagenes: {data.name}")
                if info_image.file_size > size_limit:
                    raise ValidationError(f"El zip contiene una o varias imagenes demasiado pesadas (>10MB)): {data.name}")
        return data

    def clean_images(self):
        data = self.cleaned_data['images']
        for file in self.files.getlist("images"):
            if not file.content_type.startswith("image/"):
                raise ValidationError(f"Imagen no valida: {file.name}")
            if file.size >  (10 * (1024**2)): #10 MB
                raise ValidationError(f"La imagen tiene un tamaño mayor al soportado.")
            
        return data