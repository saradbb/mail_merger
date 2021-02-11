#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
names = []
template = ""

def get_names():
    """
    A function that reads all the names from the file and stores in an array.
    :return:
    """
    global names
    with open ("Input/Names/invited_names.txt") as name_input:
        values = name_input.read()
        names = values.split()

def get_template():
    """
    Function that reads a template file and store in string
    :return:
    """
    global template
    with open("Input/Letters/starting_letter.txt") as template_input:
        template = template_input.read()

def send_invites():
    """
    Create individual invite for everyone in the list
    :return:
    """
    for name in names:
        file_name = "Output/ReadyToSend/"+"letter_for_" + name +".txt"
        with open (file_name,'w') as output_file:
            val = template.replace("[name]",name)
            output_file.write(val)


get_names()
get_template()
send_invites()
print(template)




