# Python-Comprehensions-Lambdas-y-Manejo-de-Errores

## El Zen de Python

El Zen de Python se compone por los principios para escribir tu código de manera clara, sencilla y precisa. Estos son:

- **Bello es mejor que feo**:
  Pyhton es estéticamente superior a cualquier otro lenguaje de programación. Al momento de escribir código, es mejor que sea de manera limpia y estética.
- **Explícito es mejor que implícito**:
  Hacer más fácil que las otras personas entiendan el código.
- **Simple es mejor que complejo**:
  Es mejor tener una implementación simple, que ocupe pocas lineas de código y sea entendible, a que sea una larga y complicada.
- **Complejo es mejor que complicado**:
  Si tenemos que extendernos en la implementación y hacerla más compleja para que el código si se entienda, esto es mejor que hacerlo simple y mal.
- **Plano es mejor que anidado**:
  El anidamiento es cuando tenemos un bloque de código dentro de otro bloque de código (dependiendo de este). Esto se nota en Python por la identación, nos quedarían estos bloques muy corridos a la derecha.
  Es mejor evitar el anidamiento, y hacer las cosas de manera plana.
- **Espaciado es mejor que denso**:
  Por la identación de Python (sus sangrías), este principio se nos hace imposible de esquivar. El código inevitablemente es espaciado.
- **La legibilidad es importante**:
  Es importante que otros programadores puedan entender lo que estamos escribiendo. Esto hace más fáciles las cosas cuando trabajemos con otros en los proyectos.
- **Los casos especiales no son lo suficientemente especiales cpmo para romper las reglas (sin embargo, la practicidad le gana a la pureza):**
  Siempre que podamos respetar estas reglas que nos plantea Python, es mejor así. Sin embargo, si por el hecho de hacer un código muy puro o muy ‘Pythonista’, este pierde legibilidad, es mejor ser más prácticos y romper o saltearnos algunas de estas reglas para que el código sea más eficiente. Por lo tanto, llegado el momento debermos decidir si es mejor hacer las cosas de manera pura o práctica.
- **Los errores nunca deberían pasar silenciosamente (a menos que se silencien explícitamente)**:
  Manejar los erroes es fundamental. Cada error nos dice algo y hay que prestarle atención. A menos que seas capaz de silenciar un error explícitamente, aunque para esto hay que tener criterio.
- **Frente a la ambiguedad, evitar la tentación de adivinar**:
  Nuestro código debería solamente tener una interpretación. Si en un contexto significa algo, y en otro otra cosa, es mejor que lo revisemos y busquemos una solución.
- **Debería haber una, y preferiblemente sola, una manera obvia de hacerlo. (A pesar de que esa manera no sea obvia a menos que seas holandés)**:
  Esto hace referencia al creador de Python ''Guido van Rossum", que de manera muy inteligente encontrar las soluciones precisas a los problemas, y deberíamos imitarlo.
- **Ahora es mejor que nunca**:
  Es mejor desarrollar nuestra solución cuánto antes, no dejarlo para mañana o para mas adelante.
- **A pesar de que nunca es muchas veces mejor que ahora mismo**:
  Si por hacer las cosas ya y tenemos poco tiempo, si es mejor dejarlo para después y no hacerlo apurado y mal.
- **Si la implementación es díficil de explicar, es una mala idea, y si es fácil de explicar, es una buena idea**:
  Si somos capaces de explicar nuestra implementación a otros desarrolladores paso a paso, es una buena idea. En cambio si no podemos hacerlo, significa que ni nosotros entendemos la implementación y deberíamos repensar nuestra forma de encarar la solución.
- **Los espacios de nombres son una gran idea, ¡Tengamos más de esos! (namespaces)**:
  Es el nombre que se ha indicado luego de la palabra import, es decir la ruta (namespace) del módulo. (Lo veremos a profundidad más adelante).

## ¿Qué es la documentación?

**La documentación es la biblia de cualquier programador.**

No puedes aspirar a aprender un lenguaje si no lees documentación. Sé que muchas personas se saltan eso porque piensan “ufff, es mucho texto, se ve feo”, etc. Pero es la documentación quien nos va a decir exactamente cómo funciona el lenguaje (y cualquier tecnología). No hay un solo desarrollador profesional que no lea documentación.

Docmentacion de python : https://docs.python.org/3/

## ¿Qué es un entorno virtual?

Los entornos virtuales son de mucha utilidad ya que nos ayudan a tener versiones especificas de librerías o módulos a un proyecto sin afectar a otros. De esta forma en el mismo equipo pueden coexistir distintos proyectos con distintas versiones de la misma librería o modulo.

## Creando un ambiente virtual con VENV

1. Creación de ambiente Virtual:

```
python3 -m venv nombre_venv

```

- Usualmente el nombre del ambiente virtual es venv.

2. Activación del ambiente virtual:

- Windows:

```
.\venv\Scripts\activate
```

- Unix o MacOS:

```
source venv/bin/activate
```

3. Desactivar el ambiente virtual:

```
deactivate
```

- Crear un alias en linux/mac:

```
alias nombre-alias="comando"
alias avenv="source venv/bin/activate"
```

**Para que el alias sea permanente**

Para los de mac
MacOS Catalina y superior
Apple cambió su shell predeterminado a zsh , por lo que los archivos de configuración incluyen ~/.zshenvy ~/.zshrc. Esto es como ~/.bashrc, pero para zsh. Simplemente edite el archivo y agregue lo que necesite; debe obtenerse cada vez que abra una nueva ventana de terminal:

```
nano ~/.zshenv
```

```
alias py=python
```

Luego haga ctrl + x, y, luego ingrese para guardar.

Este archivo parece ejecutarse sin importar qué (inicio de sesión, no inicio de sesión o script), por lo que parece mejor que el `~/.zshrc` archivo.

## Instalación de dependencias con pip

Básicamente, `pip` es como el `npm` de JavaScript, y el archivo `requeriments.txt` es como el `package.json` de JavaScript.
.
Es importante recordar que esto se debe correr con el entorno virtual activado (`avenv`), de esta manera todas las dependencias que instalemos se guardaran para este entorno virtual (de lo contrario se guardarían de manera global, que es justo lo que no queremos).
.
Algo importante, si estás manejando git, es bueno siempre ignorar la carpeta `venv`, esto porque realmente no nos importa subir todo eso al repositorio, puedes mirarlo como que `venv` es el `node_modules` de JavaScript, a fin de cuentas, cualquier otro programador que trabaje con nuestro código creará su propio entorno virtual e instalará las dependencias que dejamos en nuestro `requeriments.txt`.
.
Y un dato curioso es que, el operador `>` en la terminal es algo especial de UNIX, ya que este operador lo que hace es redirigir la salida de cualquier comando hacia donde lo mandes, por defecto la salida es en la terminal, pero al usar `>` le dijimos a la terminal que, en lugar de que la salida sea en la terminal, que se redirija al archivo `requeriments.txt` 👀. Si quieren jugar con ello, pueden hacerlo con este ejemplo: `ls -al > test.txt`, eso creará un archivo llamado `test.txt`, y si lo abren verán cómo es que ese comando funciona 😄

## Conceptos avanzados de funciones

Una función es simplemente código que escribimos una vez y aplicamos después en diferentes lugares donde estemos trabajando.

### funciones anónimas: Lambda

Lambda son las funciones anónimas que contienen una sola expresión, es decir: funciones sin identificación, sin nombre:

```python
lambda argumento:expresión
```

- tenemos la palabra clave lambda
- un argumento seguido de una expresión donde se colocan los argumentos

En vez de usar **def** usamos **lambda**. Estas últimas pueden tener el argumento que nosotros necesitemos, pero una sola línea de expresión.

```python
palindrome = lambda string: string === string[::-1]
print(palindrome("ana"))
#output
True
```

1. argumento o parametro que recibe la función para poder acompañado de la palabra clave lambda
2. expresión con linea de código
3. variable con identificador, ojo no es de la función, sino de la variable que va a contener un objeto de tipo función que retorna toda la función de python

## High order functions: filter, map y reduce

La diferencia entre filter y map:

- **filter** devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
- **Map** funciona muy parecido, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.

Cómo funciona reduce:

- **Reduce** toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

## Los errores en el código

Cuando python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos como traceback, puesde ser debido a:

- Errores de Sintaxis (SyntaxError) → escribimos mal alguna palabra clave (typo), el programa no se ejecuta.
- Excepciones (Exeption) → Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, tambipen pueden generarse dentro del código o fuera de el (elevar una excepción)

### Lectura de un traceback

- La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
- En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
- La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
- La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)

### Elevar una excepción

- Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback

## Debugging:

O depuración es una herramienta que traen varios editores de código con el objetivo de solucionar nuestros errores de lógica. Revisemos la herramienta debugging de VSCode

En este entorno podemos acceder a funcionalidades como:

- pause → permite pausar la ejecución del programa
- step over → permite avanazr un solo paso en el programa
- step in → igresamos a un bloque secundario del programa (funciones)
- step out → salimos del bloque secundario
- restart → reinicia el programa
- stop → detiene el programa

Además podemos generar breakpoints, que son puntos en los que el programa se detendrá para ayudarnos a depurar el código

**Nota:**

Existen herramientas de debugging propias de python como el módulo pdb o los breakpoints (a partir de python 3.7)

## Manejo de excepciones

Algo que aparece casi al final de la lectura recomendada en el documentación de Python es que se puede agregar un “else” al try-except.

- **TRY**: En el try se coloca código que esperamos que pueda lanzar algún error.
- **EXCEPT**: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
- **ELSE**: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
- **FINALLY**: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

```python
try:
    pass #Código a evaluar
except:
    pass #Si ocurre un error, llegará a esta parte
```

Ejemplo con try, raise, except:

```python
def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se pueden ingresar cadenas vacías")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")
```

## Assert statements

Es una manera poco usual de manejar los errores en python

Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo AssertionError y nos muestra un mensaje.

Su sintaxis es:

```python
assert <condicion>, <"mensaje">
<código>

```

## ¿Cómo trabajar con archivos?

Existen varias extensiones de archivos con los que podemos interactuar con python (js,csv,py,css,json,xml)

Para abrir un archivo seguimos las siguiente estructura

```python
with open(<ruta>, <modo_apertura>) as <nombre>
```

`with` Es un manejador contextual, nos ayuda a controlar el flujo del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)

`open(ruta,modo_apertura)`: es una función que necesita de dos parámetros

- **ruta**: es donde se encuentra nuestro archivo en nuestro equipo

- **modo_de_apertura**: como vamos a abrir el archivo, los modificadores son:
  - r → modo de lectura
  - w → modo de escritura (sobreescribe el archivo)
  - a → modo append (añade información al final del archivo)

`as <nombre>` nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer


