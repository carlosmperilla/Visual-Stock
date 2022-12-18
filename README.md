# Visual-Stock
Una aplicación para la visualización dinámica de tablas de productos.

- Permite visualizar stocks de productos, gastos, etcétera en formato tanto de tabla, como de tarjetas.
- Permite una edición rápida de los datos críticos, añadir imágenes guía para los productos, eliminar productos innecesarios.
- Además de contar con un sistema de restauración de cambios. El acceso a los múltiples stocks por usuario es práctico y dinámico
- Las imagenes se comprimen para ahorrar espacio y hacer más rapida el envio de las mismas al usuario.

## URL Para probar la aplicación web
http://carlosprogramacion.pythonanywhere.com/

## Dependencias
- Python 3.x

## Uso local
Ejecutando el siguiente script se puede probar el funcionamiento en local.

- Se descarga el repositorio en local.
- Se crea un entorno virtual, para las dependencias python.
- Se activa el entorno virtual.
- Se instalan las dependencias en el entorno virtual.
- Se inicia el servidor en local 0.0.0.0 es para poder usar la pagina  
  en multiples dipositivos en local,  
  como moviles, aunque la ip local del router puede variar.

```sh
git clone https://github.com/carlosmperilla/Visual-Stock.git
cd Visual-Stock
python -m venv vs-env
vs-env\Scripts\activate
pip install -r requirements.txt
cd visualstock
python -m manage runserver 0.0.0.0:8000
```

## ¿Es necesario registrarse?
No, posee un botón en la pagina principal, que permite el ingreso como invitado/a  
así se puede explorar el funcionamiento basíco, como filtrar productos y como se visualizan.

Si se quieren ingresar Stocks de productos propios, sí necesita registrar un usuario.

Si necesita más control de la aplicación el superusuario es:
> Username: Carlos
> 
> Password: 12345

Recomiendo cambiar el password por uno más seguro o eliminar el superusario y crear uno nuevo.

## Imagenes de ejemplo

### Inicio
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/index.png" alt="Inicio Visual Stock" width="600"/>

### Ingreso Invitados
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/ingreso.png" alt="Inicio Visual Stock" width="600"/>

### Tabla: Modo por defecto
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/tabla1.png" alt="Inicio Visual Stock" width="600"/>

### Tabla: Filas separadas
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/tabla2.png" alt="Inicio Visual Stock" width="600"/>

### Tabla: Tarjetas
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/tabla3.png" alt="Inicio Visual Stock" width="600"/>

### Botón - No molestar
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/eye-buton.png" alt="Inicio Visual Stock" width="600"/>

### Botón - Modo oscuro / Modo claro
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/modo-oscuro.png" alt="Inicio Visual Stock" width="600"/>

### Filtro de productos
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/filtro.png" alt="Inicio Visual Stock" width="600"/>

### Añadir Stock
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/add-stock.png" alt="Inicio Visual Stock" width="600"/>

### Modo: Eliminar productos
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/eliminar.png" alt="Inicio Visual Stock" width="600"/>

### Captcha de registro
<img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/captcha-registro.png" alt="Inicio Visual Stock" width="600"/>

### Diseño responsivo - Movil

<p float="left" align="middle">
  <img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/movil/ingreso-movil.jpg" alt="Inicio Visual Stock" width="200"/>
    <img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/movil/editar-stock-movil.jpg" alt="Inicio Visual Stock" width="200"/>
  <img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/movil/navbar-burger.jpg" alt="Inicio Visual Stock" width="200"/>
</p>
<p float="left" align="middle">
    <img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/movil/productos%20-%20movil.jpg" alt="Inicio Visual Stock" width="200"/>
  <img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/movil/filtro-movil.jpg" alt="Inicio Visual Stock" width="200"/>
    <img src="https://raw.githubusercontent.com/carlosmperilla/Visual-Stock/main/imagenes%20de%20ejemplo/movil/editar-eliminar-movil.jpg" alt="Inicio Visual Stock" width="200"/>
</p>
