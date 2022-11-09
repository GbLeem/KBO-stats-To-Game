class Power:
    def __init__(self, playerList, colsize):
        self.sumHR = 0
        self.avgHR = 0
        self.maxHR = 0
        self.minHR = 1

        self.sumSLG = 0
        self.avgSLG = 0
        self.maxSLG = 0
        self.minSLG = 0.3

        self.playerList = playerList
        self.col = colsize

    def cal_sum(self):
        for i in range(self.col):
            self.sumHR += float(self.playerList[i][11])
            self.sumSLG += float(self.playerList[i][25])

    def cal_avg(self):
        self.avgHR = self.sumHR / self.col
        self.avgSLG = self.avgSLG / self.col

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
                temp_avgSLG += plusSLG # 평균값에서 tick을 더해서 자기 자신의 갯수까지 오기전 까지 처리
                tick_SLG += plusSLG # 더해진 plusTick 저장
        else:
            while temp_avgSLG >= float(playerlist[index][11]):
                temp_avgSLG += minusSLG
                tick_SLG += minusSLG

        print(f"tickHR : {tick_HR}, tickSLG : {tick_SLG}")

        return playerPower + (tick_HR*2 + tick_SLG)/3

    def printAll(self):
        print(f"maxHR : {self.maxHR}\nminHR : {self.minHR} \navgHR : {self.avgHR} \n")

