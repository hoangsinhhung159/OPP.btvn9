import time
tong_giay = time.time()
so_ngay = tong_giay // 86400
giay_con_lai = tong_giay % 86400
gio = giay_con_lai // 3600
phut = (giay_con_lai % 3600) // 60
giay = giay_con_lai % 60
print(int(so_ngay))
print(int(gio), "giờ", int(phut), "phút", int(giay), "giây")