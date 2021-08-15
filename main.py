"""
GUI RANDOM PASSWORD GENERATOR
A simple GUI random password generator.
User can choose the length of the password, if they want it to be
all uppercase, have numbers and special characters in it. Generated password
can be saved to a text file of user's choice.
"""

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

    password = ''

    if uppercase:
        characters = ascii_lowercase + ascii_uppercase
    else:
        characters = ascii_lowercase

    if numbers:
        numbers = ''.join([str(number) for number in range(10)])
    else:
        numbers = ''

    if special_characters:
        special_characters = punctuation
    else:
        special_characters = ''

    pool = characters + numbers + special_characters

    for _ in range(length):
        password += choice(pool)

    return password


def main():
    """
    The main function that zips everything together.
    :return: None
    """

    root = Tk()
    root.geometry('500x500')
    root.title('Random password generator')

    font = 'Consolas {0} {1}'

    available_lengths = tuple(range(8, 17))
    length = IntVar()
    length.set(available_lengths[0])

    """
    Creating variables that hold information if the user wants specific 
    additions to the password.
    """
    uppercase = BooleanVar()
    numbers = BooleanVar()
    special_characters = BooleanVar()

    title_label = Label(root, text='Random password generator',
                        font=font.format(32, 'bold'), pady=20)
    title_label.pack()

    length_label = Label(root, text='Length:',
                         font=font.format(16, 'normal'))
    length_label.pack()

    length_choice = OptionMenu(root, length, *available_lengths)
    length_choice.pack()

    """
    Creating a checkbox to indicate if user wants uppercase letters in the
    password.
    """
    uppercase_choice = Checkbutton(root, text='Uppercase',
                                   font=font.format(16, 'normal'),
                                   variable=uppercase)
    uppercase_choice.pack()

    numbers_choice = Checkbutton(root, text='Numbers',
                                 font=font.format(16, 'normal'),
                                 variable=numbers)
    numbers_choice.pack()

    """
    Creating a checkbox to indicate if user wants special characters in 
    the password.
    """
    special_characters_choice = Checkbutton(root, text='Special characters',
                                            font=font.format(16, 'normal'),
                                            variable=special_characters)
    special_characters_choice.pack()

    def generate():
        """
        Uses generate_password function to generate the password,
        then displays it on the window.
        :return: None
        """

        global password_label
        global save_button
        
        password = generate_password(length.get(), uppercase.get(),
                                     numbers.get(), special_characters.get())
        
        label_text = 'Your randomly generated password:\n{0}'.format(password)

        try:
            password_label.destroy()
        except NameError:
            pass

        password_label = Label(root, text=label_text,
                               font=font.format(18, 'bold'))
        password_label.pack()

        def save_to_file():
            """
            Saves generated password to a text file of user's choice.
            :return: None
            """

            try:
                file = filedialog.askopenfilename(
                    initialdir=os.path.join(os.path.expanduser('~'),
                                            'Desktop'),
                    title='Select a file',
                    filetypes=(
                        ('txt files', '*.txt'),
                        ('all files', '*.*')
                    )
                )
            except KeyError:
                file = filedialog.askopenfilename(
                    initialdir=os.path.join(os.environ['HOMEPATH'], 'Desktop'),
                    title='Select a file',
                    filetypes=(
                        ('txt files', '*.txt'),
                        ('all files', '*.*')
                    )
                )

            with open(file, 'w') as f:
                f.write(password)
                messagebox.showinfo('Information', 'Password saved to file '
                                                   'successfully!')

        try:
            save_button.destroy()
        except NameError:
            pass

        save_button = Button(root, text='Save to file',
                             command=save_to_file)
        save_button.pack()

    generate_button = Button(root, text='Generate password', command=generate)
    generate_button.pack()

    password_label = Label(root, text='')
    password_label.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
