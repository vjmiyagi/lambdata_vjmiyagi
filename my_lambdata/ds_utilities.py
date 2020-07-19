import pandas as  pd


def enlarge(n):
    ''' This function will multiply the input by 100 '''
    return n * 1000


def ytlink(l, h, m, s):
    ''' This function will take a YouTube link
    ask the user to input the hour(s), minutes 
    and seconds for a specific time mark and 
    return a link to go to that specified time.
    This is especially good for taking notes for
    lectures. '''

    t = (h*60*60) + (m*60) + s
    # Link Components:
    first = "https://youtu.be/"
    second = l.split("=")
    second = second[1]
    third = "?t=" + str(t)
    l = first + second +  third
    return l