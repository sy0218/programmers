
def solution(land):
    answer = 0
    for i in range(1,len(land)):
        for j in range(len(land[i])):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    #print(land)
    answer = max(land[len(land)-1])
    #print(answer)
    return answer
solution([[1,2,3,5],
          [5,6,7,8],
          [4,3,2,1]])
