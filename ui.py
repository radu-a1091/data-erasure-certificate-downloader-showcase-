from tkinter import *
from tkinter import ttk
from tkinter import filedialog

save_path = None
folder_path_program = None
folder_path_driver = None
date_from = None

gui = Tk()
gui.geometry("600x200")
gui.title("Locations")
gui.columnconfigure(1,weight=1)

def get_folder_path_program():
    global folder_path_program
    folder_selected = filedialog.askdirectory()
    folder_path_program.set(folder_selected)
    
def get_folder_path_driver():
    folder_selected = filedialog.askdirectory()
    folder_path_driver.set(folder_selected)
    
def get_folder_path_save():
    global save_path
    folder_selected = filedialog.askdirectory()
    save_path.set(folder_selected)
    gui.quit()

def transfor_path(path):
    path_listed = path.split("/")
    location = ''
    try:
        for _ in path_listed:
            if _ != path_listed[-1]:
                location += str(_+"\\")
            else:
                location += str(_)
        return location
    except:
        print("Error in path")

def get_date():
    inp = input
    
folder_path_driver = StringVar()
folder_path_program = StringVar()
save_path = StringVar()

a = Label(gui ,text="Program's folder location:")
a.grid(row=0,column = 0)
e1 = Entry(gui,textvariable=folder_path_program,width=100)
e1.grid(row=0,column=1,padx=0,pady=0)
btnFind = ttk.Button(gui, text="Browse Folder",command=get_folder_path_program)
btnFind.grid(row=0,column=2,padx=0,pady=0)

b = Label(gui ,text="driver location:")
b.grid(row=1,column = 0)
e2 = Entry(gui,textvariable=folder_path_driver,width=100)
e2.grid(row=1,column=1,padx=0,pady=0)
btnFind = ttk.Button(gui, text="Browse Folder",command=get_folder_path_driver)
btnFind.grid(row=1,column=2,padx=0,pady=0)

d = Label(gui ,text="Date from (Format: mm/dd/yyy)")
d.grid(row=2,column = 0)
e4 = Entry(gui,textvariable=date_from,width=100)
e4.grid(row=2,column=1,padx=0,pady=0)

c = Label(gui ,text="PDF save location:")
c.grid(row=3,column = 0)
e3 = Entry(gui,textvariable=save_path,width=100)
e3.grid(row=3,column=1,padx=0,pady=0)
btnFind = ttk.Button(gui, text="Browse Folder",command=get_folder_path_save)
btnFind.grid(row=3,column=2,padx=0,pady=0)


gui.mainloop()

path1 = folder_path_program.get()
path2 = folder_path_driver.get()
path3 = save_path.get()
date_from = e4.get()


print(f"{path1}\n{path2}\n{path3}\n{date_from}")
pc_data_export_location = transfor_path(path1)
folder_location = f'{transfor_path(path1)}\\certif.csv'
driver_location = f'{transfor_path(path2)}\\chromedriver.exe'
save_location = f'{transfor_path(path3)}\\Erasure Certificate'