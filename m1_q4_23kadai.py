ip_address = '192.168.3.1'
ip_spl = ip_address.split('.') # '.'で分割しリストに格納
print(ip_spl) # からの文字列
bin_exp = ''
for num in ip_spl:
	bin_exp += bin(int(num))[2:] + '.' # [2:]で'ab]を取り除き、末尾に','を追加
print(bin_exp[:-1])
