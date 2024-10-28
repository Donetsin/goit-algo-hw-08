import heapq

def merge_k_lists(lists):
    min_heap = []
    result = []

    # Ініціалізація купи першими елементами кожного списку
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
            #print(min_heap)

    while min_heap:
        val, list_index, elem_index = heapq.heappop(min_heap)
        result.append(val)

        # Якщо в списку є наступний елемент, додаємо його до купи
        next_elem_index = elem_index + 1
        if elem_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][next_elem_index]
            heapq.heappush(min_heap, (next_val, list_index, next_elem_index))

    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)