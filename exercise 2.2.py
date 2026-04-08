import math
ban_kinh_hinh_cau = 5
the_tich_hinh_cau = (4/3) * math.pi * (ban_kinh_hinh_cau ** 3)
print("Thể tích hình cầu có bán kính", ban_kinh_hinh_cau, "là:", the_tich_hinh_cau)

gia_mot_cuon_sach = 24.95
gia_mot_cuon_sach_sau_khi_giam = 24.95 * 0.6
so_luong_sach = 60
tong_tien_sach = gia_mot_cuon_sach_sau_khi_giam * so_luong_sach
chi_phi_van_chuyen = 3 + (so_luong_sach - 1) * 0.75
Tong_chi_phi = tong_tien_sach + chi_phi_van_chuyen
print("Tổng chi phí mua sách và vận chuyển là:", Tong_chi_phi)

thoi_gian_bat_dau_chay = 6 * 60 + 52
thoi_gian_chay_thong_tha = (8 * 60 + 15) * 2
thoi_gian_chay_nhanh = (7 * 60 + 12) * 3
tong_thoi_gian_chay = thoi_gian_chay_thong_tha + thoi_gian_chay_nhanh
tong_phut_chay = tong_thoi_gian_chay / 60
phut_chay_ve = thoi_gian_bat_dau_chay + tong_phut_chay
gio_chay_ve = phut_chay_ve // 60
phut_chay_ve = phut_chay_ve % 60
print("Thời gian quay về là:", gio_chay_ve, "giờ", phut_chay_ve, "phút")