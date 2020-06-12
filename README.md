## FIBERCRACK.PY

Este script en Python permite obtener claves por defecto de routers wifi de Fibertel utilizando fuerza bruta por medio de Aircrack y Crunch.

**Aviso**: Usar responsablemente. Usar solamente con fines educativos.

### Setup

Script probado en Python 3.6.9

Los requisitos se instalan por medio de:

```
$ sudo apt-get install aircrack-ng crunch
```

### Cómo usarlo
<pre>
usage: fiberCrack.py [file.cap] [mac]

arguments:
  file.cap              archivo .cap con el handshake obtenido previamente
  
  mac                   mac address del router

</pre>