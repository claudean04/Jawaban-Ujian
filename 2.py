def username_check(username):

    SpecialSym=['.','_']
    return_val1=True
    if len(username) < 8:
        return_val1=False
    if len(username) > 12:
        return_val1=False
    if return_val1:
        return return_val1

def passwd_check(passwd):
    
    SpecialSym=['$','@','#', '!', '%', '^', '&', '*','()']
    return_val= True
    if len(passwd) > 9:
        return_val=False
    if not any(char.isdigit() for char in passwd):
        return_val=False
    if not any(char in SpecialSym for char in passwd):
        return_val=False
    if return_val:
        return return_val

# print(passwd_check.__doc__)
username = input('Masukan Username :')
passwd = input('Masukan Password : ')
print(username_check(username))
print(passwd_check(passwd))