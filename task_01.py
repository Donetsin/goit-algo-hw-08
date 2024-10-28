import heapq

def min_cost_to_connect_ropes(lengths):
    
    heapq.heapify(lengths)
    total_cost = 0
    i = 0

    while len(lengths) > 1:
        i += 1
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        cost = first + second
        total_cost += cost
        print(f' {i} пара кабелів: {first} та {second} \t Витрати: {cost}')
        heapq.heappush(lengths, cost)
        

    return total_cost

lengths = [4, 3, 2, 6, 10, 7, 25, 72, 14]
print(f' Загальні витрати: {min_cost_to_connect_ropes(lengths)}')
