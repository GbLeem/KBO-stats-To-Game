import ReadData as r
import Calculate as c

data01 = r.ReadDate("code/data01.txt")
data01.makePlayerList()
playerList01 = data01.getPlayerList()
print(playerList01[149])

power = c.Power(playerList01, data01.getColsize())

power.cal_sum()
power.cal_avg()
power.cal_max_min()

player01_power = power.cal_power(playerList01, 0)
player02_power = power.cal_power(playerList01, 1)
player03_power = power.cal_power(playerList01, 2)
player04_power = power.cal_power(playerList01, 3)
player05_power = power.cal_power(playerList01, 4)

player100_power = power.cal_power(playerList01, 99)
player14_power = power.cal_power(playerList01, 13)


print(f"{playerList01[0][1]}의 파워는 {player01_power}")
print(f"{playerList01[1][1]}의 파워는 {player01_power}")
print(f"{playerList01[2][1]}의 파워는 {player01_power}")
print(f"{playerList01[3][1]}의 파워는 {player04_power}")
print(f"{playerList01[4][1]}의 파워는 {player01_power}")

#print(f"{playerList01[99][1]}의 파워는 {player100_power}")
#print(f"{playerList01[13][1]}의 파워는 {player14_power}")
