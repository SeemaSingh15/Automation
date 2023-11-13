from tkinter import *
from tkinter import ttk,filedialog
import pandas as pd



def open_file(main_window):
    global new_df
    filename = filedialog.askopenfilename(title="open a file",filetypes=[('Excel',('*.xls','*.xlsx','*.xlsm'))])

    if filename:
        try:
            filename = r"{}".format(filename)
            if filename.endswith('.csv'):
                df = pd.read_csv(filename)
            else:
                df = pd.read_excel(filename)
            new_df = df
            Label(main_window,text="file upload sucess",foreground="green").grid(row=4,columnspan=3,pady=10)
        except ValueError:
            Label(main_window,text="file could not be opened",foreground="green").grid(row=4,columnspan=3,pady=10)
        except FileNotFoundError:
            Label(main_window,text="file not found",foreground="green").grid(row=4,columnspan=3,pady=10)

    return new_df

def script_python(new_df):
    # create an instance of tkinter frame
    win = Tk()
    # set the window size
    win.geometry("800x400")
    # create style widget
    style = ttk.Style()
    style.theme_use("clam")
    output = Text(win, height=25, width=50, bg="light cyan")
    output.grid()

    lst_save = []
    lst_message = []
    print(new_df)

    for index,row in new_df.iterrows():
        name = row["name"]
        number = row["number"]
        message = row["message"]

        #Appium code is here

        output.insert(END,"saving of "+name+" is completed\n")

        #message code is here

        output.insert(END,"message is sent to "+ name+"\n")

        lst_save.append("saving of "+name+" is completed")
        lst_message.append("message is sent to "+ name)

    new_df["status_save"] = lst_save
    new_df["status_message"] = lst_message

    print(new_df)

    def Home_redirect():
        win.destroy()
        main()

    save_button = ttk.Button(win,text="save",command=lambda :file_save(new_df))
    save_button.grid()

    Home_button = ttk.Button(win,text="Home",command=Home_redirect)
    Home_button.grid()


def file_save(new_df):
    fname = filedialog.asksaveasfilename(filetypes=[('Excel',('*.xls','*.xlsx','*.xlsm'))])

    new_df.to_excel(fname+".xlsx")

def main():
    # create an instance of tkinter frame
    win = Tk()
    # set the window size
    win.geometry("800x400")
    # create style widget
    style = ttk.Style()
    style.theme_use("clam")

    def flow_redirect(new_df):
        win.destroy()
        script_python(new_df)


    #create button
    upload_button= ttk.Button(win,text="UPLOAD",command=lambda:open_file(win))
    upload_button.grid()

    #submit button
    submit_button = ttk.Button(win,text="SUBMIT",command=lambda:flow_redirect(new_df))
    submit_button.grid()


def login():
    uname = username.get()
    passwd = password.get()

    if uname == '' or passwd == '':
        message.set("fill the empty field!!")
    else:

        if uname == "admin" and passwd== "admin":
            login_screen.destroy()
            main()
        else:
            message.set("wrong username or password!!")

def login_form():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("350x250")
    global username
    global password
    global message

    username = StringVar()
    password = StringVar()
    message = StringVar()

    Label(login_screen,width="300",text="please enter your details",bg="orange",fg="white").grid()

    Label(login_screen,text="username").place(x=20,y=40)

    Entry(login_screen,textvariable=username).place(x=90,y=42)

    Label(login_screen, text="password").place(x=20, y=80)

    Entry(login_screen, textvariable=password,show="*").place(x=90, y=82)

    Label(login_screen,text="",textvariable=message).place(x=95,y=100)

    Button(login_screen,text="Login",width=10,height=1,bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()

login_form()

what_frame = ttk.Frame(main_window, padding=(60, 60, 60, 60))
what_frame.configure(borderwidth=5)
what_frame.grid(row=4, column=1)
upload = ttk.Button(what_frame, text="UPLOAD", command=lambda: open_file(main_window))
upload.grid()
submit = ttk.Button(what_frame, text="SUBMIT", command=lambda: flow_what(new_df))
submit.grid()
box1 = Label(what_frame, text="whatsapp message sending", font=('Arial_Black', 15))
box1.grid()





