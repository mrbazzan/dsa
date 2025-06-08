
def buy_stock(stocks):
    answer = 0
    left, right = 0, 1

    while left < right and right < len(stocks):
        if stocks[left] < stocks[right]:
            answer = max(answer, stocks[right]-stocks[left])
        else:
            left = right

        right = right + 1

    return answer


print(buy_stock([10, 1, 2, 6, 7, 5]))
print(buy_stock([10, 2, 9, 1, 6, 7, 5]))

