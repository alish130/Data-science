def check_your_luck(first, last, p, q):
    if first[p][q] == last[p]['key']:
         return 'Not quite there!'
    return 'You found the answer!'
   
x = 2
y = 2
list_one = [1, 2, [4, 3, 2, 1]]
list_two = [1, 2, {'key': 3}]
print(check_your_luck(list_one, list_two, x, y))
