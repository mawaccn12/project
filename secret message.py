from tkinter import *
import base64
# Tkinter GUI setup
root = Tk()
root.geometry("960x540")
root.title("Secret Communication Tool")
def encrypt_message():
    # Fetch message and key
    message = text_input.get("1.0", END)  # Get and strip input
    key = key_input.get()  # Get key and strip

    combined_message = message + key  # Concatenate message and key
    encoded_bytes = base64.b64encode(combined_message.encode("utf-8"))
    encrypted_message = encoded_bytes.decode("utf-8")  # Convert bytes to string
    result_output.delete(0, END)
    result_output.insert(0, encrypted_message)  # Show encrypted message in Entry

    def decrypt_message():
        # Fetch encrypted message and key
        encrypted_text = text_input.get("1.0", END)  # Get and strip input
        key = key_input.get()  # Get key and strip
        # Decode the encrypted message
        decoded_bytes = base64.b64decode(encrypted_text)
        decoded_message = decoded_bytes.decode("utf-8")
        # Check if key matches
        if decoded_message.endswith(key):
            original_message = decoded_message[:-len(key)]  # Remove key from end
            result_output.delete(0, END)
            result_output.insert(0, original_message)  # Show decrypted message
        else:
            result_output.delete(0, END)
            result_output.insert(0, "Error: Decryption failed. Incorrect key.")
            # Input for message
            Label(root, text="Enter your Message:", font=("Helvetica", 12)).pack(pady=5)
            text_input = Text(root, height=5, width=50)
            text_input.pack(pady=5)

            # Input for key
            Label(root, text="Enter Encryption Key:", font=("Helvetica", 12)).pack(pady=5)
            key_input = Entry(root, show="*", width=50)
            key_input.pack(pady=5)

            # Buttons
            Button(root, text="Encrypt", command=encrypt_message, bg="lightblue", font=("Helvetica", 12)).pack(pady=10)
            Button(root, text="Decrypt", command=decrypt_message, bg="lightgreen", font=("Helvetica", 12)).pack(pady=10)

            # Result display
            Label(root, text="Output (Copyable):", font=("Helvetica", 12)).pack(pady=5)
            result_output = Entry(root, font=("Helvetica", 12), width=50)
            result_output.pack(pady=5)
root.mainloop()
from tkinter import *
import base64


def encrypt_message():
    # Fetch message and key
    message = text_input.get("1.0", END)  # Get and strip input
    key = key_input.get()  # Get key and strip
    '''
    if not key:
        result_output.delete(0, END)
        result_output.insert(0, "Error: Key cannot be empty!")
        return
    if not message:
        result_output.delete(0, END)
        result_output.insert(0, "Error: Message cannot be empty!")
        return

    try:
        # Encrypt the message
        combined_message = message + key  # Concatenate message and key
        encoded_bytes = base64.b64encode(combined_message.encode("utf-8"))
        encrypted_message = encoded_bytes.decode("utf-8")  # Convert bytes to string
        result_output.delete(0, END)
        result_output.insert(0, encrypted_message)  # Show encrypted message in Entry
    except Exception as e:
        result_output.delete(0, END)
        result_output.insert(0, f"Error: {str(e)}")  # Show any error
    '''
    combined_message = message + key  # Concatenate message and key
    encoded_bytes = base64.b64encode(combined_message.encode("utf-8"))
    encrypted_message = encoded_bytes.decode("utf-8")  # Convert bytes to string
    result_output.delete(0, END)
    result_output.insert(0, encrypted_message)  # Show encrypted message in Entry


def decrypt_message():
    # Fetch encrypted message and key
    encrypted_text = text_input.get("1.0", END)  # Get and strip input
    key = key_input.get()  # Get key and strip
    '''
    if not key:
        result_output.delete(0, END)
        result_output.insert(0, "Error: Key cannot be empty!")
        return
    if not encrypted_text:
        result_output.delete(0, END)
        result_output.insert(0, "Error: Encrypted text cannot be empty!")
        return

    try:
        # Decode the encrypted message
        decoded_bytes = base64.b64decode(encrypted_text)
        decoded_message = decoded_bytes.decode("utf-8")
        # Check if key matches
        if decoded_message.endswith(key):
            original_message = decoded_message[:-len(key)]  # Remove key from end
            result_output.delete(0, END)
            result_output.insert(0, original_message)  # Show decrypted message
        else:
            result_output.delete(0, END)
            result_output.insert(0, "Error: Decryption failed. Incorrect key.")
    except Exception as e:
        result_output.delete(0, END)
        result_output.insert(0, f"Error: {str(e)}")  # Show any error
    '''
    # Decode the encrypted message
    decoded_bytes = base64.b64decode(encrypted_text)
    decoded_message = decoded_bytes.decode("utf-8")
    # Check if key matches
    if decoded_message.endswith(key):
        original_message = decoded_message[:-len(key)]  # Remove key from end
        result_output.delete(0, END)
        result_output.insert(0, original_message)  # Show decrypted message
    else:
        result_output.delete(0, END)
        result_output.insert(0, "Error: Decryption failed. Incorrect key.")


# Tkinter GUI setup
root = Tk()
root.geometry("960x540")
root.title("Secret Communication Tool")

# Input for message
Label(root, text="Enter your Message:", font=("Helvetica", 12)).pack(pady=5)
text_input = Text(root, height=5, width=50)
text_input.pack(pady=5)

# Input for key
Label(root, text="Enter Encryption Key:", font=("Helvetica", 12)).pack(pady=5)
key_input = Entry(root, show="*", width=50)
key_input.pack(pady=5)

# Buttons
Button(root, text="Encrypt", command=encrypt_message, bg="lightblue", font=("Helvetica", 12)).pack(pady=10)
Button(root, text="Decrypt", command=decrypt_message, bg="lightgreen", font=("Helvetica", 12)).pack(pady=10)

# Result display
Label(root, text="Output (Copyable):", font=("Helvetica", 12)).pack(pady=5)
result_output = Entry(root, font=("Helvetica", 12), width=50)
result_output.pack(pady=5)

root.mainloop()
