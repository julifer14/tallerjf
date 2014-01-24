# -*- coding: utf8 -*-
from cotxes.models import Cotxe, Reparacio
from personal.models import Tecnic
#Funció que crea 4 tecnics i 6 cotxes
def crea():    
    pere = Tecnic()
    pere.numSegSocial = '01'
    pere.nom = 'Pere'
    pere.esBaixa = False
    pere.save()
    
    joan = Tecnic()
    joan.numSegSocial = '02'
    joan.nom = 'Joan'
    joan.esBaixa = False
    joan.save()
    
    biel = Tecnic()
    biel.numSegSocial = '03'
    biel.nom = 'Biel'
    biel.esBaixa = False
    biel.save()
    
    oriol = Tecnic()
    oriol.numSegSocial = '04'
    oriol.nom = 'Oriol'
    oriol.esBaixa = False
    oriol.save()
    
    cotxe1 = Cotxe()
    cotxe1.matricula = '00001'
    cotxe1.nomPropietari = 'Pau'
    cotxe1.nomMarca = 'Seat'
    cotxe1.nomModel = 'Ibiza'
    cotxe1.dataMatriculacio = '2003-02-02'
    cotxe1.color = 'negre'
    cotxe1.esImportat = False
    cotxe1.save()
    
    cotxe2 = Cotxe()
    cotxe2.matricula = '00002'
    cotxe2.nomPropietari = 'David'
    cotxe2.nomMarca = 'Seat'
    cotxe2.nomModel = 'Leon'
    cotxe2.dataMatriculacio = '2003-02-02'
    cotxe2.color = 'blanc'
    cotxe2.esImportat = False
    cotxe2.save()
    
    cotxe3 = Cotxe()
    cotxe3.matricula = '00003'
    cotxe3.nomPropietari = 'Daniel'
    cotxe3.nomMarca = 'Opel'
    cotxe3.nomModel = 'Corsa'
    cotxe3.dataMatriculacio = '2003-02-02'
    cotxe3.color = 'groc'
    cotxe3.esImportat = False
    cotxe3.save()
    
    cotxe4 = Cotxe()
    cotxe4.matricula = '00004'
    cotxe4.nomPropietari = 'Montse'
    cotxe4.nomMarca = 'Renault'
    cotxe4.nomModel = 'Megan'
    cotxe4.dataMatriculacio = '2003-02-02'
    cotxe4.color = 'vermell'
    cotxe4.esImportat = False
    cotxe4.save()
    
    cotxe5 = Cotxe()
    cotxe5.matricula = '00005'
    cotxe5.nomPropietari = 'Marta'
    cotxe5.nomMarca = 'Citroen'
    cotxe5.nomModel = 'Xsara Picaso'
    cotxe5.dataMatriculacio = '2003-02-02'
    cotxe5.color = 'blanc'
    cotxe5.esImportat = False
    cotxe5.save()
    cotxe6 = Cotxe()
    cotxe6.matricula = '00006'
    cotxe6.nomPropietari = 'Albert'
    cotxe6.nomMarca = 'Opel'
    cotxe6.nomModel = 'Combo'
    cotxe6.dataMatriculacio = '2003-02-02'
    cotxe6.color = 'blanc'
    cotxe6.esImportat = False
    cotxe6.save()
    
    