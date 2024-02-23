#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

names = [name.strip() for name in names]

#Replace the [name] placeholder with the actual name.

with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
    
    for name in names:
        named_letter = content.replace("[name]", name)
        
        #Save the letters in the folder "ReadyToSend".
        
        with open(f"./OutPut/ReadyToSend/letter_for_{name}.txt", "w") as file:
            file.write(named_letter)
    


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp