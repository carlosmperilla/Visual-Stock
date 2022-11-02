from PIL import Image
from tempfile import TemporaryFile

from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.core.files.base import ContentFile

def set_product_availability(sender, instance, *args, **kwargs):
    instance.available = int(instance.quantity) > 0
        
def set_unique_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)
        while sender.objects.filter(slug=slug).exists():
            slug = slugify(instance.name+'-' + get_random_string(8))
        instance.slug = slug

def set_compressed_image(sender, instance, *args, **kwargs):
    pre_instance = sender.objects.filter(pk=instance.pk).first()

    if not instance.image:
        return None

    if (not pre_instance) or (instance.image != pre_instance.image):
        with TemporaryFile() as fp:
            image_to_compress = Image.open(instance.image)
            compressed_image = image_to_compress.convert("RGB")
            compressed_image.save(fp, "JPEG", optimize = True, quality = 10)
            fp.seek(0)
            instance.image = ContentFile(fp.read(), name=instance.name+".jpg")
