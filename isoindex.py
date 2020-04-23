import tkinter as tk
from tkinter.ttk import Combobox  
from tkinter import messagebox
from tkinter import filedialog as fd
import xlwt
import xlrd
import time

def get_changes(sheetmas):
	for val1 in sheetmas[0]:
		for val2 in sheetmas[1]:
			for val3 in sheetmas[2]:
				val3 = int(val3)
				for val4 in sheetmas[3]:
					for val5 in sheetmas[4]:
						for val6 in sheetmas[5]:
							for val7 in sheetmas[6]:
								if val2 == 'N':
									val8='050'
									for val9 in sheetmas[8]:
										val9 = int(val9)
										for val10 in sheetmas[9]:
											val10 = int(val10)
											vals = [str(val1), str(val2), str(val3), str(val4), str(val5), str(val6), str(val7), str(val8), str(val9), str(val10)]
											#yield ''.join(vals)
											yield vals
								else:
									for val8 in sheetmas[7]:
										for val9 in sheetmas[8]:
											val9 = int(val9)
											for val10 in sheetmas[9]:
												val10 = int(val10)

												vals = [str(val1), str(val2), str(val3), str(val4), str(val5), str(val6), str(val7), str(val8), str(val9), str(val10)]
												#yield ''.join(vals)
												yield vals

def getfile():
	global workbook
	filepath = fd.askopenfilename(filetypes=( ("EXCEL files", "*.xls;*.xlsx"),
											  ("All files", "*.*")))
	while not(filepath): 
		messagebox.showerror("Ошибка", "Укажите файл для закодирования")
		filepath = fd.askopenfilename()

	workbook = xlrd.open_workbook(str(filepath))
	print(workbook.nsheets)
	lbl.configure(text= 'Вы выбрали: '+str(filepath))
	openbutton.configure(text='Создать базу артикулов', command=createbase)

def createbase():
	starttime=time.time()
	newworkbook = xlwt.Workbook()
	worksheet = newworkbook.add_sheet('A Sheet',  cell_overwrite_ok=True)
	sheetmas = []
	for sheetindex in range(workbook.nsheets):
		sheet = workbook.sheet_by_index(sheetindex)
		coldata = sheet.col_values(0)
		sheetmas.append(coldata)
	
	
	row = 0
	col = 1
	for data in get_changes(sheetmas):
		worksheet.write(row, 0, row+1)
		for val in data:
			worksheet.write(row, col, val)
			col += 1
		worksheet.write(row, col, ''.join(data))
		col = 1
		row+=1
	print('\a')

	newworkbook.save('base_{}.xls'.format(time.strftime('%H-%M %d_%b_%G')))

	worktime.configure(text=f"Время генерации: {round(time.time()-starttime, 2)} сек")
	worktime.place(x=100, y=120)
	lengthlabel.configure(text=f"Строк в файле: {row}")
	lengthlabel.place(x=100, y=150)



root = tk.Tk()
root.title("ISOTERM GENERATOR")
root.geometry('500x500+0+0')


lbl = tk.Label(root, text="Выбор файла параметров для закодирования артикулов")
lbl.place(x=40, y=30)

worktime = tk.Label(root, text="Время работы: ")
lengthlabel = tk.Label(root, text="Строк в файле: ")
# combo = Combobox(root)  
# combo['values'] = (1, 2, 3, 4, 5, "Текст")  
# combo.current(0)  # установите вариант по умолчанию  
# combo.grid(column=0, row=1) 

openbutton = tk.Button(root, text='открыть', command=getfile)
openbutton.place(x=50, y=70)

root.mainloop()



