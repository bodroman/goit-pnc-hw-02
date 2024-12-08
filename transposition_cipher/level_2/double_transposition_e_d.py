# Реалізуємо шифр подвійної перестановки

def generate_permutation(key):
    return sorted(range(len(key)), key=lambda i: key[i])

def transposition_encrypt(text, key):
    key = key.upper()
    permutation = generate_permutation(key)
    block_size = len(key)
    encrypted_text = ""
    
    # Розбиваємо текст на блоки
    for i in range(0, len(text), block_size):
        block = text[i:i+block_size]
        # Якщо блок коротший, додаємо пробіли
        if len(block) < block_size:
            block += ' ' * (block_size - len(block))
        encrypted_block = ''.join(block[j] for j in permutation)
        encrypted_text += encrypted_block

    return encrypted_text

def transposition_decrypt(encrypted_text, key):
    key = key.upper()
    permutation = generate_permutation(key)
    block_size = len(key)
    reverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    decrypted_text = ""
    
    # Розбиваємо текст на блоки
    for i in range(0, len(encrypted_text), block_size):
        block = encrypted_text[i:i+block_size]
        # Враховуємо довжину блоку при створенні дешифрованого тексту
        decrypted_block = ''.join(block[j] if j < len(block) else '' for j in reverse_permutation)
        decrypted_text += decrypted_block

    return decrypted_text

def double_transposition_encrypt(text, key1, key2):
    first_pass = transposition_encrypt(text, key1)
    second_pass = transposition_encrypt(first_pass, key2)
    return second_pass

def double_transposition_decrypt(encrypted_text, key1, key2):
    first_pass = transposition_decrypt(encrypted_text, key2)
    second_pass = transposition_decrypt(first_pass, key1)
    return second_pass

# Тестування
if __name__ == "__main__":
    key1 = "SECRET"
    key2 = "CRYPTO"
    plaintext = """The artist is the creator of beautiful things. 
To reveal art and conceal the artist is art's aim. 
The critic is he who can translate into another manner or a new material his impression of beautiful things. 
The highest, as the lowest, form of criticism is a mode of autobiography. 
Those who find ugly meanings in beautiful things are corrupt without being charming. 
This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. 
For these there is hope. They are the elect to whom beautiful things mean only Beauty. 
There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. 
The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. 
The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. 
The moral life of man forms part of the subject matter of the artist, 
but the morality of art consists in the perfect use of an imperfect medium. 
No artist desires to prove anything. Even things that are true can be proved. 
No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. 
No artist is ever morbid. The artist can express everything. 
Thought and language are to the artist instruments of an art. 
Vice and virtue are to the artist materials for an art. 
From the point of view of form, the type of all the arts is the art of the musician. 
From the point of view of feeling, the actor's craft is the type. 
All art is at once surface and symbol. Those who go beneath the surface do so at their peril. 
Those who read the symbol do so at their peril. 
It is the spectator, and not life, that art really mirrors. 
Diversity of opinion about a work of art shows that the work is new, complex, vital. 
When critics disagree the artist is in accord with himself. 
We can forgive a man for making a useful thing as long as he does not admire it. 
The only excuse for making a useless thing is that one admires it intensely. 
All art is quite useless."""

    print(f"Оригінальний текст: {plaintext}")

    # Шифрування
    encrypted = double_transposition_encrypt(plaintext, key1, key2)
    print(f"Зашифрований текст: {encrypted}")

    # Дешифрування
    decrypted = double_transposition_decrypt(encrypted, key1, key2)
    print(f"Розшифрований текст: {decrypted}")
