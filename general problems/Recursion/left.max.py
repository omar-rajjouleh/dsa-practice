#return list having the left max number 
#[1,3,5,7,4,2] => [1,3,5,7,7,7]
#[1,2,3] => [1,2,3]
#[] => []
#[1,0,2,0,3] => [1,1,2,2,3]

def left_max(lst):
    if len(lst)<=1:
        return lst
    head= left_max(lst[:-1])
    last=max(head[-1],lst[-1])
    head.append(last)
    return head


print(left_max([8]))



