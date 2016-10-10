#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve


if __name__ == "__main__":
    parser = make_parser()
    prueba = SmallSMILHandler()
    parser.setContentHandler(prueba)
    urls = []
    locales = []
    try:
        parser.parse(open(sys.argv[1]))
    except:
        sys.exit("Usage: Python karaoke.py file.smil")
    lista = prueba.get_tags()
    strExit = "\n"
    for element in lista:
        for tag in element:
            strExit += tag
            for atr in element[tag]:
                for val in atr:
                    strExit += "\t" + val + "=" + "\"" + atr[val] + "\""
                    if val == "src":
                        urls.append(atr[val])
        strExit += "\n"
    print(strExit)
    with open(sys.argv[1][:-5] + ".json", 'w') as doc_json:
        json.dump(lista, doc_json, indent=4,separators=(',',': ')) 
    for url in urls:
        if url[0:7] == "http://":
            prueba = urlretrieve(url)
            locales.append(url.split('/')[-1])
    for element in locales:
        print(element)
