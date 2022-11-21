import ReadData as r
import Calculate as c
import Fan as F

data01 = r.ReadDate("code/data01.txt")
data01.makePlayerList()
playerList01 = data01.getPlayerList()
#print(playerList01[149])

#==================================================

power = c.Power(playerList01, data01.getColsize())

power.cal_sum()
power.cal_avg()
power.cal_max_min()

player01_power = power.cal_power(playerList01, 0)
player02_power = power.cal_power(playerList01, 1)
player03_power = power.cal_power(playerList01, 2)
player04_power = power.cal_power(playerList01, 3)
player05_power = power.cal_power(playerList01, 4)

# player100_power = power.cal_power(playerList01, 99)
player14_power = power.cal_power(playerList01, 13)

print("===power===\n")
print(f"{playerList01[0][1]}의 파워는 {player01_power}")
print(f"{playerList01[1][1]}의 파워는 {player02_power}")
print(f"{playerList01[2][1]}의 파워는 {player03_power}")
print(f"{playerList01[3][1]}의 파워는 {player04_power}")
print(f"{playerList01[4][1]}의 파워는 {player05_power}")

print(f"{playerList01[13][1]}의 파워는 {player14_power}")

#==================================================

speed = c.Speed(playerList01,data01.getColsize())

speed.cal_run_ratio()
speed.cal_sum()
speed.cal_avg()
speed.cal_max_min()

player01_speed = speed.cal_speed(playerList01, 0)
player02_speed = speed.cal_speed(playerList01, 1)
player03_speed = speed.cal_speed(playerList01, 2)
player04_speed = speed.cal_speed(playerList01, 3)
player05_speed = speed.cal_speed(playerList01, 4)
#print(speed.runRatio)

print("\n")
print("===speed===\n")
print(f"{playerList01[0][1]}의 스피드는 {player01_speed}")
print(f"{playerList01[1][1]}의 스피드는 {player02_speed}")
print(f"{playerList01[2][1]}의 스피드는 {player03_speed}")
print(f"{playerList01[3][1]}의 스피드는 {player04_speed}")
print(f"{playerList01[4][1]}의 스피드는 {player05_speed}")

#==================================================

contact = c.Contact(playerList01,data01.getColsize())

contact.cal_sum()
contact.cal_avg()
contact.cal_max_min()

player01_contact = contact.cal_contact(playerList01, 0)
player02_contact = contact.cal_contact(playerList01, 1)
player03_contact = contact.cal_contact(playerList01, 2)
player04_contact = contact.cal_contact(playerList01, 3)
player05_contact = contact.cal_contact(playerList01, 4)
#print(speed.runRatio)

print("\n")
print("===contact===\n")
print(f"{playerList01[0][1]}의 컨텍트는 {player01_contact}")
print(f"{playerList01[1][1]}의 컨텍트는 {player02_contact}")
print(f"{playerList01[2][1]}의 컨텍트는 {player03_contact}")
print(f"{playerList01[3][1]}의 컨텍트는 {player04_contact}")
print(f"{playerList01[4][1]}의 컨텍트는 {player05_contact}")

#==================================================

print("\n")
print("===fans===\n")
fan = F.Fan("code/fan.txt")
