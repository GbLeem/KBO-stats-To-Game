'''
파워 계산
홈런-11, 장타율-25
'''
class Power:
    def __init__(self, playerList, colsize):
        #for power
        self.sumHR = 0
        self.avgHR = 0
        self.maxHR = 0
        self.minHR = 1

        self.sumSLG = 0
        self.avgSLG = 0
        self.maxSLG = 0
        self.minSLG = 0.3

        #get player list
        self.playerList = playerList
        self.col = colsize

    def cal_sum(self):
        for i in range(self.col):
            self.sumHR += float(self.playerList[i][11])
            self.sumSLG += float(self.playerList[i][25])

    def cal_avg(self):
        self.avgHR = self.sumHR / self.col
        self.avgSLG = self.sumSLG / self.col

    def cal_max_min(self):
        for i in range(self.col):
            if float(self.playerList[i][11]) > self.maxHR:
                self.maxHR = float(self.playerList[i][11])
            if float(self.playerList[i][11]) < self.minHR:
                self.minHR = float(self.playerList[i][11])
        
        for i in range(self.col):
            if float(self.playerList[i][25]) > self.maxSLG:
                self.maxSLG = float(self.playerList[i][25])
            if float(self.playerList[i][25]) < self.minSLG:
                self.minSLG = float(self.playerList[i][25])

    def cal_power(self, playerlist, index):
        plusPower = (self.maxHR + self.avgHR) / 100
        minusPower = -(self.minHR + self.avgHR) / 100

        plusSLG = (self.maxSLG + self.avgSLG) / 100
        minusSLG = -(self.minSLG + self.avgSLG) / 100

        temp_avgHR = self.avgHR
        temp_avgSLG = self.avgSLG
        
        tick_HR = 0
        tick_SLG = 0

        playerPower = 70

        if float(playerlist[index][11]) >= self.avgHR:
            while temp_avgHR <= float(playerlist[index][11]):
                temp_avgHR += plusPower # 평균값에서 tick을 더해서 자기 자신의 갯수까지 오기전 까지 처리
                tick_HR += plusPower # 더해진 plusTick 저장
        else:
            while temp_avgHR >= float(playerlist[index][11]):
                temp_avgHR += minusPower
                tick_HR += minusPower

        if float(playerlist[index][25]) >= self.avgSLG:
            while temp_avgSLG <= float(playerlist[index][11]):
                temp_avgSLG += plusSLG 
                tick_SLG += plusSLG 
        else:
            while temp_avgSLG >= float(playerlist[index][11]):
                temp_avgSLG += minusSLG
                tick_SLG += minusSLG

        #print(f"{tick_HR}, {tick_SLG}")
        return playerPower + (tick_HR*2 + tick_SLG)/3


    def printAll(self):
        print(f"maxHR : {self.maxHR}\nminHR : {self.minHR} \navgHR : {self.avgHR} \n")


'''
스피드 계산
도루, 도루 성공률, 병살타
'''
class Speed:
    def __init__(self, playerList, colsize):
        #for speed
        self.sumRunRatio = 0
        self.avgRunRatio = 0
        self.maxRunRatio = 0
        self.minRunRatio = 0
        
        self.runRatio = []

        self.sumRun = 0
        self.avgRun = 0
        self.maxRun = 0
        self.minRun = 0

        self.sumDoublePlay = 0
        self.avgDoublePlay = 0
        self.maxDoublePlay = 0
        self.minDoublePlay = 0

        #get player list
        self.playerList = playerList
        self.col = colsize

    def cal_run_ratio(self):
        for i in range(self.col):
            self.runRatio.append(0)

        for i in range(self.col):
            if(int(self.playerList[i][14]) != 0 and int(self.playerList[i][15]) == 0):
                self.runRatio[i] = 100
            elif(int(self.playerList[i][14]) == 0 and int(self.playerList[i][15]) == 0):
                self.runRatio[i] = 0 
            else:
                self.runRatio[i] = (int(self.playerList[i][14]) / (int(self.playerList[i][14])+int(self.playerList[i][15]))* 100) 

            
    def cal_sum(self):
        for i in range(self.col):
            self.sumRun += int(self.playerList[i][14])
            self.sumRunRatio += self.runRatio[i]
            self.sumDoublePlay += float(self.playerList[i][20])

    def cal_avg(self):
        self.avgRun = self.sumRun / self.col
        self.avgRunRatio = self.sumRunRatio / self.col
        self.avgDoublePlay = self.sumDoublePlay / self.col

    def cal_max_min(self):
        for i in range(self.col):
            if float(self.playerList[i][14]) > self.maxRun:
                self.maxRun = float(self.playerList[i][14])
            if float(self.playerList[i][14]) < self.minRun:
                self.minRun = float(self.playerList[i][14])

        for i in range(self.col):
            if float(self.runRatio[i]) > self.maxRunRatio:
                self.maxRunRatio = float(self.runRatio[i])
            if float(self.runRatio[i]) < self.minRunRatio:
                self.minRunRatio = float(self.runRatio[i])
        
        for i in range(self.col):
            if float(self.playerList[i][20]) > self.maxDoublePlay:
                self.maxDoublePlay = float(self.playerList[i][20])
            if float(self.playerList[i][20]) < self.minDoublePlay:
                self.minDoublePlay = float(self.playerList[i][20])

    def cal_speed(self, playerlist, index):
        plusRun = (self.maxRun + self.avgRun) / 100
        minusRun = -(self.minRun + self.avgRun) / 100
        
        plusRunRatio = (self.maxRunRatio + self.avgRunRatio) / 100
        minusRunRatio = -(self.minRunRatio + self.avgRunRatio) / 100

        plusDoublePlay = (self.maxDoublePlay + self.avgDoublePlay) / 100
        minusDoublePlay = -(self.minDoublePlay + self.avgDoublePlay) / 100

        # average temporary
        temp_avgRun = self.avgRun
        temp_avgRunRatio = self.avgRunRatio
        temp_avgDoublePlay = self.avgDoublePlay
        
        tick_Run = 0
        tick_RunRatio = 0
        tick_DoublePlay = 0

        playerSpeed = 70

        # use number of run
        if float(playerlist[index][14]) >= self.avgRun:
            while temp_avgRun <= float(playerlist[index][14]):
                temp_avgRun += plusRun 
                tick_Run += plusRun 
        else:
            while temp_avgRun >= float(playerlist[index][14]):
                temp_avgRun += minusRun
                tick_Run += minusRun

        # use ratio of run
        if float(self.runRatio[index]) >= self.avgRunRatio:
            while temp_avgRunRatio <= float(self.runRatio[index]):
                temp_avgRunRatio += plusRunRatio 
                tick_RunRatio += plusRunRatio 
        else:
            while temp_avgRunRatio >= float(self.runRatio[index]):
                temp_avgRunRatio += minusRunRatio
                tick_RunRatio += minusRunRatio

        # use double play
        if float(playerlist[index][20]) >= self.avgDoublePlay:
            while temp_avgDoublePlay <= float(playerlist[index][20]):
                temp_avgDoublePlay += plusDoublePlay
                tick_DoublePlay += plusDoublePlay 
        else:
            while temp_avgDoublePlay >= float(playerlist[index][20]):
                temp_avgDoublePlay += minusDoublePlay
                tick_DoublePlay += minusDoublePlay

        #print(f"{tick_Run}, {tick_RunRatio}, {tick_DoublePlay}")

        return playerSpeed + (tick_Run + tick_RunRatio/2 - tick_DoublePlay)/5
        

    def printAll(self):
        print(f"maxRun : {self.maxRun}\nminRun : {self.minRun} \navgRun : {self.avgRun} \n")
        print(f"maxRunRatio : {self.maxRunRatio}\nminRunRatio : {self.minRunRatio} \navgRunRatio : {self.avgRunRatio} \n")


'''
컨텍트 계산
타율-23, 출루율(OBP)-24
'''
class Contact:
    def __init__(self, playerList, colsize):
        self.sumAverage = 0
        self.avgAverage = 0
        self.maxAverage = 0
        self.minAverage = 0.3
        
        self.sumOBP = 0
        self.avgOBP = 0
        self.maxOBP = 0
        self.minOBP = 0.3

        #get player list
        self.playerList = playerList
        self.col = colsize
            
    def cal_sum(self):
        for i in range(self.col):
            self.sumAverage += float(self.playerList[i][23])
            self.sumOBP += float(self.playerList[i][24])

    def cal_avg(self):
        self.avgAverage = self.sumAverage / self.col
        self.avgOBP = self.sumOBP / self.col

    def cal_max_min(self):
        for i in range(self.col):
            if float(self.playerList[i][23]) > self.maxAverage:
                self.maxAverage = float(self.playerList[i][23])
            if float(self.playerList[i][23]) < self.minAverage:
                self.minAverage = float(self.playerList[i][23])

        for i in range(self.col):
            if float(self.playerList[i][24]) > self.maxOBP:
                self.maxOBP = float(self.playerList[i][24])
            if float(self.playerList[i][24]) < self.minOBP:
                self.minOBP = float(self.playerList[i][24])

    def cal_contact(self, playerlist, index):
        plusAverage = (self.maxAverage + self.avgAverage) / 100
        minusAverage = -(self.minAverage + self.avgAverage) / 100

        plusOBP = (self.maxOBP + self.avgOBP) / 100
        minusOBP = -(self.minOBP + self.avgOBP) / 100

        # average temporary
        temp_avgAverage = self.avgAverage
        temp_avgOBP = self.avgOBP
        
        tick_Average = 0
        tick_OBP = 0

        playerContact = 70

        # use average
        if float(playerlist[index][23]) >= self.avgAverage:
            while temp_avgAverage <= float(playerlist[index][23]):
                temp_avgAverage += plusAverage 
                tick_Average += plusAverage 
        else:
            while temp_avgAverage >= float(playerlist[index][23]):
                temp_avgAverage += minusAverage
                tick_Average += minusAverage

        # use OBP
        if float(playerlist[index][24]) >= self.avgOBP:
            while temp_avgOBP <= float(playerlist[index][24]):
                temp_avgOBP += plusOBP
                tick_OBP += plusOBP 
        else:
            while temp_avgOBP >= float(playerlist[index][24]):
                temp_avgOBP += minusOBP
                tick_OBP += minusOBP

        #print(f"{tick_Average}, {tick_OBP}")

        return playerContact + (tick_OBP + tick_Average) * 100
        

    def printAll(self):
        print(f"maxAverage : {self.maxAverage}\nminAverage : {self.minAverage} \navgAverage : {self.avgAverage} \n")
        print(f"maxOBP : {self.maxOBP}\nminOBP : {self.minOBP} \navgOBP : {self.avgOBP} \n")


'''
스로잉 계산
보살(BK) - 9, 외야수인 경우 BK - 9 + ARM - 14
'''
class Throwing:
    def __init__(self, playerList, colsize):
        self.sumBK = 0 # int
        self.avgBK = 0
        self.maxBK = 0
        self.minBK = 0
        
        self.sumARM = 0. # float
        self.avgARM = 0.
        self.maxARM = 0.
        self.minARM = 0.

        #get player list
        self.playerList = playerList
        self.col = colsize
            
    def cal_sum(self):
        for i in range(self.col):
            self.sumBK += int(self.playerList[i][9])
            if float(self.playerList[i][14]) != 0:
                self.sumARM += float(self.playerList[i][14])

    def cal_avg(self):
        self.avgBK = self.sumBK / self.col
        self.avgARM = self.sumARM / self.col

    def cal_max_min(self):
        for i in range(self.col):
            if int(self.playerList[i][9]) > self.maxBK:
                self.maxBK = int(self.playerList[i][9])
            if float(self.playerList[i][9]) < self.minBK:
                self.minBK = float(self.playerList[i][9])

        for i in range(self.col):
            if float(self.playerList[i][14]) != 0:
                if float(self.playerList[i][14]) > self.maxARM:
                    self.maxARM = float(self.playerList[i][14])
                if float(self.playerList[i][14]) < self.minARM:
                    self.minARM = float(self.playerList[i][14])

    def cal_throwing(self, playerlist, index):
        plusBK = (self.maxBK + self.avgBK) / 100
        minusBK = -(self.minBK + self.avgBK) / 100

        plusARM = (self.maxARM + self.avgARM) / 100
        minusARM = -(self.minARM + self.avgARM) / 100

        # average temporary
        temp_avgBK = self.avgBK
        temp_avgARM = self.avgARM
        
        tick_BK = 0
        tick_ARM = 0

        playerThrowing = 70

        # use BK
        if float(playerlist[index][9]) >= self.avgBK:
            while temp_avgBK <= float(playerlist[index][9]):
                temp_avgBK += plusBK 
                tick_BK += plusBK 
        else:
            while temp_avgBK >= float(playerlist[index][9]):
                temp_avgBK += minusBK
                tick_BK += minusBK

        # use ARM
        if float(playerlist[index][14]) != 0:
            if float(playerlist[index][14]) >= self.avgARM:
                while temp_avgARM <= float(playerlist[index][14]):
                    temp_avgARM += plusARM
                    tick_ARM += plusARM 
            else:
                while temp_avgARM >= float(playerlist[index][14]):
                    temp_avgARM -= minusARM
                    tick_ARM += minusARM

        #print(f"{tick_BK}, {tick_ARM}")

        if tick_ARM == 0:
            return playerThrowing + tick_BK/15  #비율 조정을 위한 나눗셈
        else:
            return playerThrowing + tick_BK+tick_ARM*2
        
        

    def printAll(self):
        print(f"maxBK : {self.maxBK}\nminBK : {self.minBK} \navgBK : {self.avgBK} \n")
        print(f"maxARM : {self.maxARM}\nminARM : {self.minARM} \navgARM : {self.avgARM} \n")


'''
수비 계산
수비율(FP)-10, WWA-3 
'''
class Defense:
    def __init__(self, playerList, colsize):
        self.sumFP = 0 # int
        self.avgFP = 0
        self.maxFP = 0
        self.minFP = 0
        
        self.sumWWA = 0. # float
        self.avgWWA = 0.
        self.maxWWA = 0.
        self.minWWA = 0.

        #get player list
        self.playerList = playerList
        self.col = colsize
            
    def cal_sum(self):
        for i in range(self.col):
            self.sumFP += int(self.playerList[i][10])
            #if float(self.playerList[i][14]) != 0:
            self.sumWWA += float(self.playerList[i][3])

    def cal_avg(self):
        self.avgFP = self.sumFP / self.col
        self.avgWWWA = self.sumWWA / self.col

    def cal_max_min(self):
        for i in range(self.col):
            if int(self.playerList[i][10]) > self.maxFP:
                self.maxFP = int(self.playerList[i][10])
            if float(self.playerList[i][10]) < self.minFP:
                self.minFP = float(self.playerList[i][10])

        for i in range(self.col):
            #if float(self.playerList[i][14]) != 0:
            if float(self.playerList[i][3]) > self.maxWWA:
                self.maxWWA = float(self.playerList[i][3])
            if float(self.playerList[i][3]) < self.minWWA:
                self.minWWA = float(self.playerList[i][3])

    def cal_defense(self, playerlist, index):
        plusFP = (self.maxFP + self.avgFP) / 100
        minusFP = -(self.minFP + self.avgFP) / 100

        plusWWA = (self.maxWWA + self.avgWWA) / 100
        minusWWA = -(self.minWWA + self.avgWWA) / 100

        # average temporary
        temp_avgFP = self.avgFP
        temp_avgWWA = self.avgWWA
        
        tick_FP = 0
        tick_WWA = 0

        playerDefense = 70

        # use BK
        if float(playerlist[index][10]) >= self.avgFP:
            while temp_avgFP <= float(playerlist[index][10]):
                temp_avgFP += plusFP 
                tick_FP += plusFP 
        else:
            while temp_avgFP >= float(playerlist[index][10]):
                temp_avgFP += minusFP
                tick_FP += minusFP

        # use ARM
        #if float(playerlist[index][14]) != 0:
        if float(playerlist[index][3]) >= self.avgWWA:
            while temp_avgWWA <= float(playerlist[index][3]):
                temp_avgWWA += plusWWA
                tick_WWA += plusWWA 
        else:
            while temp_avgWWA >= float(playerlist[index][3]):
                temp_avgWWA -= minusWWA
                tick_WWA += minusWWA

        #print(f"{tick_FP}, {tick_WWA}")


        return playerDefense + tick_FP + tick_WWA