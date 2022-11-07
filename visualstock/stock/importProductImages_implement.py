import shutil
from zipfile import ZipFile
from PIL import Image

from django.conf import settings
from django.utils.crypto import get_random_string
from django.core.files.base import ContentFile

from django.contrib import messages


def process_image_in_zipfile(request, product, image_name, path_tmp_extraction):
    """
        Validates if the files of the sent zip file are images and assigns it to its corresponding product.
    """
    error = f"El archivo {image_name} esta corrupto. Revise su zip y vuelva a intentarlo."
    path_img = path_tmp_extraction.joinpath(image_name)
    try:
        im = Image.open(path_img)
        if im.verify() != None:
            return error
    except IOError:
        return error
    else:
        with open(path_img, "rb") as f:
            product.image = ContentFile(f.read(), name=image_name)
            product.save(update_fields=['image'])


def process_zipfile(request, stock_by_name, zip):
    """
        Extract the zip files to a temporary folder and process them.
    """
    with ZipFile(zip) as customzip:
        images = {"".join(image.split(".")[:-1]):image for image in customzip.namelist()}
        products_to_import_images = stock_by_name.products.filter(name__in=images.keys())
        path_tmp_extraction = settings.MEDIA_ROOT.joinpath("Temporal", "zip_images-" + get_random_string(8))
        try:
            customzip.extractall(path=path_tmp_extraction)
        except:
            messages.error(request, "Ha ocurrido un error, intentelo más tarde.")
        else:
            for product in products_to_import_images:
                error =  process_image_in_zipfile(
                                                    request, 
                                                    product, 
                                                    images.get(product.name), 
                                                    path_tmp_extraction
                                                    )
                if error:
                    messages.error(request, error)
                    break
            else:
                messages.success(request, "Imagenes importadas/actualizadas correctamente")
                if hasattr(stock_by_name, 'backup'):
                    stock_by_name.backup.rotate_backup()
        finally:
            shutil.rmtree(path_tmp_extraction)