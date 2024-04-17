from django.shortcuts import render
from .models import Message


def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + key) %
                               26) + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') - key) %
                               26) + ord('a' if char.islower() else 'A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


def encrypt_message(request):
    if request.method == 'POST':
        original_text = request.POST.get('original_text')
        # Retrieve key value from the form
        key = int(request.POST.get('key', 5))
        encrypted_text = encrypt(original_text, key)
        message = Message.objects.create(
            text=original_text, encrypted_text=encrypted_text)
        return render(request, 'cipher/encrypted_message.html', {'encrypted_message': encrypted_text})
    else:
        return render(request, 'cipher/encrypt_form.html')


def decrypt_message(request):
    if request.method == 'POST':
        encrypted_text = request.POST.get('encrypted_text')

        key = int(request.POST.get('key', 5))
        decrypted_text = decrypt(encrypted_text, key)
        return render(request, 'cipher/decrypted_message.html', {'decrypted_message': decrypted_text})
    else:
        return render(request, 'cipher/decrypt_form.html')
