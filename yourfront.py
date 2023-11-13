from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import pandas as pd
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy




# to open a file
def open_file(main_window):
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
            Label(main_window, text="file upload sucess", foreground="green").grid(row=4, columnspan=3, pady=10)
        except ValueError:
            Label(main_window, text="file could not be opened", foreground="green").grid(row=4, columnspan=3, pady=10)
        except FileNotFoundError:\
            Label(main_window, text="file not found", foreground="green").grid(row=4, columnspan=3, pady=10)

    return new_df
# This is to save contact and send message

def script_python(new_df):
    main_window = Tk()
    main_window.geometry("1200x1200")
    main_window.configure(bg='#B0B0E2')
    style = ttk.Style()
    style.theme_use("clam")
    style = ttk.Style()
    style.configure("TButton", foreground="#000000", background="#F5F5F5")
    output = Text(main_window, height=25, width=50, bg="light cyan")
    output.grid()


    lst_save = []
    lst_message = []
    print(new_df)
    for index, row in new_df.iterrows():
        name = row["name"]
        number = row["number"]
        desired_cap1 = {
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "RZ8RC1F7A3W",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.samsung.android.dialer",
        "appium:appActivity": "com.samsung.android.dialer.DialtactsActivity",
        "appium:appWaitForLaunch": "false",
        "appium:noReset": "true"
        }
        driver1 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap1)
        driver1.implicitly_wait(10)
        el1 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.dialer:id/contactlist_tab_button")
        el1.click()
        driver1.implicitly_wait(10)
        element1 = driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create new contact")
        driver1.implicitly_wait(5)
        element1.click()
        driver1.implicitly_wait(5)
        element2 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/nameEdit")
        driver1.implicitly_wait(5)
        element2.send_keys(name)
        element3 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/edit_fields_container")
        driver1.implicitly_wait(5)
        element3.click()
        driver1.implicitly_wait(5)
    # element3.send_keys(number)
        element4 = driver1.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.EditText")
        driver1.implicitly_wait(5)
        element4.send_keys(number)
        driver1.implicitly_wait(5)
        element5 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/menu_done")
        element5.click()
        driver1.implicitly_wait(5)
        element6 = driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
        element6.click()

        print("saving of " + name + " completed")
        driver1.quit()
        output.insert(END, "saving of " + name + " is completed\n")
    for index, row in new_df.iterrows():
        name = row["name"]
        number = row["number"]
        message = row["message"]
        desired_cap2 = {
                "platformName": "Android",
                "appium:platformVersion": "13",
                "appium:deviceName": "RZ8RC1F7A3W",
                "appium:automationName": "UiAutomator2",
                "appium:appPackage": "com.whatsapp",
                "appium:appActivity":"com.whatsapp.HomeActivity",
                "appium:appWaitForLaunch": "false",
                "appium:noReset": "true"
            }
        driver2 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap2)
        driver2.implicitly_wait(5)
        el1 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WhatsApp")
        el1.click()
        driver2.implicitly_wait(5)
        el2 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="New chat")
        el2.click()
        driver2.implicitly_wait(5)
        el3 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el3.click()
        driver2.implicitly_wait(5)
        el5 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/search_src_text")
        el5.click()
        driver2.implicitly_wait(5)
        el5.send_keys(number)
        driver2.implicitly_wait(5)
        el6 = driver2.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView")
        el6.click()
        driver2.implicitly_wait(5)
        el7 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/entry")
        el7.click()
        driver2.implicitly_wait(5)
        el8 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/entry")
        el8.send_keys(message)
        driver2.implicitly_wait(5)
        el9 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send")
        el9.click()
        driver2.quit()
        output.insert(END, "message is sent to " + name + "\n")
        lst_save.append("saving of " + name + " is completed")
        lst_message.append("message is sent to " + name)

    new_df["status_save"] = lst_save
    new_df["status_message"] = lst_message
    print(new_df)
# this function is for saving the file after doing the process and a button to gome page
    def Home_redirect():
        main_window .destroy()
        main()

    save_home_frm = ttk.Frame(main_window, padding=(50, 50, 50, 50))
    save_home_frm.grid(row=1, column=1)
    save_button = ttk.Button(main_window, text="save", command=lambda: file_save(new_df))
    save_button.grid()

    Home_button = ttk.Button(main_window, text="Home", command=Home_redirect)
    Home_button.grid()


# this is used to save the file after completing the process
def file_save(new_df):
    filename = filedialog.asksaveasfilename(filetypes=[('Excel',('*.xls','*.xlsx','*.xlsm'))])

    new_df.to_excel(filename+".xlsx")

# to only save the contact
def saving(new_df):
    main_window = Tk()
    main_window.geometry("1200x1200")
    main_window.configure(bg='#B0B0E2')
    style = ttk.Style()
    style.theme_use("clam")
    style = ttk.Style()
    style.configure("TButton", foreground="#000000", background="#F5F5F5")
    output = Text(main_window, height=25, width=50, bg="light cyan")
    output.grid()
    lst_save = []
    print(new_df)
    for index, row in new_df.iterrows():
        name = row["name"]
        number = row["number"]
        desired_cap1 = {
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "RZ8RC1F7A3W",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.samsung.android.dialer",
        "appium:appActivity": "com.samsung.android.dialer.DialtactsActivity",
        "appium:appWaitForLaunch": "false",
        "appium:noReset": "true"
        }
        driver1 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap1)
        driver1.implicitly_wait(10)
        el1 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.dialer:id/contactlist_tab_button")
        el1.click()
        driver1.implicitly_wait(10)
        element1 = driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create new contact")
        driver1.implicitly_wait(5)
        element1.click()
        driver1.implicitly_wait(5)
        element2 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/nameEdit")
        driver1.implicitly_wait(5)
        element2.send_keys(name)
        element3 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/edit_fields_container")
        driver1.implicitly_wait(5)
        element3.click()
        driver1.implicitly_wait(5)
    # element3.send_keys(number)
        element4 = driver1.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.EditText")
        driver1.implicitly_wait(5)
        element4.send_keys(number)
        driver1.implicitly_wait(5)
        element5 = driver1.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/menu_done")
        element5.click()
        driver1.implicitly_wait(5)
        element6 = driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
        element6.click()
        output.insert(END, "saving of " + name + " is completed\n")
        lst_save.append("saving of " + name + " is completed")

    new_df["status_save"] = lst_save
    print(new_df)
# this is to save the file after procss completion and a home button option

    def Home_redirect():
        main_window.destroy()
        main()
    save_home_frm=ttk.Frame(main_window,padding=(50,50,50,50))
    save_home_frm.grid(row=1,column=1)
    save_button = ttk.Button(save_home_frm, text="save", command=lambda: file_save(new_df))
    save_button.grid()

    Home_button = ttk.Button(save_home_frm, text="Home", command=Home_redirect)
    Home_button.grid()
# function to save the file after completion of the process
def file_save(new_df):
    filename = filedialog.asksaveasfilename(filetypes=[('Excel', ('*.xls', '*.xlsx', '*.xlsm'))])
    new_df.to_excel(filename + ".xlsx")

# to send message on whatsapp
def what_message(new_def):
    main_window = Tk()
    main_window.geometry("1200x1200")
    main_window.configure(bg='#B0B0E2')
    style = ttk.Style()
    style.theme_use("clam")
    style = ttk.Style()
    style.configure("TButton", foreground="#000000", background="#F5F5F5")
    output = Text(main_window, height=25, width=50, bg="light cyan")
    output.grid()

    lst_save = []
    lst_message = []
    print(new_df)
    for index, row in new_df.iterrows():
        name = row["name"]
        number = row["number"]
        message = row["message"]
        desired_cap2 = {
                "platformName": "Android",
                "appium:platformVersion": "13",
                "appium:deviceName": "RZ8RC1F7A3W",
                "appium:automationName": "UiAutomator2",
                "appium:appPackage": "com.whatsapp",
                "appium:appActivity":"com.whatsapp.HomeActivity",
                "appium:appWaitForLaunch": "false",
                "appium:noReset": "true"
            }
        driver2 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap2)
        driver2.implicitly_wait(5)
        el1 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WhatsApp")
        el1.click()
        driver2.implicitly_wait(5)
        el2 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="New chat")
        el2.click()
        driver2.implicitly_wait(5)
        el3 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el3.click()
        driver2.implicitly_wait(5)
        el5 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/search_src_text")
        el5.click()
        driver2.implicitly_wait(5)
        el5.send_keys(number)
        driver2.implicitly_wait(5)
        el6 = driver2.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView")
        el6.click()
        driver2.implicitly_wait(5)
        el7 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/entry")
        el7.click()
        driver2.implicitly_wait(5)
        el8 = driver2.find_element(by=AppiumBy.ID, value="com.whatsapp:id/entry")
        el8.send_keys(message)
        driver2.implicitly_wait(5)
        el9 = driver2.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send")
        el9.click()
        driver2.quit()
        output.insert(END, "message is sent to " + name + "\n")
        lst_message.append("message is sent to " + name)
    new_df["status_message"] = lst_message
    print(new_df)
#to save the file after completion of process and a home page button
    def Home_redirect():
        main_window.destroy()
        main()
    Save_home_frm=ttk.Frame(main_window,padding=(50,50,50,50))
    Save_home_frm.grid( row=1,column=1)
    save_button = ttk.Button(Save_home_frm, text="save", command=lambda: file_save(new_df))
    save_button.grid()

    Home_button = ttk.Button(Save_home_frm, text="Home", command=Home_redirect)
    Home_button.grid()
#to save the file after completion of process
def file_save(new_df):
    filename = filedialog.asksaveasfilename(filetypes=[('Excel', ('*.xls', '*.xlsx', '*.xlsm'))])

    new_df.to_excel(filename + ".xlsx")
#here the main function starts
def main():
    main_window = Tk()
    main_window.geometry("1200x1200")
    main_window.configure(bg='#B0B0E2')
    style = ttk.Style()
    style.theme_use("clam")
    style = ttk.Style()
    style.configure("TButton", foreground="#000000", background="#F5F5F5")

# here we are giving the function on which we need to perform and the gui
    def flow_redirect(new_df):
        main_window.destroy()
        script_python(new_df)
        #saving(new_df)
        #message(new_df)
    def flow_saveing(new_df):
        main_window.destroy()
        saving(new_df)

    def flow_what(new_df):
        main_window.destroy()
        what_message(new_df)
# text part
    lable = Label(main_window, text="AUTOMATING", font=('bold', 52))
    lable.grid(row=1,column=1)
    lable = Label(main_window, text="saving the contact and sending messages on whatsapp by just one click",
                  font=('Helvetica', 17))
    lable.grid(row=2,column=1)

# to save contact and send message on whatsapp
    both_frame = ttk.Frame(main_window, padding=(50, 50, 50, 50))
    both_frame.configure(borderwidth=5)
    both_frame.grid()
    upload = ttk.Button(both_frame, text="UPLOAD", command=lambda: open_file(main_window))
    upload.grid()
    submit = ttk.Button(both_frame, text="SUBMIT", command=lambda: flow_redirect(new_df))
    submit.grid()
    box3 = Label(both_frame, text="Saving and sending message", font=('Arial_Black', 15))
    box3.grid()
# to send message on whatsapp
    what_frame = ttk.Frame(main_window, padding=(60, 60, 60, 60))
    what_frame.configure(borderwidth=5)
    what_frame.grid(row=4, column=1)
    upload = ttk.Button(what_frame, text="UPLOAD", command=lambda: open_file(main_window))
    upload.grid()
    submit = ttk.Button(what_frame, text="SUBMIT", command=lambda: flow_what(new_df))
    submit.grid()
    box1 = Label(what_frame, text="whatsapp message sending", font=('Arial_Black', 15))
    box1.grid()

#to save the contact
    save_frame = ttk.Frame(main_window, padding=(50, 50, 50, 50))
    save_frame.configure(borderwidth=5)
    save_frame.grid(row=5,column=2)
    upload = ttk.Button(save_frame, text="UPLOAD", command=lambda: open_file(main_window))
    upload.grid()
    submit = ttk.Button(save_frame, text="SUBMIT", command=lambda: flow_saveing(new_df))
    submit.grid()
    box2 = Label(save_frame, text="only saving of contacts", font=('Arial_Black', 15))
    box2.grid()


# login code starts here
def login():
    uname = username.get()
    passwd = password.get()

    if uname == '' or passwd == '':
        message.set("fill the empty field!!")
    else:

        if uname == "seema" and passwd== "singh":
            login_screen.destroy()
            main()
        else:
            message.set("wrong username or password!!")

def login_form():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("800x700")
    login_screen.configure(bg='#EEEEEE')
    style = ttk.Style()
    style.theme_use("clam")


    global username
    global password
    global message

    username = StringVar()
    password = StringVar()
    message = StringVar()
    # text label
    lable = Label(login_screen, text="AUTOMATING", font=('bold', 52))
    lable.grid(row=1, column=1)
    lable = Label(login_screen, text="saving the contact and sending messages on whatsapp by just one click",
                  font=('Roman', 17))
    lable.grid(row=2,column=1)
    lable =Label(login_screen,text="Please enter your details to start the process",font=('bold',15))
    lable.grid(row=5,column=1)
    # image part
   # img = PhotoImage(file="C:\Users\seema\Downloads\login.png")
    #label= Label(login_screen,image=img)
   # label.place(x=0,y=200)
    # for login details

    Label(login_screen ,text="USERNAME:",font=('bold',13)).place(x=400,y=250)

    Entry(login_screen ,textvariable=username).place(x=510,y=250)

    Label(login_screen , text="PASSWORD:",font=('bold',13)).place(x=400, y=300)

    Entry(login_screen , textvariable=password,show="*").place(x=510, y=300)

    Label(login_screen ,text="",textvariable=message).place(x=400,y=200)

    Button(login_screen ,text="Login",width=10,height=1,bg="orange",command=login).place(x=460,y=350)
    login_screen.mainloop()

login_form()