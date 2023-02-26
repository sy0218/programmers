
def solution(numbers, hand):
    answer = ''
    num_dic = {1:[0,0], 2:[0,1], 3:[0,2],
               4:[1,0], 5:[1,1], 6:[1,2],
               7:[2,0], 8:[2,1], 9:[2,2],
               '*':[3,0], 0:[3,1], '#':[3,2]}
    L_point = num_dic['*']
    R_point = num_dic['#']

    #print(L_point)
    #print(R_point)
    
    
    for i in numbers:
        now_point = num_dic[i]
        if i==1 or i==4 or i==7:
            answer+='L'
            L_point = num_dic[i]
        elif i==3 or i==6 or i==9:
            answer+='R'
            R_point = num_dic[i]
        elif i==2 or i==5 or i==8 or i==0:
            L_dis = abs(L_point[0]-now_point[0])+abs(L_point[1]-now_point[1])
            R_dis = abs(R_point[0]-now_point[0])+abs(R_point[1]-now_point[1])
            
            if L_dis == R_dis:
                if hand == 'right':
                    answer+='R'
                    R_point = num_dic[i]
                else:
                    answer+='L'
                    L_point = num_dic[i]

            elif L_dis < R_dis:
                answer += 'L'
                L_point = num_dic[i]

            elif R_dis < L_dis:
                answer += 'R'
                R_point = num_dic[i]
    print(answer)
    return answer
    
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],'right')
'''
a=[1,2]
b=[0,4]
#print(a[0])
#print(c)
'''