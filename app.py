import tkinter as tk
from functions import face_recognition, bluetooth_connection, take_pic

# Initialize Bluetooth connection
bt_socket = bluetooth_connection()

# Function for facial recognition
def facial_recognition():
    root.withdraw()  # Hide the main window
    print("Taking a picture for comparison...")
    f1 = "C:\\Users\\Manav\\Desktop\\Faces\\3.jpg"
    f2 = take_pic()

    if f2 is None:
        print("No picture was saved. Returning to main menu.")
    elif face_recognition(f1, f2):
        bt_socket.send(b"BLINK")

    root.deiconify()  # Show the main window again

# Function for custom command mode
def custom_command_mode():
    root.withdraw()  # Hide the main window
    command_window = tk.Toplevel()
    command_window.title("Custom Command Mode")
    command_window.geometry("300x200")

    def send_command(event=None):  # Allow the event parameter for key binding
        command = command_entry.get()
        if command == "-1":
            root.quit()
        else:
            bt_socket.send(command.encode())
            print(f"Command sent: {command}")
            command_entry.delete(0, tk.END)  # Clear the entry field after sending

    def go_back():
        command_window.destroy()  # Close the custom command window
        root.deiconify()  # Show the main window again

    command_label = tk.Label(command_window, text="Enter Command:")
    command_label.pack(pady=10)
    command_entry = tk.Entry(command_window)
    command_entry.pack(pady=10)

    # Bind the "Enter" key to the send_command function
    command_entry.bind("<Return>", send_command)

    back_button = tk.Button(command_window, text="Back", command=go_back)
    back_button.pack(pady=10)

# Function to exit the app
def exit_app():
    bt_socket.close()
    root.quit()

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Facial Recognition App")
root.geometry("300x200")

# Add buttons to the window
facial_recognition_button = tk.Button(root, text="Facial Recognition", command=facial_recognition)
facial_recognition_button.pack(pady=10)

custom_command_button = tk.Button(root, text="Custom Command Mode", command=custom_command_mode)
custom_command_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=10)

#Run the Tkinter event loop
root.mainloop()