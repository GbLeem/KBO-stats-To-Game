from matplotlib import pyplot as plt
import numpy as np

import ReadData as r
import Calculate as c
import Fan as F


data01 = r.ReadDate("data/data01.txt")
data01.makePlayerList()
playerList01 = data01.getPlayerList()
#print(playerList01[149])

#==================================================

power = c.Power(playerList01, data01.getColsize())

power.cal_sum()
power.cal_avg()
power.cal_max_min()

# player01_power = power.cal_power(playerList01, 0)
# player02_power = power.cal_power(playerList01, 1)
# player03_power = power.cal_power(playerList01, 2)
# player04_power = power.cal_power(playerList01, 3)
# player05_power = power.cal_power(playerList01, 4)

# # player100_power = power.cal_power(playerList01, 99)
# player14_power = power.cal_power(playerList01, 13)

# print("===power===\n")
# print(f"{playerList01[0][1]}의 파워는 {player01_power}")
# print(f"{playerList01[1][1]}의 파워는 {player02_power}")
# print(f"{playerList01[2][1]}의 파워는 {player03_power}")
# print(f"{playerList01[3][1]}의 파워는 {player04_power}")
# print(f"{playerList01[4][1]}의 파워는 {player05_power}")

# print(f"{playerList01[13][1]}의 파워는 {player14_power}")

#==================================================

speed = c.Speed(playerList01,data01.getColsize())

speed.cal_run_ratio()
speed.cal_sum()
speed.cal_avg()
speed.cal_max_min()

# player01_speed = speed.cal_speed(playerList01, 0)
# player02_speed = speed.cal_speed(playerList01, 1)
# player03_speed = speed.cal_speed(playerList01, 2)
# player04_speed = speed.cal_speed(playerList01, 3)
# player05_speed = speed.cal_speed(playerList01, 4)
# #print(speed.runRatio)

# print("\n")
# print("===speed===\n")
# print(f"{playerList01[0][1]}의 스피드는 {player01_speed}")
# print(f"{playerList01[1][1]}의 스피드는 {player02_speed}")
# print(f"{playerList01[2][1]}의 스피드는 {player03_speed}")
# print(f"{playerList01[3][1]}의 스피드는 {player04_speed}")
# print(f"{playerList01[4][1]}의 스피드는 {player05_speed}")

#==================================================

contact = c.Contact(playerList01,data01.getColsize())

contact.cal_sum()
contact.cal_avg()
contact.cal_max_min()

# player01_contact = contact.cal_contact(playerList01, 0)
# player02_contact = contact.cal_contact(playerList01, 1)
# player03_contact = contact.cal_contact(playerList01, 2)
# player04_contact = contact.cal_contact(playerList01, 3)
# player05_contact = contact.cal_contact(playerList01, 4)
# #print(speed.runRatio)

# print("\n")
# print("===contact===\n")
# print(f"{playerList01[0][1]}의 컨텍트는 {player01_contact}")
# print(f"{playerList01[1][1]}의 컨텍트는 {player02_contact}")
# print(f"{playerList01[2][1]}의 컨텍트는 {player03_contact}")
# print(f"{playerList01[3][1]}의 컨텍트는 {player04_contact}")
# print(f"{playerList01[4][1]}의 컨텍트는 {player05_contact}")

#====================팬 인기 순위 데이터 입니다==============================

# print("\n")
# print("===fans===\n")
# fan = F.Fan("data/fan.txt")

#============================ 위로는 파컨스에 대한 내용입니다=======================

#============================ 스로잉에 대한 내용입니다=======================
IF = r.ReadDate("data/IF.txt")
IF.makePlayerList()
playerIFList = IF.getPlayerList()

OF = r.ReadDate("data/OF.txt")
OF.makePlayerList()
playerOFList = OF.getPlayerList()

# print(playerIFList[0])
# print(playerOFList[1])

IFthrowing = c.Throwing(playerIFList,IF.getColsize())
OFthrowing = c.Throwing(playerOFList,OF.getColsize())

IFthrowing.cal_sum()
IFthrowing.cal_avg()
IFthrowing.cal_max_min()

OFthrowing.cal_sum()
OFthrowing.cal_avg()
OFthrowing.cal_max_min()


# playerIF01_throwing = IFthrowing.cal_throwing(playerIFList, 0)
# playerIF02_throwing = IFthrowing.cal_throwing(playerIFList, 1)
# playerIF03_throwing = IFthrowing.cal_throwing(playerIFList, 2)
# playerIF04_throwing = IFthrowing.cal_throwing(playerIFList, 3) 
# playerIF05_throwing = IFthrowing.cal_throwing(playerIFList, 4)

# playerOF01_throwing = OFthrowing.cal_throwing(playerOFList, 0)
# playerOF02_throwing = OFthrowing.cal_throwing(playerOFList, 1)
# playerOF03_throwing = OFthrowing.cal_throwing(playerOFList, 2)
# playerOF04_throwing = OFthrowing.cal_throwing(playerOFList, 3)
# playerOF05_throwing = OFthrowing.cal_throwing(playerOFList, 4)

# print("\n")
# print("===throwing===\n")
# print(f"{playerIFList[0][1]}의 스로잉는 {playerIF01_throwing}")
# print(f"{playerIFList[1][1]}의 스로잉는 {playerIF02_throwing}")
# print(f"{playerIFList[2][1]}의 스로잉는 {playerIF03_throwing}")
# print(f"{playerIFList[3][1]}의 스로잉는 {playerIF04_throwing}")
# print(f"{playerIFList[4][1]}의 스로잉는 {playerIF05_throwing}")

# print("\n")
# print(f"{playerOFList[0][1]}의 스로잉는 {playerOF01_throwing}")
# print(f"{playerOFList[1][1]}의 스로잉는 {playerOF02_throwing}")
# print(f"{playerOFList[2][1]}의 스로잉는 {playerOF03_throwing}")
# print(f"{playerOFList[3][1]}의 스로잉는 {playerOF04_throwing}")
# print(f"{playerOFList[4][1]}의 스로잉는 {playerOF05_throwing}")

#============================ 수비에 대한 내용입니다=======================
IFdefense = c.Defense(playerIFList,IF.getColsize())
OFdefense = c.Defense(playerOFList,OF.getColsize())

IFdefense.cal_sum()
IFdefense.cal_avg()
IFdefense.cal_max_min()

OFdefense.cal_sum()
OFdefense.cal_avg()
OFdefense.cal_max_min()


# playerIF01_defense = IFdefense.cal_defense(playerIFList, 0)
# playerIF02_defense = IFdefense.cal_defense(playerIFList, 1)
# playerIF03_defense = IFdefense.cal_defense(playerIFList, 2)
# playerIF04_defense = IFdefense.cal_defense(playerIFList, 3) 
# playerIF05_defense = IFdefense.cal_defense(playerIFList, 4)

# playerOF01_defense = OFdefense.cal_defense(playerOFList, 0)
# playerOF02_defense = OFdefense.cal_defense(playerOFList, 1)
# playerOF03_defense = OFdefense.cal_defense(playerOFList, 2)
# playerOF04_defense = OFdefense.cal_defense(playerOFList, 3)
# playerOF05_defense = OFdefense.cal_defense(playerOFList, 4)

# print("\n")
# print("===defense===\n")
# print(f"{playerIFList[0][1]}의 수비는 {playerIF01_defense}")
# print(f"{playerIFList[1][1]}의 수비는 {playerIF02_defense}")
# print(f"{playerIFList[2][1]}의 수비는 {playerIF03_defense}")
# print(f"{playerIFList[3][1]}의 수비는 {playerIF04_defense}")
# print(f"{playerIFList[4][1]}의 수비는 {playerIF05_defense}")

# print("\n")
# print(f"{playerOFList[0][1]}의 수비는 {playerOF01_defense}")
# print(f"{playerOFList[1][1]}의 수비는 {playerOF02_defense}")
# print(f"{playerOFList[2][1]}의 수비는 {playerOF03_defense}")
# print(f"{playerOFList[3][1]}의 수비는 {playerOF04_defense}")
# print(f"{playerOFList[4][1]}의 수비는 {playerOF05_defense}")

#============================통합하기=======================

# <category>
# power
# contact
# speed
# OFthrowing
# OFdefense

# <data list>
# playerList01
# playerOFList

HongChangKi_name = playerList01[0][1]
HongChangKi_power = power.cal_power(playerList01, 0)
HongChangKi_contact = contact.cal_contact(playerList01, 0)
HongChangKi_speed = speed.cal_speed(playerList01, 0)
HongChangKi_throwing = OFthrowing.cal_throwing(playerList01, 115)
HongChangKi_defense = OFdefense.cal_defense(playerList01, 115)

HongChangKi = [HongChangKi_power,HongChangKi_contact,HongChangKi_speed,HongChangKi_throwing,HongChangKi_defense]
#print(f"{playerList01[0][1]} = 파워: {HongChangKi_power}, 컨텍:{HongChangKi_contact}, 스피드:{HongChangKi_speed}, 스로잉:{HongChangKi_throwing}, 수비:{HongChangKi_defense}")



LeejungHoo_power = power.cal_power(playerList01, 1)
LeejungHoo_contact = contact.cal_contact(playerList01, 1)
LeejungHoo_speed = speed.cal_speed(playerList01, 1)
LeejungHoo_throwing = OFthrowing.cal_throwing(playerList01, 14)
LeejungHoo_defense = OFdefense.cal_defense(playerList01, 14)

LeejungHoo = [LeejungHoo_power,LeejungHoo_contact,LeejungHoo_speed,LeejungHoo_throwing,LeejungHoo_defense]
#print(f"{playerList01[1][1]} = 파워: {LeejungHoo_power}, 컨텍:{LeejungHoo_contact}, 스피드:{LeejungHoo_speed}, 스로잉:{LeejungHoo_throwing}, 수비:{LeejungHoo_defense}")

ma9data = r.ReadDate("data/ma9data01.txt")
ma9data.makePlayerList()
ma9playerlist = ma9data.getPlayerList()

#print(ma9playerlist)

# bar_width = 0.35
# x = ["power","contact","speed","throwing","defense"]
# index = np.arange(len(x))
# newY = [float(ma9playerlist[0][1]),float(ma9playerlist[0][2]),float(ma9playerlist[0][3]),float(ma9playerlist[0][4]),float(ma9playerlist[0][5])]
# plt.bar(index, HongChangKi, color = "blue",width=0.35)
# plt.bar(index+bar_width, newY, color = "red",width=0.35)
# plt.xticks(index, x, fontsize = 15)
# plt.show()

bar_width = 0.35
x = ["power","contact","speed","throwing","defense"]
index = np.arange(len(x))
newY = [float(ma9playerlist[1][1]),float(ma9playerlist[1][2]),float(ma9playerlist[1][3]),float(ma9playerlist[1][4]),float(ma9playerlist[1][5])]
plt.bar(index, LeejungHoo, color = "blue",width=0.35)
plt.bar(index+bar_width, newY, color = "red",width=0.35)
plt.xticks(index, x, fontsize = 15)
plt.show()
