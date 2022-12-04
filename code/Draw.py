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
        x = ["power","contact","speed","throwing","defense"]
        index = np.arange(len(x))
        ma9Y = [float(ma9playerlist[self.ma9index][1]),float(ma9playerlist[self.ma9index][2]),float(ma9playerlist[self.ma9index][3]),float(ma9playerlist[self.ma9index][4]),float(ma9playerlist[self.ma9index][5])]
        plt.title(self.name, fontsize=20)
        plt.bar(index, self.calculate_list, color="blue",width=0.35)
        plt.bar(index+0.35, ma9Y, color="red",width=0.35)
        plt.xticks(index, x, fontsize=15)
        plt.show()

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

    def draw_all(self):
        self.calcuate_all()
        x = ["power","contact","speed","throwing","defense"]
        index = np.arange(len(x))
        ma9Y = [float(ma9playerlist[self.ma9index][1]),float(ma9playerlist[self.ma9index][2]),float(ma9playerlist[self.ma9index][3]),float(ma9playerlist[self.ma9index][4]),float(ma9playerlist[self.ma9index][5])]
        plt.title(self.name, fontsize=20)
        plt.bar(index, self.calculate_list, color="blue",width=0.35)
        plt.bar(index+0.35, ma9Y, color="red",width=0.35)
        plt.xticks(index, x, fontsize=15)
        plt.show()