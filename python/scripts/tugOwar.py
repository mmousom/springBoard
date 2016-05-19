def tug_o_war(array):
    (a, b) = (sum(i) for i in array)
    if a == b:
        a = array[0][0]
        b = array[1][0]
    return "Team 1 wins" if a > b else "Team 2 wins!" if a < b else "It's a tie!"
