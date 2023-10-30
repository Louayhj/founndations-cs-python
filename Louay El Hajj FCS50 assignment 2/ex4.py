names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]
while True:
  letter = input("Enter a letter (to stop the program type stop ): ")
  if letter == 'stop':
      break
  print("Names containing '" + letter + "':")
  for name in names:
     if letter in name:
        print(name)