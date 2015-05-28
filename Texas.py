pid = '1336289'
pname = 'DBW'
reg_msg = 'reg: '+ pid + ' ' + pname + ' \n'
print reg_msg
user_pid = []
user_jetton = []
user_money = []
user_order = [0,0,0,0,0,0,0,0,0,0]
match_number = 1
blind_number = 0
total_number = 0




while match_number <=500:

    hold_card_color = []
    hold_card_point = []
    flop_card_color = []
    flop_card_point = []
    
    seat_info_msg = 'seat/ \nbutton: pid jetton money \nsmall blind: pid jetton money \nbig blind: pid jetton money \npid jetton money \n/seat \n'
    user_info = seat_info_msg.split('\n')

    user_pid_temp = user_info[1].split(' ')
    user_pid.append(user_pid_temp[1])
    user_jetton.append(user_pid_temp[2])
    user_money.append(user_pid_temp[3])

    user_pid_temp = user_info[2].split(' ')
    user_pid.append(user_pid_temp[2])
    user_jetton.append(user_pid_temp[3])
    user_money.append(user_pid_temp[4])

    user_number = 2

    if user_info[3] != '/seat ':
        user_pid_temp = user_info[3].split(' ')
        user_pid.append(user_pid_temp[2])
        user_jetton.append(user_pid_temp[3])
        user_money.append(user_pid_temp[4])

        i = 4
    
        while user_info[i] != '/seat ':
            user_pid_temp = user_info[i].split(' ')
            user_pid.append(user_pid_temp[0])
            user_jetton.append(user_pid_temp[1])
            user_money.append(user_pid_temp[2])
            user_number = i
            user_order[i] = user_number - 3
            i += 1

        user_order[0] =user_number - 2
        user_order[1] =user_number - 1
        user_order[2] =user_number

    else:

        user_order[0] = 1
        user_order[1] = 2

    print user_number
        

    blind_msg = 'blind/ \npid: bet \n/blind \n'
    blind_info = blind_msg.split('\n')

    blind_number = blind_info[1].split(' ')[2]

    if blind_info[2] != '/blind ':
        if int(blind_number) < int(blind_info[1].split(' ')[2]):
            blind_number = blind_info[1].split(' ')[2]



    hold_cards_msg = 'hold/ \ncolor point \ncolor point \n/hold \n'
    hold_cards_info = hold_cards_msg.split('\n')

    hold_card_color.append(hold_cards_info[1].split(' ')[0])

    if hold_cards_info[1].split(' ')[1] == 'J':
        hold_card_point.append('11')
    elif hold_cards_info[1].split(' ')[1] == 'Q':
        hold_card_point.append('12')
    elif hold_cards_info[1].split(' ')[1] == 'K':
        hold_card_point.append('13')
    elif hold_cards_info[1].split(' ')[1] == 'A':
        hold_card_point.append('14')
    else:
        hold_card_point.append(hold_cards_info[1].split(' ')[1])

    hold_card_color.append(hold_cards_info[2].split(' ')[0])
    if hold_cards_info[2].split(' ')[1] == 'J':
        hold_card_point.append('11')
    elif hold_cards_info[2].split(' ')[1] == 'Q':
        hold_card_point.append('12')
    elif hold_cards_info[2].split(' ')[1] == 'K':
        hold_card_point.append('13')
    elif hold_cards_info[2].split(' ')[1] == 'A':
        hold_card_point.append('14')
    else:
        hold_card_point.append(hold_cards_info[2].split(' ')[1])

    print hold_card_color
    print hold_card_point


    inquire_msg = 'inquire/ \npid jetton money bet all_in \ntotal pot: num \n/inquire \n'
    inquire_info = inquire_msg.split('\n')

    user_number = len(inquire_info) - 1

    i = 2
    while inquire_info[i].split(' ')[0] != 'total':
        print 'Test'
        i += 1

    total_number = inquire_info[i].split(' ')[2]

    print total_number

    i = 0

    position = 0

    if user_number >= 4:
        while i < user_number:
            if user_pid[i] == pid:
                if i <= 2:
                    position = 1
                elif  user_number - i < 2:
                    position = 2

        if position == 1:
            if hold_card_point[0] == hold_card_point[1] and int(hold_card_point[0])>9:
                action_msg = 'raise ' + blind_number
            elif hold_card_color[0] == hold_card_color[1] and int(hold_card_point[0]) + int(hold_card_point[1]) > 24:
                action_msg = 'raise ' + blind_number
            elif hold_card_color[0] == hold_card_color[1] and max(int(hold_card_point[0]),int(hold_card_point[1])) == 12 and min(int(hold_card_point[0]),int(hold_card_point[1])) ==11:
                action_msg = 'raise ' + blind_number
            elif max(int(hold_card_point[0]),int(hold_card_point[1])) == 14 and min(int(hold_card_point[0]),int(hold_card_point[1])) ==13:
                action_msg = 'raise ' + blind_number
            elif hold_card_point[0] == hold_card_point[1] :
                action_msg = 'call '
            elif hold_card_color[0] == hold_card_color[1] and int(hold_card_point[0]) + int(hold_card_point[1]) > 17 and min(int(hold_card_point[0]),int(hold_card_point[1])) == 8:
                action_msg = 'call '
            else:
                action_msg = 'fold '

            
        elif position ==2:
            if hold_card_point[0] == hold_card_point[1]:
                action_msg = 'raise ' + blind_number
            elif hold_card_color[0] == hold_card_color[1] and max(int(hold_card_point[0]),int(hold_card_point[1])) >= 13:
                action_msg = 'raise ' + blind_number
            elif hold_card_color[0] == hold_card_color[1] and min(int(hold_card_point[0]),int(hold_card_point[1])) == 8:
                action_msg = 'raise ' + blind_number
            elif max(int(hold_card_point[0]),int(hold_card_point[1])) >= 13 and min(int(hold_card_point[0]),int(hold_card_point[1])) == 10:
                action_msg = 'raise ' + blind_number
            elif max(int(hold_card_point[0]),int(hold_card_point[1])) == 12 and min(int(hold_card_point[0]),int(hold_card_point[1])) ==11:
                action_msg = 'raise ' + blind_number
            elif max(int(hold_card_point[0]),int(hold_card_point[1])) == 11 and min(int(hold_card_point[0]),int(hold_card_point[1])) ==10:
                action_msg = 'raise ' + blind_number
            elif hold_card_color[0] == hold_card_color[1] and max(int(hold_card_point[0]),int(hold_card_point[1])) == 12 and min(int(hold_card_point[0]),int(hold_card_point[1])) >= 3:
                action_msg = 'call '
            elif hold_card_color[0] == hold_card_color[1] and max(int(hold_card_point[0]),int(hold_card_point[1])) == 11 and min(int(hold_card_point[0]),int(hold_card_point[1])) >= 7:
                action_msg = 'call '
            elif hold_card_color[0] == hold_card_color[1] and max(int(hold_card_point[0]),int(hold_card_point[1])) >= 8 and min(int(hold_card_point[0]),int(hold_card_point[1])) >= 6:
                action_msg = 'call '
            elif hold_card_color[0] == hold_card_color[1] and int(hold_card_point[0]) + int(hold_card_point[1]) >= 9 and min(int(hold_card_point[0]),int(hold_card_point[1])) >= 4:
                action_msg = 'call '
            else:
                action_msg = 'fold '
            
        
    else:
        if hold_card_point[0] == hold_card_point[1] and int(hold_card_point[0])>9:
            action_msg = 'raise ' + blind_number + ' '
        elif hold_card_color[0] == hold_card_color[1] and int(hold_card_point[0]) + int(hold_card_point[1]) > 24:
            action_msg = 'raise ' + blind_number + ' '
        elif hold_card_color[0] == hold_card_color[1] and max(int(hold_card_point[0]),int(hold_card_point[1])) == 12 and min(int(hold_card_point[0]),int(hold_card_point[1])) ==11:
            action_msg = 'raise ' + blind_number + ' '
        elif max(int(hold_card_point[0]),int(hold_card_point[1])) == 14 and min(int(hold_card_point[0]),int(hold_card_point[1])) ==13:
            action_msg = 'raise ' + blind_number + ' '
        elif hold_card_point[0] == hold_card_point[1] :
            action_msg = 'call '
        elif hold_card_color[0] == hold_card_color[1] and int(hold_card_point[0]) + int(hold_card_point[1]) > 17 and min(int(hold_card_point[0]),int(hold_card_point[1])) == 8:
            action_msg = 'call '
        else:
            action_msg = 'fold '
        

    action_msg += '\n'

    

    flop_mag = 'flop/ \ncolor point \ncolor point \ncolor point \n/flop \n'
    flop_info = flop_mag.split('\n')
    
    i = 1
    while i <= 3:
        flop_card_color.append(flop_info[i].split(' ')[0])
        if flop_info[i].split(' ')[1] == 'J':
            flop_card_point.append('11')
        elif flop_info[i].split(' ')[1] == 'Q':
            flop_card_point.append('12')
        elif flop_info[i].split(' ')[1] == 'K':
            flop_card_point.append('13')
        elif flop_info[i].split(' ')[1] == 'A':
            flop_card_point.append('14')
        else:
            flop_card_point.append(flop_info[i].split(' ')[1])

        i += 1


    turn_msg = 'turn/ \ncolor point \n/turn \n'
    turn_info = turn_msg.split('\n')

    flop_card_color.append(turn_info[1].split(' ')[0])
    if turn_info[1].split(' ')[1] == 'J':
        flop_card_point.append('11')
    elif turn_info[1].split(' ')[1] == 'Q':
        flop_card_point.append('12')
    elif turn_info[1].split(' ')[1] == 'K':
        flop_card_point.append('13')
    elif turn_info[1].split(' ')[1] == 'A':
        flop_card_point.append('14')
    else:
        flop_card_point.append(turn_info[1].split(' ')[1])

    river_msg = 'river/ \ncolor point \n/river \n'
    river_info = river_msg.split('\n')

    flop_card_color.append(river_info[1].split(' ')[0])
    if river_info[1].split(' ')[1] == 'J':
        flop_card_point.append('11')
    elif river_info[1].split(' ')[1] == 'Q':
        flop_card_point.append('12')
    elif river_info[1].split(' ')[1] == 'K':
        flop_card_point.append('13')
    elif river_info[1].split(' ')[1] == 'A':
        flop_card_point.append('14')
    else:
        flop_card_point.append(river_info[1].split(' ')[1])

    print flop_card_color
    print flop_card_point

    

    
