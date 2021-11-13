#!/usr/bin/env python3

import os
import hashlib
import logging

logging.basicConfig(filename='hashh.log', encoding='utf-8', level=logging.INFO)

def FuncionHO(Directorio, Carpeta):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    sha512 = hashlib.sha512()
    root = Directorio
    Carpeta = Carpeta
    os.makedirs(Carpeta)
    logging.info(root)
    logging.info(Carpeta)


    for item in os.listdir(root):
        RutaCompArchivo = os.path.join(root, item)
        if os.path.isfile(RutaCompArchivo):
            with open(RutaCompArchivo, 'rb') as UnArchivo:
                buf = UnArchivo.read(BLOCKSIZE)

                while len(buf) > 0:
                    hasher.update(buf)
                    sha512.update(buf)
                    buf = UnArchivo.read(BLOCKSIZE)

            print("File: {0}".format(item))
            print("MD5: {0}".format(hasher.hexdigest()))
            print("SHA512: {0}\n".format(sha512.hexdigest()))

            with open(Carpeta + "/Output.txt", "a") as myfile:
                myfile.write("File: {}\n".format(item))
                myfile.write("MD5: {}\n".format(hasher.hexdigest()))
                myfile.write("SHA512: {}\n\n".format(sha512.hexdigest()))
