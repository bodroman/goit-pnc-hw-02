# Шифрування та дешифрування методом Перестановки

def generate_permutation(key):
    key_sorted = sorted(list(key))
    permutation = [key_sorted.index(char) + key[:i].count(char) for i, char in enumerate(key)]
    return permutation

def transposition_encrypt(text, key):
    key = key.upper()
    permutation = generate_permutation(key)
    block_size = len(key)
    encrypted_text = ""
    
    # Розбиваємо текст на блоки
    for i in range(0, len(text), block_size):
        block = text[i:i+block_size]
        # Додаємо пробіли, якщо блок коротший за ключ
        if len(block) < block_size:
            block += ' ' * (block_size - len(block))
        # Використовуємо перестановку для шифрування блоку
        encrypted_text += ''.join(block[j] for j in permutation)
    
    return encrypted_text

def transposition_decrypt(encrypted_text, key):
    key = key.upper()
    permutation = generate_permutation(key)
    block_size = len(key)
    reverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    decrypted_text = ""
    
    # Розбиваємо зашифрований текст на блоки
    for i in range(0, len(encrypted_text), block_size):
        block = encrypted_text[i:i+block_size]
        # Використовуємо зворотну перестановку для дешифрування блоку
        decrypted_text += ''.join(block[j] for j in reverse_permutation)
    
    return decrypted_text.rstrip()  # Видаляємо зайві пробіли

# Тестування
key_phrase = "SECRET"
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
encrypted = transposition_encrypt(plaintext, key_phrase)
print(f"Зашифрований текст: {encrypted}")

# Дешифрування
decrypted = transposition_decrypt(encrypted, key_phrase)
print(f"Розшифрований текст: {decrypted}")
