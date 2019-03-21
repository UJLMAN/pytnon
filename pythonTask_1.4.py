n = int(input())
sl = {'command': None, 'namespace': None, 'parent': None, 'var': None}
sp = []

def create():
    global command,namespace,parOrVar
    global sl
    sp_cr = []
    if sl.get('command')!=None:
        sp_cr = sl.get('command')
        sp_cr.append(command)
        sl['command'] = sp_cr
        sp_cr = []
        sp_cr = sl.get('namespace')
        sp_cr.append(namespace)
        sl['namespace'] = sp_cr
        sp_cr = []
        sp_cr = sl.get('var')
        sp_cr.append(parOrVar)
        sl['var'] = sp_cr
        sp_cr = []
        sp_cr = sl.get('parent')
        sp_cr.append('None')
        sl['parent'] = sp_cr
        sp_cr = []
def add():
    global command,namespace,parOrVar
    global sl
    sp_cr = []
    sp_cr = sl.get('command')
    sp_cr.append(command)
    sl['command'] = sp_cr
    sp_cr = []
    sp_cr = sl.get('namespace')
    sp_cr.append(namespace)
    sl['namespace'] = sp_cr
    sp_cr = []
    sp_cr = sl.get('var')
    sp_cr.append('None')
    sl['var'] = sp_cr
    sp_cr = []
    sp_cr = sl.get('parent')
    sp_cr.append(parOrVar)
    sl['parent'] = sp_cr
    sp_cr = []
def poisk(namespace,pos):
    global sl
    for i in range(sl.get('namespace')):
        if namespace==sl.get('namespace')[i] and sl.get('command')[i] == 'create':

def get_func():
    global command,namespace,parOrVar
    global sl
    mas = sl.get('var')
    sp_num = []
    sp_ns = []
    flag = False
    rez = ''
    for i in range(len(mas)):
        if mas[i]==parOrVar:
            sp_num.append(i)
    if len(sp_num)>1:
        for i in range(len(sp_num)):
            if sl.get('namespace')[sp_num[i]] == namespace:
                flag = True
                rez = namespace
                break
            else:
                sp_ns = sl.get('namespace')


    elif len(sp_num)==1:
        if sl.get('namespace')[sp_num[0]] == namespace:
            flag = True
            rez = namespace
        else:



if 1<=n<=100:
    for i in range(n):
        command, namespace, parOrVar = input().split()
        if command == 'create':
            create()
        elif command=='add':
            add()
        elif command == 'get':
            get_func()
else:
    print('Error')