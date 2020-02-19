string=input()
iff=open(string,"r")

Mslices,Ptypes = map(int,iff.readline().split())
Pslices = list(map(int,iff.read().split()))



def subsetsum(array,num):

    
    if len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0])) 
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)
            


x=True
while(x==True):
    ans=subsetsum(Pslices,Mslices)
    if(ans!=None):
        x=False
    Mslices-=1
#print(ans)
finalans=[]
for i in ans:
    finalans.append(Pslices.index(i))
#print(finalans)
arr=string.split(".")[0]+".out"
op=open(arr,"w+")
op.write(str(len(finalans))+"\n"+" ".join(map(str,finalans)))

iff.close()
op.close()