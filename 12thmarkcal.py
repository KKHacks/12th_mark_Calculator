
mark_10_1 = 77
mark_10_2 = 76
mark_10_3 = 74
mark_10_total = mark_10_1+mark_10_2+mark_10_3
mark_10_fulltotal = mark_10_total/300 * 50
print("Total 10th mark %s" %int(mark_10_fulltotal))

mark_11_tam = 49
mark_11_eng = 42
mark_11_mat = 25
mark_11_phy = 15
mark_11_che = 28
mark_11_com = 48



# def markper_90_11th(mark):
#     tot = mark/90 * 20
#     print(int(tot))


# def markper_70_11th(mark):
#     tot = mark/70 * 20
#     print(int(tot))


mark_11_tamtot = mark_11_tam/90*20
mark_11_engtot = mark_11_eng/90*20
mark_11_mattot = mark_11_mat/90*20
mark_11_phytot = mark_11_phy/70*20
mark_11_chetot = mark_11_che/70*20
mark_11_comtot = mark_11_com/70*20

mark_12_1 = 30
mark_12_2 = 30
mark_12_3 = 30
mark_12_4 = 30
mark_12_5 = 30
mark_12_6 = 30

num_11 = (int(mark_11_tamtot),int(mark_11_engtot),int(mark_11_mattot),int(mark_11_phytot),int(mark_11_chetot),int(mark_11_comtot))

for x in num_11:
    print(x)

tot_10 = mark_10_fulltotal * 6
tot_11 = int(mark_11_tamtot)+int(mark_11_engtot)+int(mark_11_mattot)+int(mark_11_phytot)+int(mark_11_chetot)+int(mark_11_comtot)
tot_12 = 30*6
print("Total 11th mark %s" %tot_11)

def totalmark():
    fullmark = tot_10+tot_11+tot_12
    print("Total 12th mark %s" %int(fullmark))

totalmark()