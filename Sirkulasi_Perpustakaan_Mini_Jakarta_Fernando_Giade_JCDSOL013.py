"""
Berikut adalah program sederhana untuk proses Sirkulasi Perpustakaan Mini Jakarta.
Terdapat beberapa ketentuan yang dipakai untuk pembuatan program ini yaitu:
1. 1 judul buku hanya terdiri dari 1 eksemplar buku
2. bookID bersifat unik dan dapat diisi alphanumeric atau karakter khusus
3. bookTitle dan bookAuthor dapat diisi alphanumeric atau karakter khusus
4. Biaya peminjaman adalah IDR 5.000/buku
5. Masa pengembalian adalah 7 hari kalender setelah tanggal peminjaman
6. bookDataMaster menampung seluruh data buku (tidak terpengaruh atas buku yang dihapus)

Adapun menu-menu dari program adalah:
0. Login
1. Menampilkan Daftar Buku
2. Pencarian Buku
3. Penambahan Buku
4. Peminjaman Buku
5. Pengembalian Buku
6. Penghapusan Buku
7. Exit Program
"""

from tabulate import tabulate
import datetime

search=[]
borrow=[]
returned=[]
bookDataMaster=[]
feeBorrow=5000
login=False

userDict = {
    'DODO': {'password': 'Jakarta1'},
    'MAUDY': {'password': 'Jakarta2'},
    'SHEILA': {'password': 'Jakarta3'},
    'ANWAR': {'password': 'Jakarta4'}
}

bookData =[
    {'bookID':'BMA','bookTitle':'BUMI MANUSIA','bookAuthor':'PRAMOEDYA ANANTA TOER','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'BEA','bookTitle':'BEAUTY IS A WOUND','bookAuthor':'EKA KURNIAWAN','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'LPI','bookTitle':'LASKAR PELANGI','bookAuthor':'ANDREA HIRATA','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'EPL','bookTitle':'EAT, PRAY, LOVE','bookAuthor':'ELIZABETH GILBERT','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'IET','bookTitle':'INDONESIA, ETC','bookAuthor':'ELIZABETH PISANI','bookGenre':'NON FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'COA','bookTitle':'CHILD OF ALL NATIONS','bookAuthor':'PRAMOEDYA ANANTA TOER','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'PKS','bookTitle':'PERAHU KERTAS','bookAuthor':'DEE LESTARI','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'SAM','bookTitle':'SAMAN','bookAuthor':'AYU UTAMI','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'SPI','bookTitle':'SANG PEMIMPI','bookAuthor':'ANDREA HIRATA','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':1,'borrower':'','borrowDate':'','returnDate':''},
    {'bookID':'MTR','bookTitle':'MAN TIGER','bookAuthor':'EKA KURNIAWAN','bookGenre':'FICTION','bookInput': '2024-02-10','bookStock':0,'borrower':'DODO','borrowDate':'2024-02-11','returnDate':'2024-02-18'}
]

print('''
###### HALO SELAMAT DATANG DI ######
##### PERPUSTAKAAN MINI JAKARTA ####
############ MENU LOGIN ############    
''') 
userID=input('Masukkan UserID Anda (jika User tidak terdaftar, maka program akan exit): ')

#Fuction to display data
def bookList():
    print('''
    ##### PERPUSTAKAAN MINI JAKARTA ####
    ######### MENU DAFTAR BUKU #########
    ''')
    print('Berikut adalah daftar buku PERPUSTAKAAN MINI JAKARTA')
    print(f'Tanggal {datetime.date.today()}')
    print(tabulate(bookData, headers='keys', tablefmt='psql', showindex=True))

#Fuction to search data
def searchBook():
    print('''
    ##### PERPUSTAKAAN MINI JAKARTA ####
    ######## MENU PENCARIAN BUKU #######
    ''')
    found=False
    while True:
        keyword=input('Masukkan kata pencarian Anda untuk judul atau pengarang buku: ')
        for i in range(0,len(bookData)):
            if all(x in bookData[i]['bookTitle'] for x in keyword.upper()):
                search.append({                
                    'bookID':bookData[i]['bookID'],
                    'bookTitle':bookData[i]['bookTitle'],
                    'bookAuthor':bookData[i]['bookAuthor'],
                    'bookGenre':bookData[i]['bookGenre'],
                    'bookInput':bookData[i]['bookInput'],
                    'bookStock':bookData[i]['bookStock'],
                    'borrower':bookData[i]['borrower'],
                    'borrowDate':bookData[i]['borrowDate'],
                    'returnDate':bookData[i]['returnDate']
                })
                found=True
        for i in range(0,len(bookData)):
            if all(x in bookData[i]['bookAuthor'] for x in keyword.upper()):
                search.append({                
                    'bookID':bookData[i]['bookID'],
                    'bookTitle':bookData[i]['bookTitle'],
                    'bookAuthor':bookData[i]['bookAuthor'],
                    'bookGenre':bookData[i]['bookGenre'],
                    'bookInput':bookData[i]['bookInput'],
                    'bookStock':bookData[i]['bookStock'],
                    'borrower':bookData[i]['borrower'],
                    'borrowDate':bookData[i]['borrowDate'],
                    'returnDate':bookData[i]['returnDate']
                })
                found=True
        if found is True:
            print('\nDaftar Pencarian Buku: ')
            print(f'Kata pencarian Anda {keyword} terdapat di: ')
            print(tabulate(search, headers = 'keys', tablefmt='psql'))
        else:
            print(f'Kata pencarian Anda {keyword} tidak ditemukan')
        search.clear()
        break

#Function to add new book
def addBook():
    print('''
    ##### PERPUSTAKAAN MINI JAKARTA ####
    ######## MENU PENAMBAHAN BUKU ######
    ''')
    bookID = input('Masukkan ID buku (harus unik): ')
    bookTitle = input('Masukkan judul buku: ')
    bookAuthor = input('Masukkan pengarang buku: ')
    bookGenre = input('Masukkan genre buku (NON FICTION/FICTION): ')
    bookInput = datetime.date.today()
    bookStock = 1
    searchBook=False

    for i in bookData:
        if bookID.upper()==i['bookID']:
            searchBook=True
            break
        else:
            continue

    if searchBook!=True:
        if (bookGenre.upper()=='NON FICTION' or bookGenre.upper()=='FICTION'):
            bookData.append({                
                'bookID':bookID.upper(),
                'bookTitle':bookTitle.upper(),
                'bookAuthor':bookAuthor.upper(),
                'bookGenre':bookGenre.upper(),
                'bookInput':bookInput,
                'bookStock':bookStock
            })
            print("Data berhasil ditambahkan.")
            bookDataMaster=bookData.copy()
        else:
            print('Pemambahan buku gagal, mohon dicek kembali inputan bookGenre')     
    else:
        print('Pemambahan buku gagal, bookID tidak boleh sama')
    bookList()

#Function to borrow book
def borrowBook():
    print('''
    ##### PERPUSTAKAAN MINI JAKARTA ####
    ######## MENU PEMINJAMAN BUKU ######
    ''')
    bookList()
    while True:
        bookIDBorrow=input('Masukkan ID buku yang ingin dipinjam: ')
        borrowDate=datetime.date.today()
        returnDate=borrowDate+datetime.timedelta(days=7)
        totalFee=0
        for i in range(0,len(bookData)):
            if bookIDBorrow.upper() == bookData[i]['bookID'] and bookData[i]['bookStock']!=0:
                borrowerName=input('Masukkan nama Peminjam: ')
                borrow.append({
                    'bookID':bookIDBorrow,
                    'bookTitle':bookData[i]['bookTitle'],               
                    'bookQty':1,
                    'borrower':borrowerName.upper(),
                    'borrowDate':borrowDate,
                    'returnDate':returnDate,
                    'feeBorrow':feeBorrow,
                    })
            elif bookIDBorrow.upper() == bookData[i]['bookID'] and bookData[i]['bookStock']==0:
                print(f'Buku ID {bookIDBorrow.upper()} sedang beredar')
        checker = input('Anda ingin meminjam buku lain (Y/T): ')
        if checker.upper()=='T':
            break

    print('\nDaftar Peminjaman Buku: ')
    print(tabulate(borrow, headers = 'keys', tablefmt='psql'))    
    for item in borrow:
        totalFee+=item['bookQty']*item['feeBorrow']
    
    while True:
        try:
            print(f'\nTotal biaya peminjaman buku Anda sebesar: {totalFee}') 
            payment=int(input('Masukkan jumlah pembayaran: '))
            if totalFee>0 and payment >= totalFee:
                change = payment-totalFee
                print(f'Total pembayaran Anda sebesar: {payment}\nUang kembalian Anda sebesar: {change}\n\nTerima kasih atas pembayaran Anda')
                print(f'\n\nMohon buku dikembalikan pada (YYYY-MM-DD): {returnDate}')
                for i in range(0,len(borrow)):
                    for j in range(0,len(bookData)):
                        if borrow[i]['bookID']==bookData[j]['bookID']:
                            bookData[j]['bookStock']=0
                            bookData[j]['borrower']=borrow[i]['borrower']
                            bookData[j]['borrowDate']=borrow[i]['borrowDate']
                            bookData[j]['returnDate']=borrow[i]['returnDate']
                borrow.clear()
                break          
            elif totalFee>0 and payment < totalFee:
                insufficientPayment=totalFee-payment 
                print(f'Uang pembayaran Anda kurang sebesar {insufficientPayment}, mohon lakukan pembayaran kembali')
            elif totalFee<=0:
                print('Terima kasih')
                break
        except ValueError:
            print('Input Anda salah')
            borrow.clear()
    bookList()

#Function to return book
def returnBook():
    print('''
    ##### PERPUSTAKAAN MINI JAKARTA ####
    ####### MENU PEMGEMBALIAN BUKU #####
    ''')
    while True:
        bookIDReturn=input('Masukkan ID buku yang ingin dikembalikan: ')
        returnDateActual=datetime.date.today()
        found=False
        for a in range(0,len(bookData)):
            if bookIDReturn.upper()==bookData[a]['bookID']:
                returnerName=input('Masukkan nama Peminjam: ')
                returned.append({
                    'bookID':bookIDReturn,
                    'bookTitle':bookData[a]['bookTitle'],               
                    'bookQty':1,
                    'returner':returnerName.upper(),
                    'returnDateActual':returnDateActual,
                    })
                found=True
        if found is False:
            print(f'bookID yang diinput {bookIDReturn} tidak ditemukan')
        checker = input('Anda ingin mengembalikan buku lain (Y/T): ')
        if checker.upper()=='T':
            break
    
    while True:
        if found is True:
            print('\nDaftar Pengembalian Buku: ')
            print(tabulate(returned, headers = 'keys', tablefmt='psql'))
            print('Terima kasih atas pengembalian buku Anda')
            break
        else:
            break

    while True:
        try:
            for b in range(0,len(returned)):
                for c in range(0,len(bookData)):
                    if returned[b]['bookID']==bookData[c]['bookID']:
                        bookData[c]['bookStock']=1
                        bookData[c]['borrower']=''
                        bookData[c]['borrowDate']=''
                        bookData[c]['returnDate']=''
            returned.clear()
            break
        except ValueError:
            print('Input Anda salah')
            returned.clear()
    bookList()

#Function to delete a book
def deleteBook():
    bookList()
    bookDataMaster=bookData.copy()
    while True:
        try:
            print('''
            ##### PERPUSTAKAAN MINI JAKARTA ####
            ####### MENU PENGHAPUSAN BUKU ######
            ''')
            bookIndexDelete=int(input('Masukkan index buku yang ingin dihapus (paling kiri tabel): '))
            if bookIndexDelete in range(0,len(bookData)):
                del bookData[bookIndexDelete]
                bookList()
                print('\n\n Daftar buku master (tidak termasuk penghapusan): ')
                print(tabulate(bookDataMaster, headers='keys', tablefmt='psql', showindex=True))
                break
            else:
                print(f'BookIndex yang diinput {bookIndexDelete} tidak ditemukan')
        except ValueError:
            print('Input Anda salah')
            break

#Main Menu Function
def mainBook():
    while True:
        pilihanMenu = input('''
            ####### HALO SELAMAT DATANG DI ######
            ##### PERPUSTAKAAN MINI JAKARTA #####
            
            Daftar Menu:
            1. Menampilkan Daftar Buku
            2. Pencarian Buku
            3. Penambahan Buku
            4. Peminjaman Buku
            5. Pengembalian Buku
            6. Penghapusan Buku
            7. Exit Program
                            
            Masukkan angka Menu yang ingin dijalankan (1 s.d. 7):''')
        
        if pilihanMenu=='1':
            bookList()
        elif pilihanMenu=='2':
            searchBook()
        elif pilihanMenu=='3':
            addBook()
        elif pilihanMenu=='4':
            borrowBook()
        elif pilihanMenu=='5':
            returnBook()
        elif pilihanMenu=='6':
            deleteBook()
        elif pilihanMenu=='7':
            print('\nSampai jumpa lagi\n\nversion 1.0\nFernando Giade - 2024\nTerima kasih')
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak valid')
            break

#cek login dan password
for i, j in userDict.items():
    if userID.upper()==i:
        password=input('Masukkan password Anda (jika password salah, maka program akan exit) ')
        if password==j['password']:
            print(f'Selamat Datang {i}')   
            mainBook()    
        else:
            print('Password yang Anda masukkan tidak benar\nMohon jalankan program dan login kembali\n\nversion 1.0\nFernando Giade - 2024\nTerima kasih')
        break
    else:
        print('User ID yang Anda masukkan tidak benar\nMohon jalankan program dan login kembali\n\nversion 1.0\nFernando Giade - 2024\nTerima kasih')
    break