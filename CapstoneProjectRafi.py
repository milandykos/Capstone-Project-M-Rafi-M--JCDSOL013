def home_menu():
    print (58*'-')
    Menu_Pertama = input('''
Selamat datang di toko Sunscreen Wotsans
            
0. Masuk sebagai admin
1. Masuk sebagai buyer
9. Exit program
Masukan angka untuk melihat yang ingin di jalankan = ''')

    if Menu_Pertama == "0":
        menupertama_admin()
    elif Menu_Pertama == "1":
        menupertama_buyer()
    elif Menu_Pertama == "9":
        exit()

def menupertama_admin():
    while True:
        pwdd = str(input('Masukan password terlebih dahulu: '))
        if pwdd != "admin" :
            print (f'Password anda salah !')
            continue
        else:
            menukedua_admin()
            break
        
def menupertama_buyer():
    while True:
        user = input('''Hai selamat datang di Wotsans
Sebelum masuk ke menu, tolong masukan username dulu ya kak !
Masukan nama minimal 5 karakter= ''')
        if len(user) < 5 :
            print ('Minimal 5 karakter!!!')
            print (' ')
            continue
        else:
            print (f'|Berhasil masuk kak {user}|')
            print (30*'-')
            print (' ')
            menukedua_buyer()
            break

def menukedua_admin():
    print(' ')
    SelamatDatang = input('''
List menu :
1. Tampilkan Sunscreen yang tersedia
2. Tambahkan stock
3. Kurangi stock 
0. Kembali ke menu awal
        
Masukan angka untuk melihat yang ingin di jalankan = ''')
    if (SelamatDatang == '1'):
        menu_display()
    if (SelamatDatang == '2'):
        menu_add_stock()
    elif (SelamatDatang == '3'):
        menu_substract_stock()
    elif (SelamatDatang == '0'):
        home_menu()
    else:
        None
        
def menukedua_buyer():
    SelamatDatang = input('''
List menu :
1. Tampilkan Sunscreen yang tersedia
2. Beli sunscreen
0. Kembali ke menu awal
        
Masukan angka untuk melihat yang ingin di jalankan = ''')
    if (SelamatDatang == '1'):
        menu_display()
    # create data
    if (SelamatDatang == '2'):
        menu_purchase()
    elif (SelamatDatang == '0'):
        home_menu()
    else:
        None
    #elif (SelamatDatang ==  '5'):
        
def akhir_buyer():
    SelamatDatang = input ('''
Masukan angka 0 untuk kembali ke menu awal
''')
    if SelamatDatang == "0":
        menukedua_buyer()

def akhir_admin():
    SelamatDatang = input ('''
Masukan angka 0 untuk kembali ke menu awal
''')
    if SelamatDatang == "0":
        menukedua_admin()
    #else:
        #print('Menu tidak dikenal')
        #akhir()

def menu_display():
    print ('  ')
    print ('Pilihan Angka 1')
    print (f'Tampilkan Sunscreen yang tersedia ')
    print (' ')
    print (58*'-')
    print (f'|SKU \t|Produk \t|Top 10 \t|Stock \t|Harga \t|')
    print (58*'-')
    for n in range(len(List_barang)):
        print ('|{}\t|{}     \t|{}     \t|{} \t|{} |'.format(n+1000,List_barang[n][0],List_barang[n][1],List_barang[n][2],List_barang[n][3]))
        print (58*'-')
    if Menu_Pertama == "0":
        akhir_admin()
    elif Menu_Pertama == "1":
        akhir_buyer()

def menu_add_stock():
    produk = input(('masukan nama produk = ').capitalize())
    Top_Non = input(('Apakah bang ini termasuk Top/Tidak = ').capitalize())
    stockProduk = int(input('masukan stock = '))
    hargaProduk = int(input('masukan harga produk = '))
    List_barang.append([produk,Top_Non,stockProduk,hargaProduk])
    print('Pilihan angka 2')
    print('Daftar Sunscreen\n')
    print (f'SKU \t| Produk \t| Top 10 \t| Stock \t| Harga \t')
    for c in range(len(List_barang)):
        print ('{}\t|{}     \t|{}     \t|{}     \t|{}     \t'.format(c+1000,List_barang[c][0],List_barang[c][1],List_barang[c][2],List_barang[c][3]))
    if Menu_Pertama == "0":
        akhir_admin()
    elif Menu_Pertama == "1":
        akhir_buyer()

def menu_substract_stock():
    print ('Piliha angka 3')
    print (' ')
    print (f'Tampilkan sunscreen yang tersedia')
    print (f'SKU \t| Produk \t| Stock \t| Harga')
    for f in range(len(List_barang)):
        print ('{}\t|{}     \t|{}     \t|{}     \t|'.format(f+1000,List_barang[f][0],List_barang[f][1],List_barang[f][2]))
    Sunscreen = int(input('masukan index yang ingin dihapus : '))
    del List_barang [Sunscreen]
    print (' ')
    print (f'setelah di hapus')
    print (' ')
    print (f'SKU \t| Produk \t| Stock \t| Harga \t|')
    for c in range(len(List_barang)):
        print ('{}\t|{}     \t|{}     \t|{}     \t|'.format(c+1000,List_barang[c][0],List_barang[c][1],List_barang[c][2],List_barang[c][3]))
    if Menu_Pertama == "0":
        akhir_admin()
    elif Menu_Pertama == "1":
        akhir_buyer()

def menu_purchase():
    print ('Piliha angka 4')
    print (' ')
    print (f'Tampilkan sunscreen yang tersedia')
    print (f'SKU \t| Produk \t| Stock \t| Harga \t')
    for c in range(len(List_barang)):
        print ('{}\t|{}     \t|{}     \t|{}     \t|'.format(c+1000,List_barang[c][0],List_barang[c][2],List_barang[c][3]))
    while True  : 
        Sunscreen = int(input('masukan index sunscreen yang ingin dibeli = '))
        Stock = int(input('masukan jumlah sunscreen : '))
        if (Stock >= List_barang[Sunscreen][2]):
            print ('Maaf, Pilihan produk {} hanya memiliki stock {}'.format(List_barang[0][0],List_barang[0][2]))
            continue #tambahan 
        else:
            keranjang.append([List_barang[Sunscreen][0], Stock,List_barang[Sunscreen][3],Sunscreen])
        print (' ')
        print ('Keranjangmu : ')
        print (' ')
        print ('|Produk \t|Harga \t|Stock \t|')
        for item in keranjang :
            print ('|{}     \t|{}\t|{}\t|'.format(item[0],item[2],item[1]))
        checker = str(input('Sudah yakin tidak ada yang di ganti? (yakin/Tidak)= '))
        if (checker == 'yakin'):
            break
    print (' ')
    print (f' Daftar belanja')
    print(' ')
    print ('|Produk \t|Harga \t        |Stock \t|Total Harga \t|')
    Hargatotal = 0
    for item2 in keranjang:
        print ('|{}  \t|{}  \t|{}  \t|{}  \t|'.format(item2[0],item2[2],Stock,item2[2]*Stock))
        Hargatotal = Hargatotal + (Stock * item2[2])
    print ('Total Harga : ' + str(Hargatotal))
    while True :
        Uang_yg_diberi = int(input('masukan jumlah uang = '))
        if (Uang_yg_diberi > Hargatotal) : 
            kembalianya = Uang_yg_diberi - Hargatotal
            print ('Terimakasih atas Belanjanya\n\n Kembalianya  ' +  str(kembalianya))
            for item3 in keranjang :
                List_barang [item3[1]][2] = List_barang [item3[1]][2]-item3[1]
                keranjang.clear()
            break
        elif (Uang_yg_diberi == Hargatotal) :
            print (f'Uang anda pas \n\n Terimakasih ')
            break
        else :
            uang_kurang = Hargatotal - Uang_yg_diberi
            print ('uang anda kurang {}'.format(uang_kurang))           
    if Menu_Pertama == "0":
        akhir_admin()
    elif Menu_Pertama == "1":
        akhir_buyer()

List_barang = [['Anessa','Non Top', 30, 450000],
               ['LRP','Top', 20, 400000],
               ['Skintipic','Top', 50, 150000],
               ['Erha','Non Top',15,200000],
               ['Azarine','Non Top', 10, 80000],
               ['Biore','Non Top', 10, 100000],
               ['Cetapil','Top', 50, 175000]]


keranjang = []

while True:
    print (58*'-')
    Menu_Pertama = input('''
Selamat datang di toko Sunscreen Wotsans
            
0. Masuk sebagai admin
1. Masuk sebagai buyer
Masukan angka untuk melihat yang ingin di jalankan = ''')

    if Menu_Pertama == "0":
        menupertama_admin()
    elif Menu_Pertama == "1":
        menupertama_buyer()

