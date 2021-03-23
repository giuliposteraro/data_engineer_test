import codecs

fileInput = codecs.open("datos_data_engineer.tsv", 'r', 'utf-16 LE')
fileOutput = codecs.open("datos_data_engineer.csv", 'w', 'utf-8')
fila = ''
primeraVuelta = True
for linea in fileInput:
    separador = linea.replace("\t", "|")
    if primeraVuelta:
        header = separador
        primeraVuelta = False
    fila = fila + separador
    if len(fila.split('|')) != len(header.split('|')):
        fila = fila.strip('\n')
    else:
        fileOutput.write(fila)
        fila = ''

fileInput.close()
fileOutput.close()

