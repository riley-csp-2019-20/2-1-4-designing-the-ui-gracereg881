##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk


def test_my_button():
    frame_auth.tkraise()
    #TODO: Use get method of ent_password when the button is pressed, and store result
    password = ent_password.get()
    #TODO: Configure the label in frame_auth to display the password
    lbl_display_pass.config(text = password)

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.title("Authentication")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row = 0, column = 0, sticky = "news")

# label for username
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(padx=120)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

#label for password
lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

#creating button
btn_login = tk.Button(frame_login, text = 'Login', command = test_my_button)
btn_login.pack()

# create 2nd frame
frame_auth = tk.Frame(root)
frame_auth.grid(row = 0, column = 0, sticky = "news")
frame_login.tkraise(frame_auth)

#TODO: Add a label to frame_auth
lbl_display_pass = tk.Label(frame_auth)
lbl_display_pass.pack()


root.mainloop()