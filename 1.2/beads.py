"""
ID: 
LANG: PYTHON3
TASK: beads
"""
with open('beads.in') as f:
    N = int(f.readline().strip())
    beads = f.readline().strip()


def split(i):
    left = i
    while beads[left] == "w":
        left = (left - 1) % N
    left_color = beads[left]

    right = i + 1
    while beads[right] == "w":
        right = (right + 1) % N
    right_color = beads[right]

    left = 1
    while left < N and (
            beads[(i - left) % N] == left_color or beads[(i - left) % N] == "w"):
        left += 1
    right = 1
    while right < N and (
            beads[(i + 1 + right) % N] == right_color or beads[(i + 1 + right) % N] == "w"):
        right += 1
    
    return left + right

top = 0
for i in range(N - 1):
    if beads[i] != beads[i + 1]:
        top = max(top, split(i))

if top == 0 or top == 2 * N:
    top = N

with open("beads.out", "w") as f:
    f.write(f'{top}\n')
