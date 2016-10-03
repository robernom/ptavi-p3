#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.ListTags = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            width = {'width': attrs.get('width', "")}    # "" default
            height = {'height': attrs.get('height', "")}
            BGColor = {'background-color': attrs.get('background-color', "")}
            self.RLayout = {'root-layout': [width, height, BGColor]}
            self.ListTags.append(self.RLayout)
        elif name == 'region':
            ID = {'id': attrs.get('id', "")}
            top = {'top': attrs.get('top', "0")}
            bottom = {'bottom': attrs.get('bottom', "0")}
            left = {'left': attrs.get('left', "0")}
            right = {'right': attrs.get('right', "0")}
            self.Reg = {'region': [ID, top, bottom, left, right]}
            self.ListTags.append(self.Reg)
        elif name == 'img':
            src = {'src': attrs.get('src', "")}
            region = {'region': attrs.get('region', "")}
            begin = {'begin': attrs.get('begin', "0s")}
            dur = {'dur': attrs.get('dur', "0s")}
            self.img = {'img': [src, region, begin, dur]}
            self.ListTags.append(self.img)
        elif name == 'audio':
            src = {'src': attrs.get('src', "")}
            begin = {'begin': attrs.get('begin', "0s")}
            dur = {'dur': attrs.get('dur', "0s")}
            self.audio = {'audio': [src, begin, dur]}
            self.ListTags.append(self.audio)
        elif name == 'textstream':
            src = {'src': attrs.get('src', "")}
            region = {'region': attrs.get('region', "")}
            self.TStream = {'textstream': [src, region]}
            self.ListTags.append(self.TStream)

    def get_tags(self):
        return self.ListTags
