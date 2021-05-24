#코드업 16진법 만들기

a = input()

sixt = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
for k,v in sixt.items():
    if v == a:
        p=k

for i in range(1,16):
    m = p*i//16
    r = p*i%16
    if p*i<16 :
        print(a+"*"+sixt[i]+"="+a)
    else:
        print(a+"*"+sixt[i]+"="+sixt[m]+sixt[r])
