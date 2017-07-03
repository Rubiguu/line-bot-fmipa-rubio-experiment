#tipe text.Message
from keyword_umum  import keyword_umum, cek_umum
from keyword_ultah import keyword_ultah, kalender
#tipe Image.Message
from keyword_latex import keyword_latex

# well, ceritanya saya bingung. Beberapa keyword enaknya ngeluarin teks
# sedangkan yang lainnya gambar. tapi ngeliat app.py ... bagaimana cara
# tahu harus ngeluarin teks atau gambar? solusi sementara ane, pakai if
# else sederhana
def TypeOutput(Input):
    if cek_umum(Input) or (Input[:10] == '!cek-ultah'):
        return('Text')
    else:
        return('Image')

# lalu tampilkan hasilnya
def Result(Input):
    if cek_umum(Input):
        return(keyword_umum(Input))
    elif Input[:10] == '!cek-ultah':
        return(keyword_ultah())
    elif Input[:6] == '!latex':
        return(keyword_latex(Input[6:]))
