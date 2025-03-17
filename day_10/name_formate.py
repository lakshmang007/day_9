def formate_name(f_name, l_name):   
    print( f"{f_name.capitalize()} {l_name.capitalize()}")
    name = f_name + " " + l_name
    return name.title()
formate_name("lakshman", "g")
formate_name(f_name=input("Enter your first name: "), l_name=input("Enter your last name: "))