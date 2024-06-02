import random
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime

data_list = []

def sistem_pemesanan_hotel():
    root = Tk()
    root.geometry("1700x800")
    root.title("Reservasi Hotel Anafesa")
    root.configure(bg="#DEB887")
    root.attributes('-fullscreen', True)

    nomor_pemesanan = StringVar()
    nama_tamu = StringVar()
    waktu_sekarang_var = StringVar()
    tipe_kamar = StringVar()
    harga_kamar = StringVar()
    pajak = StringVar()
    total_biaya = StringVar()
    lama_tinggal = IntVar(value="")
    check_in_var = StringVar()
    check_out_var = StringVar()

    harga_kamar_dict = {
        "Kamar Tipe 1": 120000,
        "Kamar Tipe 2": 230000,
        "Kamar Tipe 3": 310000,
        "Kamar Tipe 4": 420000,
        "Kamar Tipe 5": 580000
    }

    def hitung_total():
        nomor_pemesanan_val = nomor_pemesanan.get()
        nama_tamu_val = nama_tamu.get()
        waktu_pemesanan_val = time.strftime("%Y-%m-%d %H:%M:%S")
        tipe_kamar_val = tipe_kamar.get()
        harga_kamar_val = harga_kamar_dict.get(tipe_kamar_val, 0)

        pajak_val = harga_kamar_val * 0.1
        total_biaya_val = (harga_kamar_val + pajak_val) * lama_tinggal.get()


        harga_kamar.set(harga_kamar_val * lama_tinggal.get())
        pajak.set(pajak_val * lama_tinggal.get())
        total_biaya.set(total_biaya_val)

    def reset():
        nomor_pemesanan.set("")
        nama_tamu.set("")
        tipe_kamar.set("")
        harga_kamar.set("")
        pajak.set("")
        total_biaya.set("")
        lama_tinggal.set("")
        check_in_var.set("")
        check_out_var.set("")  
        waktu_sekarang_var.set("")

    def keluar_dari_sistem():
        root.destroy()

    def buka_halaman_paket():
        halaman_paket = Toplevel(root)
        halaman_paket.geometry("450x500")
        halaman_paket.title("Paket Kamar")
        
        halaman_paket.configure(bg="#8B4513")

        label_paket = Label(halaman_paket, text="😃 Pilih Tipe Kamar 😃", font=('Calibri', 16, 'bold'), bg="#D2B48C")
        label_paket.pack(pady=10)

        def pilih_paket(tipe_kamar_paket):
            tipe_kamar.set(tipe_kamar_paket)
            halaman_paket.destroy()

        info_paket = {
            "Kamar Tipe 1": "--> Single Bed, 1 AC, 1 Kamar Mandi <--",
            "Kamar Tipe 2": "-->Double Bed, 2 AC, 1 Kamar Mandi<--",
            "Kamar Tipe 3": "-->King Bed, 1 AC, 2 Kamar Mandi<--",
            "Kamar Tipe 4": "-->Suite, 2 AC, 2 Kamar Mandi<--",
            "Kamar Tipe 5": "-->VIP Suite, King Bed, 3 AC, 2 Kamar Mandi, 1 Dapur Pribadi<--"
        }

        for tipe_kamar_paket, info_kamar in info_paket.items():
            tombol_paket = Button(halaman_paket, text=tipe_kamar_paket, font=('Calibri', 14), command=lambda t=tipe_kamar_paket: pilih_paket(t), bg="#D3D3D3")
            tombol_paket.pack(pady=5)
            info_kamar_label = Label(halaman_paket, text=info_kamar, font=('Calibri', 12), anchor=W, justify=LEFT, bg="#DEB887")
            info_kamar_label.pack(pady=5)
    
    def buka_jendela_nota():
        item_terpilih = tree_view.selection()
        if not item_terpilih:
            messagebox.showinfo("Error606", "Anda belum memilih pemesanan mana yang ingin dicetak nota!")
            return

        nilai_terpilih = tree_view.item(item_terpilih, 'values')
        nomor_pemesanan_val = nilai_terpilih[0]
        nama_tamu_val = nilai_terpilih[1]
        waktu_val = nilai_terpilih[2]
        check_in_val = nilai_terpilih[3]
        check_out_val = nilai_terpilih[4]
        tipe_kamar_val = nilai_terpilih[5]
        harga_val = nilai_terpilih[7]
        pajak_val = nilai_terpilih[8]
        total_val = nilai_terpilih[9]
        lama_tinggal_val = nilai_terpilih[6]

        jendela_nota = Toplevel(root)
        kiri = Frame(root, width=100, height=100, bg="#DEB887")
        kiri.pack(side=LEFT)

        kanan = Frame(root, width=300, height=400, bg="#DEB887")
        kanan.pack(side=RIGHT)
        jendela_nota.title("Nota Pembayaran")

        label_header = Label(jendela_nota, text=">>>RESERVASI HOTEL ANAFESA<<<", font=('Calibri', 18, 'bold'), fg='black', bg='#D3D3D3')
        label_header.pack(pady=10)

        Label(jendela_nota, text=f"Booking No: {nomor_pemesanan_val}").pack()
        Label(jendela_nota, text=f"Nama Pemesan: {nama_tamu_val}").pack()
        Label(jendela_nota, text=f"Tanggal & Waktu Pemesanan: {waktu_val}").pack()
        Label(jendela_nota, text=f"Tanggal Check In: {check_in_val}").pack()
        Label(jendela_nota, text=f"Tanggal Check Out: {check_out_val}").pack()
        Label(jendela_nota, text=f"Tipe Kamar: {tipe_kamar_val}").pack()
        Label(jendela_nota, text=f"Lama Tinggal: {lama_tinggal_val} Hari").pack()
        Label(jendela_nota, text=f"Harga: Rp. {harga_val}").pack()
        Label(jendela_nota, text=f"Pajak 10%: Rp. {pajak_val}").pack()
        separator = Label(jendela_nota, text="-" * 60)
        separator.pack()
        Label(jendela_nota, text=f"Total Biaya:                Rp. {total_val}", bg='#D3D3D3').pack()
        separator = Label(jendela_nota, text="-" * 60)
        separator.pack()
        Label(jendela_nota, text=f"Kami Tidak Pernah Mengabaikan Tamu Meski", fg='#D4A328', font=('Calibri', 12, 'bold italic')).pack()
        Label(jendela_nota, text=f"Permintaannya Aneh-Aneh!", fg='#D4A328', font=('Calibri', 12, 'bold italic')).pack()

    frame_atas = Frame(root, bg="#DEB887", width=800, height=50)
    frame_atas.pack(side=TOP)

    frame_kiri = Frame(root, width=400, height=600, bg="#DEB887")
    frame_kiri.pack(side=TOP)

    frame_tree = Frame(root, width=400, height=600, bg="#DEB887")
    frame_tree.pack(side=TOP)

    def LihatData():
        tree_view.delete(*tree_view.get_children())
        for data in data_list:
            tree_view.insert('', 'end', values=data)

    style = ttk.Style()
    style.configure("Treeview.Heading",
                background="#6B4C35",  
                foreground="black")  

    style.configure("Treeview",
                background="white",  
                foreground="black",  
                rowheight=40,
                fieldbackground="#6B4C35")  

    style.map('Treeview',
          background=[('selected', '#6B4C35')])


    tree_view = ttk.Treeview(frame_tree, style="Treeview")
    tree_view['columns'] = ("nomor_pemesanan", "nama_tamu", "waktu", "check_in", "check_out", "tipe_kamar", "lama_tinggal", "harga", "pajak", "total")

    scrollbar_vertikal = ttk.Scrollbar(frame_tree, orient="vertical")
    scrollbar_vertikal.configure(command=tree_view.yview)
    tree_view.configure(yscrollcommand=scrollbar_vertikal.set)
    scrollbar_vertikal.pack(fill=Y, side=RIGHT)

    tree_view.column("#0", width=0, minwidth=0)
    tree_view.column("nomor_pemesanan", anchor=CENTER, width=80, minwidth=25)
    tree_view.column("waktu", anchor=CENTER, width=130, minwidth=25)
    tree_view.column("lama_tinggal", anchor=CENTER, width=80, minwidth=25)
    tree_view.column("check_in", anchor=CENTER, width=110, minwidth=25)
    tree_view.column("check_out", anchor=CENTER, width=110, minwidth=25)
    tree_view.column("tipe_kamar", anchor=CENTER, width=110, minwidth=25)
    tree_view.column("harga", anchor=CENTER, width=100, minwidth=25)
    tree_view.column("pajak", anchor=CENTER, width=100, minwidth=25)
    tree_view.column("total", anchor=CENTER, width=100, minwidth=25)

    tree_view.heading("nomor_pemesanan", text="Nomor Pemesanan", anchor=CENTER)
    tree_view.heading("nama_tamu", text="Nama Pemesan", anchor=CENTER)
    tree_view.heading("waktu", text="Tanggal & Waktu", anchor=CENTER)
    tree_view.heading("check_in", text="Tanggal Check In", anchor=CENTER)
    tree_view.heading("check_out", text="Tanggal Check Out", anchor=CENTER)  
    tree_view.heading("tipe_kamar", text="Tipe Kamar", anchor=CENTER)
    tree_view.heading("lama_tinggal", text="Lama Tinggal", anchor=CENTER)
    tree_view.heading("harga", text="Harga", anchor=CENTER)
    tree_view.heading("pajak", text="Pajak", anchor=CENTER)
    tree_view.heading("total", text="Total Biaya", anchor=CENTER)

    tree_view.pack()
    LihatData();

    def validasi_tanggal(tanggal_str):
        try:
            datetime.datetime.strptime(tanggal_str,  '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def tambah_pemesanan():
        nomor_pemesanan_val = nomor_pemesanan.get()
        nama_tamu_val = nama_tamu.get()
        waktu_pemesanan_val = time.strftime("%Y-%m-%d %H:%M:%S")
        tipe_kamar_val = tipe_kamar.get()
        harga_kamar_val = float(harga_kamar.get())
        pajak_val = float(pajak.get())
        total_biaya_val = float(total_biaya.get())
        lama_tinggal_val = lama_tinggal.get()
        check_in_val = check_in_var.get()
        check_out_val = check_out_var.get() 

        pesanan_ada = [data[0] for data in data_list]
       
        if (
            nomor_pemesanan_val == ""
            or nama_tamu_val == ""
            or waktu_pemesanan_val == ""
            or tipe_kamar_val == ""
            or harga_kamar_val == ""
            or pajak_val == ""
            or total_biaya_val == ""
            or lama_tinggal_val == ""
            or check_in_val == ""
            or check_out_val == ""
        ):
            messagebox.showinfo("Peringatan", "Tolong isi seluruh data terlebih dahulu!!!")
        elif nomor_pemesanan_val in pesanan_ada:
            messagebox.showinfo("Peringatan", f"Nomer Order {nomor_pemesanan_val} telah digunakan!")
        elif not validasi_tanggal(check_in_val):
            messagebox.showinfo("Peringatan", "Format tanggal Check In tidak valid. Harap masukkan waktu dalam format DD/MM/YYYY dengan data tanggal yang benar.")
        elif not validasi_tanggal(check_out_val):
            messagebox.showinfo("Peringatan", "Format tanggal Check Out tidak valid. Harap masukkan waktu dalam format DD/MM/YYYY dengan data tanggal yang benar.")
        elif int(lama_tinggal_val) < 1:
            messagebox.showinfo("Peringatan", "Lama tinggal harus lebih besar dari atau sama dengan 1.")
        else:
            tree_view.delete(*tree_view.get_children())
            data_list.append((nomor_pemesanan_val, nama_tamu_val, waktu_pemesanan_val, check_in_val, check_out_val, tipe_kamar_val, lama_tinggal_val, harga_kamar_val, pajak_val, total_biaya_val))
            LihatData()
            
    localtime = time.asctime(time.localtime(time.time()))

    main_lbl = Label(frame_atas, font=('Helvetica', 25, 'bold'), text="HOTEL ANAFESA", fg="#964B00", anchor=W, bg="#DEB887")
    main_lbl.grid(row=0, column=0)
    main_lbl = Label(frame_atas, font=('Helvetica', 12, 'bold'), text=localtime, fg="white", anchor=W, bg="#DEB887")
    main_lbl.grid(row=1, column=0)

    path_gambar = "C:/Users/Rafly/Desktop/anafesa.jpg"
    gambar = Image.open(path_gambar)
    ukuran_baru = (1400, 120)
    gambar_terubah = gambar.resize(ukuran_baru)
    photo = ImageTk.PhotoImage(gambar_terubah)
    label = Label(frame_atas, image=photo)
    label.grid(row=2, column=0)

        
    nomer_pesan_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Booking No.", fg="black", bd=3, anchor=W, bg="#DEB887").grid(row=1, column=0, sticky='e')
    nomer_pesan_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=nomor_pemesanan,width=30).grid(row=1, column=1,pady=(7,7))

    nama_pemesan_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Nama Lengkap", bd=3, anchor=W, bg="#DEB887").grid(   row=2, column=0, sticky='e')
    nama_pemesan_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=nama_tamu, width=30).grid(row=2, column=1)
    tipe_kamar_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Tipe Kamar", bd=3, anchor=W, bg="#DEB887").grid(row=3, column=0, sticky='e')
    tipe_kamar_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=tipe_kamar, width=30).grid(row=3, column=1)

    check_in_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Tanggal Check In", bd=3, anchor=W, bg="#DEB887").grid(row=4, column=0, sticky='e')
    check_in_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=check_in_var, width=30).grid(row=4, column=1)

    check_out_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Tanggal Check Out", bd=3, anchor=W, bg="#DEB887").grid(row=5, column=0, sticky='e')
    check_out_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=check_out_var, width=30).grid(row=5, column=1,pady=(7,7))

    duration_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Lama Tinggal", bd=3, anchor=W, bg="#DEB887").grid(row=6, column=0, sticky='e')
    duration_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=lama_tinggal, width=30).grid(row=6, column=1)

    harga_kamar_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Harga", bd=3, anchor=W, bg="#DEB887").grid(row=7, column=0, sticky='e')
    harga_kamar_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=harga_kamar, width=30).grid(row=7, column=1,pady=(7,0))

    pajak_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Pajak", bd=3, anchor=W, bg="#DEB887").grid(row=8, column=0, sticky='e')
    pajak_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=pajak, width=30).grid(row=8, column=1)

    total_lbl = Label(frame_kiri, font=('Calibri', 16, 'bold'), text="Total Harga", bd=3, anchor=W, bg="#DEB887").grid(row=9, column=0, sticky='e')
    total_txt = Entry(frame_kiri, font=('Times New Roman', 16, 'bold'), bd=6, insertwidth=4, justify='left', textvariable=total_biaya, width=30).grid(row=9, column=1)


    total_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Total", bg="#91672C", fg="black", bd=3, relief="ridge", padx=6, pady=6, width=12, command=hitung_total, overrelief="solid", highlightthickness=1, highlightbackground="black").grid(row=3, column=3)

    reset_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Hapus", bg="#91672C", fg="black", relief="ridge", bd=3, padx=6, pady=6, width=12, command=reset,  overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B").grid(row=9, column=2)

    exit_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Keluar", bg="#91672C", fg="black", relief="ridge", overrelief="solid", bd=3, padx=6, pady=6, width=12, command=keluar_dari_sistem, highlightthickness=1, highlightbackground="#FFD39B").grid(row=9, column=3)
    
    add_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Add Booking", bg="#91672C", fg="black", relief="ridge", overrelief="solid", bd=3, padx=6, pady=6, width=12, command=tambah_pemesanan, highlightthickness=1, highlightbackground="#FFD39B").grid(row=8, column=2)

    package_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Paket Kamar", bg="#91672C", fg="black", relief="ridge", overrelief="solid", bd=3, padx=6, pady=6, width=12, command=buka_halaman_paket, highlightthickness=1, highlightbackground="#FFD39B").grid(row=3, column=2)

    cek_nota_btn = Button(frame_kiri, font=('Calibri', 16, 'bold'), text="Cek Nota", bg="#91672C", fg="black", bd=3, relief="ridge", padx=6, pady=6, width=12, command=buka_jendela_nota, overrelief="solid", highlightthickness=1, highlightbackground="#FFD39B").grid(row=8, column=3)
    root.mainloop()

sistem_pemesanan_hotel()
