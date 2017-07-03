from datetime import timedelta, date
from time import sleep
import csv

#pertama, kita buat dict kalender, dengan key tanggal (seperti '1403'), dan value
#nya adalah list yang ultah hari itu (seperti ['Keyka', 'Einstein']. tapi karena 
#ada sekitar 233 orang belum ngisi, kita assign tanggal ultah mereka ke '0000' aja.

kalender = {'0000':[]} 

start_date = date(2016,1,1)
end_date   = date(2016,12,31)

def daterange(start_date,end_date):
    for n in range(int ((end_date - start_date).days+1)):
        yield start_date + timedelta(n)				# intinya, kita melengkapi daftar
for tanggal in daterange(start_date,end_date):		# tanggal-tangal dikalender
    kalender[tanggal.strftime('%d%m')]=[]			# dari '0101' sampai '3112'

with open('datacsv/ultah.csv',newline='') as csvfile:
    baris  = csv.reader(csvfile,delimiter=',')
    temp   = []
    for x in baris:                                 # intinya, sekarang isi ultah_csv
        temp.append(x)              				# ada di variabel temp

for datum in temp:									# untuk setiap datum di temp
    nama   = datum[0]                               # ambil nama dia dan
    tanggal= datum[1].zfill(2) + datum[2].zfill(2)  # kapan ultahnya
    kalender[tanggal].append(nama.title())			# tambahkan ke dict kalender


def keyword_ultah(kalender=kalender):
    today     = date.today().strftime('%d%m')
    yg_ultah  = kalender[today]
    if len(yg_ultah)==0:                            #ngga ada yg ultah
        pesan = 'sorry guys, gaada yang ultah hari ini :v'
    else:
        pesan ='ada yg ultah bung: '
        for nama in yg_ultah:
            pesan+=nama + '! '
    return(pesan)
