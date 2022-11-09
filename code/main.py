# 클래스 구조
# 1. class Read : 데이터 들어오면 리스트로 split해서 저장하는 클래스
# 2. class Calculate : 선수 하나의 데이터가 담은 리스트가 들어오면 해당 리스트에서 필요한 데이터만 뽑아서 계산해주기
# 아니면 그냥 파워, 컨텍트 능력치 별로 계산하기?

# 해야 할 것
# 1. 모든 선수의 팔요한 column값을 더해서 평균 구하기 -> OK(11/08)
# 2. 해당 선수의 값이 평균과 어느정도 차이가 나는지 + - 값 구하기 -> 대충 개념만 구현(11/08)
# 3. 내야수랑 외야수랑 구분해서 다른 리스트에 넣기 -> for 수비 능력치

# def fprint(s):
#     print(str(s) + f": {s}")


f = open("data01.txt", "r", encoding='utf-8')
lines = f.readlines()


player = [] # 선수 넣는 리스트
colsize = 0 # colsize계산

for line in lines:
    colsize+=1
    player.append(line.split())    

# 컨택트 : 타율(col 23), 출루율(col 24), wOBA(col 27), wRC+(col 28)
# 파워 : 홈런(col 11) , 장타율(col 25)
# 스피드 : 도루(col 14), 병살(col 20)

# 스로잉
# 수비

sumAVG = 0
avgAVG = 0
sumHR = 0
avgHR = 0
sumSLG = 0
avgSLG = 0

# 평균 구하기
for i in range(colsize):
    sumAVG += float(player[i][23])
    sumHR += int(player[i][11])
    sumSLG += float(player[i][25])

avgAVG = sumAVG/colsize
avgHR = sumHR/colsize
avgSLG = sumSLG/colsize

#print(avgAVG)
#print(avgHR)
#print(avgSLG)

maxHR = 0
minHR = 1

# 최대값 최솟값 구하기
for i in range(colsize):
    if (float(player[i][11]) > maxHR):
        maxHR = float(player[i][11])
    if (float(player[i][11]) < minHR):
        minHR = float(player[i][11])

#print(minHR)
#print(maxHR)


#60부터 100이라고 생각?
playerHRPoint = 70


# 자기 자신이 몇번째 칸인지 생각해서 더하기
# 평균보다 높다면: 평균부터 최고점 사이를 100으로 나누고 자신의 능력치가 해당하는 부분의 n/100을 기준 점수인 70에서부터 더하기
# 평균보다 낮으면 반대로 빼주기


# 평균부터 최대까지는 100을 나누기 -> +가중치 tick 
# 평균부터 최소까지는 100을 나누기 -> -가중치 tick
plusTick = (maxHR+avgHR)/100
minusTick = -(minHR+avgHR)/100

def checkPower(playerHRcount, index):
    tempavg = avgHR 
    tickCnt = 0
    if float(playerHRcount[index][11]) >= avgHR:
        while tempavg <= float(player[index][11]):
            tempavg += plusTick # 평균값에서 tick을 더해서 자기 자신의 갯수까지 오기전 까지 처리
            tickCnt += plusTick # 더해진 plusTick 저장
    else:
        while tempavg >= float(playerHRcount[index][11]):
            tempavg += minusTick
            tickCnt += minusTick

    print(f"{player[index][1]}의 파워는 {70 + tickCnt}")


checkPower(player,0)
checkPower(player,1)
checkPower(player,2)
checkPower(player,3)

# print(avgHR)
# print(tempavg)
# print(tickCnt)


# 걍 생각난 계산 방식 코드 *3 대신 알맞은 가중치를 넣자
# for i in range(colsize):
#     if (float(player[i][11]) >= avgHR):
#         playerHRPoint += plusTick * TickHR * 3
#     else:
#         playerHRPoint -= plusTick * TickHR * 3



#print(plusTick)
#print(minusTick)
#print(TickHR)

f.close()