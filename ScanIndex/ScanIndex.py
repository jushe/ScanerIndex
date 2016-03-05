import os

SYSTEMList = ["System", "SYSTEM", "system", "windows", "Windows", "WINDOWS", '$', '_', 'DRIVERS']
def getTheTargetDisk():
	""" 
	Get the scanner 
	return: the input string
	"""
	input = raw_input("-->Disk: ")
	return input

def theLevelIndex(root):
	""" 
	Find the root's level
	root: string, the index you want to judge
	return: int, 0 for A, 1 for B
	"""
	if os.path.isdir(root):
		for filepath in os.listdir(root):
			if  os.path.isfile (root + '//' + filepath):
				return 1
	return 0
scanfile = open("E://scanReport.txt", "a")
root = getTheTargetDisk()
listA = os.listdir(root + '//')
listB = []
#排除系统目录
for dirpath in listA:
	for sysName in SYSTEMList:
		if sysName in dirpath:
			listA.remove(dirpath)
for index in range(len(listA)):
	listA[index] = root + '//' + listA[index]
while len(listA) > 0:
	for dirroot in listA:
		listA.remove(dirroot)
		if os.path.isdir(dirroot):
			if theLevelIndex(dirroot + '//') == 0:
				for filepath in os.listdir(dirroot + '//'):
					listA.append(dirroot + '//' + filepath)
			else:
				print dirroot
				listB.append(dirroot)
		else:
			print dirroot
			listB.append(dirroot)
for item in listB:
	scanfile.writelines(item + '\n')
scanfile.close()