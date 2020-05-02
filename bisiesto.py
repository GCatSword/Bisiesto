
def anno_bisiesto(anno):
    anno = int(anno)

    if anno % 4 == 0 and anno % 100 != 0 or anno % 400 == 0:
        return 'Es un año bisiesto'
    else:
        return 'No es bisiesto'

  


    





