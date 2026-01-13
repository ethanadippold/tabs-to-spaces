 InputProgramFile = open("WithTabs.txt")
OutputProgramFile = open("NoTabs.txt","w")


SPACES_FOR_A_TAB = 4

listOfLines=InputProgramFile.readlines()

NumOfTabs = 0

for LineIndex in range(len(listOfLines)):
  TheLineOfProg = listOfLines[LineIndex]
  LineWithoutTabs = ""

  for i in range(len(TheLineOfProg)):
    if (TheLineOfProg[i] == "\t"):  
      NumOfTabs = NumOfTabs + 1
      print("found one, we now have found ",NumOfTabs," tabs.")
      for j in range(SPACES_FOR_A_TAB):
        LineWithoutTabs=LineWithoutTabs+" "
    else:
        LineWithoutTabs=LineWithoutTabs+TheLineOfProg[i]

  LineWithoutTabs = LineWithoutTabs.rstrip()

  print(LineWithoutTabs, file=OutputProgramFile)

OutputProgramFile.close()
print("done")
