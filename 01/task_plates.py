plates = int(input())
soap   = int(input())

remain_plates = plates - (soap*2)
remain_soap   = soap - (plates*0.5)

if remain_soap <= 0 and remain_plates > 0:
		print('Моющее средство закончилось. Осталось ' + str(int(remain_plates)) + ' тарелок')
elif remain_soap > 0 and remain_plates <= 0:
		print('Все тарелки вымыты. Осталось ' + str(float(remain_soap)) + ' ед. моющего средства')
elif remain_soap == 0 and remain_plates == 0:
		print('Все тарелки вымыты, моющее средство закончилось')