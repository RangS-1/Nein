<div align="center">
<a href="github.com/RangS-1/Nein">
<img src="icon.ico" alt="Nein Icon"/>
</a>

# Nein

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows 8+](https://img.shields.io/badge/Platform-Windows%2010+-red?logo=windows&logoColor=white)](https://github.com/RangS-1/RangSpreter)

</div>

**Nein** adalah text editor sederhana ala **nano** yang dirancang khusus untuk berjalan di **Windows** menggunakan terminal CMD (aku tak tahu apakah bisa di powershell). Aku yakin kalau kau sebagai developer semisal proyekmu selesai, kau menutup text editor mu lalu menjalankan proyekmu di terminal, tetapi ada yang perlu diubah sedikit dan kau akhirnya kembali membuka text editormu dan kembali menjalankannya di terminal. Pengalaman yang agak menyebalkan sebagai developer -_-.

> **Catatan penting**: Proyek ini masih dalam tahap pengembangan awal (**uncompleted**). Banyak fitur yang belum diimplementasikan dan kemungkinan besar masih banyak bug, Silakan kontribusi kalau ingin tambah fitur baru.

## Fitur

- Membuka file teks
- Menampilkan isi file
- Navigasi dasar menggunakan keyboard
- Tampilan ala nano (footer sederhana)

## Tujuan yang belum selesai

- Cari teks (`Ctrl+W`)
- Potong, copy, paste baris
- Undo sederhana
- Syntax highlighting

## Instalasi dan penggunaan 

```
> git clone https://github.com/RangS-1/Nein.git
> cd Nein
> python -m venv venv
> cd venv/Scripts
> activate
> cd ../..
> pip install -r requirements.txt
> python nein.py filename.txt

# kau bisa mulai Edit setelah dependencies terinstall
# disarankan menggunakan venv/virtual environment
```

## Kontribusi

Proyek ini sangat terbuka untuk kontribusi, terutama dalam aspek:
- Penambahan fitur
- UI yang lebih unik/menarik dibanding Nano

## Lisensi

This project is licensed under the [GPL-3.0](LICENSE) - see the [LICENSE](LICENSE) file for details.
