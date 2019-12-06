#!/usr/bin/env python

import zeep

wsdl = 'http://localhost:7777/ws/AcademicoWebService?wsdl'
client = zeep.Client(wsdl=wsdl)

while True:
    print('◄◄◄◄◄◄◄ Bievenid@ al Portal Estudiantil ►►►►►►►')
   