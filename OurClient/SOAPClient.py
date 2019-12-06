#!/usr/bin/env python

import zeep

wsdl = 'http://localhost:7777/ws/AcademicoWebService?wsdl'
client = zeep.Client(wsdl=wsdl)

while True:
    print('◄◄◄◄◄◄◄ Bievenid@ al Portal Estudiantil ►►►►►►►')
    print('\n1) Listar todos los estudiantes\t\n2) Consultar una asignatura\n3) Consultar un profesor')
    opcion = int(input("◄◄◄◄◄◄◄ Ingrese el número de la opción deseada ►►►►►►►: "))

    if opcion == 1:
        print(client.service.getAllEstudiante())

    if opcion == 2:
        asignatura = int(input('◄◄◄◄◄◄◄ Digite el nombre de la asignatura ►►►►►►►: '))
        print(client.service.getAsignatura(asignatura))

    if opcion == 3:
        profesor = int(input('◄◄◄◄◄◄◄ Digite el ID del profesor ►►►►►►►: '))
        print(client.service.getProfesor(profesor))
