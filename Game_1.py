#It is game made by Priya Dutta
#randit for random number


from random import randint   
#player choice first/turn
player = input('Rock(r),Paper(p) or Scissor (s)?')
print(player,'V/S',end=' ') #end=' ' prints the computer choice on same line with a space instead of new ine

#computer choice/turn
chosen = randint(1,3)
#print(chosen)

if(chosen==1):
  computer='r'
elif(chosen==2):
    computer='p'
else:
      computer='s'
print(computer)

#who won the game
#if player chooses r
if(player==computer):
  print('DRAW AWWW!')
elif(player=='r' and computer=='s'):
  print('YOU WIN!')
elif(player=='r' and computer=='p'):
  print('COMPUTER WIN    AWWW!')
#if player choses p
elif(player=='p' and computer=='s'):
  print('COMPUTER WIN Better luck next time')
elif(player=='p' and computer=='r'):
  print('YOU WON ,machines are machines at last ; )')
#if player choses s
elif(player=='s' and computer=='r'):
  print('OH NO! Computer wins i make it intelligent than you ;)')
elif(player=='s' and computer=='p'):
  print('Ha Ha! you won cut the shity computer paper')
else:
  print('choose a valid option')
