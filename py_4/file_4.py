place=int(input('Введите место в списке поступающих: '))
point=int(input('Введите количество баллов за экзамены: '))
if place <= 10:
  print ('Поздравляем, Вы поступили!')
  if point >= 290 :
   print ('Бонусом Вам будет начисляться стипендия')
  else :
    print ('Но Вам не хватило баллов для стипендии')
else:
  print('К сожеленыю Вы не поступили')



