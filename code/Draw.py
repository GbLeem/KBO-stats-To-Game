from matplotlib import pyplot as plt
import numpy as np

# 한글 출력
import matplotlib
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

# my module
import Calculate as c
import ReadData as r

# read txt file
data = r.ReadDate("data/data01.txt")
data.makePlayerList()
playerList = data.getPlayerList()

IF = r.ReadDate("data/IF.txt")
IF.makePlayerList()
playerIFList = IF.getPlayerList()

OF = r.ReadDate("data/OF.txt")
OF.makePlayerList()
playerOFList = OF.getPlayerList()

ma9data = r.ReadDate("data/ma9data01.txt")
ma9data.makePlayerList()
ma9playerlist = ma9data.getPlayerList()

# calculate power, contact, speed
power = c.Power(playerList, data.getColsize())
power.cal_sum()
power.cal_avg()
power.cal_max_min()

speed = c.Speed(playerList,data.getColsize())
speed.cal_run_ratio()
speed.cal_sum()
speed.cal_avg()
speed.cal_max_min()

contact = c.Contact(playerList,data.getColsize())
contact.cal_sum()
contact.cal_avg()
contact.cal_max_min()

# caculate defense, throwing
IFthrowing = c.Throwing(playerIFList,IF.getColsize())
OFthrowing = c.Throwing(playerOFList,OF.getColsize())

IFthrowing.cal_sum()
IFthrowing.cal_avg()
IFthrowing.cal_max_min()

OFthrowing.cal_sum()
OFthrowing.cal_avg()
OFthrowing.cal_max_min()

IFdefense = c.Defense(playerIFList,IF.getColsize())
OFdefense = c.Defense(playerOFList,OF.getColsize())

IFdefense.cal_sum()
IFdefense.cal_avg()
IFdefense.cal_max_min()

OFdefense.cal_sum()
OFdefense.cal_avg()
OFdefense.cal_max_min()

# print class

# 내야수 선수를 마구마구 데이터와 비교할 때 사용하는 클래스
class IFPlayer():
    def __init__(self,index1,index2, index3):
        self.pcsindex = index1
        self.tdindex = index2
        self.ma9index = index3
        self.name = playerList[self.pcsindex][1]
        self.calculate_list = []
        
    def calcuate_all(self):
        self.calculate_list.append(power.cal_power(playerList, self.pcsindex))
        self.calculate_list.append(contact.cal_contact(playerList, self.pcsindex))
        self.calculate_list.append(speed.cal_speed(playerList, self.pcsindex))

        self.calculate_list.append(IFthrowing.cal_throwing(playerIFList, self.tdindex))
        self.calculate_list.append(IFdefense.cal_defense(playerIFList, self.tdindex))
        

    def print_all(self):
        #print(f"{playerList[self.pcsindex][1]}")
        print(self.calculate_list)

    def draw_all(self):
        self.calcuate_all()
        ma9Y = [float(ma9playerlist[self.ma9index][1]),float(ma9playerlist[self.ma9index][2]),float(ma9playerlist[self.ma9index][3]),float(ma9playerlist[self.ma9index][4]),float(ma9playerlist[self.ma9index][5])]
        ma9Y = [*ma9Y, ma9Y[0]]
        self.calculate_list = [*self.calculate_list, self.calculate_list[0]]
        x = ["power","contact","speed","throwing","defense"]
        x = [*x, x[0]]
        
        index = np.linspace(start = 0, stop = 2*np.pi, num = len(self.calculate_list))

        plt.figure(figsize=(6,6))
        ax = plt.subplot(polar =True)

        plt.title(self.name, fontsize=20)
        plt.xticks(index, labels=x, fontsize= 13)
        ax.plot(index, self.calculate_list, color="blue",label= "기록 데이터")
        ax.fill(index, self.calculate_list, color="skyblue",alpha=0.3)
        ax.plot(index, ma9Y, color = "red", label = "마구마구 데이터")
        ax.fill(index, ma9Y, color = "violet",alpha= 0.3)
        ax.legend(loc = "upper left", ncol =1)
        plt.show()


# 외야수 선수를 마구마구 데이터와 비교할 때 사용하는 클래스
class OFPlayer():
    def __init__(self,index1,index2, index3):
        self.pcsindex = index1
        self.tdindex = index2
        self.ma9index = index3
        self.name = playerList[self.pcsindex][1]
        self.calculate_list = []
        
    def calcuate_all(self):
        self.calculate_list.append(power.cal_power(playerList, self.pcsindex))
        self.calculate_list.append(contact.cal_contact(playerList, self.pcsindex))
        self.calculate_list.append(speed.cal_speed(playerList, self.pcsindex))

        self.calculate_list.append(OFthrowing.cal_throwing(playerOFList, self.tdindex))
        self.calculate_list.append(OFdefense.cal_defense(playerOFList, self.tdindex))
        
    def print_all(self):
        #print(f"{playerList[self.pcsindex][1]}")
        print(self.calculate_list)

    # 방사형으로 그리기
    def draw_all(self):
        self.calcuate_all()
        ma9Y = [float(ma9playerlist[self.ma9index][1]),float(ma9playerlist[self.ma9index][2]),float(ma9playerlist[self.ma9index][3]),float(ma9playerlist[self.ma9index][4]),float(ma9playerlist[self.ma9index][5])]
        ma9Y = [*ma9Y, ma9Y[0]]
        self.calculate_list = [*self.calculate_list, self.calculate_list[0]]
        x = ["power","contact","speed","throwing","defense"]
        x = [*x, x[0]]
        
        index = np.linspace(start = 0, stop = 2*np.pi, num = len(self.calculate_list))

        plt.figure(figsize=(6,6))
        ax = plt.subplot(polar =True)

        plt.title(self.name, fontsize=20)
        plt.xticks(index, labels=x, fontsize= 13)
        ax.plot(index, self.calculate_list, color="blue",label= "기록 데이터")
        ax.fill(index, self.calculate_list, color="skyblue",alpha=0.3)
        ax.plot(index, ma9Y, color = "red", label = "마구마구 데이터")
        ax.fill(index, ma9Y, color = "violet",alpha= 0.3)
        ax.legend(loc = "upper left", ncol =1)
        plt.show()


# 특정 선수 두명을 비교하여 출력하는 코드 - 실제 데이터 / 마구마구 데이터
class CompareIFPlayer():
    def __init__(self, player1_index1,player1_index2, player1_ma9, player2_index1, player2_index2, player2_ma9):
        self.p1_pcsindex = player1_index1
        self.p1_tdindex = player1_index2
        self.p1_ma9index = player1_ma9
        self.p1_name = playerList[self.p1_pcsindex][1]
        self.p1_calculate_list = []
        
        self.p2_pcsindex = player2_index1
        self.p2_tdindex = player2_index2
        self.p2_ma9index = player2_ma9
        self.p2_name = playerList[self.p2_pcsindex][1]
        self.p2_calculate_list = []
        
    def calcuate_all(self):
        # player1
        self.p1_calculate_list.append(power.cal_power(playerList, self.p1_pcsindex))
        self.p1_calculate_list.append(contact.cal_contact(playerList, self.p1_pcsindex))
        self.p1_calculate_list.append(speed.cal_speed(playerList, self.p1_pcsindex))

        self.p1_calculate_list.append(IFthrowing.cal_throwing(playerIFList, self.p1_tdindex))
        self.p1_calculate_list.append(IFdefense.cal_defense(playerIFList, self.p1_tdindex))
        
        # player2
        self.p2_calculate_list.append(power.cal_power(playerList, self.p2_pcsindex))
        self.p2_calculate_list.append(contact.cal_contact(playerList, self.p2_pcsindex))
        self.p2_calculate_list.append(speed.cal_speed(playerList, self.p2_pcsindex))

        self.p2_calculate_list.append(IFthrowing.cal_throwing(playerIFList, self.p2_tdindex))
        self.p2_calculate_list.append(IFdefense.cal_defense(playerIFList, self.p2_tdindex))

    def print_all(self):
        #print(f"{playerList[self.pcsindex][1]}")
        print(f"{self.p1_calculate_list},{self.p2_calculate_list}")

    def draw_all(self):
        self.calcuate_all()
        x = ["power","contact","speed","throwing","defense"]
        index = np.arange(len(x))

        ma9_1Y = [float(ma9playerlist[self.p1_ma9index][1]),float(ma9playerlist[self.p1_ma9index][2]),float(ma9playerlist[self.p1_ma9index][3]),float(ma9playerlist[self.p1_ma9index][4]),float(ma9playerlist[self.p1_ma9index][5])]
        ma9_2Y = [float(ma9playerlist[self.p2_ma9index][1]),float(ma9playerlist[self.p2_ma9index][2]),float(ma9playerlist[self.p2_ma9index][3]),float(ma9playerlist[self.p2_ma9index][4]),float(ma9playerlist[self.p2_ma9index][5])]

        plt.subplots(constrained_layout=True)
        plt.subplot(211)
        plt.title(f"실제 기록을 통한 능력치 : {self.p1_name} vs {self.p2_name}" , fontsize=15)
        plt.bar(index, self.p1_calculate_list, color="blue", width=0.35)
        plt.bar(index+0.35, self.p2_calculate_list, color="red", width=0.35)
        plt.xticks(index, x, fontsize=15)

        plt.subplot(212)
        plt.title(f"마구마구 능력치 : {self.p1_name} vs {self.p2_name}" , fontsize=15)
        plt.bar(index, ma9_1Y, color="blue", width=0.35)
        plt.bar(index+0.35, ma9_2Y, color="red", width=0.35)
        plt.xticks(index, x, fontsize=15)

        plt.show()


# 외야수 선수 두명을 비교하여 출력하는 코드 - 실제 데이터 / 마구마구 데이터
class CompareOFPlayer():
    def __init__(self, player1_index1,player1_index2, player1_ma9, player2_index1, player2_index2, player2_ma9):
        self.p1_pcsindex = player1_index1
        self.p1_tdindex = player1_index2
        self.p1_ma9index = player1_ma9
        self.p1_name = playerList[self.p1_pcsindex][1]
        self.p1_calculate_list = []
        
        self.p2_pcsindex = player2_index1
        self.p2_tdindex = player2_index2
        self.p2_ma9index = player2_ma9
        self.p2_name = playerList[self.p2_pcsindex][1]
        self.p2_calculate_list = []
        
    def calcuate_all(self):
        # player1
        self.p1_calculate_list.append(power.cal_power(playerList, self.p1_pcsindex))
        self.p1_calculate_list.append(contact.cal_contact(playerList, self.p1_pcsindex))
        self.p1_calculate_list.append(speed.cal_speed(playerList, self.p1_pcsindex))

        self.p1_calculate_list.append(OFthrowing.cal_throwing(playerOFList, self.p1_tdindex))
        self.p1_calculate_list.append(OFdefense.cal_defense(playerOFList, self.p1_tdindex))
        
        # player2
        self.p2_calculate_list.append(power.cal_power(playerList, self.p2_pcsindex))
        self.p2_calculate_list.append(contact.cal_contact(playerList, self.p2_pcsindex))
        self.p2_calculate_list.append(speed.cal_speed(playerList, self.p2_pcsindex))

        self.p2_calculate_list.append(OFthrowing.cal_throwing(playerOFList, self.p2_tdindex))
        self.p2_calculate_list.append(OFdefense.cal_defense(playerOFList, self.p2_tdindex))

    def print_all(self):
        #print(f"{playerList[self.pcsindex][1]}")
        print(f"{self.p1_calculate_list},{self.p2_calculate_list}")

    def draw_all(self):
        self.calcuate_all()
        x = ["power","contact","speed","throwing","defense"]
        index = np.arange(len(x))

        ma9_1Y = [float(ma9playerlist[self.p1_ma9index][1]),float(ma9playerlist[self.p1_ma9index][2]),float(ma9playerlist[self.p1_ma9index][3]),float(ma9playerlist[self.p1_ma9index][4]),float(ma9playerlist[self.p1_ma9index][5])]
        ma9_2Y = [float(ma9playerlist[self.p2_ma9index][1]),float(ma9playerlist[self.p2_ma9index][2]),float(ma9playerlist[self.p2_ma9index][3]),float(ma9playerlist[self.p2_ma9index][4]),float(ma9playerlist[self.p2_ma9index][5])]


        # 그래프에 이름 써주기
        #plt.figure(1)
        plt.subplots(constrained_layout=True)
        plt.subplot(211)
        plt.title(f"실제 기록을 통한 능력치 : {self.p1_name} vs {self.p2_name}" , fontsize=15)
        plt.bar(index, self.p1_calculate_list, color="blue", width=0.35)
        plt.bar(index+0.35, self.p2_calculate_list, color="red", width=0.35)
        plt.xticks(index, x, fontsize=15)
        #plt.figure(2)
        plt.subplot(212)
        plt.title(f"마구마구 능력치 : {self.p1_name} vs {self.p2_name}" , fontsize=15)
        plt.bar(index, ma9_1Y, color="blue", width=0.35)
        plt.bar(index+0.35, ma9_2Y, color="red", width=0.35)
        plt.xticks(index, x, fontsize=15)

        plt.show()
