#!/usr/bin/env python

import pytest as pt
import stock_price_summary as sps




def test_acquire_data():
    assert sps.acquire_data('AAPL.csv',5) == [114.71,115,114.32,113.4,115.21]
    assert sps.acquire_data('AAPL.csv',5.2) == [114.71,115,114.32,113.4,115.21]
    with pt.raises(IOError):
        sps.acquire_data('AAPL',5)
    with pt.raises(ValueError):
        sps.acquire_data('AAPL.csv',300)
    
    #I know it wasn't supposed to do this, but threw it in for fun
    with pt.raises(IndexError):
        sps.acquire_data('AAPL.csv',-5)
        
        
def test_is_all_numbers():
    assert sps.is_all_numbers([1,2,3,4,5]) == True
    assert sps.is_all_numbers([0.5,10,30,25]) == True
    assert sps.is_all_numbers([1,2,'l','m']) == False
    with pt.raises(TypeError):
        sps.is_all_numbers("apples are awesome")
    with pt.raises(TypeError):
        sps.is_all_numbers(3)

def test_get_median():
    assert sps.get_median([0,1,2]) == 1
    assert sps.get_median([0,1,1,2]) == 1
    assert sps.get_median([0,1,3,4]) == 2
    assert sps.get_median([10,1,5]) == 5
    assert sps.get_median([10,2,3,34,50.38,60]) == 22
    with pt.raises(TypeError):
        sps.get_median(1)
    with pt.raises(TypeError):
        sps.get_median("a")
    with pt.raises(TypeError):
        sps.get_median([0,1,2,"l","j"])

def test_get_centered():
    assert sps.get_centered([1,2,3,4,5,5,5]) == 3
    assert sps.get_centered([1,1,2,3,4,5,6,6]) == 3.5
    assert sps.get_centered([10.2,3.56,3.1415,5.2,8]) == 5.2
    with pt.raises(TypeError):
        sps.get_centered(1)
    with pt.raises(TypeError):
        sps.get_centered("a")
    with pt.raises(TypeError):
        sps.get_centered([0,1,2,"l","j"])


def test_get_average():
    assert sps.get_average([1,2,3,4]) == 2.5
    assert sps.get_average([1.5,2,2.5]) == 2.0
    with pt.raises(TypeError):
        sps.get_average(2)
    with pt.raises(TypeError):
        sps.get_average([1,2,3,'l','h'])

def test_get_filename_from_ticker():
    assert sps.get_filename_from_ticker('aapl') == '/Users/laurenhsu-locus/python/intermed_python/hw6/stock_prices/AAPL.csv'
    assert sps.get_filename_from_ticker('AaPl') == '/Users/laurenhsu-locus/python/intermed_python/hw6/stock_prices/AAPL.csv'
    with pt.raises(TypeError):
        sps.get_filename_from_ticker(5)
    with pt.raises(TypeError):
        sps.get_filename_from_ticker(['a','b'])
