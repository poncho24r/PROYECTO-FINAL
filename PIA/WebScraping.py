#!/usr/bin/env python3
import logging
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

logging.basicConfig(filename='web.log', encoding='utf-8', level=logging.INFO)

def FuncionWS(URL, Carpeta):

    #Ubicacion y creacion de directorios
    Ubicacion = str(os.path.dirname(os.path.abspath(__file__)))
    Carpeta = Carpeta
    logging.info(Carpeta)
    os.makedirs(Carpeta + "/Imagenes/")
    os.makedirs(Carpeta + "/Outputs/")

    # Parte de Web Scraping
    #URL = input("Ingrese la URL: ")
    print("\nHaciendo el Web Scraping, espere un segundo...")
    r = requests.get(URL)
    logging.info(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.find_all("img"):
        link = item["src"]
        split = link.split("/")
        with open(Ubicacion + "/" + Carpeta + "/Imagenes/" + split[-1], "wb") as f:
            imagen = requests.get(link)
            f.write(imagen.content)

    # Parte de sacar Metadata y el output a un .txt
    print("\nExtrayendo el metadata de las imagenes, espere un segundo...\n")
    for item in os.listdir(Ubicacion + "/" + Carpeta + "/Imagenes/" ):
        image = Image.open(Ubicacion + "/" + Carpeta + "/Imagenes/" + item)
        exifdata = image.getexif()
        for tagid in exifdata:
            tagname = TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)
            with open(Ubicacion + "/" + Carpeta + "/Outputs/" + item + ".txt", "a") as myfile:
                myfile.write(f"{tagname:25}: {value}\n")

