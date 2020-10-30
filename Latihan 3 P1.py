#3
ind = int(input('Nilai Bahasa Indonesia :'))
mtk = int(input('Nilai Matematika :'))
ipa = int(input('Nilai IPA:'))

print('==========================')

if(ind < 0 or ind > 100):
    print('Maaf input ada yang tidak valid')
elif(ipa < 0 or ipa > 100):
    print('Maaf input ada yang tidak valid')
elif (mtk < 0 or mtk > 100):
    print('Maaf input ada yang tidak valid')
    
elif(ind > 60 and ipa > 60 and mtk > 70):
    print ('Status kelulusan : Lulus')
else:
    print ('Status kelulusan : Tidak lulus')
    print('Sebab :')
    
    if(ind < 60):
        print('Nilai Bahasa Indonesia Kurang Dari 60')
    if(mtk < 70):
        print('Nilai Matematika Kurang Dari 70')
    if(ipa < 60):
        print('Nilai IPA Kurang Dari 60')
