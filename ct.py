from tkinter import *
import tkinter as tk
# Tạo cửa sổ
top = tk.Tk()
top.title('Giải Bất Phương Trình')
top.geometry("800x400")
top.attributes('-topmost',True ) #Lệnh luôn hiển thị trên mọi cửa sổ
top['bg']= '#ffb6c1'

#tạo hàm giải phương trình
def giaiphuongtrinh():
	try:
		#khi các số được nhập vào thành công và chuyển từ String sang Float
		a= float(entrya.get())
		b= float(entryb.get())
		c= float(entryc.get())
		if a!=0:
			denta=b*b-4*a*c
			if denta>=0:
				x1=(-b+denta**(1/2))/(2*a)
				x2=(-b-denta**(1/2))/(2*a)
				textkp = 'Nghiệm là: '+ str(x1) + ' và ' + str(x2)
			else:
				x1=(complex((-b)/(2*a),((-denta)**(1/2))/(2*a)))
				x2=(complex((-b)/(2*a),(-(-denta)**(1/2))/(2*a)))
				textkp = 'Nghiệm là: '+ str(x1) + ' và ' + str(x2)
		else:
			if (b==0) and (c!=0):
				textkp = 'Vô nghiệm'
			if (b==0) and (c==0):
				textkp='Lập nghiệm là: R'
			if (b!=0):
				textkp='Nghiệm của phương trình là: '+str(-c/b)
	except:
		#Khi các số nhập vào bị lỗi thì xưa ra lời cảnh báo
		textkp="Vui lòng nhập đầy đủ không có khoảng trống và ký tự đặc biệt"
	text.set(textkp) #Thay đổi text của label Kết quả
	

name = Label(top, text = 'Giải Bất Phương Trình Bậc 2', font=('Time New Romans',20), fg='black',bg='#ffb6c1')
name.place(x = 220, y = 20)
# label của a
a = Label(top, text = 'Nhập hệ số a :', font=('Time New Romans',10),bg='#ffb6c1')
a.place(x = 10, y = 80)
# label của b
b = Label(top, text = 'Nhập hệ số b :', font=('Time New Romans',10),bg='#ffb6c1')
b.place(x = 10, y = 130)
# label của c
c = Label(top, text = 'Nhập hệ số c :', font=('Time New Romans',10),bg='#ffb6c1')
c.place(x = 10, y = 180)
# Tạo entry
# entry của a
entrya = Entry(top, width ='20', font=('Time New Roman',10),fg='black',bg='#ffb6c1')
entrya.place(x = 100, y = 80)
# entry của b
entryb = Entry(top, width ='20', font=('Time New Roman',10),fg='black',bg='#ffb6c1')
entryb.place(x = 100, y = 130)
# entry của c
entryc = Entry(top, width ='20', font=('Time New Roman',10),fg='black',bg='#ffb6c1')
entryc.place(x = 100, y = 180)
# button xac nhan
but = Button(top, text='Giải phương trình',bg='#ffb6c1',command = giaiphuongtrinh) #thuộc tính comand dùng để gọi hàm
but.place(x= 120, y= 210, width='120', height='20' )

#khởi tạo text cho label Kết quả
text = tk.StringVar()
text.set("") #Đặt text tành rỗng
#Khởi tạo Label kết quả với biến text
kp = Label(top, textvariable=text, font=('Time New Romans',10),bg='#ffb6c1')
kp.place(x = 10, y = 230)
top.mainloop()


