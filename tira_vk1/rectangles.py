def area(rec1, rec2, rec3):
    return (
        rec_area(rec1) 
        + rec_area(rec2) 
        + rec_area(rec3) 
        - rec_area(overlapping_square(rec1,rec2)) 
        - rec_area(overlapping_square(rec1,rec3)) 
        - rec_area(overlapping_square(rec2,rec3)) 
        + rec_area(overlapping_square(overlapping_square(rec1,rec2),overlapping_square(rec2,rec3)))
        )

def overlapping_square(rec1,rec2):
    x1=max(rec1[0],rec2[0])
    x2=min(rec1[2],rec2[2])
    y1=min(rec1[1],rec2[1])
    y2=max(rec1[3],rec2[3])
    if (x1>x2 or y1<y2):
        return (0,0,0,0)
    return (x1,y1,x2,y2)

def rec_area(rec):
    return abs(rec[0]-rec[2])*abs(rec[1]-rec[3])

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16
    print(area([2,-1,3,-3],[0,2,3,0],[-3,0,1,-1]))#12
    # print(overlapping_square(rec1,rec2))
    # print(overlapping_square(rec1,(4,5,6,3)))
    print(overlapping_square([2,-1,3,-3],[0,2,3,0]))
    # print(rec_area((0,0,0,0)))
