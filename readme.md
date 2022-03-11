# Expresiones Regulares
```javascript
/*
    Querys GET: [\?&](\w+)=([^&\n]+)
    Urls: https?:\/\/[\w\-\.]+\.\w{2,6}\/?\S*
    Mails: [\w\._]{5,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}
    Coordenadas 1: ^\-?\d{1,3}\.\d{1,6},\s?\-?\d{1,3}\.\d{1,6},.*$
    Coordenadas 2: ^\-?\d{1,3}\s\d{1,2}'\s\d{1,2}\.\d{2,2}"[WE],\s?\-?\d{1,3}\s\d{1,2}'\s\d{1,2}\.\d{2,2}"[NS]$
    
*/
```
# 
```javascript
/*
    \w : caracteres de palabras
    \d : digitos
    \s : espacios/invisibles en blanco
    \W : contrario al /w
    \D : contrario al /d
    \S : contrario al /s
    [0-9] : \d
    [0-9a-zA-Z_] : \w
    [A-z] :  mayúsculas y minúsculas
    . : caracter universal
    * : cero o mas caracteres
    + : uno o mas caracteres
    ? : el caracter o regla es opcional | el match se subdivide **tener cuidado**
    /d{4,10} : rango de regla
    /d{4,} : rango de regla de inicio a infinito
    ^ : negar la regla example: [^0-5a-c]
    ^.+$ : Inicio y fin de linea
    (\d{2,2}\W?) : grupos funciona para subdividir el texto a filtrar en lenguajes de programacion
*/
```

