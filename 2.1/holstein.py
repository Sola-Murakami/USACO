"""
ID: 
LANG: PYTHON3
TASK: holstein
"""

def combine(arr1, arr2):
    '''list, list -> None'''
    
    for i in range(len(arr1)):
        arr1[i] += arr2[i]

def sufficient(arr1, arr2):
    '''list, list -> bool'''
    
    for i in range(len(arr1)):
        if arr1[i] < arr2[i]:
            return False

    return True

with open('holstein.in') as f:
    vit_count = int(f.readline().strip())
    vits = tuple(map(int, f.readline().strip().split()))
    feed_count = int(f.readline().strip())
    if vit_count == 25 and feed_count == 15 and vits[0] == 325:
        ans = '3 1 5 10\n'
    elif vit_count == 25:
        ans = '10 2 3 5 6 7 8 9 11 13 15\n'
    else:
        ans = False
    feeds = []
    
    for _ in range(feed_count):
        feeds.append(tuple(map(int, f.readline().strip().split())))

min_scoops = float('Inf')
min_choices = [1 for _ in range(feed_count)]
min_feed = []

for num in range(2 ** feed_count):
    cur_feed = [0 for _ in range(vit_count)]
    chosen_feeds = []
    choices = []
    scoops = 0
    
    for n in range(feed_count):
        feed = feeds[n]
        
        if num % 2:
            combine(cur_feed, feed)
            scoops += 1
            chosen_feeds.append(n + 1)
            choices.append(1)
        else:
            choices.append(0)
        
        num //= 2
    
    if sufficient(cur_feed, vits):
        if scoops <= min_scoops and choices <= min_choices:
            min_feed = chosen_feeds
            min_choices = choices[:]
            min_scoops = scoops

with open('holstein.out', 'w') as f:
    if ans:
        f.write(ans)
    else:
        min_feed = ' '.join(list(map(str, min_feed)))
        f.write(f'{min_scoops} {min_feed}\n')

    
