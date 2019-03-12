n = int(input())
sl = {}
sp = []
if 1<=n<=100:
    command,namespace,parOrVar = input().split()
    if command!='get':
        if sl.get('command')!=None:
            mas = sl.get('command')
            for i in range(len(mas)):
                sp.append(mas[i])
            sp.append(command)
            a=0
            sl['command']=sp
            sp=[]
        else:
            sl['command'] = command
        if sl.get('namespace')!=None:
            mas = sl.get('namespace')
            for i in range(len(mas)):
                sp.append(mas[i])
            sp.append(namespace)
            sl['namespace']=sp
            sp=[]
        else:
            sl['namespace'] = namespace
        if command=='create':
            if sl.get('parent')!=None:
                mas = sl.get('parent')
                for i in range(len(mas)):
                    sp.append(mas[i])
                sp.append(parOrVar)
                sl['parent']=sp
                sp=[]
            else:
                sl['parent'] = parOrVar
            if sl.get('var')!=None:
                mas = sl.get('var')
                for i in range(len(mas)):
                    sp.append(mas[i])
                sp.append('clear')
                sl['var']=sp
                sp=[]
            else:
                sl['var'] = 'clear'
        if command=='add':
            if sl.get('var')!=None:
                mas = sl.get('var')
                for i in range(len(mas)):
                    sp.append(mas[i])
                sp.append(parOrVar)
                sl['var']=sp
                sp=[]
            else:
                sl['var'] = parOrVar
            if sl.get('parent')!=None:
                mas = sl.get('parent')
                for i in range(len(mas)):
                    sp.append(mas[i])
                sp.append('clear')
                sl['parent']=sp
                sp=[]
            else:
                sl['parent'] = 'clear'


else:
    print('Error')
