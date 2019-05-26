class database:
    def __init__(self,filename):
        self.filename = filename
        self.elements = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename)
        self.elements = ()
        
        b = 0
        for line in self.file:
            a = ""
            if b == 0:
                if  ';' in line:
                    c = line.partition(';')
                    original = a + c[0]
                    b = 1
                    a = ""
                    """original, crypted, key1, key2 = line.split(";")
                    self.elements = (original, crypted, key1, key2)"""
                else:
                    a += line + """
                                    """
            else:
                if  ';' in line:
                    c = line.partition(';')
                    crypted = a + c[0]
                    key1 = c[1]
                    if len(c) == 4:
                        key2 = c[3]
                    else:
                        key2 = ""
                    b = 1
                    """original, crypted, key1, key2 = line.split(";")
                    self.elements = (original, crypted, key1, key2)"""
                else:
                    a += line + """
                                    """
            
        self.file.close()
        

    def get_msg(self):
        return self.elements

    def add_msg(self, original, crypted, key1, key2=""):
            self.elements = (original,crypted,key1,key2)
            self.save()

    def save(self):
        with open(self.filename, "w") as f:
            a = self.elements[0] + ";" + self.elements[1] + ";" + self.elements[2] + ";" + self.elements[3]
            f.write(a)
