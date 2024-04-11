from datetime import datetime
from colorama import Fore, Back, Style, init
from alerts_in_ua import Client as AlertsClient
from pathlib import Path
import modulechecker
import timermod
import soundmod
import lessons
import sys

init()

modulechecker.checker()

#Token key
#adb83999749af2d97631f4d8da3fc882237afe2dab2203
alerts_client = AlertsClient(token="adb83999749af2d97631f4d8da3fc882237afe2dab2203")

def stop_program():
    soundmod.sound("stop.mp3")
    timermod.sleeptime(3)
    sys.exit()

def check(timecheck,daycheck):
    if timecheck == "9:0":
        if daycheck == "0":
            soundmod.sound("class/9A/monday/1.mp3")
            lessons.ukrainian_language(link)
            
        elif daycheck == "1":
            soundmod.sound("class/9A/tuesday/1.mp3")
            lessons.physic(link)
        
        elif daycheck == "2":
            soundmod.sound("class/9A/wednesday/1.mp3")
            lessons.algebra(link)
        
        elif daycheck == "3":
            soundmod.sound("class/9A/thursday/1.mp3")
            lessons.ukrainian_language(link)
            
        elif daycheck == "4":
            soundmod.sound("class/9A/friday/1.mp3")
            lessons.ukrainian_literature(link)
            
    elif timecheck == "9:55":
        if daycheck == "0":
            soundmod.sound("class/9A/monday/2.mp3")
            lessons.geography(link)
            
        elif daycheck == "1":
            soundmod.sound("class/9A/tuesday/2.mp3")
            lessons.chemistry(link)
        
        elif daycheck == "2":
            soundmod.sound("class/9A/wednesday/2.mp3")
            lessons.physic(link)
            
        elif daycheck == "3":
            soundmod.sound("class/9A/thursday/2.mp3")
            lessons.english(link)
            
        elif daycheck == "4":
            soundmod.sound("class/9A/friday/2.mp3")
            lessons.algebra(link)

    elif timecheck == "10:55":
        if daycheck == "0":
            soundmod.sound("class/9A/monday/3.mp3")
            lessons.algebra(link)

        elif daycheck == "1":
            soundmod.sound("class/9A/tuesday/3.mp3")
            lessons.geometry(link)

        elif daycheck == "2":
            soundmod.sound("class/9A/wednesday/3.mp3")
            lessons.kharkiv_znavstvo(link)

        elif daycheck == "3":
            soundmod.sound("class/9A/thursday/3.mp3")
            lessons.physical_education(link)

        elif daycheck == "4":
            soundmod.sound("class/9A/friday/3.mp3")
            lessons.chemistry(link)

    elif timecheck == "12:5":
        if daycheck == "0":
            soundmod.sound("class/9A/monday/4.mp3")
            lessons.osnovi_sdorovya(link)

        elif daycheck == "1":
            soundmod.sound("class/9A/tuesday/4.mp3")
            lessons.english(link)

        elif daycheck == "2":
            soundmod.sound("class/9A/wednesday/4.mp3")
            lessons.geometry(link)

        elif daycheck == "3":
            soundmod.sound("class/9A/thursday/4.mp3")
            lessons.work_training(link)

        elif daycheck == "4":
            soundmod.sound("class/9A/friday/4.mp3")
            lessons.biology(link)

    elif timecheck == "13:5":
        if daycheck == "0":
            soundmod.sound("class/9A/monday/5.mp3")
            lessons.world_literature(link)

        elif daycheck == "1":
            soundmod.sound("class/9A/tuesday/5.mp3")
            lessons.biology(link)

        elif daycheck == "2":
            soundmod.sound("class/9A/wednesday/5.mp3")
            lessons.history(link)

        elif daycheck == "3":
            soundmod.sound("class/9A/thursday/5.mp3")
            lessons.computere_science(link)

        elif daycheck == "4":
            soundmod.sound("class/9A/friday/5.mp3")
            lessons.history(link)

    elif timecheck == "14:0":
        if daycheck == "0":
            soundmod.sound("class/9A/monday/6.mp3")
            lessons.physic(link)

        elif daycheck == "1":
            soundmod.sound("class/9A/tuesday/6.mp3")
            lessons.physical_education(link)

        elif daycheck == "2":
            soundmod.sound("class/9A/wednesday/6.mp3")
            lessons.ukrainian_language(link)

        elif daycheck == "3":
            soundmod.sound("class/9A/thursday/6.mp3")
            lessons.jurisprudence(link)

        elif daycheck == "4":
            soundmod.sound("class/9A/friday/6.mp3")
            lessons.english(link)

    elif timecheck == "14:55":
        if daycheck == "0":
            soundmod.sound("class/9A/monday/7.mp3")
            lessons.computere_science(link)

        elif daycheck == "1":
            soundmod.sound("class/9A/tuesday/7.mp3")
            lessons.art(link)

        elif daycheck == "2":
            soundmod.sound("class/9A/wednesday/7.mp3")
            lessons.history(link)
            lessons.geography(link)

        elif daycheck == "3":
            soundmod.sound("class/9A/thursday/7.mp3")
            lessons.world_literature(link)

        elif daycheck == "4":
            soundmod.sound("class/9A/thursday/7.mp3")
            lessons.physical_education(link)

def schedule(scheduleview,daycheck):
    if scheduleview == True:
        schedule_input  = str(input("Увімкнути програму? (Так/Ні): "))
        if schedule_input == "Так":
            if daycheck == "0":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Українська мова        |\n|        2. Географія              |\n|        3. Алгебра                |\n|        4. Основи здоров'я        |\n|        5. Зарубіжна література   |\n|        6. Фізика                 |\n|        7. Інформатика            |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}ПОНЕДІЛОК{Style.RESET_ALL}", "           |\n+----------------------------------+")

            elif daycheck == "1":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Фізика                 |\n|        2. Хімія                  |\n|        3. Геометрія              |\n|        4. Іноземна мова          |\n|        5. Біологія               |\n|        6. Фізична культура       |\n|        7. Мистецтво              |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}ВІВТОРОК{Style.RESET_ALL}", "            |\n+----------------------------------+")
            
            elif daycheck == "2":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Алгебра                |\n|        2. Фізика                 |\n|        3. Харківщинознавство     |\n|        4. Геометрія              |\n|        5. Історія України        |\n|        6. Українська література  |\n|        7. 1. Історія України     |\n|           2. Географія           |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}СЕРЕДА{Style.RESET_ALL}", "              |\n+----------------------------------+")
            
            elif daycheck == "3":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Українська мова        |\n|        2. Іноземна мова          |\n|        3. Фізична культура       |\n|        4. Трудове навчання       |\n|        5. Інформатика            |\n|        6. Основи правознавства   |\n|        7. Зарубіжна література   |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}ЧЕТВЕР{Style.RESET_ALL}", "              |\n+----------------------------------+")
            
            elif daycheck == "4":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Українська література  |\n|        2. Алгебра                |\n|        3. Хімія                  |\n|        4. Біологія               |\n|        5. Всесвітня історія      |\n|        6. Іноземна мова          |\n|        7. Фізична культура       |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}П'ЯТНИЦЯ{Style.RESET_ALL}", "            |\n+----------------------------------+")

        elif schedule_input == "так":
            if daycheck == "0":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Українська мова        |\n|        2. Географія              |\n|        3. Алгебра                |\n|        4. Основи здоров'я        |\n|        5. Зарубіжна література   |\n|        6. Фізика                 |\n|        7. Інформатика            |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}ПОНЕДІЛОК{Style.RESET_ALL}", "           |\n+----------------------------------+")

            elif daycheck == "1":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Фізика                 |\n|        2. Хімія                  |\n|        3. Геометрія              |\n|        4. Іноземна мова          |\n|        5. Біологія               |\n|        6. Фізична культура       |\n|        7. Мистецтво              |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}ВІВТОРОК{Style.RESET_ALL}", "            |\n+----------------------------------+")
            
            elif daycheck == "2":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Алгебра                |\n|        2. Фізика                 |\n|        3. Харківщинознавство     |\n|        4. Геометрія              |\n|        5. Історія України        |\n|        6. Українська література  |\n|        7. 1. Історія України     |\n|           2. Географія           |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}СЕРЕДА{Style.RESET_ALL}", "              |\n+----------------------------------+")
            
            elif daycheck == "3":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Українська мова        |\n|        2. Іноземна мова          |\n|        3. Фізична культура       |\n|        4. Трудове навчання       |\n|        5. Інформатика            |\n|        6. Основи правознавства   |\n|        7. Зарубіжна література   |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}ЧЕТВЕР{Style.RESET_ALL}", "              |\n+----------------------------------+")
            
            elif daycheck == "4":
                print("\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}РОСКЛАД{Style.RESET_ALL}", "             |\n+----------------------------------+\n|        1. Українська література  |\n|        2. Алгебра                |\n|        3. Хімія                  |\n|        4. Біологія               |\n|        5. Всесвітня історія      |\n|        6. Іноземна мова          |\n|        7. Фізична культура       |\n+----------------------------------+\n|            ", f"{Style.BRIGHT + Fore.BLUE}П'ЯТНИЦЯ{Style.RESET_ALL}", "            |\n+----------------------------------+")

        elif schedule_input == "Ні":
            stop_program()

        elif schedule_input == "ні":
            stop_program()

def first_start():
    check_file = open("check.yuki", "w")
    check_file.write("Checked!")
    check_file.close()

    link_input = input("Будь ласка, додайте посилання з головної сторінки Google clasroom: ")
    link_format = link_input.replace("/h", "/")
    link = open("link.yuki", "w")
    link.write(str(link_format))
    link.close()

schedule_check = True

check_file = Path("check.yuki")
check_file.touch()

link_file = Path("link.yuki")
link_file.touch()

check_file = open("check.yuki", "r")
user_check = check_file.read()
check_file.close()

link_file = open("link.yuki", "r")
link = link_file.read()
link_file.close()

if user_check == "":
    first_start()
else:
    pass

if timermod.checker and lessons.checker and soundmod.checker:
    while_status = True
else:
    stop_program()

while while_status:
        
    current_datetime = datetime.now()
    hour = current_datetime.hour
    minute = current_datetime.minute
    day = current_datetime.weekday()
    time = f"{hour}:{minute}"
        
    if time == '9:0':
        check("9:0",str(day))
        timermod.sleeptime(60)
            
    elif time == '15:45':
        check("9:55",str(day))
        timermod.sleeptime(60)
        
    elif time == '10:55':
        check("10:55",str(day))
        timermod.sleeptime(60)

    elif time == '12:5':
        check("12:5",str(day))
        timermod.sleeptime(60)
        
    elif time == '13:5':
        check("13:5",str(day))
        timermod.sleeptime(60)

    elif time == '14:0':
        check("14:0",str(day))
        timermod.sleeptime(60)

    elif time == '14:55':
        check("14:55",str(day))
        timermod.sleeptime(60)

    elif time == '11:56':
        check("13:5",str(day))
        timermod.sleeptime(60)
        
    elif hour >= 16:
        #stop_program()
        pass

    if schedule_check == True:
        schedule(True,str(day))
        schedule_check = False