#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Verification.VerificationEntier import Verification
from Configuration.configurationFichierLogs import loggingConf
from Gestion.Calcul import CalculPourcentage

''' execution de la methode de controle des saisies de l utilisateur '''


loggingConf()

Verification()
CalculPourcentage()