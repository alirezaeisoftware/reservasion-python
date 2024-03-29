class Entity:
    def get_att(self):
        s=''
        for v in self.__dict__.values():
            s+=str(v)+'$'
        s=s[:-1]
        s+='#'
        return s
    def sabt(self,filename):
        f=open(filename,'a+',encoding='utf-8')
        att=self.get_att()
        f.write(att)
        f.close()
    def virayesh(self,filename,t):
        old=self.get_att()
        new=''
        for  v in t:
            new+=str(v)+'$'
        new=new[:-1]
        new+='#'
        f=open(filename,'r',encoding='utf-8')
        s=f.read()
        f.close()
        print(new)
        print(old)
        s=s.replace(old, new)
        f=open(filename,'w',encoding='utf-8')
        f.write(s)
        f.close()
    def hazf(self,filename):
        old=self.get_att()
        f=open(filename,'r',encoding='utf-8')
        s=f.read()
        f.close()
        s=s.replace(old, '')
        f=open(filename,'w',encoding='utf-8')
        f.write(s)
        f.close()



class Person(Entity): 
     ''' this class define person  '''
     def __init__(self, name, famil): 
           self.name = name 
           self.famil= famil
    #  def __str__(self):
    #       return self.name+' '+self.famil

class Docter(Person):
    filename='Docter.txt'
    def __init__(self,name,famil, code):
        Person.__init__(self , name , famil)
        self.code=code
    def __str__(self):
        return self.name+' '+self.famil
    def save(self):
        self.sabt(Docter.filename)
    def edit(self,*t):
        self.virayesh(Docter.filename,t)
    def delete(self,*t):
        self.hazf(Docter.filename)
        
    def __str__(self):
        return self.name+' '+self.famil
    @classmethod
    def open_file(cls):
        f=open(Docter.filename,'r',encoding='utf-8')
        s=f.read().split('#')
        s.pop()
        lst=[]
        for t in  s:
            v=t.split('$')
            lst.append(Docter(v[0], v[1], v[2]))
        f.close()
        return lst
      
class Patient(Person):
    filename='patient.txt'
    def __init__(self, name, famil, doctor=None, turn=None, prescription=None):
        Person.__init__(self, name, famil)
        self.doctor = doctor
        self.turn = turn
        self.prescription = prescription
        
    def save(self):
            self.sabt(Patient.filename)
    def edit(self,*t):
            self.virayesh(Patient.filename,t)
            self.__init__(*t)
    def delete(self , *t):
            self.hazf(Patient.filename)
            
    def __str__(self):
            return self.name+' '+self.famil
    @classmethod
    def open_file(cls):
            f=open(Patient.filename,'r',encoding='utf-8')
            s=f.read().split('#')
            s.pop()
            lst=[]
            for t in  s:
                v=t.split('$')
                try:
                    lst.append(Patient(v[0], v[1], v[2], v[3], v[4]))
                except:
                    try:
                        lst.append(v[0], v[1], v[2], v[3])
                    except:
                        lst.append(Patient(v[0], v[1]))
            f.close()
            return lst
            
class Turn(Entity):
    filename='turns.txt'
    def __init__(self, start, end, number):
        self.start = start
        self.end = end
        self.number = number
        
    def save(self):
            self.sabt(Turn.filename)
    def edit(self,*t):
            self.virayesh(Turn.filename,t)
    def delete(self):
            self.hazf(Turn.filename)
            
    def __str__(self):
            return 'شماره: ' + self.number + 'تایم شروع: ' + self.start + 'تایم پایان: ' + self.end
    @classmethod
    def open_file(cls):
            f=open(Turn.filename,'r',encoding='utf-8')
            s=f.read().split('#')
            s.pop()
            lst=[]
            for t in  s:
                v=t.split('$')
                lst.append(Turn(v[0], v[1], v[2]))
            f.close()
            return lst 
            
            
            