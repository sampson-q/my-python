# -*- coding: utf-8 -*-
"""
Created on Wed May 12 02:14:23 2021

@author: Hash
"""

# usersNames = ['ABDUL BASIT ISSAKA', 'ADJEI RICHMOND ASARE', 'AFIAWO EUGENE SENYO', 'ASSEM ALFRED', 'ATUAHENE KELVIN OWARE', 
#                 'ANTWI  CHRISTIAN', 'AGBEDOHIA LINDA EWOENAM', 'AMOAKO DERRICK', 'ADAMU SANI', 'AFATSAWO TERRY KWAMES',
#                 'AWAL AMINU MOHAMMED', 'AMOAH APAAWEN MATHIAS', 'ABAKAH BENJAMIN', 'AZONG GABRIEL', 'AGBODJI YAO', 'ARTHUR PETER',
#                 'AKOTO ERIC', 'ARKO NII DANSO DAVID', 'AWENTRIM ASAI GODFRED', 'ANSONG FELIX', 'ANIM EMMANUEL', 'ADIL MUSTAPHA', 
#                 'AWUNI GODFRED', 'AGYEI YEBOAH KWABENA', 'ANTWI EMMANUEL', 'AGYAPONG ERIC KWESI', 'AFENYO-KATSI KEKELI', 
#                 'ACQUAH JEFFIN', 'ABDUL KADIR ISSAH', 'ABOAGYE KWAME', 'ABROKWA EMMANUEL ASANTE', 'ADJEI FELIX', 'ASSEM ALFRED', 
#                 'AWU DELA', 'AGYEI KWADWO JUNIOR', 'ADJAH NII BODAIFIO', 'BRIMAH ZAKIYYA MUHAMMED', 'BONSU ROLAND NANA',
#                 'BREMPONG OPOKU GIDEON', 'BOAMAH-WIAFE FREDRICK', 'BUDU-LARBI ROBERT', 'BASOAH GEORGE', 'BAAH ALEX', 
#                 'BANINI SAMUEL MAWUSE KOBLA', 'BOAHENE NANA NYARKO QUANSAH', 'BOATENG KELVIN AKWASI', 'DODOO ROLAND', 
#                 'DUNYOH KIIRPAL BRIGHT CHARITY', 'DAGBANA EMMANUEL', 'EFUNWOLE OLA JACOB', 'FRIMPONG  NANA OWUSU', 
#                 'GAISEY EKOW-SAM EUGENE', 'HAMZA MOHAMMED', 'HODOH CHRISTOPHER', 'HOLASI DANIEL', 'KLUTSEY-BORKLO DELIGHT', 
#                 'KETENI PRINCE', 'KILLIAN JAMES-ETORNAM EDEM', 'KOKOR ELTON JOHN', 'LUMOR MAWULI', 'LARYEA JOSEPH', 'MANTE ELVIS', 
#                 'MOHAMMED SANI ABDUL RAHMAN ZIYAD', 'MWINWULE ERIC YAW', 'MOHAMMED RAZAK WUSUFOR', 'MANTE NYAMEKYE DIVINE', 
#                 'MENSAH JAMES KOFFE', 'MENSAH AUGUSTINA AKPENE', 'MOHAMMED YUSIF FARID', 'MANSO DERRICK FRIMPONG', 
#                 'NORTEY EDWIN NII NARKU', 'NARTEY JOSEPH LOMOTEY', 'NYARKOH GODWIN', 'NYARKO SAMUEL KWAME', 'NWEKE VICTOR', 
#                 'NUAMAH BENJAMIN KOFI', 'OKYERE OSEI SAMUEL', 'OSABUTEY ISHMAEL NARH', 'OHENE EMMANUEL SAE', 
#                 'ODOI NII KOMMEY-TETTEY ARNOLD', 'OSEI KWADZO GYIMAH SAMUEL', 'OWUSU YEBOAH JESSE', 'OPPONG DONKOR BENJAMIN', 
#                 'OPARE PRINCE', 'OKOE BENJAMINE', 'OBOUR BENSON', 'QUAYE MIRACLE', 'QUARTEY BENJAMIN', 'SARPONG MAXWEL AGYEI', 
#                 'SACKEY NYARKO KWESI', 'SACKEY ABEL TEYE', 'SACKEY KOFI AMEYAW', 'SIADAH PHILIP', 'SEIDU IKBARU', 'SACKEY OBED', 
#                 'SAKYI EBENEZER', 'SACKEY DANIEL OSAMAU', 'SACKEY DANIEL MENSAH', ' SARPONG MAXWELL AGYEI', 'SEIDU ABDUL SALAM', 
#                 'TONJOUKOUE CLAUDE AREKEMBO', 'TOKPO NELSON', 'TETTEH NARH SOLOMON', 'TIERNYE TORKOR MARTIN', 'TEYE BISMARK', 
#                 'VORVOR MORRIS JAMES', 'ENOCH ELLIAH', 'ATARIBA BENJAMIN', 'JESSICA DAVIDSON APREKU', 'YIRENKYI SAMUEL', 
#                 'OKINE SHERIFF AYIKWEY', 'NABDOYA JOSEPH', 'AMOAKOHENE ALFRED PEPRAH', 'KOKOR ELTON JOHN', 'ANNOR BRIGHT', 
#                 'ASARE WISDOM', 'PRISCILLA NAA YARLEY YARTEY', 'OBED MENSAH', 'MOHAMMED AHMED TIJANI', 'QUARSHIE ERIC TAWIAH', 
#                 'NANKA – BRUCE MELVIN', 'YAKUBU RASHID']

# usersIds = ['01203272D','01204678D','01204183D','01202042D','01202869D','01202330D','01200404D','01201821D','01202356D','01201727D',
#             '01202242D','01205011D','01200644D','01203235D','01202505D','01204054D','01203108D','01201450D','01203080D','01201943D',
#             '01204269D','01204378D','01204351D','01202611D','01204474D','01200466D','01201977D','01201439D','01202618D','01202329D',
#             '01201295D','01200309D','01202042D','01204096D','01200121D','01203485D','01201312D','01204718D','01202676D','01201696D',
#             '01204914D','01200724D','01200894D','01202332D','01201855D','01200088D','01201917D','01204246D','01203554D','01201995D',
#             '01203752D','01201336D','01204072D','01203906D','01202O16D','01202134D','01204570D','01204236D','01204974D','01200493D',
#             '01201419D','01201563D','01204470D','01201181D','01201118D','01203422D','01202975D','01202646D','01203994D','01201350D',
#             '01202300D','01201969D','01202490D','01203951D','01202414D','01202599D','01202186D','01200364D','01204737D','01200292D',
#             '01203468D','01202834D','01204265D','01204304D','01201761D','01201535D','01200603D','01202943D','01203023D','01202187D',
#             '01200593D','01201997D','01203949D','01201803D','01203417D','01201135D','01203950D','01200583D','01203023D','01201194D',
#             '01200496D','01203750D','01201644D','01202727D','01204098D','01202800D','01201513D','01204529D','01204979D','01205133D',
#             '01205146D','01204904D','01205225D','01204974D','01205164D','01205197D','01205393D','01205358D','01205336D','10215363D',
#             '01205334D','01205338D','01205421D']

usersIds = [
        '01202628D','01201937D','01201291D','01202243D','01201657D','01201100D','01201928D','01202325D','01200312D','01200792D','01202451D','01203637D','01202320D',
        '01202619D','01200712D','01203723D','01203745D','01204061D','01203092D','01203354D','01201348D','01202803D','01201668D','01203769D','01201753D','01203347D',
        '01201743D','01201763D','01202449D','01200329D','01202040D','01203773D','01205575D','01201451D','01202507D','01201715D','01202533D','01202621D','01200751D','01204396D','01201185D',
        '01203809D','01200609D','01200663D','01201993D','01202060D','01203249D','01201998D','01203409D','01203843D','01200031D','01201665D','01205551D','01200941D','01202207D',
        '01200803D','01200801D','01203728D','01200127D','01201381D','01203721D','01202072D','01201092D','01203567D','01200130D','01202502D','01203233D','01201463D',
        '01203993D','01202259D','01204047D','01202329D','01201121D','01200645D','01203685D','01203659D','01201446D','01202934D','01203874D',
        '01200139D','01202159D','01202022D','01204570D','01202073D','01202399D','No ID','01200644D','01204871D','01204896D','01204961D','01204996D',
        '01203181D','01201684D','01204998D','0125435D','01205338D','01204602D','01204894D','01205401D','01205136D','01205165D','01205367D','01205475D',
        '01205371D','01205541D','01200194D','01202901D','01200246D','01201041D','01200035D','No ID','01201408D','01201621D','01201346D','01201645D','01202339D',
        '01204562D','No ID','01205435D'
    ]
space = ' '


# for i in range(0, len(usersNames)):
#     print('<tr>')
#     print(space * 4 + '<td>{}</td>'.format(i + 1))
#     print(space * 4 + '<td>{}</td>'.format(usersIds[i]))
#     print(space * 4 + '<td>{}</td>'.format(usersNames[i]))
#     print(space * 4 + '<td><input type="text" name="attStatus[] value="{}"></td>'.format(usersIds[i]))
#     print('</tr>\n')

for i in usersIds:
    if usersIds.count(i) >= 2:
        print(i)