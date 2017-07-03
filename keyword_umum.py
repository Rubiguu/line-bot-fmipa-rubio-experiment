import csv

# pertama, kita buat dict keyword, yg berisi keyword yang
# umum seperti info-beasiswa atau yang-dibawa-ospek.

keyword = {}

with open('datacsv/umum.csv',newline='') as csvfile:            # delimiternya '|', karena ini jarang dipakai
    baris  = csv.reader(csvfile,delimiter='|')                  # kalau ','... bisa jadi hancur.
    temp   = []
    for x in baris:                                             # intinya, sekarang isi ultah_csv
        temp.append(x)              				# ada di variabel temp

keyword = {temp[i][0]:temp[i][1] for i in range(len(temp))}     # ubah temp (tipe list) jadi keyword (tipe dict)

def cek_umum(Input,keyword=keyword):
    if Input in Input in keyword:
        return(True)                                            # Inputnya ada di keyword kategori umum, alias disini
    else:
        return(False)
def keyword_umum(Input, keyword=keyword):
    return(keyword[Input])
