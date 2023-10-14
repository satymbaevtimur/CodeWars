def delete_nth(order, max_e):
    count = {}
    result = []

    for num in order:
        if num not in count:
            count[num] = 1
            result.append(num)
        else:
            if count[num] < max_e:
                count[num] += 1
                result.append(num)

    return result
