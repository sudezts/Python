import random

with open("C:/Users/sudeo/OneDrive/Masaüstü/Words.txt") as f:
    words = f.readlines()
    random_word = random.choice(words).strip()
    word_size = len(random_word)
    temp = "_" * word_size

    print(temp)

    guesslist = []
    count = 0
    c=0
    if(word_size>6):
        while c < word_size:
            c+=1
            guess = input("Enter a character: ")
            guesslist.append(guess)
            if guess not in random_word:
                count+=1

            temp2 = ""
            for i in range(word_size):
                if random_word[i] in guesslist:
                    temp2 += random_word[i]
                else:
                    temp2 += "_"
                    

            print(temp2)
            if count==0:
                print(" -----\n |  |\n    |\n    |\n    |\n    |")
            if count==1:
                print(" -----\n |  |\n O  |\n    |\n    |\n    |")
            elif count==2:
                print(" -----\n |  |\n O  |\n |  |\n    |\n    |")
            elif count==3:
                print(" -----\n |  |\n O  |\n/|  |\n    |\n    |")
            elif count==4:
                print(" -----\n |  |\n O  |\n/|\\|\n    |\n    |")
            elif count==5:
                print(" -----\n |  |\n O  |\n/|\\|\n/   |\n    |")
            elif count==6:
                print(" -----\n |  |\n O  |\n/|\\|\n/ \\|\n    |")
                print("Game Over!")
                break
        
        if(count>6):
            print("You Win!")

    else:
        while temp==random_word:
            c+=1
            guess = input("Enter a character: ")
            guesslist.append(guess)
            if guess not in random_word:
                count+=1

            temp2 = ""
            for i in range(word_size):
                if random_word[i] in guesslist:
                    temp2 += random_word[i]
                else:
                    temp2 += "_"
            temp=temp2

            print(temp2)
            if count==0:
                print(" -----\n |  |\n    |\n    |\n    |\n    |")
            if count==1:
                print(" -----\n |  |\n O  |\n    |\n    |\n    |")
            elif count==2:
                print(" -----\n |  |\n O  |\n |  |\n    |\n    |")
            elif count==3:
                print(" -----\n |  |\n O  |\n/|  |\n    |\n    |")
            elif count==4:
                print(" -----\n |  |\n O  |\n/|\\|\n    |\n    |")
            elif count==5:
                print(" -----\n |  |\n O  |\n/|\\|\n/   |\n    |")
            elif count==6:
                print(" -----\n |  |\n O  |\n/|\\|\n/ \\|\n    |")
                print("Game Over!")
                break
        
        if(count>6):
            print("You Win!")
