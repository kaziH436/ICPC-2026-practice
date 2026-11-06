

n=int(input())




hash_g={
    'a': ['g'], # fishing ['g','f']
    'b': ['f'], # golf ['f']
    'c': ['y'] # hockey
}




arr=[]
for i in range(n):
    row=input()
    arr.append(row) # extend for multiple inputs


for i in range(len(arr)):
    first_i=arr[i][0]
    last_i=arr[i][len(arr[i])-1]
    if first_i in hash_g and last_i not in hash_g.get(first_i):
        # own=hasxh.get(first_i,last_i)
        name=''
        own=''
        game=''
       
        for key, value in hash_g.items():
            if last_i in value: # for lists
                own+=key
                break
        # print(first_i)
        owner=''
        if own=='a':
            # print(own)
            owner+='alice'
            # print(owner)
        if own=='b':
            owner+='bob'
        if own=='c':
            owner+='charlie'


        # print(last_i)
        if last_i =='f':
            game+='golf'
            # print(last_i)
        if last_i=='g':
            game+='fishing'
        if last_i=='y':
            game+='hockey'
       
        if first_i == 'a':
            name+='alice'
        if first_i == 'b':
            name+='bob'
        if first_i =='c':
            name+='charlie'
        # print(game)
        # print(owner)
        print(name+' borrows '+game+ ' from '+owner)


        print(hash_g[first_i])
        if hash_g[first_i] != last_i and len(hash_g.get(first_i)) == 1:
            hash_g[first_i]+=last_i
        elif hash_g[first_i] != last_i and len(hash_g.get(first_i)) > 1:
            hash_g[first_i].append(last_i)
        print(hash_g[first_i])


        print(hash_g[own])
        if len(hash_g[own])==1:
            hash_g[own]=['']
        elif len(hash_g[own])>1:
            hash_g[own].remove(last_i)
        print(hash_g[own])
       
       
       


    elif first_i in hash_g and last_i in hash_g.get(first_i):
        name=''
        own=''
        game=''
        if last_i == 'f':
            game+='golf'
        if last_i=='g':
            game+='fishing'
        if last_i=='y':
            game+='hockey'




        if first_i == 'a':
            name+='alice'
        if first_i == 'b':
            name+='bob'
        if first_i =='c':
            name+='charlie'
        print(name+' already has '+game)
