def main():
    #write your code below this line
    intList = []
    while(True):
      number = int(input())
      if(number==-1):
        break
      intList.append(number)
    for i in range(len(intList)):
      print(intList[i])

if __name__ == '__main__':
    main()
