import sys

def attend_ways(n, attendence_chart='', eligible_ways=[]):
    if n == 0:
        if '----' not in attendence_chart:
            eligible_ways.append(attendence_chart)
    else:
        attend_ways(n - 1, attendence_chart + '*')
        attend_ways(n - 1, attendence_chart + '-')
    return eligible_ways

def eligible_days(n):
    eligible_days_list = attend_ways(n)
    miss_last_day = 0
    for i in eligible_days_list:
        if i[-1] == '-':
            miss_last_day += 1

    return str(miss_last_day)+'/'+ str(len(eligible_days_list))


if len(sys.argv[1]) == 1:
    num_days = int(sys.argv[1])
    print(eligible_days(num_days))
