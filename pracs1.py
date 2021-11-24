# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:43:16 2021

@author: Hash
"""

namesList = []

numbers = """
Abdul Lahie Abdul Rahman Ninche
Abdul Malik Abubakar
Abdulai Rashidatu Nasara
Abubakar Nabil
Adam Sallim 
Addai Peter
Addo Joel Bless
Frimpong Eunice 
Adorkor Samuel Mawulorm
Aduamoah Benjamin
Afful Esther Nhyira
Afriyie Adusei Cliford
Agaba Samuel Kweku
Agyenim Boateng Prince
Agyin Joseph
Akatse Bernadette Yayra
Aklasu Sandra
Akuffo Nell Tackie
Alhassan Buba
Allotey Frederick Nii Adotey
Amankrah Kingsley
Amedzrovi Wisdom
Amidu Nuhu 
Ampaw Justice Safo
Amponsah Isaac Kweku
Anang Asher Dromo
Anim yirenkyi Obed 
Annan Samuel Tete
Annor Samuel Yeboah 
Antwi Blessed
Antwi Opoku Yaw 
Anyankwah Laywerence
Asare Ernest 
Attuouayefio El Lyan
Badarodeen Sani
Bannor Ernest
Boamah Jeffery 
Boamah Jesmine
Jephter  Quaofio
Nkansah Raymond Konedu
Nunoo Belinda
Obeng Bright
Odum Ewuakye Daniel Miguel
Offei Gilda Kwayisibea
Okyere Samuel
Opei Isaac Ayisi
Otoo Esther Ntiamoah
Owusu Godwin
Quainoo Edmund
Quaye Jonathan Ayi Damey
Razak Moazu
Awuah James Mckeown
Sebi Christopher T. T
Sebi Clifford Brian T. T
Tagoe Eric
Tay theophilus Mawunyegah
Tetteh Blessings 
Thompson Othnie Nii Okai
Pio Abdul Karim
Twum Maxwell
Yakubu Toufik
Zegah Ernest Elikplim
Mensah Sedem Junior
Dugbatey Wisdom
Ofori-Sam Pius
Moses Fosu
Tagoe Nii Commey
Agoe Gabriel
Gideon Evans Tettey
Aboagye Kwame
Mark Adonteng
Borketey Daniel
Opoku Joseph
Odame Horthman
Ochere Robert
Antwi Blessed
Leslie Adriene Nunoo
Asamoah Nkrumah Richmond
Dominic Emmanuel Abalo
Ankah Bernard Asiamah
Jephtha Lamptey
Kenteni Prince
Asiamah-Konadu Nana Kwame
James Nerquaye-Tetteh
Jephter Quaofio Nii
Abakah Benjamin
Frimpong Eunice
Asempa Theophilus 
Zillion Mawunyo Williams
Joshua Modunu
Sydney Sosi Sackey
Bakpah Kwame James
James Nerquaye-Tetteh
Assan Issah
Emmanuel Gyan
Kdrom Osing
Yakubu Rahad
Kenneth Kusi Prepeh
Agor Jeffrey
Elgar Christ Benit
Agbator Courage 
Fred Oppong Boamah
Nurudeen Salim
Botchway Sowah Solomon
Gyimah Nicholas 
Mohammed Shiraz Deen
Dazie Benjamin Gakpo
Deku Israel
Ewusi-Essel Daniel
Fuseni Abubakar Sidiq
Gankui Wisdom Kwame
Gmanye Ananias Kwaku
Gyesey Prince Derrick
Iddi Moagri Waris
Kumah Anorvey Daniel Bright
Kwakye Emmanuel Okyere
Amankwah Jeffrey
Anum Nii Odai Joshua
Ignatius Daniel Arthur
Kwame Aboagye
Nkrumah Obeng Michael
Dugbatey Wisdom 

"""
sorteds = []
arrays = ['0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c']

for i in range(0, len(arrays)):
    sorteds.append(arrays[i])

# final = "'ABDUL LAHIE ABDUL RAHMAN NINCHE', 'ABDUL MALIK ABUBAKAR', 'ABDULAI RASHIDATU NASARA', 'ABUBAKAR NABIL', 'ADAM SALLIM ', 'ADDAI PETER', 'ADDO JOEL BLESS', 'FRIMPONG EUNICE ', 'ADORKOR SAMUEL MAWULORM', 'ADUAMOAH BENJAMIN', 'AFFUL ESTHER NHYIRA', 'AFRIYIE ADUSEI CLIFORD', 'AGABA SAMUEL KWEKU', 'AGYENIM BOATENG PRINCE', 'AGYIN JOSEPH', 'AKATSE BERNADETTE YAYRA', 'AKLASU SANDRA', 'AKUFFO NELL TACKIE', 'ALHASSAN BUBA', 'ALLOTEY FREDERICK NII ADOTEY', 'AMANKRAH KINGSLEY', 'AMEDZROVI WISDOM', 'AMIDU NUHU ', 'AMPAW JUSTICE SAFO', 'AMPONSAH ISAAC KWEKU', 'ANANG ASHER DROMO', 'ANIM YIRENKYI OBED ', 'ANNAN SAMUEL TETE', 'ANNOR SAMUEL YEBOAH ', 'ANTWI BLESSED', 'ANTWI OPOKU YAW ', 'ANYANKWAH LAYWERENCE', 'ASARE ERNEST ', 'ATTUOUAYEFIO EL LYAN', 'BADARODEEN SANI', 'BANNOR ERNEST', 'BOAMAH JEFFERY ', 'BOAMAH JESMINE', 'JEPHTER  QUAOFIO', 'NKANSAH RAYMOND KONEDU', 'NUNOO BELINDA', 'OBENG BRIGHT', 'ODUM EWUAKYE DANIEL MIGUEL', 'OFFEI GILDA KWAYISIBEA', 'OKYERE SAMUEL', 'OPEI ISAAC AYISI', 'OTOO ESTHER NTIAMOAH', 'OWUSU GODWIN', 'QUAINOO EDMUND', 'QUAYE JONATHAN AYI DAMEY', 'RAZAK MOAZU', 'AWUAH JAMES MCKEOWN', 'SEBI CHRISTOPHER T. T', 'SEBI CLIFFORD BRIAN T. T', 'TAGOE ERIC', 'TAY THEOPHILUS MAWUNYEGAH', 'TETTEH BLESSINGS ', 'THOMPSON OTHNIE NII OKAI', 'PIO ABDUL KARIM', 'TWUM MAXWELL', 'YAKUBU TOUFIK', 'ZEGAH ERNEST ELIKPLIM', 'MENSAH SEDEM JUNIOR', 'DUGBATEY WISDOM', 'OFORI-SAM PIUS', 'MOSES FOSU', 'TAGOE NII COMMEY', 'AGOE GABRIEL', 'GIDEON EVANS TETTEY', 'ABOAGYE KWAME', 'MARK ADONTENG', 'BORKETEY DANIEL', 'OPOKU JOSEPH', 'ODAME HORTHMAN', 'OCHERE ROBERT', 'ANTWI BLESSED', 'LESLIE ADRIENE NUNOO', 'ASAMOAH NKRUMAH RICHMOND', 'DOMINIC EMMANUEL ABALO', 'ANKAH BERNARD ASIAMAH', 'JEPHTHA LAMPTEY', 'KENTENI PRINCE', 'ASIAMAH-KONADU NANA KWAME', 'JAMES NERQUAYE-TETTEH', 'JEPHTER QUAOFIO NII', 'ABAKAH BENJAMIN', 'FRIMPONG EUNICE', 'ASEMPA THEOPHILUS ', 'ZILLION MAWUNYO WILLIAMS', 'JOSHUA MODUNU', 'SYDNEY SOSI SACKEY', 'BAKPAH KWAME JAMES', 'JAMES NERQUAYE-TETTEH', 'ASSAN ISSAH', 'EMMANUEL GYAN', 'KDROM OSING', 'YAKUBU RAHAD', 'KENNETH KUSI PREPEH', 'AGOR JEFFREY', 'ELGAR CHRIST BENIT', 'AGBATOR COURAGE ', 'FRED OPPONG BOAMAH', 'NURUDEEN SALIM', 'BOTCHWAY SOWAH SOLOMON', 'GYIMAH NICHOLAS ', 'MOHAMMED SHIRAZ DEEN', 'DAZIE BENJAMIN GAKPO', 'DEKU ISRAEL', 'EWUSI-ESSEL DANIEL', 'FUSENI ABUBAKAR SIDIQ', 'GANKUI WISDOM KWAME', 'GMANYE ANANIAS KWAKU', 'GYESEY PRINCE DERRICK', 'IDDI MOAGRI WARIS', 'KUMAH ANORVEY DANIEL BRIGHT', 'KWAKYE EMMANUEL OKYERE', 'AMANKWAH JEFFREY', 'ANUM NII ODAI JOSHUA', 'IGNATIUS DANIEL ARTHUR', 'KWAME ABOAGYE', 'NKRUMAH OBENG MICHAEL', 'DUGBATEY WISDOM '"


# temp = ''

# for i in numbers:
#     if i == '\n' or i == '\t':
#         namesList.append(temp.upper())
#         temp = ''
#     else:
#         temp += i

# # print(namesList)
    
    
# # for i in numbers:
# #     if i == "\n" or i == "\t":
# #         namesList.append(temp)
# #         temp = ''
# #     else:
# #         temp += i


# # print(namesList)

# # string = ''
# namesList1 = "'01202628D', '01201937D', '01201291D', '01202243D', '01201657D', '01201100D', '01201928D', '01202325D', '01200312D', '01200792D', '01202451D', '01203637D', '01202320D', '01202619D', '01200712D', '01203723D', '01203745D', '01204061D', '01203092D', '01203354D', '01201348D', '01202803D', '01201668D', '01203769D', '01201753D', '01203347D', '01201743D', '01201763D', '01202449D', '01200329D', '01202040D', '01203773D', '01201451D', '01202507D', '01201715D', '01202533D', '01202621D', '01200751D', '01204396D', '01203809D', '01200609D', '01200663D', '01201993D', '01202060D', '01203249D', '01201998D', '01203409D', '01203843D', '01200031D', '01201665D', '01200941D', '01202207D', '01200803D', '01200801D', '01203728D', '01200127D', '01201381D', '01203721D', '01202072D', '01201092D', '01203567D', '01200130D', '01202502D', '01203233D', '01201463D', '01203993D', '01202723D', '01202259D', '01204047D', '01202329D', '01201121D', '01200645D', '01203685D', '01203659D', '01201446D', '01200329D', '01202934D', '01203874D', '01200139D', '01202159D', '01204503D', '01204570D', '01202073D', '01202399D', '01202022D', '01200644D', '01202325D', '01204871D', '01204896D', '01204961D', '01204996D', '01203181D', '01202399D', '01201684D ', '0120998D', '0125435D', '01205338D', '01204602D', '01204894D', '01205401D', '01205136D', '01205165D', '01205367D', '01205475D', '01205371D', '01205541D', '01200194D', '01202901D', '01200246D', '01201041D', '01200035D', '01200035D', '01201408D', '01201621D', '01201346D', '01201645D', '01202339D', '01204562D', 'No ID', '01202329D', 'No ID', '01203033D'"
# commaCounter = 0

# for m in final:
#     if m == ',':
#         commaCounter += 1
    
#     if commaCounter == 5:
#         print(',\n')
#         commaCounter = 0
#     else:
#         print(m, end='')


# # names = """ """
# # chaff = ''
# # final = []
# # temp = ''

# # for i in name:
# #     if i in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
# #         chaff += i;
# #     else:
# #         names += i;

# # for i in names:
# #     if i == '\n' or i == '\t':
# #         final.append(temp)
# #         temp = ''
# #     else:
# #         temp += i

# # for i in final:
# #     if i == "" or i == " ":
# #         final.remove(i)

# # print(final)