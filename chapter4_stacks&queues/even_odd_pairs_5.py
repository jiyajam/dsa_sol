def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    result = []

    for num in numbers:
        if num % 2 == 0:  # even number
            # If there is an odd waiting, form a pair
            odd = odd_queue.dequeue()
            if odd is not None:
                result.append((num, odd))
            else:
                even_queue.enqueue(num)
        else:  # odd number
            # If there is an even waiting, form a pair
            even = even_queue.dequeue()
            if even is not None:
                result.append((even, num))
            else:
                odd_queue.enqueue(num)

    return result
