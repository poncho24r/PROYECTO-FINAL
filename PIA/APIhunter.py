#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Este script devolverá los correos electrónicos recopilados de hunter.io dado un dominio
import logging
import sys
import requests
import xlsxwriter

logging.basicConfig(filename='api.log', encoding='utf-8', level=logging.INFO)

def exportar_resultados(emails):
    """
    exportar resuktados a un archivo XLSX
    """
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    count = 0
    try:
        print("Exportando los resultados en un Excel")
        # Crear un nuevo libro de excel y agregamos una hoja.
        workbook = xlsxwriter.Workbook('hunter.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, "email")
        row += 1

        # guardar cada email que aroje la bsuqueda
        for email in emails:
            col = 0
            worksheet.write(row, col, email)
            row += 1
            count += 1

        #Close the excel
        workbook.close()

    except Exception as excp:
        print("Error en exportar_resultados" + str(excp))


def manage_response(data):
    """
    Respuesta obtenida de la API
    """
    emails = []
    try:
        for email in data['data']['emails']:
            print("\n[*]Email: " + str(email['value']))
            emails.append(str(email['value']))
    except Exception:
        print("Could not find any information about that")
        emails = "-"
    return emails


def send_request(url):
    """
    Sends custom request to the API
    """
    response = None
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
    except Exception as excp:
        print(excp)
    return response.json()



def buscardominios(dominio):

    api =input("ingrese su api_key de Hunter.io")
    logging.info(api)
    logging.info(dominio)
    response = None
    emails = []
    limit = 10 # by default limit=10

    url = url = "https://api.hunter.io/v2/domain-search?domain="+dominio+"&api_key="+api+"&limit="+str(limit)
    #Sent request
    response = send_request(url)
    # Manage the response
    emails = manage_response(response)
    #Export results
    if emails != "-":
        exportar_resultados(emails)

       

