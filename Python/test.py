import os
class UsersLIst():
    def __init__(self):
        self.usersList = []
    def appendToList(self, element):
        self.usersList.append(element)
class User():
    def __init__(self, name, age, mail, password):
        self.name = name
        self.age = age
        self.mail = mail
        self.password = password
        
def newElement(_list, _user):
    _list.appendToList(_user)
def showData(_list):
    print(_list)

if __name__ == '__main__':
    os.system('cls')
    usersList = UsersLIst()
    user = User('Sergio', 21, 'sergionvte11@gmail.com', 'Watercolor')
    newElement(usersList, user)
    user = User('Claudia', 20, 'adi_cast@outlook.com', 'Harrystyles')
    newElement(usersList, user)
    
    input()
