import Levenshtein

encrypted_file = r'C:\Users\trost\github-classroom\bucs110SPRING23\portfolio-David-Trost\ch07\exercises\encrypted-#B00829653.txt'
decrypted_file = 'ch07/exercises/decrypted.txt'
target = "The quick brown fox jumps over the lazy dog"

with open(encrypted_file, 'r') as file:
    ciphertext = file.read()

best_decrypted = ""
best_distance = float('inf')

for shift in range(-26,26):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            decrypted += shifted
        else:
            decrypted += char

   
    distance = Levenshtein.distance(decrypted.lower(), target.lower())
    if distance < best_distance:
        best_distance = distance
        best_decrypted = decrypted

# Write the decrypted text to the file (failed to get "T in the first "The")
with open(decrypted_file, 'w') as file:
    file.write(best_decrypted)
