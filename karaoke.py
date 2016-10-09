#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


def str_list(list):
    strExit = "\n"
    for element in datos:
        for tag in element:
            strExit += tag
            for atr in element[tag]:
                for val in atr:
                    strExit += "\t" + val + "=" + '"' + atr[val] + '"'
        strExit += "\n"
    return strExit

if __name__ == "__main__":
    parser = make_parser()
    prueba = SmallSMILHandler()
    parser.setContentHandler(prueba)
    try:
        parser.parse(open(sys.argv[1]))
    except:
        sys.exit("Usage: Python karaoke.py file.smil")
    datos = prueba.get_tags()
    print(str_list(datos))
