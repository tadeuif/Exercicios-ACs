# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:48:43 2019

@author: Alex Carneiro
"""

import pandas as pd
import json
import pytest

from cidades import cidades_por_estado, \
                    cidades_por_letra, \
                    estado_por_cidade, \
                    arvore_do_brasil


def test_item_1():
    df = pd.read_csv('cidades_br.csv')
    
    d1 = cidades_por_estado(df)
    
    with open('item_1.json', 'r') as f:
        gab1 = json.load(f)
    gab1['SP'].pop()
    assert d1 == gab1

def test_item_2():
    df = pd.read_csv('cidades_br.csv')
    d2 = cidades_por_letra(df)
    
    with open('item_2.json', 'r') as f:
        gab2 = json.load(f)
    
    assert d2 == gab2

def test_item_3():
    df = pd.read_csv('cidades_br.csv')
    d3 = estado_por_cidade(df)
    
    with open('item_3.json', 'r') as f:
        gab3 = json.load(f)
    
    assert d3 == gab3

def test_item_4():
    df = pd.read_csv('cidades_br.csv')
    d4 = arvore_do_brasil(df)
    
    with open('item_4.json', 'r') as f:
        gab4 = json.load(f)
    
    assert d4 == gab4