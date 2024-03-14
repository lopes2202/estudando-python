metros = float(input('Informe um valor em Metros '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print("A medida em de {}m corresponde a \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm ".format(metros, km, hm, dam, dm, cm, mm))