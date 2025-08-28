"""
Deep Reverse V1
normal reverse from python
lst=[1,[2,3,4],[5,6]] if we apply normal reverse from build in python function it will give us [[5,6],[2,3,4],1]

but deep reverse will give [[6,5],[4,3,2],1]
"""

"""
my solution with i and j where i is the start of the list and j is where it end
"""

def deep_reverse(lst,i=0,j=0):
    if i>j:
        return

    first=lst[i]
    second=lst[j]

    if isinstance(first,list):
        deep_reverse(first,0,len(first)-1)
    if isinstance(second,list) and i!=j:
        deep_reverse(second,0,len(second)-1)

    lst[i],lst[j]=second,first
    deep_reverse(lst,i+1,j-1)


lst=[1,[2,3,4],[5,[6,7,8]]]
deep_reverse(lst,0,len(lst)-1)

print(lst)



