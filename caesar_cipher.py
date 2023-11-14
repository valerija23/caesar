a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def e(t, o):
  r = ""
  for c in t:
    if (a.find(c) == -1):
      r += c
    else:
      r += (a[(a.find(c) + o) % len(a)])
  return r

def d(t, o):
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

if mode == 1:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + e(text, rotation))
elif mode == 2:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + d(text, rotation))
elif mode == 3:
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
