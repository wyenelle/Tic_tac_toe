print(' Attention pls!!! \n In this game, all keywords are to be enclosed in quotes \n \n \n the game keywords are as follows\n\n')
print(" First line keywords: '1a','1b','1c' \n Second line keywords: '2a','2b','2c' \n Third line keywords: '3a','3b','3c'\n\n")

# this is a tic tac toe game
# basic python project
'''check your keywords carefully before you play'''
#        assigning players their choice of letter
player1 = 'x'
player2 = 'o'
    
rows = ['_','_','_']
second_row = ['_','_','_']
third_row =['_','_','_']
print(rows)
print(second_row)
print(third_row)
#       Game keywords
first_denotions = ['1a','1b','1c']
second_denotions = ['2a','2b','2c']
third_denotions =['3a','3b','3c']



#       players choose
player1_choose = []
player2_choose = []

#    winner list
winning_denotions = [['1a','1b','1c'],['2a','2b','2c'],['3a','3b','3c'],
                    ['1a','2b','3c'],['1c','2b','3a'],['1a','2a','3a'],
                    ['1c','2c','3c']]
while True:
    #    first row functionality
    var = input('Player1,where do you want to place your choose: ') 
    while var not in first_denotions and  var not in second_denotions and  var not in third_denotions:
            print(var + '  is not a game keyword')
            var = input('Player1,where do you want to place your choose: ') 
    if var in first_denotions:
        rows.pop(first_denotions.index(var))
        rows.insert(first_denotions.index(var),player1)
        print(first_denotions.index(var))
            


      #  second row functionality

      
    if var in second_denotions:
        second_row.pop(second_denotions.index(var))    
        second_row.insert(second_denotions.index(var),player1)
        print(second_denotions.index(var))
           



    #       Third row functionality
    
    if var in third_denotions:
        third_row.pop(third_denotions.index(var))     
        third_row.insert(third_denotions.index(var),player1)
        print(third_denotions.index(var))
        


    
    print(rows)
    print(second_row)
    print(third_row)
    player1_choose.append(var)


    if player1_choose in winning_denotions:
        print('PLAYER1 wins')
        break
        

    elif  player2_choose in winning_denotions:
        print('PLAYER2 WINS')
        break


    
   





    

    #    second player

    var2 = input('Player2,where do you want to place your choose: ') 
    while var2 not in first_denotions and  var2 not in second_denotions and  var2 not in third_denotions:
            print(var2 + '  is not a game keyword')
            var2 = input('Player2,where do you want to place your choose: ') 
    
     #      first row functionality   
    if var2 in first_denotions:
        rows.pop(first_denotions.index(var2))  
        rows.insert(first_denotions.index(var2),player2)
        print(first_denotions.index(var2))
      

                

    #   second row functionality
    if var2 in second_denotions:
        second_row.pop(second_denotions.index(var2))       
        second_row.insert(second_denotions.index(var2),player2)
        print(second_denotions.index(var2))
       



    #   third row functionality
    if var2 in third_denotions:
        third_row.pop(third_denotions.index(var2))     
        third_row.insert(third_denotions.index(var2),player2)
        print(third_denotions.index(var2))
     

    

    print(rows)
    print(second_row)
    print(third_row)
    player2_choose.append(var2)


    if player1_choose in winning_denotions:
        print('PLAYER1 wins')
        break

    elif  player2_choose in winning_denotions:
        print('PLAYER2 WINS')
        break

        print('THANKS FOR PLAYING')











        
