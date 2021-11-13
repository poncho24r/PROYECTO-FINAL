#!/usr/bin/env python3

import argparse
import subprocess
import sys
import WebScraping
import HashObtainer
import Servidor
import Cliente
import APIhunter
import correo
import logging


def main():
    parser = argparse.ArgumentParser(prog='PIA',
                                     description='Script multitarea de ciberseguridad',
                                     usage='\n'
                                     'main.py A [-U] [-C]\n'
                                     'main.py B [-D]\n'
                                     'main.py C  \n'
                                     'main.py D [-R] [-C]\n'
                                     'main.py E \n'
                                     'main.py F \n')
    parser.add_argument(
        'script', help='Elija el script a ejecutar: '
        'A). WebScraping, B). APIhunter, C). correo, '
        'D). HashObtainer, E). Powershell, F). Servidor',
        type=str, choices=['A', 'B', 'C', 'D', 'E', 'F'])

    parser.add_argument('-U', '--URL', help='URL de la pagina web incluyendo "https://"')
    
    parser.add_argument('-C', '--Carpeta',
                        help='Nombre que se le asignará a la carpeta')
    parser.add_argument('-R', '--Directorio',
                        help='Ruta de la carpeta')
    parser.add_argument('-D', '--dominio',
                        help='Dominio de email')

    try:
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
        args = parser.parse_args()
        if args.script == 'A':
            WebScraping.FuncionWS(args.URL, args.Carpeta)   
        elif args.script == 'B':
            APIhunter.buscardominios(args.dominio)
        elif args.script == 'C':
            correo.enviarImagen()
        elif args.script == 'D':
            HashObtainer.FuncionHO(args.Directorio, args.Carpeta)
        elif args.script == 'E':
            p = subprocess.Popen(["powershell.exe",
                                  ".\\E1Script.ps1"],
                                 stdout=sys.stdout)
            p.communicate()
        elif args.script == 'F':
            print("abra una terminal y escriba python3 Cliente.py")
            Servidor.hola()

        else:
            print('operando invalido')
        
            


    except:
        print("main: falta un operando\nPruebe 'main -h' o 'main --help' para más información.")
        logging.error("main: falta un operando\nPruebe 'main -h' o 'main --help' para más información.")



        

if __name__ == "__main__":
    main()
    
    
