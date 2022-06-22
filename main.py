#MADE BY PHIKO


from tkinter import *
from tkinter import Label

from PIL import ImageTk
import os
import datetime
import mysql.connector

# variable text
winTitle = "(INSERT COMPANY NAME HERE) Checkind System"
window_state = 'zoomed'
checkin_text = "Checked in"
checkout_text = "Checked out"
ennf = "Employer number not found"
pcif = "Please check in first"
enic = "employer number is correct"
ptiyen = "Plase type in your Employer number"
ehnci = "Employer has not checked in"
ehaci = "Employer has already checked in"

# variable File
iconfile = "icon.ico"
backgroundfile = "picture.png"
picfoldet = "\pictures\\"

# Mysql
# Login
hostname = "remotemysql.com"
username = "INSERT YOUR DATABASE USERNAME HERE"
password = "INSERT YOUR DATABASE PASSWORD HERE"
dbname = "INSERT YOUR DATABASE NAME HERE"
# Check
login = "Login"

# Buttom config
buttom_width = 1.6
buttom_text_size = 20
buttom_front = "times"
buttom_emphasis = "bold"
buttom_color = "black"
buttom1_text = "Check in"
buttom2_text = "Exit"
buttom3_text = "Check out"

# Error label config
errorLabel_text_size = 20
errorLabel_front = ""
errorLabel_emphasis = "bold"
errorLabel_color = "black"

# inputspace config
inputspace_text_size = 20
inputspace_front = "times"
inputspace_emphasis = "bold"
inputspace_color = "black"

# Time config
# Time label
time_text = "Time"
time_text_size = 50
time_front = "arial"
time_emphasis = "italic"
time_color = "red"
timepositionx = 50
timepositiony = 100

# clock and date label
clda_size = 50
clda_front = "times"
clda_emphasis = "bold"
clda_color = "black"

########################################################################################################################
#                                                                                                                      #
# ██████╗░░█████╗░        ███╗░░██╗░█████╗░████████╗        ████████╗░█████╗░██╗░░░██╗░█████╗░██╗░░██╗                 #
# ██╔══██╗██╔══██╗        ████╗░██║██╔══██╗╚══██╔══╝        ╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██║░░██║                 #
# ██║░░██║██║░░██║        ██╔██╗██║██║░░██║░░░██║░░░        ░░░██║░░░██║░░██║██║░░░██║██║░░╚═╝███████║                 #
# ██║░░██║██║░░██║        ██║╚████║██║░░██║░░░██║░░░        ░░░██║░░░██║░░██║██║░░░██║██║░░██╗██╔══██║                 #
# ██████╔╝╚█████╔╝        ██║░╚███║╚█████╔╝░░░██║░░░        ░░░██║░░░╚█████╔╝╚██████╔╝╚█████╔╝██║░░██║                 #
# ╚═════╝░░╚════╝░        ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░        ░░░╚═╝░░░░╚════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝                 #
#                                                                                                                      #
# ░█████╗░███╗░░██╗██╗░░░██╗        ████████╗██╗░░██╗██╗███╗░░██╗░██████╗░                                             #
# ██╔══██╗████╗░██║╚██╗░██╔╝        ╚══██╔══╝██║░░██║██║████╗░██║██╔════╝░                                             #
# ███████║██╔██╗██║░╚████╔╝░        ░░░██║░░░███████║██║██╔██╗██║██║░░██╗░                                             #
# ██╔══██║██║╚████║░░╚██╔╝░░        ░░░██║░░░██╔══██║██║██║╚████║██║░░╚██╗                                             #
# ██║░░██║██║░╚███║░░░██║░░░        ░░░██║░░░██║░░██║██║██║░╚███║╚██████╔╝                                             #
# ╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░        ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░                                             #
#                                                                                                                      #
# ██╗░░░██╗███╗░░██╗██████╗░███████╗██████╗░        ██╗░░██╗███████╗██████╗░███████╗                                   #
# ██║░░░██║████╗░██║██╔══██╗██╔════╝██╔══██╗        ██║░░██║██╔════╝██╔══██╗██╔════╝                                   #
# ██║░░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝        ███████║█████╗░░██████╔╝█████╗░░                                   #
# ██║░░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗        ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░                                   #
# ╚██████╔╝██║░╚███║██████╔╝███████╗██║░░██║        ██║░░██║███████╗██║░░██║███████╗                                   #
# ░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝        ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝                                   #                                                                              #
#                                                                                                                      #
########################################################################################################################

# system variable
# Get running directory
dir_path = os.path.dirname(os.path.realpath(__file__))
checkinUpdateMysql = " checkin = %s WHERE EmployerNumber = %s"
updatetabelmysql = "UPDATE Employer SET"
window = Tk()
timeformat = "%d-%m-%Y %H:%M:%S/%p"

# Destroy window
def close():
    window.destroy()

# Mysql Function
def mysqlconnect(statement, input_space, time, date, checkin, errorlabel=Label):
    # Connect to mysql
    # connect to mysql Database
    mydb = mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        database=dbname
    )
    mycursor = mydb.cursor()
    # create table
    mycursor.execute(
        'CREATE TABLE IF NOT EXISTS Employer (EmployerNumber INT NOT NULL PRIMARY KEY, WorkTimeIn VARCHAR(255) NOT '
        'NULL, WorkDateIn VARCHAR(255) NOT NULL, WorkTimeOut VARCHAR(255) NOT NULL, WorkDateOut VARCHAR(255) NOT '
        'NULL, checkin VARCHAR(255))')
    if statement == "New user":
        mycursor.execute('SELECT checkin FROM Employer WHERE EmployerNumber = ?', (input_space,))
        EmployerNb1 = mycursor.fetchone()
        print(EmployerNb1)
        if input_space == EmployerNb1:
            errorlabel.config(text=enic)
        # insert data
        mycursor.execute(
            'INSERT INTO Employer (EmployerNumber, WorkTimeIn, WorkDatein, WorkDateOut, WorkDateout, checkin) VALUES (%s, %s, %s, %s)',
            (input_space, time, date, time, date, checkin))
    elif statement == login:
        mycursor.execute("SELECT checkin FROM Employer WHERE EmployerNumber = %s", (input_space,))
        checkincheck = mycursor.fetchone()
        # check if employer has checkin
        if input_space == "":
            errorlabel.config(text=ptiyen)
        else:
            if checkin:
                errorlabel.config(text=enic)
                if checkincheck == (0,):
                    # Update checkin
                    mycursor.execute(updatetabelmysql + checkinUpdateMysql, (checkin, input_space))
                    mycursor.execute(updatetabelmysql + " WorktimeIn = %s WHERE EmployerNumber = %s",
                                     (time, input_space))
                    mycursor.execute(updatetabelmysql + " WorkdateIn = %s WHERE EmployerNumber = %s",
                                     (date, input_space))
                    mydb.commit()
                    errorlabel.config(text=checkin_text)
                elif checkincheck == (1,):
                    errorlabel.config(text=ehaci)
                else:
                    errorlabel.config(text=ennf)
            elif not checkin:
                errorlabel.config(text=enic)
                if checkincheck == (0,):
                    errorlabel.config(text=ehnci)
                elif checkincheck == (1,):
                    # Update checkin
                    mycursor.execute(updatetabelmysql + checkinUpdateMysql, (checkin, input_space))
                    mycursor.execute(updatetabelmysql + " WorktimeOut = %s WHERE EmployerNumber = %s",
                                     (time, input_space))
                    mycursor.execute(updatetabelmysql + " WorkdateOut = %s WHERE EmployerNumber = %s",
                                     (date, input_space))
                    mydb.commit()
                    errorlabel.config(text=checkout_text)
                else:
                    errorlabel.config(text=ennf)
    mydb.close()


# Clock Function
def clock(time_label=Label, date_label=Label):
    date_time = datetime.datetime.now().strftime(timeformat)
    date, time1 = date_time.split()
    time2, time3 = time1.split('/')
    hour, minutes, seconds = time2.split(':')
    # Split Time
    if 12 < int(hour) < 24:
        time = str(int(hour)) + ':' + minutes + ':' + seconds
    else:
        time = time2
    time_label.config(text=time)
    date_label.config(text=date)
    time_label.after(1000, clock)
    first = False
    if not first:
        while True:
            date_time = datetime.datetime.now().strftime(timeformat)
            date, time1 = date_time.split()
            time2, time3 = time1.split('/')
            hour, minutes, seconds = time2.split(':')
            # Split Time
            if 12 < int(hour) < 24:
                time = str(int(hour)) + ':' + minutes + ':' + seconds
            else:
                time = time2
            time_label.config(text=time)
            date_label.config(text=date)
            time_label.update()
            date_label.update()


# GUI Function
def gui():
    # Create window
    window.title(winTitle)
    # Set icon
    # Set full dir path
    iconimg = dir_path + picfoldet + iconfile
    window.iconbitmap(iconimg)
    # Set window size
    # Set window to full screen
    window.state(window_state)
    # Disable resizing the GUI
    window.resizable(0, 0)
    # bgimg variable
    bgimg = ImageTk.PhotoImage(file=str(dir_path + picfoldet + backgroundfile))
    # Set picture in window
    my_canvas = Canvas(window, width=800, height=500)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(window.winfo_width() / 2, window.winfo_height() / 2 - 200, image=bgimg, anchor="center")
    # Create canvas text
    message = Label(window, font=(time_front, time_text_size, time_emphasis), text=time_text, fg=time_color)
    message.place(x=timepositionx, y=timepositiony)
    clock_label = Label(window, font=(clda_front, clda_size, clda_emphasis), fg=clda_color)
    clock_label.place(x=timepositionx, y=timepositiony * 2)
    date_label = Label(window, font=(clda_front, clda_size, clda_emphasis), fg=clda_color)
    date_label.place(x=timepositionx, y=timepositiony * 3)

    # Create input space
    input_space = Entry(window, font=(inputspace_front, inputspace_text_size, inputspace_emphasis), fg=inputspace_color)
    input_space.place(x=window.winfo_width() / 2.5, y=window.winfo_height() / 2)
    # Create button Check In
    button = Button(window, text=buttom1_text, font=(buttom_front, buttom_text_size, buttom_emphasis), fg=buttom_color,
                    command=lambda: mysqlconnect(login, input_space.get(), clock_label.cget("text"),
                                                 date_label.cget("text"), True, errorlabel))
    button.place(x=window.winfo_width() / 2.9, y=window.winfo_height() / buttom_width)
    # Create button Check Out
    button = Button(window, text=buttom3_text, font=(buttom_front, buttom_text_size, buttom_emphasis), fg=buttom_color,
                    command=lambda: mysqlconnect(login, input_space.get(), clock_label.cget("text"),
                                                 date_label.cget("text"), False, errorlabel))
    button.place(x=window.winfo_width() / 1.8, y=window.winfo_height() / buttom_width)
    # Create button Exit
    button = Button(window, text=buttom2_text, font=(buttom_front, buttom_text_size, buttom_emphasis), fg=buttom_color, command=close)
    button.place(x=window.winfo_width() / 2.2, y=window.winfo_height() / buttom_width)

    # Create Lablel
    errorlabel = Label(window, font=(errorLabel_front, errorLabel_text_size, errorLabel_emphasis), fg=errorLabel_color)
    errorlabel.place(x=window.winfo_width() / 2.6, y=window.winfo_width() / 2.6)

    # Loading timer function
    clock(clock_label, date_label)
    # Run GUI
    window.mainloop()


gui()
