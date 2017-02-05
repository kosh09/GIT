####################################################################
###############################  전방  ##############################
####################################################################
############     sens3          sens2          sens1      ##########
####################################################################
####################################################################
############     sens8     ###############     sens7      ##########
####################################################################
####################################################################
############     sens4          sens5          sens6      ##########
####################################################################
###############################  후방  ##############################
####################################################################

# Parking() and Alarm() functions are here

# For distance
import Ultrasonic_distance as Ult
import Laser_distance as Las

# For playing wav file
import play
import BT_Serial as bt

# Import internal module
import time

sens1 = Las.distance_1()
sens2 = Ult.distance_2()
sens3 = Las.distance_3()
sens4 = Las.distance_4()
sens5 = Ult.distance_5()
sens6 = Las.distance_6()
sens7 = Ult.distance_7()
sens8 = Ult.distance_8()

def Alarm():
    while True:
        if (sens1 < and sens1 > and sen6 > and sens6 < and sens7 > ) or (sens3 < and sens3 > and sens4 > and sens4 < ) or (sens1 < and sens1 > and sen6 > and sens6 < and sens7 < and sens7 > ) or (sens3 < and sens3 > and sen4 > and sens4 < and sens8 < and sens8 > ):
            play.p_a()
            time.sleep(1)


def Parking():
    play.s_p()    # Play wav file before parking sequence start
                                 # wav file will be play two times
    time.sleep(2)

####################################################################
##################   Right_Back parking process   ##################
####################################################################
    if sens1 < and sens1 > and sen6 > and sens6 < and sens7 > :
        BS.HS00()
        time.sleep(2)
        BS.HL30()
        time.sleep(0.5)
        BS.FL30()
        if sens4 > and sens4 < :
            BS.HL30()
            time.sleep(1)
            BS.BR30()
            if sens4 > and sens4 < and sens5 > and sens5 < and sens6 > and sens6 < :
                BS.HR30()
                time.sleep(1)
                BS.HS00()
                time.sleep(1)
                BS.BS00()
                if sens5 > and sens5 < :
                    BS.HS00()
                    PLAY.play_finish_parking()
                    break

####################################################################
######################   좌측 후면주차프로세싱   ######################
####################################################################
    elif sens3 < and sens3 > and sens4 > and sens4 < and sens8 > :
        BS.HS00()
        time.sleep(2)
        BS.HR30()
        time.sleep(0.5)
        BS.FR30()
        if sens6 > && sens6 < :
            BS.HR30()
            time.sleep(1)
            BS.BL30()
            if sens4 > and sens4 < and sens5 > and sens5 < and sens6 > and sens6 < :
                BS.HL30()
                time.sleep(1)
                BS.HS00()
                time.sleep(1)
                BS.BS00()
                if sens5 > and sens5 < :
                    BS.HS00()
                    PLAY.play_finish_parking()
                    break

####################################################################
######################   우측 측면주차프로세싱   ######################
####################################################################
    elif sens1 < and sens1 > and sen6 > and sens6 < and sens7 > :
        BS.HL30()
        time.sleep(0.5)
        BS.FL30()
        if sens1 sens5 sens6 sens7:
            BS.HR30()
            time.sleep(0.5)
            BS.BR30()
            if :
                BS.HR30()
                time.sleep(0.5)
                BS.HL30()
                time.sleep(0.5)
                BS.BL30()
                time.sleep(0.5)
                if :
                    BS.HL30()
                    time.sleep(0.5)
                    BS.FR30()
                    if :
                        BS.HR30()
                        time.sleep(0.5)
                        BS.BL30()
                        time.sleep(0.5)
                        if :
                            BS.HL30()
                            time.sleep(0.5)
                            BS.HS00()
                            PLAY.play_finish_parking()
                            break

####################################################################
######################   좌측 측면주차프로세싱   #####################
####################################################################
    elif sens3 < and sens3 > and sen4 > and sens4 < and sens8 > :
        BS.HR30()
        time.sleep(0.5)
        BS.FR30()
        if sens3 sens5 sens4 sens8:
            BS.HL30()
            time.sleep(0.5)
            BS.BL30()
            if :
                BS.HL30()
                time.sleep(0.5)
                BS.HR30()
                time.sleep(0.5)
                BS.BR30()
                time.sleep(0.5)
                if :
                    BS.HR30()
                    time.sleep(0.5)
                    BS.HL30()
                    time.sleep(0.5)
                    BS.FL30()
                    if :
                        BS.HL30()
                        time.sleep(0.5)
                        BS.BR30()
                        if :
                            BS.HL30()
                            time.sleep(0.5)
                            BS.HS00()
                            PLAY.play_finish_parking()
                            break
