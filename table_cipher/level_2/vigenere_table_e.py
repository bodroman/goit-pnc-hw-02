# Шифрування методами Віженера та Табличним

def vigenere_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = key.upper()
    key_repeated = (key * ((len(text) // len(key)) + 1))[:len(text)]
    encrypted = ""
    
    for t, k in zip(text, key_repeated):
        if t.isalpha():
            encrypted += chr(((ord(t) - ord('A')) + (ord(k) - ord('A'))) % 26 + ord('A'))
        else:
            encrypted += t  # Неалфавітні символи без шифрування
    
    return encrypted


def generate_table(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(sorted(set(key.upper()), key=key.upper().index))  # Видаляємо дублікати, зберігаємо порядок
    table = key + "".join(c for c in alphabet if c not in key)  # Додаємо решту алфавіту
    return [table[i:i + 5] for i in range(0, len(table), 5)]  # Розділяємо на рядки по 5 символів


def find_position(char, table):
    for row_idx, row in enumerate(table):
        if char in row:
            return row_idx, row.index(char)
    return None


def encrypt_table_cipher(text, key):
    table = generate_table(key)
    text = text.upper().replace(" ", "").replace("J", "I")  # Видаляємо пробіли, замінюємо J на I
    encrypted = ""
    
    for char in text:
        if char.isalpha():
            row, col = find_position(char, table)
            encrypted += table[(row + 1) % 5][col]  # Переходимо на наступний рядок
        else:
            encrypted += char  # Неалфавітні символи без шифрування
    
    return encrypted


# Тестування
if __name__ == "__main__":
    text = """The artist is the creator of beautiful things. 
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

    vigenere_key = "CRYPTO"
    table_key = "CRYPTO"
    
    print("Оригінальний текст:", text)
    
    # Шифрування Віженером
    vigenere_encrypted = vigenere_encrypt(text, vigenere_key)
    print("Зашифровано шифром Віженера:", vigenere_encrypted)
    
    # Шифрування табличним шифром
    double_encrypted = encrypt_table_cipher(vigenere_encrypted, table_key)
    print("Додатково зашифровано табличним шифром:", double_encrypted)