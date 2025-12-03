met = float(input('Qual a quantidade de metros:'))
klm = met / 1000
hm = met / 100
dam = met /10
dc = met * 10
c = met * 100
mil = met * 1000
espaço = "="
print('{:=^20}'.format(espaço))
print("São {} kilometros \nSão {} hectómetro \nSão {}dacámetro \nSão {} metros".format(klm, hm, dam, met))
print('São {} decímetros \nSão {} centímetros \nSão {} milímetros'.format(dc, c, mil))
print('{:=^20}'.format(espaço))