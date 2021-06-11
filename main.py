"""
GUI RANDOM PASSWORD GENERATOR
A simple GUI random password generator.
User can choose the length of the password, if they want it to be
all uppercase, have numbers and special characters in it. Generated password
can be saved to a text file of user's choice.
"""

# Required imports.
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from string import ascii_lowercase, ascii_uppercase, punctuation
from random import choice
import os


def generate_password(length, uppercase, numbers, special_characters):
    """
    Generates a random password for user.
    :param length: int
    :param uppercase: bool
    :param numbers: bool
    :param special_characters: bool
    :return: password: str
    """

    # A variable to hold the password.
    password = ''

    # If user wants uppercase letters in the password, add them to characters.
    if uppercase:
        characters = ascii_lowercase + ascii_uppercase
    else:
        characters = ascii_lowercase

    # If user wants numbers in the password, add them to characters.
    if numbers:
        numbers = ''.join([str(number) for number in range(10)])
    else:
        numbers = ''

    # If user wants special characters in the password, add them to characters.
    if special_characters:
        special_characters = punctuation
    else:
        special_characters = ''

    # Creating the character pool to choose from.
    pool = characters + numbers + special_characters

    # Adding randomly chosen characters to the password
    for _ in range(length):
        password += choice(pool)

    # Returning generated password.
    return password


def main():
    """
    The main function that zips everything together.
    :return: None
    """

    # Create the main window.
    root = Tk()
    # Set window's dimensions.
    root.geometry('500x500')
    # Set window's title.
    root.title('Random password generator')

    # A variable that holds the font used by labels.
    font = 'Consolas {0} {1}'

    # All available length values.
    available_lengths = tuple(range(8, 17))
    # A variable that holds the value representing length of the password.
    length = IntVar()
    # Setting the value of the variable to the first available length value.
    length.set(available_lengths[0])

    """
    Creating variables that hold information if the user wants specific 
    additions to the password.
    """
    uppercase = BooleanVar()
    numbers = BooleanVar()
    special_characters = BooleanVar()

    # Creating the title label.
    title_label = Label(root, text='Random password generator',
                        font=font.format(32, 'bold'), pady=20)
    # Displaying the label on the window.
    title_label.pack()

    # Creating the length label.
    length_label = Label(root, text='Length:',
                         font=font.format(16, 'normal'))
    # Displaying the label on the window.
    length_label.pack()

    # Creating the dropdown menu to select the length of the password.
    length_choice = OptionMenu(root, length, *available_lengths)
    # Displaying the menu on the window.
    length_choice.pack()

    """
    Creating a checkbox to indicate if user wants uppercase letters in the
    password.
    """
    uppercase_choice = Checkbutton(root, text='Uppercase',
                                   font=font.format(16, 'normal'),
                                   variable=uppercase)
    # Displaying the checkbox on the window.
    uppercase_choice.pack()

    # Creating a checkbox to indicate if user wants numbers in the password.
    numbers_choice = Checkbutton(root, text='Numbers',
                                 font=font.format(16, 'normal'),
                                 variable=numbers)
    # Displaying the checkbox on the window.
    numbers_choice.pack()

    """
    Creating a checkbox to indicate if user wants special characters in 
    the password.
    """
    special_characters_choice = Checkbutton(root, text='Special characters',
                                            font=font.format(16, 'normal'),
                                            variable=special_characters)
    # Displaying the checkbox on the window.
    special_characters_choice.pack()

    def generate():
        """
        Uses generate_password function to generate the password,
        then displays it on the window.
        :return: None
        """

        # Using the global variable password_label.
        global password_label
        global save_button
        # Generating the password with provided specifications.
        password = generate_password(length.get(), uppercase.get(),
                                     numbers.get(), special_characters.get())
        # Setting the password label text.
        label_text = 'Your randomly generated password:\n{0}'.format(password)

        # If password label exists, delete it, otherwise pass.
        try:
            password_label.destroy()
        except NameError:
            pass

        # Creating the password label.
        password_label = Label(root, text=label_text,
                               font=font.format(18, 'bold'))
        # Displaying the label on the window.
        password_label.pack()

        def save_to_file():
            """
            Saves generated password to a text file of user's choice.
            :return: None
            """

            # If user's operating system is Linux/macOS:
            try:
                # Ask user for a file to save password to.
                file = filedialog.askopenfilename(
                    initialdir=os.path.join(os.path.expanduser('~'),
                                            'Desktop'),
                    title='Select a file',
                    filetypes=(
                        ('txt files', '*.txt'),
                        ('all files', '*.*')
                    )
                )
            # If user's operating system is Windows:
            except KeyError:
                # Ask user for a file to save password to.
                file = filedialog.askopenfilename(
                    initialdir=os.path.join(os.environ['HOMEPATH'], 'Desktop'),
                    title='Select a file',
                    filetypes=(
                        ('txt files', '*.txt'),
                        ('all files', '*.*')
                    )
                )

            # Open provided file, write password and show a message box.
            with open(file, 'w') as f:
                f.write(password)
                messagebox.showinfo('Information', 'Password saved to file '
                                                   'successfully!')

        # If a save button exists, delete it.
        try:
            save_button.destroy()
        except NameError:
            pass

        # Creating a save button.
        save_button = Button(root, text='Save to file',
                             command=save_to_file)
        # Displaying the button on the window.
        save_button.pack()

    # Creating a button to generate the password.
    generate_button = Button(root, text='Generate password', command=generate)
    # Displaying the button on the window.
    generate_button.pack()

    # Creating the password label.
    password_label = Label(root, text='')
    # Displaying the label on the window.
    password_label.pack()

    # The main program loop.
    root.mainloop()


if __name__ == '__main__':
    main()
