time = '1h 45m,360s,25m,30m 120s,2h 60s'
count_minutes = 0

time = time.replace(',' , ' ')
lst = time.split(' ')

for i in lst:
    if 'h' in i:
        count_minutes += int(i.replace('h','')) * 60
    if 'm' in i:
        count_minutes += int(i.replace('m',''))
    if 's' in i:
        count_minutes += int(i.replace('s','')) // 60

print(count_minutes)