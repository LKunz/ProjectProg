import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from Caesar import *
from Substitution import *
from Symmetric import *
from RSA import *

from database import database
from kivy.graphics import Color

## First, creating all classes = windows

class welcomewindow(Screen):
    pass

class helpwindow(Screen):
    pass
        
class choicewindow(Screen):
    pass

class encryptwindow(Screen):
    pass

class decryptwindow(Screen):
    pass     
    
            
class caesarwindow(Screen):
    
    # setting the objectproperties to none, temporarely
    caesarmsg = ObjectProperty(None) # Msg to encrypt
    key = ObjectProperty(None) # Key for encryption

    def encrypt(self): # function to encrypt the Msg
        try: # error handling, for any type of error
            # checking the validity of inputs
            if self.caesarmsg.text != "" and self.key.text != "": 
                # transforming to string
                original = str(self.caesarmsg.text) 
                # using the CaesarEncrypt method and adapting variables
                crypted = CaesarEncrypt(self.caesarmsg.text,
                                        int(round(float(self.key.text),0)))
                key = str(self.key.text) # transforming the variable
                # passing the variables to the finalwindow, and storing
                # them in a textfile so the user can retrieve them
                finalwindow.finalmsg = db.add_msg(original,crypted , key)
                # setting the button "back" of the final window for the 
                # user to be able to go back to this window
                finalwindow.back = "caesar"
                # changing window to the final window
                sm.current = "final"
            else: # error handling, activate a popup
                invalidform()
        
        except:
            invalidform()
                
        
class substitutionwindow(Screen):
    substitutionmsg = ObjectProperty(None)
    key = ObjectProperty(None)
    
# Adapting the function encrypt to the method    
    
    def encrypt(self):
        try:    
            key = str(self.key.text)
            original = str(self.substitutionmsg.text)
            method = "substitution"
        
            if self.substitutionmsg.text != "":
                key, ciphertext = SubstitutionEncrypt(self.substitutionmsg.text,make_dic(key))
                keystr = convertDict(key)
                finalwindow.finalmsg = db.add_msg(original , ciphertext, keystr)
                finalwindow.back = method
                sm.current = "final"
            else:
                invalidform()
        except:
            invalidform()
        
    def gotofinal(self):
        sm.current = "final"

class symmetricwindow(Screen):
    symmetricmsg = ObjectProperty(None)
    key = ObjectProperty(None)
    
# Adapting the function encrypt to the method
    
    def encrypt(self):
        try:
            original = str(self.symmetricmsg.text)
            key = str(self.key.text)
            method = "symmetric"
            key_ok = key_valid(key)
        
           
            if self.symmetricmsg.text != "" and key_ok == 0:
                ciphertext = SymmetricEncrypt(original, key)
                finalwindow.finalmsg = db.add_msg(original , ciphertext, key)
                finalwindow.back = method
                sm.current = "final"
            else:
                invalidform()
        except:
            invalidform()
    def gotofinal(self):
        sm.current = "final"

class rsawindow(Screen):
    rsamsg = ObjectProperty(None)
    p = ObjectProperty(None)
    q = ObjectProperty(None)
    
# Adapting the function encrypt to the method
    
    def encrypt(self):
        
        try:
            original = str(self.rsamsg.text)
            p = int(self.p.text)
            q = int(self.q.text)
            method = "rsa"
        
        
            if self.rsamsg.text != "":
                keypair = generate_keypair(p,q)
                pub_key = keypair[0]
                private_key = keypair[1]
                ciphertext = EncryptRSA(original, pub_key)
                print (ciphertext)
                finalwindow.finalmsg = db.add_msg(original , list_tostr(ciphertext), inttuptostr(pub_key), inttuptostr(private_key))
                finalwindow.back = method
                sm.current = "final"
            else:
                invalidform()
        except:
            invalidform()
    
    def gotofinal(self):
        sm.current = "final"
        
class dcaesarwindow(Screen):
    caesarmsg = ObjectProperty(None)
    key = ObjectProperty(None)
    
# Adapting the function encrypt to the method
    
    def decrypt(self):
        try:
            if self.caesarmsg.text != "" and self.key.text != "":
                original = str(self.caesarmsg.text)
                decrypted = CaesarDecrypt(self.caesarmsg.text, int(round(float(self.key.text),0)))
                key = str(self.key.text)
                method = "caesar"
                dfinalwindow.finalmsg = db.add_msg(original,decrypted , key)
                dfinalwindow.back = method
                sm.current = "dfinal"
            else:
                invalidform()
        except:
            invalidform()        
                
    def gotofinal(self):
        sm.current = "dfinal"
        
class dsymmetricwindow(Screen):
    symmetricmsg = ObjectProperty(None)
    key = ObjectProperty(None)
    
# Adapting the function encrypt to the method
    
    def decrypt(self):
        
        try: 
            ciphertext = str(self.symmetricmsg.text)
            key = str(self.key.text)
            method = "symmetric"
            key_ok = key_valid(key)
            
           
            if self.symmetricmsg.text != "" and key_ok == 0:
                deciphertext = SymmetricDecrypt(ciphertext, key)
                dfinalwindow.finalmsg = db.add_msg(ciphertext , deciphertext, key)
                dfinalwindow.back = method
                sm.current = "dfinal"
            else:
                invalidform()
        except:
            invalidform()    
            
    def gotofinal(self):
        sm.current = "dfinal"
        
class dsubstitutionwindow(Screen):
    substitutionmsg = ObjectProperty(None)
    key = ObjectProperty(None)
    
# Adapting the function encrypt to the method
    
    def decrypt(self):
        try:
            key = str(self.key.text)
            original = str(self.substitutionmsg.text)
            method = "dsubstitution"
        
        
            deciphertext = SubstitutionDecrypt(self.substitutionmsg.text,make_dic(key))
            dfinalwindow.finalmsg = db.add_msg(original , deciphertext, key)
            dfinalwindow.back = method
            sm.current = "dfinal"
        except:
            invalidform()
    def gotofinal(self):
        sm.current = "dfinal"
        
class drsawindow(Screen):
    rsamsg = ObjectProperty(None)
    private_key = ObjectProperty(None)

# Adapting the function encrypt to the method
    
    def decrypt(self):
        try:
            encrypted = str(self.rsamsg.text)
            encrypted_int = list(map(int, encrypted.split(",")))
            print(type(encrypted_int[0]))
            print(type(encrypted_int[1]))
            print(type(encrypted_int[2]))
            key = str(self.private_key.text)
            method = "drsa"
        
        
            if self.rsamsg.text != "":
                private_key = str_totup(key)
                print(type(private_key[0]))
                print(type(private_key[1]))
                plaintext = DecryptRSA(encrypted_int , private_key)
                finalwindow.finalmsg = db.add_msg(encrypted , plaintext, "", key)
                finalwindow.back = method
                sm.current = "dfinal"
            else:
                invalidform()
        except:
            invalidform()


# Functions to adapt the type of variables to the encryption functions
def str_totup(string):
    
    a = string.split("/")
    tup = (int(a[0]), int(a[1]))
    return tup
    

def make_dic(string):
    
    string = string.split(',')
    dic = {}
    for item in string:
        dic[item[0]] = item[2]
    return dic

def inttuptostr(tup):
    
    a = ""
    b = str(tup[0])
    c = str(tup[1])
    a = b + "/" + c
    return a

def convertDict(a):
    
    B = ""
    for key in a:
        B += key + ":" + a.get(key,"") + ","
    
    return(B[:-1])

def list_tostr(lis):
    
    a = ""
    for i in lis:
        a = a + "," + str(i)
    return a[1:]
        

def key_valid(key):
    
    if key != "":
        key_ok = 0
        for s in key:
            if s in "abcdefghijklmnopqrstuvwxyz" or s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                key_ok += 0
            else:
                key_ok += 1
    else:
        key_ok = 1
    return key_ok

def invalidform():
    
    p = Popup(title='Invalid use',
            content=Label(text='Error while encoding, check the inputs'),
            size_hint=(None,None), size=(400, 400),)
    p.open()
    

class finalwindow(Screen):
    
    originalmsg= ""
    finalmsg = ""
    key = ""
    back = ""

    
    def getback(self):
        sm.current = self.back
        
    def on_enter(self, *args):
       
        original,final, key1, key2 = db.get_msg()
        
        if key2 != "":
            self.finalmsg.text = final
            self.originalmsg.text = original
            self.key.text = "Public Key = " + key1 + """
""" + "Private key = " + key2
        else:
            self.finalmsg.text = final
            self.originalmsg.text = original
            print(type(self.key), type(self.finalmsg))
            self.key.text = key1
            
class dfinalwindow(Screen):
    
    originalmsg= ""
    finalmsg = ""
    key = ""
    back = ""

    
    def getback(self):
        sm.current = self.back
        
    def on_enter(self, *args):
       
        original,final, key1, key2 = db.get_msg()
        
        if key2 != "":
            self.finalmsg.text = final
            self.originalmsg.text = original
            self.key.text = "Private Key = " + key2 
        else:
            self.finalmsg.text = final
            self.originalmsg.text = original
            print(type(self.key), type(self.finalmsg))
            self.key.text = key1
            
class infowindow(Screen):
    text = ""
    
    def on_enter(self):
        self.text.text =   """Hello new user!

Welcome to the best encryption program.

As you might have something to hide to someone (otherwise you would not use this program), we propose to encrypt your text according to different methods. Here are the following methods and how to use it:

Encryption:

caesar method: This method is straightforward, you enter your message, a key which should be an integer and then press encrpyt. You will find your encrypted message with the key used. Don't forget to save them if you want your receipient to be able to retrieve your original message!

Substitution method: 
This method needs you to inform us about which letter you want to change by which one. An example is propsed to you. You can keep it as it is or change it. Remember, you need to keep the same format otherwise it will not work!

Symmetric method:
It is another method to encrypt a message. For this one, you need to input a text as a key. Again, remember that you need to keep your secret key!

RSA method:
For this method, you need to input two prime numbers as your keys. The multiplication of p and q should be four digits (a bit of maths won't kill you, come on..). For example you could use p = 89 and q = 97.

Decryption:

To decrypt with any method, you need to insert your given crypted message with the appropriate key. Remember, No key means no message (that's the whole point!)."""
    
    def getback(self):
        sm.current = "welcome"
            
class WindowManager(ScreenManager):
    pass

## Main Code creating the environment

kv = Builder.load_file("encryption.kv")
sm = WindowManager()
db = database("MSG.txt")

screens = [welcomewindow(name="welcome"), helpwindow(name="help"),
           choicewindow(name="choice"), encryptwindow(name="encrypt"),
           decryptwindow(name="decrypt"),
           caesarwindow(name="caesar"), substitutionwindow(name="substitution"),
           symmetricwindow(name="symmetric"),
           dcaesarwindow(name="dcaesar"), dsymmetricwindow(name="dsymmetric"), 
           dsubstitutionwindow(name="dsubstitution"), rsawindow(name="rsa"), 
           drsawindow(name="drsa"), infowindow(name="info"), 
           finalwindow(name="final"), dfinalwindow(name="dfinal")]

for screen in screens:
    sm.add_widget(screen)
    
sm.current = "welcome"

class MyMainApp(App):
    def build(self):
        return sm
    

if __name__ == "__main__":
    MyMainApp().run()



