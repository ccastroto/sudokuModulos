Sudoku Modules
==============

Kata sobre programación modular en Python, a partir de uno de los ejercicios propuestos en el _problem set_ de la _Lesson 3: How to Manage Data_ del curso [_Intro to computer science_](https://www.youtube.com/watch?v=9nkR2LLPiYo&list=PLAwxTw4SYaPmjFQ2w9j05WDX8Jtg5RXWW) del Prof. Dave Evans [@evansuva](https://github.com/evansuva) en Udacity. 

Se trata de investigar y comprender los contextos de ejecución al invocar módulos Python.

Por este motivo, la configuración del `sys.path` en el código de `checkSudoku.py` y los `import`
de las dependencias se han hecho explícitas. Lee los comentarios en el código.

Además, se incluyen unos prints estilo _devil guide to debugging_ en `checkCuadrado.py`para hacer explícita la ejecución del código de un módulo cuando lo importamos y entender el comportamiento de los _Mixed Usage Modes_ `__name__` y ` __main__`.

La estructura de directorios y sus nombres tampoco son muy ortodoxas ya que responden a la intención de forzar comportamientos para comprender el sistema de importación de módulos de Python.

No se utiliza una suite de testing, ya que se accede a los casos test utilizando la **reflexión** de Python, accediendo a los mismos como propiedades del objeto módulo `casosTest.py`.

No se utiliza el nombre `test` en el directorio con los casos test porque sino el entorno Python intenta importar desde ese paquete los módulos que no encuentra cuando importamos el contenido del directorio con los casos test (precedencia de nombre).

## Uso

Ejecutar el `checksudoku.py` desde consola.

`$ python3 checksudoku.py`

Ejecutar los diferentes modulos de *checkSudoku* desde dentro de la carpte de `src`:

`src $ python3 checkCuadrado.py`

## Casos Test

Inicializar el ***.venv*** y instalar los *requierements.txt*:

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirementents.txt`

### Ejecutar el *pytest*:

` pytest "test\test_checkCuadrado.py"`