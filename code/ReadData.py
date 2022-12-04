'''
파일 가져와서 player라는 리스트에 한 선수당 하나의 리스트로 넣기
'''
class ReadDate:
    def __init__(self, filename):
        f = open(filename, "r", encoding='utf-8')
        self.lines = f.readlines()
        self.player = [] # 선수 넣는 리스트
        self.colsize = 0 # colsize계산

    def makePlayerList(self):
        for line in self.lines:
            line = line.split()
            #if int(line[4]) >= 3:
            self.player.append(line)
            self.colsize+=1

    def getPlayerList(self):
        return self.player

    def getColsize(self):
        return self.colsize


