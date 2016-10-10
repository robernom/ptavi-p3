#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Roberto Nombela Alonso. 3º ISAM. PTAVI """
import sys
import json
from xml.sax import make_parser
from urllib.request import urlretrieve
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal():
    """ Clase principal de la practica 3 """
    def __init__(self, fich):
        parser = make_parser()
        karhandler = SmallSMILHandler()
        parser.setContentHandler(karhandler)
        parser.parse(open(fich))
        self.lista = karhandler.get_tags()
        self.urls = []

    def __str__(self):
        """ Devuelve etiquetas y atributos como string """
        strexit = "\n"
        for element in self.lista:
            for tag in element:
                strexit += tag
                for atr in element[tag]:
                    for val in atr:
                        strexit += "\t" + val + "=" + "\"" + atr[val] + "\""
            strexit += "\n"
        return strexit

    def to_json(self, nombre):
        """ Crea un fichero JSON -> nombre.json """
        with open(nombre + ".json", 'w') as doc_json:
            json.dump(self.lista, doc_json, indent=4, separators=(',', ': '))

    def do_local(self):
        """ Cambia el nombre de archivos remotos por locales """
        for element in self.lista:
            for tag in element:
                for atr in element[tag]:
                    for val in atr:
                        if val == "src":
                            if atr[val][0:7] == "http://":
                                urlretrieve(atr[val])
                            atr[val] = atr[val].split('/')[-1]


if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except NameError:
        sys.exit("Usage: Python karaoke.py file.smil")
    karaobject = KaraokeLocal(fichero)
    print(karaobject)
    karaobject.to_json(fichero[:-5])
    karaobject.do_local()
    karaobject.to_json("local")
    print(karaobject)
