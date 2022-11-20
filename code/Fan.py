# 인기팀을 분석하기 위함 (KT가 프로야구 팀에 합류 이후)
# 게임 내에서 사용되는 인기팀을 구하고 싶었지만 해당하는 데이터는 존재하지 않았다.
class Fan: 
    def __init__(self, filename):
        f = open(filename, "r", encoding='utf-8')
        self.lines = f.readlines()
        self.fan = [] # 팬들의 수 정리
        self.teamFan = [] # 팀별 팬 수
        self.colsize = 0 # colsize계산
        self.team_name = {'삼성':1, '기아':1, '롯데':1, 'LG':1, '두산':1, '한화':1, 'SSG':1, '키움':1, 'NC':1, 'KT':1}

        # class 함수 실행
        self.makeFanList()
        self.cal_fans()
        self.team_name_sort()
        self.printAll()

    # 필요없는 것 지우기
    def makeFanList(self):
        for line in self.lines:
            self.colsize+=1
            self.fan.append(line.split())
        for i in range(self.colsize):
            del(self.fan[i][0])
            self.fan[i].pop()
    
    # 팬 수 더하기
    def cal_fans(self):
        for i in range(10):
            self.teamFan.append(0)
        for i in range(10):
            for j in range(self.colsize - 1):
                self.teamFan[i] = int(self.fan[j][i])

    # 팬들의 수로 sorting
    def team_name_sort(self):
        self.team_name['삼성'] = self.teamFan[0]
        self.team_name['기아'] = self.teamFan[1]
        self.team_name['롯데'] = self.teamFan[2]
        self.team_name['LG'] = self.teamFan[3]
        self.team_name['두산'] = self.teamFan[4]
        self.team_name['한화'] = self.teamFan[5]
        self.team_name['SSG'] = self.teamFan[6]
        self.team_name['키움'] = self.teamFan[7]
        self.team_name['NC'] = self.teamFan[8]
        self.team_name['KT'] = self.teamFan[9]

        self.team_name = sorted(self.team_name.items(), key = (lambda item : item[1]), reverse= True)
        
    def printAll(self):
        print(self.team_name)
