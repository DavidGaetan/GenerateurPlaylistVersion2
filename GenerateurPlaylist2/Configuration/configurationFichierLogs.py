#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

'''
definition du nom du fichier et du niveaux de logging
'''
def loggingConf():
    logging.basicConfig(filename='mon_fichier_de_logs', level=logging.DEBUG)
