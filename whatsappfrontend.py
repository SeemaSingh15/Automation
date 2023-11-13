from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd
from what import whatsapp
main_window = Tk()
main_window.geometry("1200x800")
main_window.configure(bg='#FAFAF0')
style = ttk.Style()
style.theme_use("clam")
#style=ttk.Style()
#style.configure("TButton", foreground="red", background="blue")
#list_themes = style.theme_names()
#current_theme = style.theme_use()




def open_file():
    global new_df
    filename = filedialog.askopenfilename(title="open a file", filetypes=[('CSV', '*.csv'), ('Excel', ('*.xls', '*.xlsx','*.xlsm'))])

    if filename:
        try:
            filename = r"{}".format(filename)
            if filename.endswith('.csv'):
                df = pd.read_csv(filename)
            else:
                df = pd.read_excel(filename)
            new_df = df
            label.config(text="file upload success")
        except ValueError:
            print("file could not be opened")
        except FileNotFoundError:
            print("file not found")
        except:
            print("something is wrong with the file")

        return new_df


def script_python(new_def):
    whatsapp(new_def)

lable = Label(main_window ,  text= "AUTOMATING",font=('bold',52) )
lable.pack()
lable= Label(main_window , text= " sending messages on whatsapp by just one click", font=('Roman',17))
lable.pack()
frm = ttk.Frame(main_window, padding=40)
frm.pack()
upload_button = ttk.Button(main_window, text="UPLOAD", command=open_file)
upload_button.pack(side=LEFT,padx=0,pady=0)
submit_button = ttk.Button(main_window, text="SUBMIT", command=lambda: script_python(new_df))
submit_button.pack()
label = Label(main_window, text="")
label.pack()


main_window.mainloop()