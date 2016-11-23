#!/usr/bin/python
#coding: utf8
from lxml import etree
import sys
from os import *
import fdb
import logging
import datetime
import timeit
import time
from odsmod import *
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        #print "Elapsed time:",time.time() - self._startTime # {:.3f} sec".form$
        st=u"Время выполнения:"+str(time.time() - self._startTime) # {:.3f} sec$
        print st
        logging.info(st)

def main():
    #Обработка параметров
    #print len (sys.argv)
    if len(sys.argv)<=1:
        print ("getfromint: нехватает параметров")
        sys.exit(2)
    print sys.argv[1]
    #Открытие файла конфигурации
    try:
        f=file('./config.xml')
    except Exception,e:
        print e
        sys.exit(2)
               
     
    cfg = etree.parse(f)
    f.close()
    cfgroot=cfg.getroot()
    systemcodepage=cfgroot.find('codepage').text
    #Ищем параметры базы
    dbparams=cfgroot.find('database_params')
    username=dbparams.find('username').text
    password=dbparams.find('password').text
    hostname=dbparams.find('hostname').text
    concodepage=dbparams.find('connection_codepage').text
    codepage=dbparams.find('codepage').text
    database=dbparams.find('database').text
    #log_file=logpar.find('log_file').text
    #log_file2=logpar.find('log_file2').text
    #Определяем тип и путь файла
    filepar=cfgroot.find('file')
    output_path=filepar.find('output_path').text 
    if sys.argv[1]=='search':
        try:
            con = fdb.connect (host=hostname, database=database, user=username, password=password,charset=concodepage)
        except  Exception, e:
            print("Ошибка при открытии базы данных:\n"+str(e))
            sys.exit(2)
        cur = con.cursor()
        f2=file('./s.txt'  )
        l=f2.readlines()
        numip= l[0]
        print numip
    
    con.close() 

if __name__ == "__main__":
    main()

