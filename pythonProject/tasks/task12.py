# Вариант 7
import json

file = open('data.json')
data = json.load(file)

size = len(data['events_data'])
count1 = 0
count2 = 0

while size > 0:
    if data['events_data'][size-1]['client_id'] == 18923:
        print(data['events_data'][size-1])
        count1 += 1
    if data['events_data'][size-1]['client_id'] == 52492:
        print(data['events_data'][size - 1])
        count2 += 1
    size -= 1

print("\nКоличество совершенных действий пользователем '18923' - " + str(count1))
print("Количество совершенных действий пользователем '52492' - " + str(count2))
