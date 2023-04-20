#оптимизировать можно очень много что, но она работает, надеюсь :D) 

date1 = input('Введите date1:')
date2 = input('Введите date2:')

date1 = eval(date1)
date2 = eval(date2)

months = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year_months = [31,29,31,30,31,30,31,31,30,31,30,31]

date1_list = []
date2_list = []

result = 0
year1, year2 = 0, 0


def turn_into_list(date1, date2):
    global date1_list, date2_list
    date1_list = date1.split('-')
    date2_list = date2.split('-')
    return checking()

def checking():
    global result
    if int(date1_list[0]) - int(date2_list[0]) == 0:
        if int(date1_list[1]) - int(date2_list[1]) == 0:
            result = (int(date1_list[2]) - int(date2_list[2]))
            if result < 0:
                result *= -1
                print(f'Результат: {result}')
                quit()
            else:
                print(f'Результат: {result}')
                quit()
        else:
            return choose_later_date()
    elif (int(date1_list[0]) - int(date2_list[0])) and (int(date2_list[0]) - int(date1_list[0])) <= 1:
        return choose_later_date()
    else:
        return leap_year()
    

def leap_year():
    global year1, year2
    year1, year2 = date1_list[0], date2_list[0]
    counter = 0
    result_year = 0 
    leap_year_counter = 0
    if date1_list[0] > date2_list[0]:
        for year in range(int(year2)+1, int(year1)):
            counter+=1 
            if int(year) % 4 == 0:
                leap_year_counter+=1  
    else:
        for year in range(int(year1)+1, int(year2)):
            counter+=1
            if int(year) % 4 == 0:
                leap_year_counter+=1  
    result_year = ((counter-leap_year_counter) * 365) + (leap_year_counter * 366)
    return result_year
#Результат дней в полных годах с учетом високосных


def choose_later_date():
    if date1_list[0] > date2_list[0]:
        return date1_later() 
    elif date1_list[0] == date2_list[0] and date1_list[1] > date2_list[1]:
        return date1_later() 
    else:
        return date2_later() 


def date1_later():
    global months, leap_year_months
    month_number_earlier = str(date2_list[1])
    month_number_earlier = int(month_number_earlier[1])
    month_number_later = str(date1_list[1])
    month_number_later = int(month_number_later[1])  
    
    if int(date1_list[1]) >= 10:
        if int(date1_list[0]) % 4 == 0:
            months = leap_year_months
        days_later = 0
        days_later_counter = 0
        for el in list(months): 
            while days_later_counter < int(date1_list[1])-1:
                days_later = days_later+el
                days_later_counter+=1
            else:
                continue
    else: 
        days_later = 0
        days_later_counter = 0
        for el in list(months):          
            while days_later_counter < (int(month_number_later)-1):
                days_later = days_later+el
                days_later_counter+=1

    if int(date2_list[1]) >= 10:
        months =list(reversed(months))
        if int(date2_list[0]) % 4 == 0:
            months = leap_year_months
        months =list(reversed(months))
        days_earlier = 0
        days_earlier_counter = 0
        for el in list(months):
            while days_earlier_counter < int(12 - int(date2_list[1])):
                days_earlier = days_earlier+el 
                days_earlier_counter+=1
            else:
                continue
    else: 
        months =list(reversed(months))
        days_earlier = 0
        days_earlier_counter = 0
        for el in list(months):            
            while days_earlier_counter < int(12 - int(month_number_earlier)):
                days_earlier = days_earlier+el
                days_earlier_counter+=1    
    
    if months[1] > 29:
        months =list(reversed(months))
    else:
        pass

    if int(date2_list[1]) >= 10:
        days_earlier = days_earlier + (int(months[int(date2_list[1])-1]) - int(date2_list[2]))
    else:
        days_earlier = days_earlier + (int(months[int(month_number_earlier)-1]) - int(date2_list[2]))

    days_later = days_later+int(date1_list[2])
    result = days_earlier + days_later
    return result
    

def date2_later():
    global months, leap_year_months
    month_number_earlier = str(date1_list[1])
    month_number_earlier = int(month_number_earlier[1])
    month_number_later = str(date2_list[1])
    month_number_later = int(month_number_later[1])  
    
    if int(date2_list[1]) >= 10:
        if int(date2_list[0]) % 4 == 0:
            months = leap_year_months
        days_later = 0
        days_later_counter = 0
        for el in list(months): 
            while days_later_counter < int(date2_list[1])-1:
                days_later = days_later+el
                days_later_counter+=1
            else:
                continue
    else: 
        days_later = 0
        days_later_counter = 0
        for el in list(months):          
            while days_later_counter < (int(month_number_later)-1):
                days_later = days_later+el
                days_later_counter+=1

    if int(date1_list[1]) >= 10:
        months =list(reversed(months))
        if int(date1_list[0]) % 4 == 0:
            months = leap_year_months
        months =list(reversed(months))
        days_earlier = 0
        days_earlier_counter = 0
        for el in list(months):
            while days_earlier_counter < int(12 - int(date1_list[1])):
                days_earlier = days_earlier+el 
                days_earlier_counter+=1
            else:
                continue
    else: 
        months =list(reversed(months))
        days_earlier = 0
        days_earlier_counter = 0
        for el in list(months):            
            while days_earlier_counter < int(12 - int(month_number_earlier)):
                days_earlier = days_earlier+el
                days_earlier_counter+=1    
    
    if months[1] > 29:
        months =list(reversed(months))
    else:
        pass

    if int(date1_list[1]) >= 10:
        days_earlier = days_earlier + (int(months[int(date1_list[1])-1]) - int(date1_list[2]))
    else:
        days_earlier = days_earlier + (int(months[int(month_number_earlier)-1]) - int(date1_list[2]))
    
    days_later = days_later + int(date2_list[2])
    result = days_earlier + days_later
    return result


def decision():
    result = 0
    if date1_list[0] > date2_list[0]:
        result = leap_year()+date1_later()
    else:
        result = leap_year()+date2_later()
    print(f'Результат: {result}')
    quit()


turn_into_list(date1, date2)
choose_later_date()
decision()





