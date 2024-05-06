from random import randint, shuffle

class Jeux:
    def __init__(self):
        self.result=0
        self.liste = ['None','None', 'Win']
        shuffle(self.liste)
        self.doors = [1,2,3]
        self.state=[1:0,2:0,3:0]

    def open_door(self,num):
        self.state[num]=1
        return
    
       
    # def porte1 (self,num):      
       
    #     if self.liste[num] == 'None':             
    #         result = 'None'
    #     else:
    #         result = 'Win'
        
    #     return (result, num)
       
  
    def new_doors(self,num):
        door=self.doors
        ind = door.pop(num)
        return (ind,door)

    def new_liste(self,num):
        liste=self.liste
        value= liste[num]
        liste.remove(num)
        return(value,liste)

    def step1 (self, num):
        if num not in self.doors:
            print('Le numéro de la porte doit ètre dans la liste [1,2,3')
        else:
            choice=[]
            choice.append(num)
            i,doors = Jeux.new_doors(self,num)
            val, liste= Jeux.new_liste(self,i)
            choice.append(val)
            if val =='None':
                if liste[0]=='None':
                    door=doors[0]
                    j= Jeux.open_door(self,door)


    def rand (num,type_jeux=1,ran=3) :
        liste_result=()
        if type_jeux ==1:
            for i in range(ran):
             result= Jeux.porte1(num)
             if result == 'None':
                 print('Jeux perdu')
             else:
            
                print('Jeux gagné')
                liste_result.append()
            return (liste_result)

        elif type_jeux == 2:
            for i in range(ran):
             res = Jeux.porte2(num)
             if res == 'None':               
                 print('Jeux perdu')
             else:
               
                print('Jeux gagné')

cla =Jeux()
res = cla.rand()