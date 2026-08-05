# Credits: Nicray
# Windows Keyboard External Library
# Version: 0.1
# Description: This is the very first library I've built myself that actually works. It's a very simple library that allows you to read keyboard input in Windows. This is the first step towards building more complex libraries like this one.

try:
    import msvcrt
    import os
except ImportError:
    print("Error: The required modules are not installed or not found.")


# 1. Dictionary for standard keys that send exactly ONE byte (credits: ChatGPT)
WINDOWS_STANDARD_KEYS = {
    # --- Action Keys ---
    b'\r': "enter",
    b'\x08': "backspace",
    b'\t': "tab",
    b' ': "space",
    b'\x1b': "escape",
    
    # --- Numbers ---
    b'0': "0", b'1': "1", b'2': "2", b'3': "3", b'4': "4",
    b'5': "5", b'6': "6", b'7': "7", b'8': "8", b'9': "9",

    # --- Lowercase letters (Direct input) ---
    b'a': "a", b'b': "b", b'c': "c", b'd': "d", b'e': "e", b'f': "f",
    b'g': "g", b'h': "h", b'i': "i", b'j': "j", b'k': "k", b'l': "l",
    b'm': "m", b'n': "n", b'o': "o", b'p': "p", b'q': "q", b'r': "r",
    b's': "s", b't': "t", b'u': "u", b'v': "v", b'w': "w", b'x': "x",
    b'y': "y", b'z': "z",

    # --- Uppercase letters (With Shift held down) ---
    b'A': "A", b'B': "B", b'C': "C", b'D': "D", b'E': "E", b'F': "F",
    b'G': "G", b'H': "H", b'I': "I", b'J': "J", b'K': "K", b'L': "L",
    b'M': "M", b'N': "N", b'O': "O", b'P': "P", b'Q': "Q", b'R': "R",
    b'S': "S", b'T': "T", b'U': "U", b'V': "V", b'W': "W", b'X': "X",
    b'Y': "Y", b'Z': "Z",

    # --- Punctuation & Mathematical Symbols ---
    b'.': ".", b',': ",", b';': ";", b':': ":", b'!': "!", b'?': "?",
    b'-': "-", b'_': "_", b'+': "+", b'=': "=", b'*': "*", b'/': "/",
    b'\\': "\\", b'|': "|", b'@': "@", b'#': "#", b'$': "$", b'%': "%",
    b'^': "^", b'&': "&", b'(': "(", b')': ")", b'[': "[", b']': "]",
    b'{': "{", b'}': "}", b'<': "<", b'>': ">", b'~': "~", b'`': "`",
    b'"': '"', b"'": "'", 
    b'\xfd': "section", b'\xf8': "degree", b'\xe6': "mu",

    # --- Ctrl Shortcuts (Windows maps Ctrl+Letter to raw ASCII 1-26) ---
    b'\x01': "ctrl_a", b'\x02': "ctrl_b", b'\x03': "ctrl_c", b'\x04': "ctrl_d",
    b'\x05': "ctrl_e", b'\x06': "ctrl_f", b'\x07': "ctrl_g", b'\x0b': "ctrl_k",
    b'\x0c': "ctrl_l", b'\x0e': "ctrl_n", b'\x0f': "ctrl_o", b'\x10': "ctrl_p",
    b'\x11': "ctrl_q", b'\x12': "ctrl_r", b'\x13': "ctrl_s", b'\x14': "ctrl_t",
    b'\x15': "ctrl_u", b'\x16': "ctrl_v", b'\x17': "ctrl_w", b'\x18': "ctrl_x",
    b'\x19': "ctrl_y", b'\x1a': "ctrl_z"
}

# 2. Dictionary for special keys that are caught during the SECOND byte read
WINDOWS_SPECIAL_KEYS = {
    # --- Navigation Keys ---
    b'H': "arrow_up",
    b'P': "arrow_down",
    b'K': "arrow_left",
    b'M': "arrow_right",
    b'R': "insert",
    b'S': "delete",
    b'G': "home",
    b'O': "end",
    b'I': "page_up",
    b'Q': "page_down",

    # --- Function Keys ---
    b';': "F1",  b'<': "F2",  b'=': "F3",  b'>': "F4",
    b'?': "F5",  b'@': "F6",  b'A': "F7",  b'B': "F8",
    b'C': "F9",  b'D': "F10", b'\x85': "F11", b'\x86': "F12",

    # --- Ctrl + Arrow Keys ---
    b'\x8d': "ctrl_arrow_up",
    b'\x91': "ctrl_arrow_down",
    b's': "ctrl_arrow_left",
    b't': "ctrl_arrow_right",
    
    # --- Ctrl + Navigation Keys ---
    b'\x92': "ctrl_insert",
    b'\x93': "ctrl_delete",
    b'w': "ctrl_home",
    b'u': "ctrl_end",
    b'\x84': "ctrl_page_up",
    b'v': "ctrl_page_down",  # <-- Corrigé ici ! b'v' au lieu de bv

    # --- Alt + Function Keys ---
    b'k': "alt_F1", b'l': "alt_F2", b'm': "alt_F3", b'n': "alt_F4",
    b'o': "alt_F5", b'p': "alt_F6", b'q': "alt_F7", b'r': "alt_F8",
    b's': "alt_F9", b't': "alt_F10"
}


# Source - https://stackoverflow.com/a/287944
# Posted by joeld, modified by community. See post 'Timeline' for change history
# This function is used to print colored text in the console.
WHITE = '\033[0m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
WARNING = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'


# Define an exception class for errors related to reading keyboard input.
class Get_Keyboard_Input_Error(Exception):
    pass

class Incompatible_OS(Exception):
    pass



# Windows is the wrost OS for handling keyboard input, so we need to use a different method than the one used on Linux in keyboard_unix.py.
# This function is used to get the keyboard input from the user. 
def get_keyboard_input():
    if os.name == 'nt':
        global WINDOWS_STANDARD_KEYS, WINDOWS_STANDARD_KEYS

        key = msvcrt.getch()

        try:

            if key in (b'\x00', b'\xe0'): # Since the Windows keyboard system is really poor, pressing a special key sends two bytes instead of just one, which means the second byte has to be retrieved.
                    secondbytes = msvcrt.getch()
                    return WINDOWS_SPECIAL_KEYS[secondbytes]

            elif key in WINDOWS_STANDARD_KEYS: # If it's not a special key, then we can just return the key as is. 
                return WINDOWS_STANDARD_KEYS[key]

            else:
                return None

        except KeyError:
            raise Get_Keyboard_Input_Error("The key you pressed is unknown.")

    else:
        raise Incompatible_OS("This program only works on Windows.")