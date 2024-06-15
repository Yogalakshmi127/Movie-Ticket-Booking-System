from tkinter import *
import tkinter.messagebox
from tkinter import ttk

root = Tk()
name = StringVar()
passwo = StringVar()
mobileno = StringVar()

def register():
    fname = 'storeddetails.txt'
    if name.get() and passwo.get() and mobileno.get():
        if len(mobileno.get()) == 10 and mobileno.get().isdigit() and mobileno.get()[0] in '6789':
            with open(fname, 'a') as f:
                f.write(f'{name.get()},{passwo.get()},{mobileno.get()}\n')
                tkinter.messagebox.showinfo('Login Successful', 'You have successfully Logged In to your Account')
                root.destroy()
                open_bookingdetails()
        else:
            tkinter.messagebox.showinfo('Input Error', 'Mobile number must be exactly 10 digits , numeric and start with 6, 7, 8, or 9')
    else:
        tkinter.messagebox.showinfo('Input Error', 'Fill all the columns')

def open_bookingdetails():
    global movie_name, movie_timing
    booking_window = Tk()
    booking_window.title('Movie Booking')
    screen_width = booking_window.winfo_screenwidth()
    screen_height = booking_window.winfo_screenheight()
    booking_window.geometry(f'{screen_width}x{screen_height}')
    booking_window.config(bg="sky blue")

    frame = Frame(booking_window, bg="sky blue")
    frame.place(relx=0.4, rely=0.45, anchor=CENTER)

    movie_name = StringVar()
    movie_timing = StringVar()

    movie_option = ['Tangled', 'Cinderella', 'Frozen', 'The Lion King']
    movie_option1 = {
        'Tangled': ['10:00 am - 12:00 pm', '03:00 pm - 05:00 pm', '07:00 pm - 09:00 pm'],
        'Cinderella': ['09:00 am - 11:00 am', '02:00 pm - 04:00 pm', '06:00 pm - 08:00 pm'],
        'Frozen': ['07:00 am - 09:00 am', '03:00 pm - 05:00 pm', '07:00 pm - 09:00 pm'],
        'The Lion King': ['10:00 am - 12:00 pm', '03:00 pm - 05:00 pm', '07:00 pm - 09:00 pm']
    }

    def getvalues(selected_movie):
        timings = movie_option1[selected_movie]
        movie_timing.set(timings[0])
        menu = dm1["menu"]
        menu.delete(0, "end")
        for timing in timings:
            menu.add_command(label=timing, command=lambda value=timing: movie_timing.set(value))

    def open_seat_selection():
        if movie_name.get() == '---Select Movie---' or movie_timing.get() == '---Select Movie Time---':
            tkinter.messagebox.showinfo('Selection Error', 'Please select a movie and time')
        else:
            booking_window.destroy()
            seat_selection_window()

    Label(frame, text="Movie Name", bg="black", fg="white", font=(30)).grid(row=0, column=0, pady=10,padx=155, sticky=E)
    dm = ttk.OptionMenu(frame, movie_name, '---Select Movie---', *movie_option, command=getvalues)
    dm.grid(row=0, column=1, pady=10, sticky=W)

    Label(frame, text="Movie Time", bg="black", fg="white", font=(30)).grid(row=1, column=0, pady=10,padx=161,sticky=E)
    dm1 = ttk.OptionMenu(frame, movie_timing, '---Select Movie Time---')
    dm1.grid(row=1, column=1, pady=10, sticky=W)

    Label(frame, text="Select Seat", bg="black", fg="white", font=(30)).grid(row=2, column=0, pady=10,padx=159,sticky=E)
    Button(frame, text="Seat Selection", bg="black", fg="white", command=open_seat_selection).grid(row=2, column=1, pady=10, sticky=W)

    booking_window.mainloop()

def seat_selection_window():
    global seat_prices
    seat_window = Tk()
    seat_window.title('Seat Selection')
    screen_width = seat_window.winfo_screenwidth()
    screen_height = seat_window.winfo_screenheight()
    seat_window.geometry(f'{screen_width}x{screen_height}')
    seat_window.config(bg="sky blue")

    frame = Frame(seat_window, bg="sky blue")
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    selected_seats = []

    def toggle_seat(seat):
        if seat in selected_seats:
            selected_seats.remove(seat)
        else:
            selected_seats.append(seat)

    def confirm_selection():
        if not selected_seats:
            tkinter.messagebox.showinfo('Selection Error', 'Please select at least one seat')
        else:
            seat_window.destroy()
            open_confirmation_window(selected_seats)

    Label(frame, text="Select Your Seats", bg="black", fg="white", font=(30)).pack(pady=10)

    seat_prices = {'A': 200, 'B': 200, 'C': 150, 'D': 150, 'E': 150, 'F': 50, 'G': 50}

    for row in 'ABCDEFG':
        seat_frame = Frame(frame, bg="sky blue")
        seat_frame.pack(pady=5)
        for col in range(1, 11):
            seat = f'{row}{col}'
            btn = Checkbutton(seat_frame, text=seat, bg="sky blue", command=lambda s=seat: toggle_seat(s))
            btn.pack(side=LEFT, padx=5)

    Button(frame, text="Confirm", bg="black", fg="white", command=confirm_selection).pack(pady=10)
    seat_window.mainloop()

def open_confirmation_window(seats):
    confirmation_window = Tk()
    confirmation_window.title('Confirmation')
    screen_width = confirmation_window.winfo_screenwidth()
    screen_height = confirmation_window.winfo_screenheight()
    confirmation_window.geometry(f'{screen_width}x{screen_height}')
    confirmation_window.config(bg="sky blue")

    frame = Frame(confirmation_window, bg="sky blue")
    frame.place(relx=0.5, rely=0.45, anchor=CENTER)

    global movie_name, movie_timing, seat_prices

    total_price = sum([seat_prices[s[0]] for s in seats])

    Label(frame, text="Name:", bg="black", fg="white", font=(30)).grid(row=0, column=0, pady=10,padx=80, sticky=E)
    Label(frame, text=name.get(), bg="white", fg="black", font=(30)).grid(row=0, column=1, pady=10, sticky=W)

    Label(frame, text="Movie Name:", bg="black", fg="white", font=(30)).grid(row=1, column=0, pady=10,padx=80, sticky=E)
    Label(frame, text=movie_name.get(), bg="white", fg="black", font=(30)).grid(row=1, column=1, pady=10, sticky=W)

    Label(frame, text="Movie Time:", bg="black", fg="white", font=(30)).grid(row=2, column=0, pady=10,padx=80,sticky=E)
    Label(frame, text=movie_timing.get(), bg="white", fg="black", font=(30)).grid(row=2, column=1, pady=10, sticky=W)

    Label(frame, text="Seat No:", bg="black", fg="white", font=(30)).grid(row=3, column=0, pady=10,padx=80, sticky=E)
    Label(frame, text=', '.join(seats), bg="white", fg="black", font=(30)).grid(row=3, column=1, pady=10, sticky=W)

    Label(frame, text="Total Price:", bg="black", fg="white", font=(30)).grid(row=4, column=0, pady=10,padx=80,sticky=E)
    Label(frame, text=total_price, bg="white", fg="black", font=(30)).grid(row=4, column=1, pady=10, sticky=W)

    Button(frame, text="Confirm", bg="black", fg="white", command=exit).grid(row=5, column=1, pady=10,padx=0,sticky=W)

    confirmation_window.mainloop()

frame = Frame(root, bg="sky blue")
frame.place(relx=0.4, rely=0.45, anchor=CENTER)

Label(frame, text="Name", bg="black", fg='White', font=(30)).grid(row=0, column=0, pady=10,padx=155, sticky=E)
Label(frame, text="Password", bg="black", fg='White', font=(30)).grid(row=1, column=0, pady=10,padx=120, sticky=E)
Label(frame, text="Mobile Number", bg="black", fg='White', font=(30)).grid(row=2, column=0, pady=10,padx=80, sticky=E)
Entry(frame, textvariable=name).grid(row=0, column=1, pady=10, sticky=W)
Entry(frame, show="*", textvariable=passwo).grid(row=1, column=1, pady=10, sticky=W)
Entry(frame, textvariable=mobileno).grid(row=2, column=1, pady=10, sticky=W)
Button(frame, text="Login", bg="black", fg="white", command=register).grid(row=3, column=1, pady=10,padx=0)

root.title('Login Page')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')
root.config(bg='sky blue')
root.mainloop()
