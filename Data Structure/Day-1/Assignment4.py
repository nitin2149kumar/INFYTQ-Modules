#DSA-Assgn-4

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game:
    def __init__(self,players_list):
        self.players_list=players_list
    def sort_players_based_on_experience(self):
        d={}
        for i in self.players_list:
            d[i.get_experience()]=i
        c=0
        for k in sorted(d.keys()):
            self.players_list[c]=d[k]
            c+=1
    def shift_player_to_new_position(self,old_index_position, new_index_position):
        ele=self.players_list.pop(old_index_position)
        self.players_list.insert(new_index_position,ele)
    def display_player_details(self):
        for i in self.players_list:
            print(i.get_name()+" "+str(i.get_experience()))
player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
#Create object of Game class, invoke the methods and test your program
game=Game(players_list)
game.sort_players_based_on_experience()
game.display_player_details()
game.shift_player_to_new_position(1,3)
game.display_player_details()
