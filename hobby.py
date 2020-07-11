data = input('Enter you hobbies: ').split()

def hobbie(data):
    j =1
    print("Total hobbies - ",len(data))
    for i in data:
        print(j," - ",i)
        j+=1

hobbie(data)