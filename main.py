import webbrowser


print('\n\t\t\t\t\t\tWELCOME TO THE APP!')
print('\t\t(After your choosing press enter)')

#list of singers
list_of_singers = ['BONES', 'NiGHT LOVELL', 'UNAVERAGE GANG', "NF", 'POP SMOKE',
                   'Drake']

empty_question = input('\nPRESS enter TO SHOW THE LIST OF SINGERS: ')
del empty_question

#SHOW THE LIST OF SINGERS
cnt = 1
for list_of_singer in list_of_singers:
    print('\n' + str(cnt) + ') ' + list_of_singer)
    cnt += 1


#DataBase
bones = ['CtrlAltDelete', 'HDMI', 'Dirt', 'RestInPeace', 'LooseScrew', 'Topaz',
         'WhoGoesThere', 'XLR', 'Propellers', 'WHERE IS MY MIND', 'IThoughtYouLookedFamiliar',
         'Canal St.', 'Calcium', 'Sodium', 'SleepMode', 'IAmCertainlyNotWorthYourTime',
         'Air', '90210', 'ArentYouASightForSoreEyes', 'KeepTellingYourselfThat']

nightlovell = ['Beneath', 'Dark Light', "I'm Okey", 'Still Cold',
               'Concept Nothing', 'Deira City Centre', 'Fukk!!CodeRED',
               'Trees Of The Valley', 'I Heard You Were Looking for Me',
               '300 Thousand', 'Off Air', 'PP15']

unaverage_gang = ['True colors', 'Cold Steel', 'got six on it', 'Deep end',
                  'UNDERWORLD']

pop_smoke = ['Aim For The Moon', 'ELEMENT ', 'AP', 'GET BACK',
             'Hello', 'INVINCIBLE']

nf = ['NO NAME', 'When i grow up', 'The Search', 'Leave Me Alone',
      'PAID MY DUES']

drake = ['Chicago Freestyle', 'Life is Good', 'Toosie Slide',
         'Laugh Now Cry Later']


def start_work():
    global order
    while True:
        order = input(
            '\nCHOOSE THE NUMBER OF THE SINGERS YOU PREFER' +
            'OR "q"/"й" TO QUIT: ')
    #Bones's music
        if order == '1':
            print('\nList of BONES songs:')
            nmbs = 1
            for songs_bones in bones:
                print(str(nmbs) + ') ' + songs_bones)
                nmbs += 1
            break
    #Night lovell's music
        elif order == '2':
            print('\nList of BONES songs NIGHT LOVELL:')
            nmbs = 1
            for songs_night in nightlovell:
                print(str(nmbs) + ') ' + songs_night)
                nmbs += 1
            break
    #Unaverage gang's music
        elif order == '3':
            print('\nList of UNAVERAGE GANG songs:')
            nmbs = 1
            for songs_gang in unaverage_gang:
                print(str(nmbs) + ') ' + songs_gang)
                nmbs += 1
            break
    #NF's music
        elif order == '4':
            print('\nList of NF songs:')
            nmbs = 1
            for songs_nf in nf:
                print(str(nmbs) + ') ' + songs_nf)
                nmbs += 1
            break
    #Pop smoke's music
        elif order == '5':
            print('\nList of POP SMOKE songs: ')
            nmbs = 1
            for songs_pop in pop_smoke:
                print(str(nmbs) + ') ' + songs_pop)
                nmbs += 1
            break
    #Drake's music
        elif order == '6':
            print('\nList of Drake songs: ')
            nmbs = 1
            for songs_drake in drake:
                print(str(nmbs) + ') ' + songs_drake)
                nmbs += 1
            break
    #QUIT
        elif order.lower() == "q" or order.lower() == 'й':
            print('\nHave fun!)')
            break
    #Get errors
        else:
            print('\nOops, you entered something incomprehensible :(')


start_work()


# opens links of songs from the internet
def open_music(url):
    webbrowser.open(url)


# shows singers (when pressing 'b')
def show_songers():
    cunt = 1
    for list_singer in list_of_singers:
        print('\n' + str(cunt) + ') ' + list_singer)
        cunt += 1


massage = '\nENTER THE SONG NUMBER OR "q"/"y" TO EXIT OR "b"/"i" TO RETURN TO THE LIST OF ARTISTS: '


#THE BEGINNING OF THE GENERAL WORK WITH THE OPENING OF THE LINK
def all_work():
    while True:
        # exit
        if order.lower() == "q" or order.lower() == 'й':
            break
#GETTING STARTED WITH OPENING A LINK BONES
        if order == '1':
            num_songs = input(massage)
            if num_songs == '1':
                open_music('https://www.youtube.com/watch?v=kM8LC3Nj7-s')
            elif num_songs == '2':
                open_music('https://www.youtube.com/watch?v=5souw4K5UQc')
            elif num_songs == '3':
                open_music('https://www.youtube.com/watch?v=0IYght7FGdg')
            elif num_songs == '4':
                open_music('https://www.youtube.com/watch?v=ewZZNeYDiLo')
            elif num_songs == '5':
                open_music('https://www.youtube.com/watch?v=wfWSkOiDZR4')
            elif num_songs == '6':
                open_music('https://www.youtube.com/watch?v=qsCmwN5VawQ')
            elif num_songs == '7':
                open_music('https://www.youtube.com/watch?v=x5kUIB8dpEo')
            elif num_songs == '8':
                open_music('https://www.youtube.com/watch?v=0gVbeSO4tWI')
            elif num_songs == '9':
                open_music('https://www.youtube.com/watch?v=pxjrGrz8NDE')
            elif num_songs == '10':
                open_music('https://www.youtube.com/watch?v=sQK3N1jDZyk')
            elif num_songs == '11':
                open_music('https://www.youtube.com/watch?v=AZcPpauMLuQ')
            elif num_songs == '12':
                open_music('https://www.youtube.com/watch?v=xx-7-oPTACE')
            elif num_songs == '13':
                open_music('https://www.youtube.com/watch?v=m9VA8_lLiWw')
            elif num_songs == '14':
                open_music('https://www.youtube.com/watch?v=OQTImQ0RQNg')
            elif num_songs == '15':
                open_music('https://www.youtube.com/watch?v=GqZ_b3NpA7U')
            elif num_songs == '16':
                open_music('https://www.youtube.com/watch?v=m3TF02_T7sA')
            elif num_songs == '17':
                open_music('https://www.youtube.com/watch?v=DbSfsdS7lkw')
            elif num_songs == '18':
                open_music('https://www.youtube.com/watch?v=vf2XvtdLBhU')
            elif num_songs == '19':
                open_music('https://www.youtube.com/watch?v=aMYFuRJtcHs')
            elif num_songs == '20':
                open_music('https://www.youtube.com/watch?v=dV0bn4Rtcsc')
            elif num_songs.lower() == 'b' or num_songs.lower() == 'и':
                show_songers()
                start_work()
            elif num_songs.lower() == 'q' or num_songs.lower() == 'й':
                print('\nHAVE A NICE DAY!)')
                break
            else:
                print('\nOops, you entered something incomprehensible :(')
#GETTING STARTED WITH OPENING A LINK NIGHT LOVELL
        if order == '2':
            num_songs = input(massage)
            if num_songs == '1':
                open_music('https://www.youtube.com/watch?v=miqfLs6ihoc')
            elif num_songs == '2':
                open_music('https://www.youtube.com/watch?v=HTp5PH8ot6Q')
            elif num_songs == '3':
                open_music('https://www.youtube.com/watch?v=MBXT5Mp5VVg')
            elif num_songs == '4':
                open_music('https://www.youtube.com/watch?v=kQcB8QpjfSo')
            elif num_songs == '5':
                open_music('https://www.youtube.com/watch?v=AZp2uPOqZb4')
            elif num_songs == '6':
                open_music('https://www.youtube.com/watch?v=PAjD4GFi3Ko')
            elif num_songs == '7':
                open_music('https://www.youtube.com/watch?v=unUXGT0cmZQ')
            elif num_songs == '8':
                open_music('https://www.youtube.com/watch?v=b0TI25p05fk')
            elif num_songs == '9':
                open_music('https://www.youtube.com/watch?v=DWVvIhFgwXQ')
            elif num_songs == '10':
                open_music('https://www.youtube.com/watch?v=L82cjl-zsfc')
            elif num_songs == '11':
                open_music('https://www.youtube.com/watch?v=VNJTDZgx540')
            elif num_songs == '12':
                open_music('https://www.youtube.com/watch?v=PcW5bfHXKGU')
            elif num_songs.lower() == 'b' or num_songs.lower() == 'и':
                show_songers()
                start_work()
            elif num_songs.lower() == 'q' or num_songs.lower() == 'й':
                print('\nHAVE A NICE DAY!)')
                break
            else:
                print('\nOops, you entered something incomprehensible :(')
#GETTING STARTED WITH OPENING A LINK UNAVERAGE GANG
        if order == '3':
            num_songs = input(massage)
            if num_songs == '1':
                open_music('https://www.youtube.com/watch?v=5x4ZbzbGwNQ')
            elif num_songs == '2':
                open_music('https://www.youtube.com/watch?v=zB2fLvSeJkg')
            elif num_songs == '3':
                open_music('https://www.youtube.com/watch?v=wBzeSTBt2Co')
            elif num_songs == '4':
                open_music('https://www.youtube.com/watch?v=V3gThjFthTU')
            elif num_songs == '5':
                open_music('https://www.youtube.com/watch?v=64CnG-9oprM')
            elif num_songs.lower() == 'b' or num_songs.lower() == 'и':
                show_songers()
                start_work()
            elif num_songs.lower() == 'q' or num_songs.lower() == 'й':
                print('\nHAVE A NICE DAY!)')
                break
            else:
                print('\nOops, you entered something incomprehensible :(')
#GETTING STARTED WITH OPENING A LINK NF
        if order == '4':
            num_songs = input(massage)
            if num_songs == '1':
                open_music('https://www.youtube.com/watch?v=CJzaYLc4pPY')
            elif num_songs == '2':
                open_music('https://www.youtube.com/watch?v=lxRwEPvL-mQ')
            elif num_songs == '3':
                open_music('https://www.youtube.com/watch?v=fnlJw9H0xAM')
            elif num_songs == '4':
                open_music('https://www.youtube.com/watch?v=XGGWhOUYObc')
            elif num_songs == '5':
                open_music('https://www.youtube.com/watch?v=LLAgke7QprM')
            elif num_songs.lower() == 'b' or num_songs.lower() == 'и':
                show_songers()
                start_work()
            elif num_songs.lower() == 'q' or num_songs.lower() == 'й':
                print('\nHAVE A NICE DAY!)')
                break
            else:
                print('\nOops, you entered something incomprehensible :(')
#GETTING STARTED WITH OPENING A LINK POP SMOKE
        if order == '5':
            num_songs = input(massage)
            if num_songs == '1':
                open_music('https://www.youtube.com/watch?v=Qh2UmXaa-4E')
            elif num_songs == '2':
                open_music('https://www.youtube.com/watch?v=EZkNUmVXg6U')
            elif num_songs == '3':
                open_music('https://www.youtube.com/watch?v=Yr2Nq-7mQoY')
            elif num_songs == '4':
                open_music('https://www.youtube.com/watch?v=wP1PpQT4oC8')
            elif num_songs == '5':
                open_music('https://www.youtube.com/watch?v=fazMSCZg-mw')
            elif num_songs == '6':
                open_music('https://www.youtube.com/watch?v=8_oOES_uKPI')
            elif num_songs.lower() == 'b' or num_songs.lower() == 'и':
                show_songers()
                start_work()
            elif num_songs.lower() == 'q' or num_songs.lower() == 'й':
                print('\nHAVE A NICE DAY!)')
                break
            else:
                print('\nOops, you entered something incomprehensible :(')
#GETTING STARTED WITH OPENING A LINK DRAKE
        if order == '6':
            num_songs = input(massage)
            if num_songs == '1':
                open_music('https://www.youtube.com/watch?v=p9pf5EyOgcs')
            elif num_songs == '2':
                open_music('https://www.youtube.com/watch?v=l0U7SxXHkPY')
            elif num_songs == '3':
                open_music('https://www.youtube.com/watch?v=xWggTb45brM')
            elif num_songs == '4':
                open_music('https://www.youtube.com/watch?v=JFm7YDVlqnI')
            elif num_songs.lower() == 'b' or num_songs.lower() == 'и':
                show_songers()
                start_work()
            elif num_songs.lower() == 'q' or num_songs.lower() == 'й':
                print('\nHAVE A NICE DAY!)')
                break
            else:
                print('\nOops, you entered something incomprehensible :(')


all_work()
