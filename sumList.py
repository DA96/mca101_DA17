
def sumList(list):
    if list == []:
        return 0
    else :
        return list[0] + sumList(list[1:])
        
def main():
    print(sumList([1,2,3]))

main()
