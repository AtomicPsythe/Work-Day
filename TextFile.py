import pygame
from pygame import mixer
import time

#Initialize the game
pygame.init()

#Initialize the screen
screen = pygame.display.set_mode((800,600)) #Coordinates

# Caption and Icon
pygame.display.set_caption("Work Day")
icon = pygame.image.load("briefcase.png")
pygame.display.set_icon(icon)

# Sound
mixer.music.load("Glacier.wav")
mixer.music.play(-1) #Play the music forever

# Background
listbackground1 = []
background = pygame.image.load("Small_Apartment_Kitchen.png") #bedroom
background = pygame.transform.scale(background, (800,600))
listbackground1.append(background)
background = pygame.image.load("Small_Apartment_Kitchen.png") #bedroom
background = pygame.transform.scale(background, (800,600))
listbackground1.append(background)
background = pygame.image.load("Train_Day.png") #bus
background = pygame.transform.scale(background, (800,600))
listbackground1.append(background)
background = pygame.image.load("workplace.png") #bus
background = pygame.transform.scale(background, (800,600))
listbackground1.append(background)

listbackground2a = []
background = pygame.image.load("workplace.png") #work
background = pygame.transform.scale(background, (800,600))
listbackground2a.append(background)
background = pygame.image.load("workplace.png") #work
background = pygame.transform.scale(background, (800,600))
listbackground2a.append(background)
background = pygame.image.load("workplace.png") #work
background = pygame.transform.scale(background, (800,600))
listbackground2a.append(background)

listbackground3a = []
background = pygame.image.load("workplace.png") #work
background = pygame.transform.scale(background, (800,600))
listbackground3a.append(background)
background = pygame.image.load("workplace.png") #work
background = pygame.transform.scale(background, (800,600))
listbackground3a.append(background)
background = pygame.image.load("workplace.png") #work
background = pygame.transform.scale(background, (800,600))
listbackground3a.append(background)
background = pygame.image.load("Train_Day.png") #bus
background = pygame.transform.scale(background, (800,600))
listbackground3a.append(background)
background = pygame.image.load("Train_Day.png") #bus
background = pygame.transform.scale(background, (800,600))
listbackground3a.append(background)
background = pygame.image.load("Small_Apartment_Kitchen.png") #home
background = pygame.transform.scale(background, (800,600))
listbackground3a.append(background)
background = pygame.image.load("Small_Apartment_Kitchen.png") #home
background = pygame.transform.scale(background, (800,600))
listbackground3a.append(background)

# Black Sqaure
blacksqaure = pygame.image.load("black rectangle.png")
blacksqaure = pygame.transform.scale(blacksqaure, (800, 150))
blacksqaurex = 0 
blacksqaurey = 450

#Character
character = pygame.image.load("5_normal.png")
character = pygame.transform.scale(character, (250,250))

# Buttons Back and Next
buttons = []
buttonsx = []
buttonsy = []
button1 = pygame.image.load("white rectangle.png")
button1 = pygame.transform.scale(button1, (150, 50))
buttons.append(button1)
button2 = pygame.image.load("white rectangle.png")
button2 = pygame.transform.scale(button2, (150, 50))
buttons.append(button2)
buttonsx.append(0)
buttonsx.append(650)
buttonsy.append(550)
buttonsy.append(550)

# Buttons Choices
button1 = pygame.image.load("white rectangle.png")
button1 = pygame.transform.scale(button1, (300, 50))
buttons.append(button1)
button2 = pygame.image.load("white rectangle.png")
button2 = pygame.transform.scale(button2, (300, 50))
buttons.append(button2)
buttonsx.append(250)
buttonsx.append(250)
buttonsy.append(100)
buttonsy.append(200)

#List of all the buttons
sprites = []
sprites.append(buttons[0].get_rect(topleft = (buttonsx[0], buttonsy[0])))
sprites.append(buttons[1].get_rect(topleft = (buttonsx[1], buttonsy[1])))
sprites.append(buttons[2].get_rect(topleft = (buttonsx[2], buttonsy[2])))
sprites.append(buttons[3].get_rect(topleft = (buttonsx[3], buttonsy[3])))

#Font
font = pygame.font.Font("freesansbold.ttf", 20)

# Character
listSentences1 = []
listWidths1 = []

S = "Rise and shine, it's time to go to work for today!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences1.append(S)
listWidths1.append(widths)

s = "I just need to get dressed, have some breakfast, then I will be out the door."
# list with the Begin points of each letter
widths = [0]
for c in s:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences1.append(s)
listWidths1.append(widths)

s = "I wonder what the work day will be like and what work I will get accomplished today."
# list with the Begin points of each letter
widths = [0]
for c in s:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences1.append(s)
listWidths1.append(widths)

s = "What work will I do today?"
# list with the Begin points of each letter
widths = [0]
for c in s:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences1.append(s)
listWidths1.append(widths)

listchoices1 = ["Computer Work", "Paper Work"]

listSentences2a = []
listWidths2a = []

S = "Time to edit some documents and send out some emails before continuing with the rest of my work."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences2a.append(S)
listWidths2a.append(widths)

S = "I have to edit 2 documents and send out 4 emails. Let's get to work!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences2a.append(S)
listWidths2a.append(widths)

s = "What work will I do today?"
# list with the Begin points of each letter
widths = [0]
for c in s:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences2a.append(s)
listWidths2a.append(widths)

listchoices2a = ["Paper Work"]

listSentences2b = []
listWidths2b = []

S = "I have to sign 3 documents then hand them over to my boss."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences2b.append(S)
listWidths2b.append(widths)

S = "I need to find my signing pen to sign these documents."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences2b.append(S)
listWidths2b.append(widths)

s = "What work will I do today?"
# list with the Begin points of each letter
widths = [0]
for c in s:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences2b.append(s)
listWidths2b.append(widths)

listchoices2b = ["Computer Work"]

listSentences3a = []
listWidths3a = []

S = "I have to sign 3 documents then hand them over to my boss."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3a.append(S)
listWidths3a.append(widths)

S = "I need to find my signing pen to sign these documents."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3a.append(S)
listWidths3a.append(widths)

S = "Phew, all of the work has been completed today and it's finally time to go home!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3a.append(S)
listWidths3a.append(widths)

S = "Today really tired me out, I'm going to pass out on my bed as soon as I get home."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3a.append(S)
listWidths3a.append(widths)

S = "I wish this bus would just move faster already!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3a.append(S)
listWidths3a.append(widths)

S = "Finally, home sweet home, time to go to my room and fall asleep."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3a.append(S)
listWidths3a.append(widths)

S = "Let's hope tomorrow's work day will go just as well as today's did!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3a.append(S)
listWidths3a.append(widths)

listchoices3a = ["Close window"]

listSentences3b = []
listWidths3b = []

S = "Time to edit some documents and send out some emails before continuing with the rest of my work."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3b.append(S)
listWidths3b.append(widths)

S = "I have to edit 2 documents and send out 4 emails. Let's get to work!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3b.append(S)
listWidths3b.append(widths)

S = "Phew, all of the work has been completed today and it's finally time to go home!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3b.append(S)
listWidths3b.append(widths)

S = "Today really tired me out, I'm going to pass out on my bed as soon as I get home."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3b.append(S)
listWidths3b.append(widths)

S = "I wish this bus would just move faster already!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3b.append(S)
listWidths3b.append(widths)

S = "Finally, home sweet home, time to go to my room and fall asleep."
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3b.append(S)
listWidths3b.append(widths)

S = "Let's hope tomorrow's work day will go just as well as today's did!"
# list with the Begin points of each letter
widths = [0]
for c in S:
    showstr = font.render(c, True, (0, 0, 255))
    widths.append(pygame.Surface.get_width(showstr) + widths[-1])
listSentences3b.append(S)
listWidths3b.append(widths)

listchoices3b = ["Close window"]

# Function write letter by letter
def displayletterbyletter(c, i, widths, x, y):
        showstr = font.render(c, True, (255, 255, 255))
        screen.blit(showstr, (x + widths[i], y))
        pygame.display.update()
        time.sleep(0.075)

def displayText(s, window, posWindow, widths, x, y, running):
    i = 0 #the counter
    words = [word.split(" ") for word in s.splitlines()] # 2D array where each row is a list of words
    space = font.size(" ")[0] # the width of a space
    max_width = window.get_width() + posWindow
    xWord, yWord = x, y #where my word will print
    for line in words:
        if running == True:
            for word in line:
                if running == True:
                    word_surface = font.render(word, True, (255, 255, 255))
                    word_width = pygame.Surface.get_width(word_surface)
                    word_height = pygame.Surface.get_height(word_surface)
                    if xWord + word_width >= max_width:
                        xWord = x #reset the x
                        yWord = yWord + word_height #start on new row
                        y = y + word_height #change line
                        # change all my values of my list of width
                        width = widths[i] #save the change value of x
                        for j in range(i, len(widths)): #change all values
                            widths[j] = widths[j] - width
                    for c in word:
                        displayletterbyletter(c, i, widths, x, y)
                        i = i + 1
                    xWord = xWord + word_width + space
                    i = i + 1 #the space
                    for event in pygame.event.get(): #Checking all of the events that the user is doing at the moment
                        if event.type == pygame.QUIT: #Cross to close the window
                            running = False
                else: 
                    break
            if i != len(widths): #if there is another line to be printed
                yWord = yWord + word_height #start on new row
                y = y + word_height
                xWord = x #reset the x, go to the left
                width = widths[i] #save the change x value
                for j in range(i, len(widths)): #change all values
                    widths[j] = widths[j] - width
        else:
            break
    return running

def displayall(s, window, posWindow, x, y, color):
    words = [word.split(" ") for word in s.splitlines()] # 2D array where each row is a list of words
    space = font.size(" ")[0] # the width of a space
    max_width = window.get_width() + posWindow
    xWord, yWord = x, y #where my word will print
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width = pygame.Surface.get_width(word_surface)
            word_height = pygame.Surface.get_height(word_surface)
            if xWord + word_width >= max_width:
                xWord = x #reset the x
                yWord = yWord + word_height #start on new row
            screen.blit(word_surface, (xWord, yWord))
            xWord = xWord + word_width + space
        # begin new line
        xWord = x # reset the x
        yWord = yWord + word_height # start on new row

# Variables for the Game 
running = True
showtext = False
numbertext = 0 # which text I need to print
architecture = "1"
currentbackground = listbackground1
currentwidths = listWidths1
currentchoices = listchoices1
currentsentences = listSentences1

# Game Loop
while running == True:
    screen.fill((0,0,0)) #Colour
    for event in pygame.event.get(): #Checking all of the events that the user is doing at the moment
        if event.type == pygame.QUIT: #Cross to close the window
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Hello\n I'm here!")
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [sp for sp in sprites if sp.collidepoint(pos)]
            # if I'm clicking on the Back button
            if sprites[0] in clicked_sprites:
                if numbertext != 0:
                    numbertext = numbertext - 1
                    showtext = False
            # if I'm clicking on the Next button
            elif sprites[1] in clicked_sprites:
                if numbertext != len(currentsentences) - 1:
                    numbertext = numbertext + 1
                    showtext = False
            # if I'm clicking on the first choice
            elif sprites[2] in clicked_sprites:
                if numbertext == len(currentsentences) - 1:
                    if architecture == "1":
                        architecture = "2a"
                        numbertext = 0
                        currentchoices = listchoices2a
                        currentbackground = listbackground2a
                        currentwidths = listWidths2a
                        currentsentences = listSentences2a
                        showtext = False
                    elif architecture == "2a":
                        architecture = "3a"
                        numbertext = 0
                        currentchoices = listchoices3a
                        currentbackground = listbackground3a
                        currentwidths = listWidths3a
                        currentsentences = listSentences3a
                        showtext = False
                    elif architecture == "2b":
                        architecture = "3b"
                        numbertext = 0
                        currentchoices = listchoices3b
                        currentbackground = listbackground3a
                        currentwidths = listWidths3b
                        currentsentences = listSentences3b
                        showtext = False
                    elif architecture == "3a" or architecture == "3b":
                        running = False
            # if I'm clicking on the second choice
            elif sprites[3] in clicked_sprites:
                if numbertext == len(currentsentences) - 1:
                    if architecture == "1":
                        architecture = "2b"
                        numbertext = 0
                        currentchoices = listchoices2b
                        currentbackground = listbackground2a
                        currentwidths = listWidths2b
                        currentsentences = listSentences2b
                        showtext = False
                    
    
    screen.blit(currentbackground[numbertext], (0, 0))
    screen.blit(character, (570,200))
    screen.blit(blacksqaure, (0, 450))

    if showtext == False:
        running = displayText(currentsentences[numbertext], blacksqaure, blacksqaurex, currentwidths[numbertext], blacksqaurex + 10, blacksqaurey + 10, running)
        showtext = True
    else:
        displayall(currentsentences[numbertext], blacksqaure, blacksqaurex, blacksqaurex + 10, blacksqaurey + 10, (255, 255, 255))
        if numbertext != 0:
            screen.blit(buttons[0], (buttonsx[0], buttonsy[0]))
            displayall("Back", buttons[0], buttonsx[0], buttonsx[0] + 10, buttonsy[0] + 10, (0, 0, 0))
        
        if numbertext != len(currentsentences) - 1:
            screen.blit(buttons[1], (buttonsx[1], buttonsy[1]))
            displayall("Next", buttons[1], buttonsx[1], buttonsx[1] + 10, buttonsy[1] + 10, (0, 0, 0))
        
        if numbertext == len(currentsentences) - 1:
            for button in range(len(currentchoices)):
                screen.blit(buttons[button + 2], (buttonsx[button + 2], buttonsy[button + 2]))
                displayall(currentchoices[button], buttons[button + 2], buttonsx[button + 2], buttonsx[button + 2] + 10, buttonsy[button + 2] + 10, (0, 0, 0))

    pygame.display.update() 