from collections import Counter
import sys

uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
u = '?u'
lowers = 'abcdefghijklmnopqrstuvwxyz'
l = '?l'
digits = '0123456789'
d = '?d'
s = '?s'


	
def main():
    passFile = sys.argv[1]
    num = int(sys.argv[2])
    #passFile = "/usr/share/seclists/Passwords/2020-200_most_used_passwords.txt"
    
    # if this does not work, you can default to UTF-8 by removing the encoding section
    readpasswords = open(passFile, 'r', encoding="latin-1")
    passwords = readpasswords.readlines()
    allwords = len(passwords)
    listOfLists = []
    for password in passwords:
        password = password.strip()
        characters = []
        for p in password:
            if p in uppers:
                characters.append(u)
            elif p in lowers:
                characters.append(l)
            elif p in digits:
                characters.append(d)
            else:
                characters.append(s)
        listOfLists.append("".join(characters))
    #print listOfLists

    count = Counter(listOfLists).most_common(num)
    whitespace = 20
    print("\nTask Completed!\nTotal of ", allwords, " passwords injested\n")
    #print("Most Common Masks:")
    print("Mask", (whitespace -len("mask")) * ' ', ':', "Count", ": Total Percentage")
    print("-"*30)
    
    for key, val in count:
        w = whitespace - len(key) 
        print(key, ' ' * w, ':', val, ":   ", (int(val)/allwords)*100, "%")

if len(sys.argv) != 3:
	print("Help: command should inlude two arguments 1). path to a passwordlist and 2). the X most common masks you want to see")
	quit
elif len(sys.argv) == 3:
	main()
