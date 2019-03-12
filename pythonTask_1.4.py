n = int(input())
sl = {}
sp = []
def get_func():
    global command,namespace,parOrVar
    global sl
    mas = sl.get('var')
    sp_var  = []
    sp_namespace = []
    flag = False
    for i in range(len(mas)):
        if parOrVar==mas[i]:
            sp_var.append(i)
    if len(sp_var)!=0:
        for i in range(len(sp_var)):
            if namespace ==sl.get('namespace')[sp_var[i]]:
                flag = True
                break
        if flag:
            return namespace
        else:
            for j in range(len(sl.get('namespace'))):
                if sl.get('namespace')[j]==namespace and sl.get('command')[j]=='create':
                    flag = True
                    break
            if flag:
                return sl.get('parent')[j]
            else:
                return 'None'
    else:
        return 'None'
if 1<=n<=100:
    for i in range(n):
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
                sp.append(command)
                sl['command'] = sp
                sp = []
            if sl.get('namespace')!=None:
                mas = sl.get('namespace')
                for i in range(len(mas)):
                    sp.append(mas[i])
                sp.append(namespace)
                sl['namespace']=sp
                sp=[]
            else:
                sp.append(namespace)
                sl['namespace'] = sp
                sp = []
            if command=='create':
                if sl.get('parent')!=None:
                    mas = sl.get('parent')
                    for i in range(len(mas)):
                        sp.append(mas[i])
                    sp.append(parOrVar)
                    sl['parent']=sp
                    sp=[]
                else:
                    sp.append(parOrVar)
                    sl['parent'] = sp
                    sp = []
                if sl.get('var')!=None:
                    mas = sl.get('var')
                    for i in range(len(mas)):
                        sp.append(mas[i])
                    sp.append('clear')
                    sl['var']=sp
                    sp=[]
                else:
                    sp.append('clear')
                    sl['var'] = sp
                    sp = []
            if command=='add':
                if sl.get('var')!=None:
                    mas = sl.get('var')
                    for i in range(len(mas)):
                        sp.append(mas[i])
                    sp.append(parOrVar)
                    sl['var']=sp
                    sp=[]
                else:
                    sp.append(parOrVar)
                    sl['var'] = sp
                    sp = []
                if sl.get('parent')!=None:
                    mas = sl.get('parent')
                    for i in range(len(mas)):
                        sp.append(mas[i])
                    sp.append('clear')
                    sl['parent']=sp
                    sp=[]
                else:
                    sp.append('clear')
                    sl['parent'] = sp
                    sp = []
        else:
            print(get_func())

else:
    print('Error')
