a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#Funkcija a definē alfabetu
def encription(text, rotation): 
  r = ""
  
  for c in t: 
    if (a.find(c) == -1): 
      r += c
    else: 
      r += (a[(a.find(c) + o) % len(a)])
  return r

def decription(text, rotation): #Funkcija d atšifrēšanas funkciju
  r = ""
  for c in t: 
    if (a.find(c) == -1): 
      r += c
    else: 
      r += (a[(a.find(c) - o) % len(a)])
  return r

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1: #Definē šifra šifrešanas funkciju 
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encription(text, rotation)) #Difinē atšifrešanas funkciju
elif mode == 2:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decription(text, rotation))
elif mode == 3:
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
