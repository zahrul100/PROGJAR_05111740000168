 **Laporan Tugas 10 :**
 
  <a href="https://github.com/zahrul100/PROGJAR_05111740000168/blob/master/Tugas%2010/LaporanTugas10.pdf"> Laporan Tugas 10 Zahrul 05111740000168</a> 
 <br>
 <br>

- Pull Update Terbaru
- Menjalankan async_server.py dengan port 9002, 9003, 9004, 9005 dengan menggunakan Terminal Linux :<br>
 
    ![gambar1](https://github.com/zahrul100/PROGJAR_05111740000168/blob/master/Tugas%2010/picture/2.png)
 - Menjalankan file lb.py dan menjalankan di port 44444: <br> dengan perintah  <br>
 `python3 lb.py`
    ![gambar2](https://github.com/zahrul100/PROGJAR_05111740000168/blob/master/Tugas%2010/picture/3.png)
 - Mengakses http://localhost:44444/page.html pada browser 
    ![gambar3](https://github.com/zahrul100/PROGJAR_05111740000168/blob/master/Tugas%2010/picture/4.png)
 - Mengecek dan melihat proses di log program bahwa setiap request akan dilayani oleh backend secara bergantian
 
    ![gambar3](https://github.com/zahrul100/PROGJAR_05111740000168/blob/master/Tugas%2010/picture/5.png)


 - Melakukan performance test seperti tugas 9, dan membandingkan penggunaan antara load balancer dengan async_server dengan server_thread_http pada folder progjar Tugas5 <br> Dengan parameter sebagai berikut : <br> Jumlah request 	:  1000 <br> Konkurensi	:  1,50, 100,500,1000 <br>
 
 <a href="https://github.com/zahrul100/PROGJAR_05111740000168/blob/master/Tugas%2010/LaporanTugas10.pdf"> Laporan Tugas 10 Zahrul 05111740000168</a> 
 
 Hasil SS performance test Asyncronus Server Dengan Load Balance
 
- ab -n 1000 -c 1 -r http://127.0.0.1:44444/
![alt text](picture/61.png)
- ab -n 1000 -c 10 -r http://127.0.0.1:44444/
![alt text](picture/610.png)
- ab -n 1000 -c 100 -r http://127.0.0.1:44444/
![alt text](picture/6100.png)
- ab -n 1000 -c 500 -r http://127.0.0.1:44444/
![alt text](picture/6500.png)

- ab -n 1000 -c 1000 -r http://127.0.0.1:44444/
![alt text](picture/61000.png)

 
   
 
   
   
