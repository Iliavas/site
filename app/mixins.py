from collections import namedtuple
from django.shortcuts import render
from .models import *

def rendering(request, model, template, name):
    a = model.objects.all()
    allObjects = namedtuple('allObjects', ['object', 'position'])
    namey, namex, ellipsey, ellipsex = 420, 110, 200, 50
    spisok = []
    for i in a:
        spisok.append(allObjects(object=i, position={'namex':namex,
                                                     'namey': {"namey": namey,
                                                               "surnamey":namey + 30,
                                                               "birthdayy": namey + 60},
                                                     'ellipsey': ellipsey,
                                                     'ellipsex': ellipsex}))
        if namex >= 1050:
            namey += 350
            ellipsey += 350
            ellipsex = 50
            namex = 110
        else:
            namex += 350
            ellipsex += 350
    return render(request, template, context={name:spisok})