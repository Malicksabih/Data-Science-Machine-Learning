import random
import pygame
from sys import exit

# initialising
pygame.init()
clock=pygame.time.Clock()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

# Classes
class Hardmode():
    def __init__(self,firstcheck,firsttube,secondcheck,secondtube,thirdcheck,thirdtube,fourthcheck,fourthtube,fifthcheck,fifthtube,sixthcheck,sixthtube,unique1,unique2,unique5,unique6,unique4,unique3):
        self.firstcheck=firstcheck
        self.firsttube=firsttube
        self.secondcheck=secondcheck
        self.secondtube=secondtube
        self.thirdcheck=thirdcheck
        self.thirdtube=thirdtube
        self.fourthcheck=fourthcheck
        self.fourthtube=fourthtube
        self.fifthcheck=fifthcheck
        self.fifthtube=fifthtube
        self.sixthcheck=sixthcheck
        self.sixthtube=sixthtube
        self.unique1=unique1
        self.unique2=unique2
        self.unique5=unique5
        self.unique6=unique6
        self.unique3=unique3
        self.unique4=unique4
    def twounique_twonotunique(self,first,firstcontainer,second,secondcontainer,uniquefirst,uniquesecond):
        if len(first)==4 and len(second)==4:
            randomnumber = random.randint(0, 1)
            if randomnumber==0:
                randomnumber1 = random.randint(0, 1)
                if randomnumber1 == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    self.fifthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                if randomnumber1 == 1:
                    self.sixthcheck.append(first[len(first) - 1])
                    self.sixthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            if randomnumber==1:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    self.fifthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                if randomnumber == 1:
                    self.sixthcheck.append(second[len(second) - 1])
                    self.sixthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
        elif uniquefirst==1 and uniquesecond!=1 and uniquesecond!=0:
            if len(self.sixthcheck) == 0 and len(self.fifthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor!=0:
                    countofcolor = 0
                    for i in first:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        first.append(second[len(second) - 1])
                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                        firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    else:
                        self.sixthcheck.append(second[len(second) - 1])
                        self.sixthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.sixthcheck.append(second[len(second) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor!=0:
                    countofcolor = 0
                    for i in first:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        first.append(second[len(second) - 1])
                        previous = eval(firstcontainer[len(self.fifthtube) - 1])
                        firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    else:
                        self.fifthcheck.append(second[len(second) - 1])
                        self.fifthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                        self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    self.fifthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(second[len(second) - 1])
                    self.sixthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor!=0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(second[len(second) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    elif countofcolor!=0:
                        countofcolor = 0
                        for i in first:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            first.append(second[len(second) - 1])
                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                            firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif second[len(second)-1]==first[len(first)-1] and first[len(first) - 2] == second[len(second) - 1] :
                            first.append(second[len(second) - 1])
                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                            firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        else:
                            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                                countofcolor = 0
                                for i in self.sixthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    self.sixthcheck.append(first[len(first) - 1])
                                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                else:
                                    self.fifthcheck.append(first[len(first) - 1])
                                    self.fifthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    self.fifthcheck.append(first[len(first) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                else:
                                    self.sixthcheck.append(first[len(first) - 1])
                                    self.sixthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    self.fifthcheck.append(first[len(first) - 1])
                                    self.fifthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                if randomnumber == 1:
                                    self.sixthcheck.append(first[len(first) - 1])
                                    self.sixthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    self.fifthcheck.append(first[len(first) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in self.sixthcheck:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        self.sixthcheck.append(first[len(first) - 1])
                                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                        self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        if first[len(first) - 1] == second[len(second) - 1]:
                                            second.append(first[len(first) - 1])
                                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                                            secondcontainer.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(first) == 1:
                                                first.pop()
                                                firstcontainer.pop()
                                                firstcontainer.pop()
                                            else:
                                                first.pop()
                                                firstcontainer.pop()
        elif uniquesecond==1 and uniquefirst!=1 and uniquefirst!=0:
            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.sixthcheck.append(first[len(first) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                else:
                    self.fifthcheck.append(first[len(first) - 1])
                    self.fifthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                else:
                    self.sixthcheck.append(first[len(first) - 1])
                    self.sixthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    self.fifthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                if randomnumber == 1:
                    self.sixthcheck.append(first[len(first) - 1])
                    self.sixthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(first[len(first) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in second:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            second.append(first[len(first) - 1])
                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                            secondcontainer.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif first[len(first)-1]==second[len(second)-1] and second[len(second) - 2] == first[len(first) - 1] :
                            second.append(first[len(first) - 1])
                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                            secondcontainer.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        else:
                            if len(self.sixthcheck) == 0 and len(self.fifthcheck) != 0:
                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    self.fifthcheck.append(second[len(second) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                elif countofcolor!=0:
                                    countofcolor = 0
                                    for i in first:
                                        if i != second[len(second) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        first.append(second[len(second) - 1])
                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    else:
                                        self.sixthcheck.append(second[len(second) - 1])
                                        self.sixthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                                        self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                                countofcolor = 0
                                for i in self.sixthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    self.sixthcheck.append(second[len(second) - 1])
                                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                    self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                elif countofcolor!=0:
                                    countofcolor = 0
                                    for i in first:
                                        if i != second[len(second) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        first.append(second[len(second) - 1])
                                        previous = eval(firstcontainer[len(self.fifthtube) - 1])
                                        firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    else:
                                        self.fifthcheck.append(second[len(second) - 1])
                                        self.fifthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                                        self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    self.fifthcheck.append(second[len(second) - 1])
                                    self.fifthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.sixthcheck.append(second[len(second) - 1])
                                    self.sixthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    self.fifthcheck.append(second[len(second) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                elif countofcolor!=0:
                                    countofcolor = 0
                                    for i in self.sixthcheck:
                                        if i != second[len(second) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        self.sixthcheck.append(second[len(second) - 1])
                                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                        self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    else:
                                        if first[len(first) - 1] == second[len(second) - 1]:
                                            first.append(second[len(second) - 1])
                                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                                            firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(second) == 1:
                                                second.pop()
                                                secondcontainer.pop()
                                                secondcontainer.pop()
                                            else:
                                                second.pop()
                                                secondcontainer.pop()
        elif uniquesecond==0 and uniquefirst==1 and len(first)!=4:
            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.sixthcheck.append(first[len(first) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(first[len(first) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
        elif uniquefirst==0 and uniquesecond==1 and len(second)!=4:
            if len(self.sixthcheck) == 0 and len(self.fifthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.sixthcheck.append(second[len(second) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor!=0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(second[len(second) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
        elif uniquefirst == 1 and uniquesecond == 1 and len(first)==len(second):
            randomgen = random.randint(0, 1)
            if randomgen==0:
                if len(self.sixthcheck) == 0 and len(self.fifthcheck) != 0:
                    countofcolor = 0
                    for i in self.fifthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.fifthcheck.append(first[len(first) - 1])
                        previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                        self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in second:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            second.append(first[len(first) - 1])
                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                            secondcontainer.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        else:
                            self.sixthcheck.append(first[len(first) - 1])
                            self.sixthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                            self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()

                elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(first[len(first) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in second:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            second.append(first[len(first) - 1])
                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                            secondcontainer.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        else:
                            self.fifthcheck.append(first[len(first) - 1])
                            self.fifthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                            self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                    countofcolor = 0
                    for i in self.fifthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.fifthcheck.append(first[len(first) - 1])
                        previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                        self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            self.sixthcheck.append(first[len(first) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            if len(second) != 0:
                                countofcolor = 0
                                for i in second:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4 = 1
                                    second.append(first[len(first) - 1])
                                    previous = eval(secondcontainer[len(secondcontainer) - 1])
                                    secondcontainer.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
            elif randomgen==1:
                if len(self.sixthcheck) == 0 and len(self.fifthcheck) != 0:
                    countofcolor = 0
                    for i in self.fifthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fifthcheck.append(second[len(second) - 1])
                        previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                        self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    elif countofcolor != 0:
                        if len(first) != 0:
                            countofcolor = 0
                            for i in first:
                                if i != second[len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                first.append(second[len(second) - 1])
                                previous = eval(firstcontainer[len(firstcontainer) - 1])
                                firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            else:
                                self.sixthcheck.append(second[len(second) - 1])
                                self.sixthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                                self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(second[len(second) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    elif countofcolor != 0:
                        if len(first) != 0:
                            countofcolor = 0
                            for i in first:
                                if i != second[len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                first.append(second[len(second) - 1])
                                previous = eval(firstcontainer[len(firstcontainer) - 1])
                                firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            else:
                                append3 = 1
                                self.fifthcheck.append(second[len(second) - 1])
                                self.fifthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                                self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                    countofcolor = 0
                    for i in self.fifthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.fifthcheck.append(second[len(second) - 1])
                        previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                        self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            self.sixthcheck.append(second[len(second) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif countofcolor != 0:
                            if len(second) != 0:
                                countofcolor = 0
                                for i in first:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    first.append(second[len(second) - 1])
                                    previous = eval(firstcontainer[len(firstcontainer) - 1])
                                    firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
        elif len(first)<len(second) and len(first)!=0:
            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in second:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        second.append(first[len(first) - 1])
                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                        secondcontainer.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    else:
                        self.sixthcheck.append(first[len(first) - 1])
                        self.sixthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.sixthcheck.append(first[len(first) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in second:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        second.append(first[len(first) - 1])
                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                        secondcontainer.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    else:
                        self.fifthcheck.append(first[len(first) - 1])
                        self.fifthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                        self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    self.fifthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(first[len(first) - 1])
                    self.sixthtube.append(f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(first[len(first) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
        elif len(second)<len(first) and len(second)!=0:
            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in first:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        first.append(second[len(second) - 1])
                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                        firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    else:
                        self.sixthcheck.append(second[len(second) - 1])
                        self.sixthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.sixthcheck.append(second[len(second) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in first:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        first.append(second[len(second) - 1])
                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                        firstcontainer.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    else:
                        self.fifthcheck.append(second[len(second) - 1])
                        self.fifthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                        self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    self.fifthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(second[len(second) - 1])
                    self.sixthtube.append(f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(second[len(second) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
    def calculating(self):
        self.unique4 = 0
        self.unique3 = 0
        self.unique2 = 0
        self.unique1 = 0
        if len(self.secondcheck) != 0:
            self.unique1 = 1
            unique1array = []
            check1 = self.secondcheck[len(self.secondcheck) - 1]
            for i in self.secondcheck:
                if check1 != i and i not in unique1array:
                    self.unique1 += 1
                    unique1array.append(i)
        if len(self.firstcheck) != 0:
            self.unique2 = 1
            unique2array = []
            check2 = self.firstcheck[len(self.firstcheck) - 1]
            for i in self.firstcheck:
                if check2 != i and i not in unique2array:
                    self.unique2 += 1
                    unique2array.append(i)
        if len(self.fifthcheck) != 0:
            self.unique5 = 1
            unique5array = []
            check5 = self.fifthcheck[len(self.fifthcheck) - 1]
            for i in self.fifthcheck:
                if check5 != i and i not in unique5array:
                    self.unique5 += 1
                    unique5array.append(i)
        if len(self.sixthcheck) != 0:
            self.unique6 = 1
            unique6array = []
            check6 = self.sixthcheck[len(self.sixthcheck) - 1]
            for i in self.sixthcheck:
                if check6 != i and i not in unique6array:
                    self.unique6 += 1
                    unique6array.append(i)
        if len(self.thirdcheck) != 0:
            self.unique3 = 1
            unique3array = []
            check3 = self.thirdcheck[len(self.thirdcheck) - 1]
            for i in self.thirdcheck:
                if check3 != i and i not in unique3array:
                    self.unique3 += 1
                    unique3array.append(i)
        if len(self.fourthcheck) != 0:
            self.unique4 = 1
            unique4array = []
            check4 = self.fourthcheck[len(self.fourthcheck) - 1]
            for i in self.fourthcheck:
                if check4 != i and i not in unique4array:
                    self.unique4 += 1
                    unique4array.append(i)
    def three_not_unique(self,first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,secondunique,thirdunique,firstpos1,firstpos2,secondpos1,secondpos2,thirdpos1,thirdpos2):
        if len(first)==4 and len(second)==4 and len(third)==4:
            randomnumber = random.randint(0, 2)
            if randomnumber == 0:
                randomnumber1 = random.randint(0, 1)
                if randomnumber1 == 0:
                    append3 = 1
                    self.fifthcheck.append(first[len(first) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                if randomnumber1 == 1:
                    append4 = 1
                    self.sixthcheck.append(first[len(first) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            if randomnumber == 1:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.fifthcheck.append(second[len(second) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(second[len(second) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            if randomnumber == 2:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.fifthcheck.append(third[len(third) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(third[len(third) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
        elif len(third)==0 or len(first)==0 or len(second)==0:
            if len(third)==0:
                if (len(first)<len(second) and firstunique!=1 and secondunique==1) or (len(first)<len(second) and firstunique==1 and secondunique==1) or (len(first) < len(second) and firstunique!=1 and secondunique!=1) or (len(second) < len(first) and secondunique==1 and firstunique!=1):
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()

                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(first[len(first) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                append3 = 1
                                self.sixthcheck.append(first[len(first) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(first[len(first) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(first[len(first) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                append4 = 1
                                self.fifthcheck.append(first[len(first) - 1])
                                self.fifthtube.append(
                                    f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                self.fifthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(first[len(first) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(unique1, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(unique1, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(first[len(first) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(unique1, unique2, unique5, unique6)
                                for i in second:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    second.append(first[len(first) - 1])
                                    previous = eval(secondcontainer[len(secondcontainer) - 1])
                                    secondcontainer.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(unique1, unique2, unique5, unique6)
                                    for i in third:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        print('fsr inside')
                                        append4 = 1
                                        third.append(first[len(first) - 1])
                                        thirdcontainer.append(
                                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",({thirdpos1}, 438),21)')
                                        thirdcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({thirdpos2}, 415, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        if (len(first) < len(second) and len(
                                                second) != 4):
                                            if second[len(second) - 1] == first[
                                                len(first) - 1]:
                                                second.append(
                                                    first[len(first) - 1])
                                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                                secondcontainer.append(
                                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(first) == 1:
                                                    first.pop()
                                                    firstcontainer.pop()
                                                    firstcontainer.pop()
                                                else:
                                                    first.pop()
                                                    firstcontainer.pop()
                                        elif (len(first) < len(third) and len(
                                                third) != 4):
                                            if third[len(third) - 1] == first[
                                                len(first) - 1]:
                                                third.append(
                                                    first[len(first) - 1])
                                                previous = eval(easytube2[len(easytube2) - 1])
                                                easytube2.append(
                                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(first) == 1:
                                                    first.pop()
                                                    firstcontainer.pop()
                                                    firstcontainer.pop()
                                                else:
                                                    first.pop()
                                                    firstcontainer.pop()

                elif (len(second)<len(first) and secondunique!=1 and firstunique==1) or (len(second)<len(first) and firstunique==1 and secondunique==1) or (len(second) < len(first) and firstunique!=1 and secondunique!=1) or (len(first) < len(second) and firstunique==1 and secondunique!=1):
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        else:
                            append3 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()

                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        else:
                            append4 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(unique1, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(unique1, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != second[len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(second[len(second) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(unique1, unique2, unique5, unique6)
                                for i in first:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    first.append(second[len(second) - 1])
                                    previous = eval(firstcontainer[len(firstcontainer) - 1])
                                    firstcontainer.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(unique1, unique2, unique5, unique6)
                                    for i in third:
                                        if i != second[len(second) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        third.append(second[len(second) - 1])
                                        thirdcontainer.append(
                                            f'pygame.draw.circle(screen,"{second[len(second) - 1]}",({thirdpos1}, 438),21)')
                                        thirdcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({thirdpos2}, 415, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    else:
                                        if (len(second) < len(first) and len(
                                                first) != 4):
                                            if second[len(second) - 1] == first[
                                                len(first) - 1]:
                                                first.append(
                                                    second[len(second) - 1])
                                                previous = eval(firstcontainer[len(firstcontainer) - 1])
                                                firstcontainer.append(
                                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(second) == 1:
                                                    second.pop()
                                                    secondcontainer.pop()
                                                    secondcontainer.pop()
                                                else:
                                                    second.pop()
                                                    secondcontainer.pop()
                                        elif (len(second) < len(third) and len(
                                                third) != 4):
                                            if third[len(third) - 1] == second[
                                                len(second) - 1]:
                                                third.append(
                                                    second[len(second) - 1])
                                                previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                                thirdcontainer.append(
                                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(second) == 1:
                                                    second.pop()
                                                    secondcontainer.pop()
                                                    secondcontainer.pop()
                                                else:
                                                    second.pop()
                                                    secondcontainer.pop()


                elif len(second)==len(first):
                    randomnumber = random.randint(0, 1)
                    if randomnumber == 0:
                        if (secondunique!=1) or (secondunique==1 and firstunique==1):
                            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4 = 1
                                    self.fifthcheck.append(second[len(second) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                else:
                                    append3 = 1
                                    self.sixthcheck.append(second[len(second) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()

                            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                                countofcolor = 0
                                for i in self.sixthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.sixthcheck.append(second[len(second) - 1])
                                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                else:
                                    append4 = 1
                                    self.fifthcheck.append(second[len(second) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.fifthcheck.append(second[len(second) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.sixthcheck.append(second[len(second) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                                # movingtube2 = 1
                                countofcolor = 0
                                # print('last step')
                                # print(easytubecheck1)
                                # print(unique1, unique2, unique5, unique6)
                                for i in self.fifthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.fifthcheck.append(second[len(second) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                elif countofcolor != 0:
                                    # print('append3' ,append3)
                                    # print('countofcolor',countofcolor)
                                    # print('inside else')
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(unique1, unique2, unique5, unique6)
                                    for i in self.sixthcheck:
                                        if i != second[len(second) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        self.sixthcheck.append(second[len(second) - 1])
                                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()

                                    elif countofcolor != 0:
                                        countofcolor = 0
                                        # print(easytubecheck1)
                                        # print(unique1, unique2, unique5, unique6)
                                        for i in first:
                                            if i != second[len(second) - 1]:
                                                countofcolor += 1
                                        if countofcolor == 0:
                                            print('fsr inside')
                                            append4 = 1
                                            first.append(
                                                second[len(second) - 1])
                                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                                            firstcontainer.append(
                                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(second) == 1:
                                                second.pop()
                                                secondcontainer.pop()
                                                secondcontainer.pop()
                                            else:
                                                second.pop()
                                                secondcontainer.pop()
                                        elif countofcolor != 0:
                                            countofcolor = 0
                                            # print(easytubecheck1)
                                            # print(unique1, unique2, unique5, unique6)
                                            for i in third:
                                                if i != second[len(second) - 1]:
                                                    countofcolor += 1
                                            if countofcolor == 0:
                                                # print('fsr inside')
                                                append4 = 1
                                                third.append(
                                                    second[len(second) - 1])
                                                thirdcontainer.append(
                                                    f'pygame.draw.circle(screen,"{second[len(second) - 1]}",({thirdpos1}, 438),21)')
                                                thirdcontainer.append(
                                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({thirdpos2}, 415, 45, 23))')
                                                if len(second) == 1:
                                                    second.pop()
                                                    secondcontainer.pop()
                                                    secondcontainer.pop()
                                                else:
                                                    second.pop()
                                                    secondcontainer.pop()
                                            else:
                                                if (len(second) < len(first) and len(
                                                        first) != 4):
                                                    if second[len(second) - 1] == \
                                                            first[
                                                                len(first) - 1]:
                                                        first.append(
                                                            second[len(second) - 1])
                                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                                        firstcontainer.append(
                                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(second) == 1:
                                                            second.pop()
                                                            secondcontainer.pop()
                                                            secondcontainer.pop()
                                                        else:
                                                            second.pop()
                                                            secondcontainer.pop()
                                                elif (len(second) < len(third) and len(
                                                        third) != 4):
                                                    if third[len(third) - 1] == \
                                                            second[
                                                                len(second) - 1]:
                                                        third.append(
                                                            second[len(second) - 1])
                                                        previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                                        thirdcontainer.append(
                                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(second) == 1:
                                                            second.pop()
                                                            secondcontainer.pop()
                                                            secondcontainer.pop()
                                                        else:
                                                            second.pop()
                                                            secondcontainer.pop()
                    elif randomnumber == 1:
                        if (firstunique!=1)  or (secondunique==1 and firstunique==1):
                            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4 = 1
                                    self.fifthcheck.append(first[len(first) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()

                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in second:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        second.append(first[len(first) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        append3 = 1
                                        self.sixthcheck.append(first[len(first) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                                countofcolor = 0
                                for i in self.sixthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.sixthcheck.append(first[len(first) - 1])
                                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in second:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        second.append(first[len(first) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        append4 = 1
                                        self.fifthcheck.append(first[len(first) - 1])
                                        self.fifthtube.append(
                                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                        self.fifthtube.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.fifthcheck.append(first[len(first) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.sixthcheck.append(first[len(first) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                                # movingtube2 = 1
                                countofcolor = 0
                                # print('last step')
                                # print(easytubecheck1)
                                # print(unique1, unique2, unique5, unique6)
                                for i in self.fifthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.fifthcheck.append(first[len(first) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                elif countofcolor != 0:
                                    # print('append3' ,append3)
                                    # print('countofcolor',countofcolor)
                                    # print('inside else')
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(unique1, unique2, unique5, unique6)
                                    for i in self.sixthcheck:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        self.sixthcheck.append(first[len(first) - 1])
                                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()

                                    elif countofcolor != 0:
                                        countofcolor = 0
                                        # print(easytubecheck1)
                                        # print(unique1, unique2, unique5, unique6)
                                        for i in second:
                                            if i != first[len(first) - 1]:
                                                countofcolor += 1
                                        if countofcolor == 0:
                                            # print('fsr inside')
                                            append4 = 1
                                            second.append(
                                                first[len(first) - 1])
                                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                                            secondcontainer.append(
                                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(first) == 1:
                                                first.pop()
                                                firstcontainer.pop()
                                                firstcontainer.pop()
                                            else:
                                                first.pop()
                                                firstcontainer.pop()
                                        elif countofcolor != 0:
                                            countofcolor = 0
                                            # print(easytubecheck1)
                                            # print(unique1, unique2, unique5, unique6)
                                            for i in third:
                                                if i != first[len(first) - 1]:
                                                    countofcolor += 1
                                            if countofcolor == 0:
                                                # print('fsr inside')
                                                append4 = 1
                                                third.append(
                                                    first[len(first) - 1])
                                                thirdcontainer.append(
                                                    f'pygame.draw.circle(screen,"{first[len(first) - 1]}",({thirdpos1}, 438),21)')
                                                thirdcontainer.append(
                                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({thirdpos2}, 415, 45, 23))')
                                                if len(first) == 1:
                                                    first.pop()
                                                    firstcontainer.pop()
                                                    firstcontainer.pop()
                                                else:
                                                    first.pop()
                                                    firstcontainer.pop()
                                            else:
                                                if (len(first) < len(second) and len(
                                                        second) != 4):
                                                    if second[len(second) - 1] == \
                                                            first[
                                                                len(first) - 1]:
                                                        second.append(
                                                            first[len(first) - 1])
                                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                                        secondcontainer.append(
                                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(first) == 1:
                                                            first.pop()
                                                            firstcontainer.pop()
                                                            firstcontainer.pop()
                                                        else:
                                                            first.pop()
                                                            firstcontainer.pop()
                                                elif (len(first) < len(third) and len(
                                                        third) != 4):
                                                    if third[len(third) - 1] == \
                                                            first[
                                                                len(first) - 1]:
                                                        third.append(
                                                            first[len(first) - 1])
                                                        previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                                        thirdcontainer.append(
                                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(first) == 1:
                                                            first.pop()
                                                            firstcontainer.pop()
                                                            firstcontainer.pop()
                                                        else:
                                                            first.pop()
                                                            firstcontainer.pop()
            elif len(first)==0:
                if (len(third) < len(second) and thirdunique!=1 and secondunique==1) or (len(third)<len(second) and thirdunique==1 and secondunique==1) or (len(third) < len(second) and thirdunique!=1 and secondunique!=1) or (len(second) < len(third) and secondunique==1 and thirdunique!=1):
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()

                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(third[len(third) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                append3 = 1
                                self.sixthcheck.append(third[len(third) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(third[len(third) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                append4 = 1
                                self.fifthcheck.append(third[len(third) - 1])
                                self.fifthtube.append(
                                    f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                                self.fifthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(third[len(third) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()

                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in second:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    second.append(third[len(third) - 1])
                                    previous = eval(secondcontainer[len(secondcontainer) - 1])
                                    secondcontainer.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in first:
                                        if i != third[len(third) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        first.append(third[len(third) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.circle(screen,"{third[len(third) - 1]}",({firstpos1}, 438),21)')
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({firstpos2}, 415, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    else:
                                        if (len(third) < len(second) and len(
                                                second) != 4):
                                            if second[len(second) - 1] == third[
                                                len(third) - 1]:
                                                second.append(
                                                    third[len(third) - 1])
                                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                                secondcontainer.append(
                                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(third) == 1:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                                    thirdcontainer.pop()
                                                else:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                        elif (len(third) < len(first) and len(
                                                first) != 4):
                                            if third[len(third) - 1] == first[
                                                len(first) - 1]:
                                                first.append(
                                                    third[len(third) - 1])
                                                previous = eval(firstcontainer[len(firstcontainer) - 1])
                                                firstcontainer.append(
                                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(third) == 1:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                                    thirdcontainer.pop()
                                                else:
                                                    third.pop()
                                                    thirdcontainer.pop()
                elif len(second) == len(third):
                    randomnumber = random.randint(0, 1)
                    if randomnumber == 0:
                        if (thirdunique!=1) or (thirdunique==1 and secondunique==1):
                            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4 = 1
                                    self.fifthcheck.append(third[len(third) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()

                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in second:
                                        if i != third[len(third) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        second.append(third[len(third) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    else:
                                        append3 = 1
                                        self.sixthcheck.append(third[len(third) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                                countofcolor = 0
                                for i in self.sixthcheck:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.sixthcheck.append(third[len(third) - 1])
                                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in second:
                                        if i != third[len(third) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        second.append(third[len(third) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    else:
                                        append4 = 1
                                        self.fifthcheck.append(third[len(third) - 1])
                                        self.fifthtube.append(
                                            f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                                        self.fifthtube.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.fifthcheck.append(third[len(third) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.sixthcheck.append(third[len(third) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                                # movingtube2 = 1
                                countofcolor = 0
                                # print('last step')
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in self.fifthcheck:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.fifthcheck.append(third[len(third) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                elif countofcolor != 0:
                                    # print('append3' ,append3)
                                    # print('countofcolor',countofcolor)
                                    # print('inside else')
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in self.sixthcheck:
                                        if i != third[len(third) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        self.sixthcheck.append(third[len(third) - 1])
                                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()

                                    elif countofcolor != 0:
                                        countofcolor = 0
                                        # print(easytubecheck1)
                                        # print(thirdunique, unique2, unique5, unique6)
                                        for i in second:
                                            if i != third[len(third) - 1]:
                                                countofcolor += 1
                                        if countofcolor == 0:
                                            # print('fsr inside')
                                            append4 = 1
                                            second.append(
                                                third[len(third) - 1])
                                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                                            secondcontainer.append(
                                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(third) == 1:
                                                third.pop()
                                                thirdcontainer.pop()
                                                thirdcontainer.pop()
                                            else:
                                                third.pop()
                                                thirdcontainer.pop()
                                        elif countofcolor != 0:
                                            countofcolor = 0
                                            # print(easytubecheck1)
                                            # print(thirdunique, unique2, unique5, unique6)
                                            for i in first:
                                                if i != third[len(third) - 1]:
                                                    countofcolor += 1
                                            if countofcolor == 0:
                                                # print('fsr inside')
                                                append4 = 1
                                                first.append(
                                                    third[len(third) - 1])
                                                firstcontainer.append(
                                                    f'pygame.draw.circle(screen,"{third[len(third) - 1]}",({firstpos1}, 438),21)')
                                                firstcontainer.append(
                                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({firstpos2}, 415, 45, 23))')
                                                if len(third) == 1:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                                    thirdcontainer.pop()
                                                else:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                            else:
                                                if (len(third) < len(second) and len(
                                                        second) != 4):
                                                    if second[len(second) - 1] == \
                                                            third[
                                                                len(third) - 1]:
                                                        second.append(
                                                            third[len(third) - 1])
                                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                                        secondcontainer.append(
                                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(third) == 1:
                                                            third.pop()
                                                            thirdcontainer.pop()
                                                            thirdcontainer.pop()
                                                        else:
                                                            third.pop()
                                                            thirdcontainer.pop()
                                                elif (len(third) < len(first) and len(
                                                        first) != 4):
                                                    if third[len(third) - 1] == \
                                                            first[
                                                                len(first) - 1]:
                                                        first.append(
                                                            third[len(third) - 1])
                                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                                        firstcontainer.append(
                                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(third) == 1:
                                                            third.pop()
                                                            thirdcontainer.pop()
                                                            thirdcontainer.pop()
                                                        else:
                                                            third.pop()
                                                            thirdcontainer.pop()
                    elif randomnumber == 1:
                        if (secondunique!=1) or (thirdunique==1 and secondunique==1):
                            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4 = 1
                                    self.fifthcheck.append(second[len(second) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                else:
                                    append3 = 1
                                    self.sixthcheck.append(second[len(second) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()

                            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                                countofcolor = 0
                                for i in self.sixthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.sixthcheck.append(second[len(second) - 1])
                                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                else:
                                    append4 = 1
                                    self.fifthcheck.append(second[len(second) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.fifthcheck.append(second[len(second) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.sixthcheck.append(second[len(second) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                                # movingtube2 = 1
                                countofcolor = 0
                                # print('last step')
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in self.fifthcheck:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.fifthcheck.append(second[len(second) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                elif countofcolor != 0:
                                    # print('append3' ,append3)
                                    # print('countofcolor',countofcolor)
                                    # print('inside else')
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in self.sixthcheck:
                                        if i != second[len(second) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        self.sixthcheck.append(second[len(second) - 1])
                                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    elif countofcolor != 0:
                                        countofcolor = 0
                                        # print(easytubecheck1)
                                        # print(thirdunique, unique2, unique5, unique6)
                                        for i in third:
                                            if i != second[len(second) - 1]:
                                                countofcolor += 1
                                        if countofcolor == 0:
                                            # print('fsr inside')
                                            append4 = 1
                                            third.append(second[len(second) - 1])
                                            previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                            thirdcontainer.append(
                                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(second) == 1:
                                                second.pop()
                                                secondcontainer.pop()
                                                secondcontainer.pop()
                                            else:
                                                second.pop()
                                                secondcontainer.pop()
                                        elif countofcolor != 0:
                                            countofcolor = 0
                                            # print(easytubecheck1)
                                            # print(thirdunique, unique2, unique5, unique6)
                                            for i in first:
                                                if i != second[len(second) - 1]:
                                                    countofcolor += 1
                                            if countofcolor == 0:
                                                # print('fsr inside')
                                                append4 = 1
                                                first.append(
                                                    second[len(second) - 1])
                                                firstcontainer.append(
                                                    f'pygame.draw.circle(screen,"{second[len(second) - 1]}",({firstpos1}, 438),21)')
                                                firstcontainer.append(
                                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({firstpos2}, 415, 45, 23))')
                                                if len(second) == 1:
                                                    second.pop()
                                                    secondcontainer.pop()
                                                    secondcontainer.pop()
                                                else:
                                                    second.pop()
                                                    secondcontainer.pop()
                                            else:
                                                if (len(second) < len(third) and len(
                                                        third) != 4):
                                                    if second[len(second) - 1] == \
                                                            third[
                                                                len(third) - 1]:
                                                        third.append(
                                                            second[len(second) - 1])
                                                        previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                                        thirdcontainer.append(
                                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(second) == 1:
                                                            second.pop()
                                                            secondcontainer.pop()
                                                            secondcontainer.pop()
                                                        else:
                                                            second.pop()
                                                            secondcontainer.pop()
                                                elif (len(second) < len(first) and len(
                                                        first) != 4):
                                                    if second[len(second) - 1] == \
                                                            first[
                                                                len(first) - 1]:
                                                        first.append(
                                                            second[len(second) - 1])
                                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                                        firstcontainer.append(
                                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(second) == 1:
                                                            second.pop()
                                                            secondcontainer.pop()
                                                            secondcontainer.pop()
                                                        else:
                                                            second.pop()
                                                            secondcontainer.pop()
                elif (len(second) < len(third) and secondunique!=1 and thirdunique==1) or (len(second)<len(third) and thirdunique==1 and secondunique==1) or (len(second) < len(third) and thirdunique!=1 and secondunique!=1) or (len(third) < len(second) and thirdunique==1 and secondunique!=1):
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        else:
                            append3 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()

                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        else:
                            append4 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != second[len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(second[len(second) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in third:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    third.append(second[len(second) - 1])
                                    previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                    thirdcontainer.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in first:
                                        if i != second[len(second) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        first.append(second[len(second) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.circle(screen,"{second[len(second) - 1]}",({firstpos1}, 438),21)')
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({firstpos2}, 415, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    else:
                                        if (len(second) < len(third) and len(
                                                third) != 4):
                                            if second[len(second) - 1] == \
                                                    third[
                                                        len(third) - 1]:
                                                third.append(
                                                    second[len(second) - 1])
                                                previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                                thirdcontainer.append(
                                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(second) == 1:
                                                    second.pop()
                                                    secondcontainer.pop()
                                                    secondcontainer.pop()
                                                else:
                                                    second.pop()
                                                    secondcontainer.pop()
                                        elif (len(second) < len(first) and len(
                                                first) != 4):
                                            if second[len(second) - 1] == \
                                                    first[
                                                        len(first) - 1]:
                                                first.append(
                                                    second[len(second) - 1])
                                                previous = eval(firstcontainer[len(firstcontainer) - 1])
                                                firstcontainer.append(
                                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(second) == 1:
                                                    second.pop()
                                                    secondcontainer.pop()
                                                    secondcontainer.pop()
                                                else:
                                                    second.pop()
                                                    secondcontainer.pop()
            elif len(second)==0:
                if (len(first)<len(third) and firstunique!=1 and thirdunique==1) or (len(first)<len(third) and thirdunique==1 and firstunique==1) or (len(first) < len(third) and thirdunique!=1 and firstunique!=1) or (len(third) < len(first) and thirdunique==1 and firstunique!=1):
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()

                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(first[len(first) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                append3 = 1
                                self.sixthcheck.append(first[len(first) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(first[len(first) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(first[len(first) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                append4 = 1
                                self.fifthcheck.append(first[len(first) - 1])
                                self.fifthtube.append(
                                    f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                self.fifthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(first[len(first) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(first[len(first) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in third:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    third.append(first[len(first) - 1])
                                    previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                    thirdcontainer.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in second:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        second.append(first[len(first) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",({secondpos1}, 438),21)')
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({secondpos2}, 415, 45, 23))')
                                        # previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        # secondcontainer.append(
                                        #     f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        if (len(first) < len(third) and len(
                                                third) != 4):
                                            if first[len(first) - 1] == \
                                                    third[
                                                        len(third) - 1] and firstunique!=1:
                                                third.append(
                                                    first[len(first) - 1])
                                                previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                                thirdcontainer.append(
                                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(first) == 1:
                                                    first.pop()
                                                    firstcontainer.pop()
                                                    firstcontainer.pop()
                                                else:
                                                    first.pop()
                                                    firstcontainer.pop()
                                        elif (len(first) < len(second) and len(
                                                second) != 4):
                                            if second[len(second) - 1] == \
                                                    first[
                                                        len(first) - 1] and firstunique!=1:
                                                second.append(
                                                    first[len(first) - 1])
                                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                                secondcontainer.append(
                                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(first) == 1:
                                                    first.pop()
                                                    firstcontainer.pop()
                                                    firstcontainer.pop()
                                                else:
                                                    first.pop()
                                                    firstcontainer.pop()
                elif len(third)==len(first):
                    randomnumber = random.randint(0, 1)
                    if randomnumber == 0:
                        if (thirdunique!=1) or (thirdunique==1 and firstunique==1):
                            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4 = 1
                                    self.fifthcheck.append(third[len(third) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()

                                else:
                                    append3 = 1
                                    self.sixthcheck.append(third[len(third) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                                countofcolor = 0
                                for i in self.sixthcheck:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.sixthcheck.append(third[len(third) - 1])
                                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                else:
                                    append4 = 1
                                    self.fifthcheck.append(third[len(third) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.fifthcheck.append(third[len(third) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.sixthcheck.append(third[len(third) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                                # movingtube2 = 1
                                countofcolor = 0
                                # print('last step')
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in self.fifthcheck:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.fifthcheck.append(third[len(third) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                elif countofcolor != 0:
                                    # print('append3' ,append3)
                                    # print('countofcolor',countofcolor)
                                    # print('inside else')
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in self.sixthcheck:
                                        if i != third[len(third) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        self.sixthcheck.append(third[len(third) - 1])
                                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    elif countofcolor != 0:
                                        countofcolor = 0
                                        # print(easytubecheck1)
                                        # print(thirdunique, unique2, unique5, unique6)
                                        for i in first:
                                            if i != third[len(third) - 1]:
                                                countofcolor += 1
                                        if countofcolor == 0:
                                            # print('fsr inside')
                                            append4 = 1
                                            first.append(third[len(third) - 1])
                                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                                            firstcontainer.append(
                                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(third) == 1:
                                                third.pop()
                                                thirdcontainer.pop()
                                                thirdcontainer.pop()
                                            else:
                                                third.pop()
                                                thirdcontainer.pop()
                                        elif countofcolor != 0:
                                            countofcolor = 0
                                            # print(easytubecheck1)
                                            # print(thirdunique, unique2, unique5, unique6)
                                            for i in second:
                                                if i != third[len(third) - 1]:
                                                    countofcolor += 1
                                            if countofcolor == 0:
                                                # print('fsr inside')
                                                append4 = 1
                                                second.append(
                                                    third[len(third) - 1])
                                                secondcontainer.append(
                                                    f'pygame.draw.circle(screen,"{third[len(third) - 1]}",({secondpos1}, 438),21)')
                                                secondcontainer.append(
                                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({secondpos2}, 415, 45, 23))')
                                                if len(third) == 1:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                                    thirdcontainer.pop()
                                                else:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                            else:
                                                if (len(third) < len(first) and len(
                                                        first) != 4):
                                                    if first[len(first) - 1] == \
                                                            third[
                                                                len(third) - 1] and thirdunique!=1:
                                                        first.append(
                                                            third[len(third) - 1])
                                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                                        firstcontainer.append(
                                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(third) == 1:
                                                            third.pop()
                                                            thirdcontainer.pop()
                                                            thirdcontainer.pop()
                                                        else:
                                                            third.pop()
                                                            thirdcontainer.pop()
                                                elif (len(third) < len(second) and len(
                                                        second) != 4):
                                                    if second[len(second) - 1] == \
                                                            third[
                                                                len(third) - 1] and thirdunique!=1:
                                                        second.append(
                                                            third[len(third) - 1])
                                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                                        secondcontainer.append(
                                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(third) == 1:
                                                            third.pop()
                                                            thirdcontainer.pop()
                                                            thirdcontainer.pop()
                                                        else:
                                                            third.pop()
                                                            thirdcontainer.pop()

                    elif randomnumber == 1:
                        if (firstunique!=1) or (thirdunique==1 and firstunique==1):
                            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                                countofcolor = 0
                                for i in self.fifthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4 = 1
                                    self.fifthcheck.append(first[len(first) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()

                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in second:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        second.append(first[len(first) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        append3 = 1
                                        self.sixthcheck.append(first[len(first) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                                countofcolor = 0
                                for i in self.sixthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.sixthcheck.append(first[len(first) - 1])
                                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in second:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        second.append(first[len(first) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        append4 = 1
                                        self.fifthcheck.append(first[len(first) - 1])
                                        self.fifthtube.append(
                                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                        self.fifthtube.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.fifthcheck.append(first[len(first) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.sixthcheck.append(first[len(first) - 1])
                                    self.sixthtube.append(
                                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                    self.sixthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                                # movingtube2 = 1
                                countofcolor = 0
                                # print('last step')
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in self.fifthcheck:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.fifthcheck.append(first[len(first) - 1])
                                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                                    self.fifthtube.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                elif countofcolor != 0:
                                    # print('append3' ,append3)
                                    # print('countofcolor',countofcolor)
                                    # print('inside else')
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in self.sixthcheck:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        self.sixthcheck.append(first[len(first) - 1])
                                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                        self.sixthtube.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    elif countofcolor != 0:
                                        countofcolor = 0
                                        # print(easytubecheck1)
                                        # print(thirdunique, unique2, unique5, unique6)
                                        for i in third:
                                            if i != first[len(first) - 1]:
                                                countofcolor += 1
                                        if countofcolor == 0:
                                            # print('fsr inside')
                                            append4 = 1
                                            third.append(first[len(first) - 1])
                                            previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                            thirdcontainer.append(
                                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(first) == 1:
                                                first.pop()
                                                firstcontainer.pop()
                                                firstcontainer.pop()
                                            else:
                                                first.pop()
                                                firstcontainer.pop()
                                        elif countofcolor != 0:
                                            countofcolor = 0
                                            # print(easytubecheck1)
                                            # print(thirdunique, unique2, unique5, unique6)
                                            for i in second:
                                                if i != first[len(first) - 1]:
                                                    countofcolor += 1
                                            if countofcolor == 0:
                                                # print('fsr inside')
                                                append4 = 1
                                                second.append(
                                                    first[len(first) - 1])
                                                secondcontainer.append(
                                                    f'pygame.draw.circle(screen,"{first[len(first) - 1]}",({secondpos1}, 438),21)')
                                                secondcontainer.append(
                                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({secondpos2}, 415, 45, 23))')
                                                if len(first) == 1:
                                                    first.pop()
                                                    firstcontainer.pop()
                                                    firstcontainer.pop()
                                                else:
                                                    first.pop()
                                                    firstcontainer.pop()
                                            else:
                                                if (len(first) < len(third) and len(
                                                        third) != 4):
                                                    if first[len(first) - 1] == \
                                                            third[
                                                                len(third) - 1] and firstunique!=1:
                                                        third.append(
                                                            first[len(first) - 1])
                                                        previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                                        thirdcontainer.append(
                                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(first) == 1:
                                                            first.pop()
                                                            firstcontainer.pop()
                                                            firstcontainer.pop()
                                                        else:
                                                            first.pop()
                                                            firstcontainer.pop()
                                                elif (len(first) < len(second) and len(
                                                        second) != 4):
                                                    if second[len(second) - 1] == \
                                                            first[
                                                                len(first) - 1] and firstunique!=1:
                                                        second.append(
                                                            first[len(first) - 1])
                                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                                        secondcontainer.append(
                                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                        if len(first) == 1:
                                                            first.pop()
                                                            firstcontainer.pop()
                                                            firstcontainer.pop()
                                                        else:
                                                            first.pop()
                                                            firstcontainer.pop()
                elif (firstunique==1 and len(third)<len(first) and thirdunique!=1) or (len(third)<len(first) and thirdunique==1 and firstunique==1) or (len(third) < len(first) and thirdunique!=1 and firstunique!=1) or (len(first) < len(third) and thirdunique!=1 and firstunique==1):
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        else:
                            append3 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        else:
                            append4 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(third[len(third) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in first:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    first.append(third[len(third) - 1])
                                    previous = eval(firstcontainer[len(firstcontainer) - 1])
                                    firstcontainer.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in second:
                                        if i != third[len(third) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        second.append(third[len(third) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.circle(screen,"{third[len(third) - 1]}",({secondpos1}, 438),21)')
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({secondpos2}, 415, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    else:
                                        if (len(third) < len(first) and len(
                                                first) != 4):
                                            if first[len(first) - 1] == \
                                                    third[
                                                        len(third) - 1] and thirdunique!=1:
                                                first.append(
                                                    third[len(third) - 1])
                                                previous = eval(firstcontainer[len(firstcontainer) - 1])
                                                firstcontainer.append(
                                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(third) == 1:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                                    thirdcontainer.pop()
                                                else:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                        elif (len(third) < len(second) and len(
                                                second) != 4):
                                            if second[len(second) - 1] == \
                                                    third[
                                                        len(third) - 1] and thirdunique!=1:
                                                second.append(
                                                    third[len(third) - 1])
                                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                                secondcontainer.append(
                                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                                if len(third) == 1:
                                                    third.pop()
                                                    thirdcontainer.pop()
                                                    thirdcontainer.pop()
                                                else:
                                                    third.pop()
                                                    thirdcontainer.pop()
        elif (len(third) == len(first)) or (len(third) == len(second)) :
            if len(third) == len(first):
                randomnumber = random.randint(0, 1)
                if randomnumber==0:
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()

                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(third[len(third) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                append3 = 1
                                self.sixthcheck.append(third[len(third) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(third[len(third) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                append4 = 1
                                self.fifthcheck.append(third[len(third) - 1])
                                self.fifthtube.append(
                                    f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                                self.fifthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(third[len(third) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in first:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    first.append(third[len(third) - 1])
                                    previous = eval(firstcontainer[len(firstcontainer) - 1])
                                    firstcontainer.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in second:
                                        if i != third[len(third) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        second.append(third[len(third) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    else:
                                        if first[len(first) - 1] == \
                                                third[
                                                    len(third) - 1]:
                                            first.append(
                                                third[len(third) - 1])
                                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                                            firstcontainer.append(
                                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(third) == 1:
                                                third.pop()
                                                thirdcontainer.pop()
                                                thirdcontainer.pop()
                                            else:
                                                third.pop()
                                                thirdcontainer.pop()
                elif randomnumber==1:
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()

                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(first[len(first) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                append3 = 1
                                self.sixthcheck.append(first[len(first) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(first[len(first) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(first[len(first) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                append4 = 1
                                self.fifthcheck.append(first[len(first) - 1])
                                self.fifthtube.append(
                                    f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                                self.fifthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(first[len(first) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(first[len(first) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in third:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    third.append(first[len(first) - 1])
                                    previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                    thirdcontainer.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in second:
                                        if i != first[len(first) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        second.append(first[len(first) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        if first[len(first) - 1] == \
                                                third[
                                                    len(third) - 1]:
                                            third.append(
                                                first[len(first) - 1])
                                            previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                            thirdcontainer.append(
                                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(first) == 1:
                                                first.pop()
                                                firstcontainer.pop()
                                                firstcontainer.pop()
                                            else:
                                                first.pop()
                                                firstcontainer.pop()
            elif len(third) == len(second):
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()

                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(third[len(third) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                append3 = 1
                                self.sixthcheck.append(third[len(third) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                second.append(third[len(third) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                append4 = 1
                                self.fifthcheck.append(third[len(third) - 1])
                                self.fifthtube.append(
                                    f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                                self.fifthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(third[len(third) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(third[len(third) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(third[len(third) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in first:
                                    if i != third[len(third) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    first.append(third[len(third) - 1])
                                    previous = eval(firstcontainer[len(firstcontainer) - 1])
                                    firstcontainer.append(
                                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(third) == 1:
                                        third.pop()
                                        thirdcontainer.pop()
                                        thirdcontainer.pop()
                                    else:
                                        third.pop()
                                        thirdcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in second:
                                        if i != third[len(third) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        second.append(third[len(third) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    else:
                                        if second[len(second) - 1] == \
                                                third[
                                                    len(third) - 1]:
                                            second.append(
                                                third[len(third) - 1])
                                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                                            secondcontainer.append(
                                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(third) == 1:
                                                third.pop()
                                                thirdcontainer.pop()
                                                thirdcontainer.pop()
                                            else:
                                                third.pop()
                                                thirdcontainer.pop()
                elif randomnumber==1:
                    if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                        countofcolor = 0
                        for i in self.fifthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        else:
                            append3 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()

                    elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                        countofcolor = 0
                        for i in self.sixthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        else:
                            append4 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                    elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                        randomnumber = random.randint(0, 1)
                        if randomnumber == 0:
                            append3 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        if randomnumber == 1:
                            append4 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                    elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                        # movingtube2 = 1
                        countofcolor = 0
                        # print('last step')
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.fifthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.fifthcheck.append(second[len(second) - 1])
                            previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif countofcolor != 0:
                            # print('append3' ,append3)
                            # print('countofcolor',countofcolor)
                            # print('inside else')
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in self.sixthcheck:
                                if i != second[len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                self.sixthcheck.append(second[len(second) - 1])
                                previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                                self.sixthtube.append(
                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in third:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    third.append(second[len(second) - 1])
                                    previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                    thirdcontainer.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    # print(easytubecheck1)
                                    # print(thirdunique, unique2, unique5, unique6)
                                    for i in first:
                                        if i != second[len(second) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        # print('fsr inside')
                                        append4 = 1
                                        first.append(second[len(second) - 1])
                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    else:
                                        if second[len(second) - 1] == \
                                                third[
                                                    len(third) - 1]:
                                            third.append(
                                                second[len(second) - 1])
                                            previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                            thirdcontainer.append(
                                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(second) == 1:
                                                second.pop()
                                                secondcontainer.pop()
                                                secondcontainer.pop()
                                            else:
                                                second.pop()
                                                secondcontainer.pop()
        elif (len(first) == len(second)):
            randomnumber=random.randint(0,1)
            if randomnumber==0:
                if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                    countofcolor = 0
                    for i in self.fifthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fifthcheck.append(second[len(second) - 1])
                        previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    else:
                        append3 = 1
                        self.sixthcheck.append(second[len(second) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()

                elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append3 = 1
                        self.sixthcheck.append(second[len(second) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    else:
                        append4 = 1
                        self.fifthcheck.append(second[len(second) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                    randomnumber = random.randint(0, 1)
                    if randomnumber == 0:
                        append3 = 1
                        self.fifthcheck.append(second[len(second) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    if randomnumber == 1:
                        append4 = 1
                        self.sixthcheck.append(second[len(second) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                    # movingtube2 = 1
                    countofcolor = 0
                    # print('last step')
                    # print(easytubecheck1)
                    # print(thirdunique, unique2, unique5, unique6)
                    for i in self.fifthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append3 = 1
                        self.fifthcheck.append(second[len(second) - 1])
                        previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    elif countofcolor != 0:
                        # print('append3' ,append3)
                        # print('countofcolor',countofcolor)
                        # print('inside else')
                        countofcolor = 0
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.sixthcheck:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            # print('fsr inside')
                            append4 = 1
                            self.sixthcheck.append(second[len(second) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in third:
                                if i != second[len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                third.append(second[len(second) - 1])
                                previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                thirdcontainer.append(
                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in first:
                                    if i != second[len(second) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    first.append(second[len(second) - 1])
                                    previous = eval(firstcontainer[len(firstcontainer) - 1])
                                    firstcontainer.append(
                                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(second) == 1:
                                        second.pop()
                                        secondcontainer.pop()
                                        secondcontainer.pop()
                                    else:
                                        second.pop()
                                        secondcontainer.pop()
                                else:
                                    if first[len(first) - 1] == \
                                            second[
                                                len(second) - 1]:
                                        first.append(
                                            second[len(second) - 1])
                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
            elif randomnumber==1:
                if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:

                    countofcolor = 0
                    for i in self.fifthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fifthcheck.append(first[len(first) - 1])
                        previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()

                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in second:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            second.append(first[len(first) - 1])
                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                            secondcontainer.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        else:
                            append3 = 1
                            self.sixthcheck.append(first[len(first) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append3 = 1
                        self.sixthcheck.append(first[len(first) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in second:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            second.append(first[len(first) - 1])
                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                            secondcontainer.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        else:
                            append4 = 1
                            self.fifthcheck.append(first[len(first) - 1])
                            self.fifthtube.append(
                                f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                            self.fifthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                    randomnumber = random.randint(0, 1)
                    if randomnumber == 0:
                        append3 = 1
                        self.fifthcheck.append(first[len(first) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    if randomnumber == 1:
                        append4 = 1
                        self.sixthcheck.append(first[len(first) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                    # movingtube2 = 1
                    countofcolor = 0
                    # print('last step')
                    # print(easytubecheck1)
                    # print(thirdunique, unique2, unique5, unique6)
                    for i in self.fifthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append3 = 1
                        self.fifthcheck.append(first[len(first) - 1])
                        previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        # print('append3' ,append3)
                        # print('countofcolor',countofcolor)
                        # print('inside else')
                        countofcolor = 0
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in self.sixthcheck:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            # print('fsr inside')
                            append4 = 1
                            self.sixthcheck.append(first[len(first) - 1])
                            previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                            self.sixthtube.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in third:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                third.append(first[len(first) - 1])
                                previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                thirdcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            elif countofcolor != 0:
                                countofcolor = 0
                                # print(easytubecheck1)
                                # print(thirdunique, unique2, unique5, unique6)
                                for i in second:
                                    if i != first[len(first) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    # print('fsr inside')
                                    append4 = 1
                                    second.append(first[len(first) - 1])
                                    previous = eval(secondcontainer[len(secondcontainer) - 1])
                                    secondcontainer.append(
                                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(first) == 1:
                                        first.pop()
                                        firstcontainer.pop()
                                        firstcontainer.pop()
                                    else:
                                        first.pop()
                                        firstcontainer.pop()
                                else:
                                    if first[len(first) - 1] == \
                                            second[
                                                len(second) - 1]:
                                        second.append(
                                            first[len(first) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
        elif len(third)<len(second) and len(third)<len(first) and len(third)!=0:
            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(third[len(third) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()

                elif countofcolor != 0:
                    countofcolor = 0
                    for i in second:
                        if i != third[len(third) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        second.append(third[len(third) - 1])
                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                        secondcontainer.append(
                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(third) == 1:
                            third.pop()
                            thirdcontainer.pop()
                            thirdcontainer.pop()
                        else:
                            third.pop()
                            thirdcontainer.pop()
                    else:
                        self.sixthcheck.append(third[len(third) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                        if len(third) == 1:
                            third.pop()
                            thirdcontainer.pop()
                            thirdcontainer.pop()
                        else:
                            third.pop()
                            thirdcontainer.pop()
            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.sixthcheck.append(third[len(third) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in second:
                        if i != third[len(third) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        second.append(third[len(third) - 1])
                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                        secondcontainer.append(
                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(third) == 1:
                            third.pop()
                            thirdcontainer.pop()
                            thirdcontainer.pop()
                        else:
                            third.pop()
                            thirdcontainer.pop()
                    else:
                        self.fifthcheck.append(third[len(third) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                        if len(third) == 1:
                            third.pop()
                            thirdcontainer.pop()
                            thirdcontainer.pop()
                        else:
                            third.pop()
                            thirdcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.fifthcheck.append(third[len(third) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
                if randomnumber == 1:
                    self.sixthcheck.append(third[len(third) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(third[len(third) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != third[len(third) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(third[len(third) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(third) == 1:
                            third.pop()
                            thirdcontainer.pop()
                            thirdcontainer.pop()
                        else:
                            third.pop()
                            thirdcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in first:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            first.append(third[len(third) - 1])
                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                            firstcontainer.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                second.append(third[len(third) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                if (len(third)<len(first) and len(first)!=4):
                                    if third[len(third)-1] == first[len(first)-1] and thirdunique!=1:
                                        first.append(third[len(third) - 1])
                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    else:
                                        self.three_not_unique_thirdlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,secondunique)
                                elif (len(third)<len(second) and len(second)!=4):
                                    if third[len(third) - 1] == second[len(second) - 1] and thirdunique!=1:
                                        second.append(third[len(third) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                    else:
                                        self.three_not_unique_thirdlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,secondunique)
                                else:
                                    self.three_not_unique_thirdlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,secondunique)
        elif len(first)<len(second) and len(first)<len(third) and len(first)!=0:
            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.fifthcheck.append(first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()

                elif countofcolor != 0:
                    countofcolor = 0
                    for i in second:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        second.append(first[len(first) - 1])
                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                        secondcontainer.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    else:
                        self.sixthcheck.append(first[len(first) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.sixthcheck.append(first[len(first) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in second:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        second.append(first[len(first) - 1])
                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                        secondcontainer.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    else:
                        self.fifthcheck.append(first[len(first) - 1])
                        self.fifthtube.append(
                            f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                        self.fifthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                if randomnumber == 1:
                    self.sixthcheck.append(first[len(first) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(first[len(first) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in third:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            third.append(first[len(first) - 1])
                            previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                            thirdcontainer.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != first[len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                second.append(first[len(first) - 1])
                                previous = eval(secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                if (len(first) < len(second) and len(second) != 4):
                                    if second[len(second) - 1] == first[
                                        len(first) - 1] and firstunique!=1:
                                        second.append(first[len(first) - 1])
                                        previous = eval(secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        self.three_not_unique_firstlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,secondunique,thirdunique)
                                elif (len(first) < len(third) and len(third) != 4):
                                    if third[len(third) - 1] == first[
                                        len(first) - 1] and firstunique!=1:
                                        third.append(first[len(first) - 1])
                                        previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                        thirdcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                    else:
                                        self.three_not_unique_firstlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,secondunique,thirdunique)
                                else:
                                    self.three_not_unique_firstlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,secondunique,thirdunique)
        elif len(second)<len(first) and len(second)<len(third) and len(second)!=0:
            if len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.fifthcheck.append(second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                else:
                    append3 = 1
                    self.sixthcheck.append(second[len(second) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()

            elif len(self.sixthcheck) != 0 and len(self.fifthcheck) == 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.sixthcheck.append(second[len(second) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                else:
                    append4 = 1
                    self.fifthcheck.append(second[len(second) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.fifthcheck.append(second[len(second) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(second[len(second) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                # movingtube2 = 1
                countofcolor = 0
                # print('last step')
                # print(easytubecheck1)
                # print(thirdunique, unique2, unique5, unique6)
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(second[len(second) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in third:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            third.append(second[len(second) - 1])
                            previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                            thirdcontainer.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in first:
                                if i != second[len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                first.append(second[len(second) - 1])
                                previous = eval(firstcontainer[len(firstcontainer) - 1])
                                firstcontainer.append(
                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            else:
                                if (len(second) < len(first) and len(first) != 4):
                                    if second[len(second)-1]== first[len(first)-1] and secondunique!=1:
                                        first.append(second[len(second) - 1])
                                        previous = eval(firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    else:
                                        self.three_not_unique_secondlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,thirdunique)
                                elif len(second) < len(third) and len(third) != 4:
                                    if third[len(third) - 1] == second[
                                        len(second) - 1] and secondunique!=1:
                                        third.append(second[len(second) - 1])
                                        previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                                        thirdcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                    else:
                                        self.three_not_unique_secondlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,thirdunique)
                                else:
                                    self.three_not_unique_secondlessthan(first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,thirdunique)
    def three_not_unique_secondlessthan(self,first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,thirdunique):
        randomnumber = random.randint(0, 1)
        if randomnumber == 0:
            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.sixthcheck.append(
                        first[len(first) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()

                else:
                    append3 = 1
                    self.fifthcheck.append(
                        first[len(first) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()

                else:
                    append4 = 1
                    self.sixthcheck.append(
                        first[len(first) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.fifthcheck.append(
                        first[len(first) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                if randomnumber == 1:
                    self.sixthcheck.append(
                        first[len(first) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    self.fifthcheck.append(
                        first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(
                            first[len(first) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in second:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            second.append(
                                first[len(first) - 1])
                            previous = eval(secondcontainer[len(secondcontainer) - 1])
                            secondcontainer.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in third:
                                if i != first[
                                    len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                third.append(
                                    first[len(first) - 1])
                                previous = eval(
                                    thirdcontainer[len(thirdcontainer) - 1])
                                thirdcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                if (len(first) < len(
                                        second) and len(
                                        second) != 4):
                                    if second[
                                        len(second) - 1] == \
                                            first[
                                                len(first) - 1] and firstunique!=1 :
                                        second.append(
                                            first[
                                                len(first) - 1])
                                        previous = eval(
                                            secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                elif (len(first) < len(
                                        third) and len(
                                        third) != 4):
                                    if third[
                                        len(third) - 1] == \
                                            first[
                                                len(first) - 1] and firstunique!=1:
                                        third.append(
                                            first[
                                                len(first) - 1])
                                        previous = eval(
                                            thirdcontainer[len(thirdcontainer) - 1])
                                        thirdcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
        elif randomnumber == 1:
            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.sixthcheck.append(
                        third[len(third) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()

                else:
                    append3 = 1
                    self.fifthcheck.append(
                        third[len(third) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        third[len(third) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()

                else:
                    append4 = 1
                    self.sixthcheck.append(
                        third[len(third) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        third[len(third) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(
                        third[len(third) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        third[len(third) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != third[len(third) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.sixthcheck.append(
                            third[len(third) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(third) == 1:
                            third.pop()
                            thirdcontainer.pop()
                            thirdcontainer.pop()
                        else:
                            third.pop()
                            thirdcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in first:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            first.append(
                                third[len(third) - 1])
                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                            firstcontainer.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[
                                    len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                second.append(
                                    third[len(third) - 1])
                                previous = eval(
                                    secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                if (len(third) < len(
                                        first) and len(
                                        first) != 4):
                                    if third[
                                        len(third) - 1] == \
                                            first[
                                                len(first) - 1] and thirdunique!=1:
                                        first.append(
                                            third[
                                                len(third) - 1])
                                        previous = eval(
                                            firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                elif (len(third) < len(
                                        second) and len(
                                        second) != 4):
                                    if third[
                                        len(third) - 1] == \
                                            second[
                                                len(second) - 1] and thirdunique!=1:
                                        second.append(
                                            third[
                                                len(third) - 1])
                                        previous = eval(
                                            secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()

    def three_not_unique_firstlessthan(self,first,firstcontainer,second,secondcontainer,third,thirdcontainer,secondunique,thirdunique):
        randomnumber = random.randint(0, 1)
        if randomnumber == 0:
            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.sixthcheck.append(
                        second[len(second) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()

                else:
                    append3 = 1
                    self.fifthcheck.append(
                        second[len(second) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()

                else:
                    append4 = 1
                    self.sixthcheck.append(
                        second[len(second) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        second[len(second) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(
                        second[len(second) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:

                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.sixthcheck.append(
                            second[len(second) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in first:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            # print('fsr inside')
                            append4 = 1
                            first.append(
                                second[len(second) - 1])
                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                            firstcontainer.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in third:
                                if i != second[
                                    len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                third.append(
                                    second[len(second) - 1])
                                previous = eval(
                                    thirdcontainer[len(thirdcontainer) - 1])
                                thirdcontainer.append(
                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            else:
                                if (len(second) < len(
                                        first) and len(
                                        first) != 4):
                                    if second[
                                        len(second) - 1] == \
                                            first[
                                                len(first) - 1] and secondunique!=1:
                                        first.append(
                                            second[
                                                len(second) - 1])
                                        previous = eval(
                                            firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                elif (len(second) < len(
                                        third) and len(
                                        third) != 4):
                                    if third[
                                        len(third) - 1] == \
                                            second[
                                                len(second) - 1] and secondunique!=1:
                                        third.append(
                                            second[
                                                len(second) - 1])
                                        previous = eval(
                                            thirdcontainer[len(thirdcontainer) - 1])
                                        thirdcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
        elif randomnumber == 1:
            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.sixthcheck.append(
                        third[len(third) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()

                else:
                    append3 = 1
                    self.fifthcheck.append(
                        third[len(third) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        third[len(third) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()

                else:
                    append4 = 1
                    self.sixthcheck.append(
                        third[len(third) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        third[len(third) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(
                        third[len(third) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{third[len(third) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:

                countofcolor = 0
                # print(easytubecheck1)
                # print(thirdunique, unique2, unique5, unique6)
                for i in self.fifthcheck:
                    if i != third[len(third) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        third[len(third) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(third) == 1:
                        third.pop()
                        thirdcontainer.pop()
                        thirdcontainer.pop()
                    else:
                        third.pop()
                        thirdcontainer.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.sixthcheck:
                        if i != third[len(third) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.sixthcheck.append(
                            third[len(third) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(third) == 1:
                            third.pop()
                            thirdcontainer.pop()
                            thirdcontainer.pop()
                        else:
                            third.pop()
                            thirdcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in first:
                            if i != third[len(third) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append4 = 1
                            first.append(
                                third[len(third) - 1])
                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                            firstcontainer.append(
                                f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(third) == 1:
                                third.pop()
                                thirdcontainer.pop()
                                thirdcontainer.pop()
                            else:
                                third.pop()
                                thirdcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in second:
                                if i != third[
                                    len(third) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                second.append(
                                    third[len(third) - 1])
                                previous = eval(
                                    secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(third) == 1:
                                    third.pop()
                                    thirdcontainer.pop()
                                    thirdcontainer.pop()
                                else:
                                    third.pop()
                                    thirdcontainer.pop()
                            else:
                                if (len(third) < len(
                                        first) and len(
                                        first) != 4):
                                    if third[
                                        len(third) - 1] == \
                                            first[
                                                len(first) - 1] and thirdunique!=1:
                                        first.append(
                                            third[
                                                len(third) - 1])
                                        previous = eval(
                                            firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
                                elif (len(third) < len(
                                        second) and len(
                                        third) != 4):
                                    if third[
                                        len(third) - 1] == \
                                            second[
                                                len(second) - 1] and thirdunique!=1:
                                        second.append(
                                            third[
                                                len(third) - 1])
                                        previous = eval(
                                            secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{third[len(third) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(third) == 1:
                                            third.pop()
                                            thirdcontainer.pop()
                                            thirdcontainer.pop()
                                        else:
                                            third.pop()
                                            thirdcontainer.pop()
    def three_not_unique_thirdlessthan(self,first,firstcontainer,second,secondcontainer,third,thirdcontainer,firstunique,secondunique):
        randomnumber = random.randint(0, 1)
        if randomnumber == 0:
            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.sixthcheck.append(
                        second[len(second) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()

                else:
                    append3 = 1
                    self.fifthcheck.append(
                        second[len(second) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()

                else:
                    append4 = 1
                    self.sixthcheck.append(
                        second[len(second) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        second[len(second) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(
                        second[len(second) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{second[len(second) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != second[len(second) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        second[len(second) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(second) == 1:
                        second.pop()
                        secondcontainer.pop()
                        secondcontainer.pop()
                    else:
                        second.pop()
                        secondcontainer.pop()
                elif countofcolor != 0:
                    # print('append3' ,append3)
                    # print('countofcolor',countofcolor)
                    # print('inside else')
                    countofcolor = 0
                    # print(easytubecheck1)
                    # print(thirdunique, unique2, unique5, unique6)
                    for i in self.sixthcheck:
                        if i != second[len(second) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        # print('fsr inside')
                        append4 = 1
                        self.sixthcheck.append(
                            second[len(second) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(second) == 1:
                            second.pop()
                            secondcontainer.pop()
                            secondcontainer.pop()
                        else:
                            second.pop()
                            secondcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in first:
                            if i != second[len(second) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            # print('fsr inside')
                            append4 = 1
                            first.append(
                                second[len(second) - 1])
                            previous = eval(firstcontainer[len(firstcontainer) - 1])
                            firstcontainer.append(
                                f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(second) == 1:
                                second.pop()
                                secondcontainer.pop()
                                secondcontainer.pop()
                            else:
                                second.pop()
                                secondcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in third:
                                if i != second[
                                    len(second) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                third.append(
                                    second[len(second) - 1])
                                previous = eval(
                                    thirdcontainer[len(thirdcontainer) - 1])
                                thirdcontainer.append(
                                    f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(second) == 1:
                                    second.pop()
                                    secondcontainer.pop()
                                    secondcontainer.pop()
                                else:
                                    second.pop()
                                    secondcontainer.pop()
                            else:
                                if (len(second) < len(
                                        first) and len(
                                        first) != 4):
                                    if second[
                                        len(second) - 1] == \
                                            first[
                                                len(first) - 1] and secondunique!=1:
                                        first.append(
                                            second[
                                                len(second) - 1])
                                        previous = eval(
                                            firstcontainer[len(firstcontainer) - 1])
                                        firstcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                                elif (len(second) < len(
                                        third) and len(
                                        third) != 4):
                                    if third[
                                        len(third) - 1] == \
                                            second[
                                                len(second) - 1] and secondunique!=1:
                                        third.append(
                                            second[
                                                len(second) - 1])
                                        previous = eval(
                                            thirdcontainer[len(thirdcontainer) - 1])
                                        thirdcontainer.append(
                                            f'pygame.draw.rect(screen,"{second[len(second) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(second) == 1:
                                            second.pop()
                                            secondcontainer.pop()
                                            secondcontainer.pop()
                                        else:
                                            second.pop()
                                            secondcontainer.pop()
                            # elif countofcolor != 0:
        elif randomnumber == 1:
            if len(self.fifthcheck) == 0 and len(self.sixthcheck) != 0:
                countofcolor = 0
                for i in self.sixthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.sixthcheck.append(
                        first[len(first) - 1])
                    previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()

                else:
                    append3 = 1
                    self.fifthcheck.append(
                        first[len(first) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) == 0:
                countofcolor = 0
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()

                else:
                    append4 = 1
                    self.sixthcheck.append(
                        first[len(first) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) == 0 and len(self.sixthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        first[len(first) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(276, 438),21)')
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.sixthcheck.append(
                        first[len(first) - 1])
                    self.sixthtube.append(
                        f'pygame.draw.circle(screen,"{first[len(first) - 1]}",(176, 438),21)')
                    self.sixthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect(153.9, 415, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
            elif len(self.fifthcheck) != 0 and len(self.sixthcheck) != 0:

                countofcolor = 0
                # print(easytubecheck1)
                # print(thirdunique, unique2, unique5, unique6)
                for i in self.fifthcheck:
                    if i != first[len(first) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.fifthcheck.append(
                        first[len(first) - 1])
                    previous = eval(self.fifthtube[len(self.fifthtube) - 1])
                    self.fifthtube.append(
                        f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(first) == 1:
                        first.pop()
                        firstcontainer.pop()
                        firstcontainer.pop()
                    else:
                        first.pop()
                        firstcontainer.pop()
                elif countofcolor != 0:
                    # print('append3' ,append3)
                    # print('countofcolor',countofcolor)
                    # print('inside else')
                    countofcolor = 0
                    # print(easytubecheck1)
                    # print(thirdunique, unique2, unique5, unique6)
                    for i in self.sixthcheck:
                        if i != first[len(first) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        # print('fsr inside')
                        append4 = 1
                        self.sixthcheck.append(
                            first[len(first) - 1])
                        previous = eval(self.sixthtube[len(self.sixthtube) - 1])
                        self.sixthtube.append(
                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(first) == 1:
                            first.pop()
                            firstcontainer.pop()
                            firstcontainer.pop()
                        else:
                            first.pop()
                            firstcontainer.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        # print(easytubecheck1)
                        # print(thirdunique, unique2, unique5, unique6)
                        for i in third:
                            if i != first[len(first) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            # print('fsr inside')
                            append4 = 1
                            third.append(
                                first[len(first) - 1])
                            previous = eval(thirdcontainer[len(thirdcontainer) - 1])
                            thirdcontainer.append(
                                f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(first) == 1:
                                first.pop()
                                firstcontainer.pop()
                                firstcontainer.pop()
                            else:
                                first.pop()
                                firstcontainer.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            # print(easytubecheck1)
                            # print(thirdunique, unique2, unique5, unique6)
                            for i in second:
                                if i != first[
                                    len(first) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                # print('fsr inside')
                                append4 = 1
                                second.append(
                                    first[len(first) - 1])
                                previous = eval(
                                    secondcontainer[len(secondcontainer) - 1])
                                secondcontainer.append(
                                    f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(first) == 1:
                                    first.pop()
                                    firstcontainer.pop()
                                    firstcontainer.pop()
                                else:
                                    first.pop()
                                    firstcontainer.pop()
                            else:
                                if (len(first) < len(
                                        second) and len(
                                        second) != 4):
                                    if second[
                                        len(second) - 1] == \
                                            first[
                                                len(first) - 1] and firstunique!=1:
                                        second.append(
                                            first[
                                                len(first) - 1])
                                        previous = eval(
                                            secondcontainer[len(secondcontainer) - 1])
                                        secondcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()
                                elif (len(first) < len(
                                        third) and len(
                                        third) != 4):
                                    if third[
                                        len(third) - 1] == \
                                            first[
                                                len(first) - 1] and firstunique!=1:
                                        third.append(
                                            first[
                                                len(first) - 1])
                                        previous = eval(
                                            thirdcontainer[len(thirdcontainer) - 1])
                                        thirdcontainer.append(
                                            f'pygame.draw.rect(screen,"{first[len(first) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(first) == 1:
                                            first.pop()
                                            firstcontainer.pop()
                                            firstcontainer.pop()
                                        else:
                                            first.pop()
                                            firstcontainer.pop()



class Easymode():
    def __init__(self,firstcheck,firsttube,secondcheck,secondtube,thirdcheck,thirdtube,fourthcheck,fourthtube,unique1,unique2,unique5,unique6):
        self.firstcheck=firstcheck
        self.firsttube=firsttube
        self.secondcheck=secondcheck
        self.secondtube=secondtube
        self.thirdcheck=thirdcheck
        self.thirdtube=thirdtube
        self.fourthcheck=fourthcheck
        self.fourthtube=fourthtube
        self.unique1=unique1
        self.unique2=unique2
        self.unique5=unique5
        self.unique6=unique6

    def firstunique_secondnotunique(self):
        if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
            countofcolor = 0
            for i in self.fourthcheck:
                if i != self.secondcheck[len(self.secondcheck) - 1]:
                    countofcolor += 1
            if countofcolor == 0:
                append4=1
                self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                if len(self.secondcheck) == 1:
                    self.secondcheck.pop()
                    self.secondtube.pop()
                    self.secondtube.pop()
                else:
                    self.secondcheck.pop()
                    self.secondtube.pop()

            else:
                self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                if len(self.secondcheck) == 1:
                    self.secondcheck.pop()
                    self.secondtube.pop()
                    self.secondtube.pop()
                else:
                    self.secondcheck.pop()
                    self.secondtube.pop()
        elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
            countofcolor = 0
            for i in self.thirdcheck:
                if i != self.secondcheck[len(self.secondcheck) - 1]:
                    countofcolor += 1
            if countofcolor == 0:
                append3 = 1
                self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                if len(self.secondcheck) == 1:
                    self.secondcheck.pop()
                    self.secondtube.pop()
                    self.secondtube.pop()
                else:
                    self.secondcheck.pop()
                    self.secondtube.pop()
            else:
                append4 = 1
                self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                if len(self.secondcheck) == 1:
                    self.secondcheck.pop()
                    self.secondtube.pop()
                    self.secondtube.pop()
                else:
                    self.secondcheck.pop()
                    self.secondtube.pop()
        elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
            randomnumber = random.randint(0, 1)
            if randomnumber == 0:
                self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                if len(self.secondcheck) == 1:
                    self.secondcheck.pop()
                    self.secondtube.pop()
                    self.secondtube.pop()
                else:
                    self.secondcheck.pop()
                    self.secondtube.pop()
            if randomnumber == 1:
                self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                if len(self.secondcheck) == 1:
                    self.secondcheck.pop()
                    self.secondtube.pop()
                    self.secondtube.pop()
                else:
                    self.secondcheck.pop()
                    self.secondtube.pop()
        elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
            countofcolor = 0
            for i in self.thirdcheck:
                if i != self.secondcheck[len(self.secondcheck) - 1]:
                    countofcolor += 1
            if countofcolor == 0:
                self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                if len(self.secondcheck) == 1:
                    self.secondcheck.pop()
                    self.secondtube.pop()
                    self.secondtube.pop()
                else:
                    self.secondcheck.pop()
                    self.secondtube.pop()
            else:
                self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                if len(self.secondcheck) == 1:
                    self.secondcheck.pop()
                    self.secondtube.pop()
                    self.secondtube.pop()
                else:
                    self.secondcheck.pop()
                    self.secondtube.pop()  
    def firstnotunique_secondunique(self):
        if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
            countofcolor = 0
            for i in self.fourthcheck:
                if i != self.firstcheck[len(self.firstcheck) - 1]:
                    countofcolor += 1
            if countofcolor == 0:
                append4=1
                self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                if len(self.firstcheck) == 1:
                    self.firstcheck.pop()
                    self.firsttube.pop()
                    self.firsttube.pop()
                else:
                    self.firstcheck.pop()
                    self.firsttube.pop()
            else:
                append3 = 1
                self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                if len(self.firstcheck) == 1:
                    self.firstcheck.pop()
                    self.firsttube.pop()
                    self.firsttube.pop()
                else:
                    self.firstcheck.pop()
                    self.firsttube.pop()
        elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
            countofcolor = 0
            for i in self.thirdcheck:
                if i != self.firstcheck[len(self.firstcheck) - 1]:
                    countofcolor += 1
            if countofcolor == 0:
                append3 = 1
                self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                if len(self.firstcheck) == 1:
                    self.firstcheck.pop()
                    self.firsttube.pop()
                    self.firsttube.pop()
                else:
                    self.firstcheck.pop()
                    self.firsttube.pop()
            else:
                append4 = 1
                self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                if len(self.firstcheck) == 1:
                    self.firstcheck.pop()
                    self.firsttube.pop()
                    self.firsttube.pop()
                else:
                    self.firstcheck.pop()
                    self.firsttube.pop()
        elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
            randomnumber = random.randint(0, 1)
            if randomnumber == 0:
                append3 = 1
                self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                if len(self.firstcheck) == 1:
                    self.firstcheck.pop()
                    self.firsttube.pop()
                    self.firsttube.pop()
                else:
                    self.firstcheck.pop()
                    self.firsttube.pop()
            if randomnumber == 1:
                append4 = 1
                self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                if len(self.firstcheck) == 1:
                    self.firstcheck.pop()
                    self.firsttube.pop()
                    self.firsttube.pop()
                else:
                    self.firstcheck.pop()
                    self.firsttube.pop()
        elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
            countofcolor = 0
            for i in self.thirdcheck:
                if i != self.firstcheck[len(self.firstcheck) - 1]:
                    countofcolor += 1
            if countofcolor == 0:
                append3 = 1
                self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                if len(self.firstcheck) == 1:
                    self.firstcheck.pop()
                    self.firsttube.pop()
                    self.firsttube.pop()
                else:
                    self.firstcheck.pop()
                    self.firsttube.pop()
            else:
                append4 = 1
                self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                if len(self.firstcheck) == 1:
                    self.firstcheck.pop()
                    self.firsttube.pop()
                    self.firsttube.pop()
                else:
                    self.firstcheck.pop()
                    self.firsttube.pop()    
    def both_not_unique(self):
        if len(self.firstcheck)==5 and len(self.secondcheck)==5:
            randomnumber = random.randint(0, 1)
            if randomnumber==0:
                randomnumber1 = random.randint(0, 1)
                if randomnumber1 == 0:
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                if randomnumber1 == 1:
                    append4 = 1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            if randomnumber==1:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
        elif self.unique2==1 and self.unique1!=1:
            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.fourthcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4=1
                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                else:
                    append3 = 1
                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                else:
                    append4 = 1
                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                elif countofcolor!=0:
                    countofcolor = 0
                    for i in self.fourthcheck:
                        if i != self.secondcheck[len(self.secondcheck) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(self.secondcheck) == 1:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                            self.secondtube.pop()
                        else:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                    elif countofcolor!=0:
                        countofcolor = 0
                        for i in self.firstcheck:
                            if i != self.secondcheck[len(self.secondcheck) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            # append4 = 1
                            self.firstcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                            previous = eval(self.firsttube[len(self.firsttube) - 1])
                            self.firsttube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.secondcheck) == 1:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                                self.secondtube.pop()
                            else:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                        elif self.secondcheck[len(self.secondcheck)-1]==self.firstcheck[len(self.firstcheck)-1] and self.firstcheck[len(self.firstcheck) - 2] == self.secondcheck[len(self.secondcheck) - 1] :
                            self.firstcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                            previous = eval(self.firsttube[len(self.firsttube) - 1])
                            self.firsttube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.secondcheck) == 1:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                                self.secondtube.pop()
                            else:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                        else:
                            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                                countofcolor = 0
                                for i in self.fourthcheck:
                                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4=1
                                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                else:
                                    append3 = 1
                                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                                countofcolor = 0
                                for i in self.thirdcheck:
                                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                else:
                                    append4 = 1
                                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                                countofcolor = 0
                                for i in self.thirdcheck:
                                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in self.fourthcheck:
                                        if i != self.firstcheck[len(self.firstcheck) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(self.firstcheck) == 1:
                                            self.firstcheck.pop()
                                            self.firsttube.pop()
                                            self.firsttube.pop()
                                        else:
                                            self.firstcheck.pop()
                                            self.firsttube.pop()
                                    else:
                                        if self.secondcheck[len(self.secondcheck) - 1] == self.firstcheck[len(self.firstcheck) - 1]:
                                            self.secondcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                            previous = eval(self.secondtube[len(self.secondtube) - 1])
                                            self.secondtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(self.firstcheck) == 1:
                                                self.firstcheck.pop()
                                                self.firsttube.pop()
                                                self.firsttube.pop()
                                            else:
                                                self.firstcheck.pop()
                                                self.firsttube.pop()
        elif self.unique2!=1 and self.unique1==1:
            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.fourthcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4=1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                else:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                else:
                    append4 = 1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                elif countofcolor!=0:
                    countofcolor = 0
                    for i in self.fourthcheck:
                        if i != self.firstcheck[len(self.firstcheck) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(self.firstcheck) == 1:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                            self.firsttube.pop()
                        else:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                    elif countofcolor!=0:
                        countofcolor = 0
                        for i in self.secondcheck:
                            if i != self.firstcheck[len(self.firstcheck) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            self.secondcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                            previous = eval(self.secondtube[len(self.secondtube) - 1])
                            self.secondtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.firstcheck) == 1:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                                self.firsttube.pop()
                            else:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                        elif self.firstcheck[len(self.firstcheck)-1]==self.secondcheck[len(self.secondcheck)-1] and self.secondcheck[len(self.secondcheck) - 2] == self.firstcheck[len(self.firstcheck) - 1] :
                            self.secondcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                            previous = eval(self.secondtube[len(self.secondtube) - 1])
                            self.secondtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.firstcheck) == 1:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                                self.firsttube.pop()
                            else:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                        else:
                            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                                countofcolor = 0
                                for i in self.fourthcheck:
                                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4=1
                                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                else:
                                    append3 = 1
                                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                                countofcolor = 0
                                for i in self.thirdcheck:
                                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                else:
                                    append4 = 1
                                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                                countofcolor = 0
                                for i in self.thirdcheck:
                                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                elif countofcolor!=0:
                                    countofcolor = 0
                                    for i in self.fourthcheck:
                                        if i != self.secondcheck[len(self.secondcheck) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(self.secondcheck) == 1:
                                            self.secondcheck.pop()
                                            self.secondtube.pop()
                                            self.secondtube.pop()
                                        else:
                                            self.secondcheck.pop()
                                            self.secondtube.pop()
                                    else:
                                        if self.secondcheck[len(self.secondcheck) - 1] == self.firstcheck[len(self.firstcheck) - 1]:
                                            self.firstcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                            previous = eval(self.firsttube[len(self.firsttube) - 1])
                                            self.firsttube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(self.secondcheck) == 1:
                                                self.secondcheck.pop()
                                                self.secondtube.pop()
                                                self.secondtube.pop()
                                            else:
                                                self.secondcheck.pop()
                                                self.secondtube.pop()
        elif len(self.secondcheck) < len(self.firstcheck) and len(self.secondcheck) != 0:
            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.fourthcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.fourthcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                    self.fourthtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                else:
                    append3 = 1
                    self.thirdcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    self.thirdtube.append(
                        f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                else:
                    append4 = 1
                    self.fourthcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    self.fourthtube.append(
                        f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.thirdcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    self.thirdtube.append(
                        f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.fourthcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    self.fourthtube.append(
                        f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.fourthcheck:
                        if i != self.secondcheck[len(self.secondcheck) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fourthcheck.append(
                            self.secondcheck[len(self.secondcheck) - 1])
                        previous = eval(
                            self.fourthtube[len(self.fourthtube) - 1])
                        self.fourthtube.append(
                            f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(self.secondcheck) == 1:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                            self.secondtube.pop()
                        else:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                    elif countofcolor != 0:
                        countofcolor = 0
                        for i in self.firstcheck:
                            if i != self.secondcheck[len(self.secondcheck) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            # append4 = 1
                            self.firstcheck.append(
                                self.secondcheck[len(self.secondcheck) - 1])
                            previous = eval(
                                self.firsttube[len(self.firsttube) - 1])
                            self.firsttube.append(
                                f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.secondcheck) == 1:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                                self.secondtube.pop()
                            else:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                        elif self.secondcheck[len(self.secondcheck)-1] == self.firstcheck[len(self.firstcheck)-1] and self.firstcheck[len(self.firstcheck) - 2] == self.secondcheck[len(self.secondcheck) - 1]:
                            self.firstcheck.append(
                                self.secondcheck[len(self.secondcheck) - 1])
                            previous = eval(
                                self.firsttube[len(self.firsttube) - 1])
                            self.firsttube.append(
                                f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.secondcheck) == 1:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                                self.secondtube.pop()
                            else:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                        else:
                            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                                countofcolor = 0
                                for i in self.fourthcheck:
                                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4 = 1
                                    self.fourthcheck.append(
                                        self.firstcheck[len(self.firstcheck) - 1])
                                    previous = eval(
                                        self.fourthtube[len(self.fourthtube) - 1])
                                    self.fourthtube.append(
                                        f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                else:
                                    append3 = 1
                                    self.thirdcheck.append(
                                        self.firstcheck[len(self.firstcheck) - 1])
                                    self.thirdtube.append(
                                        f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                                    self.thirdtube.append(
                                        f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                                countofcolor = 0
                                for i in self.thirdcheck:
                                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.thirdcheck.append(
                                        self.firstcheck[len(self.firstcheck) - 1])
                                    previous = eval(
                                        self.thirdtube[len(self.thirdtube) - 1])
                                    self.thirdtube.append(
                                        f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                else:
                                    append4 = 1
                                    self.fourthcheck.append(
                                        self.firstcheck[len(self.firstcheck) - 1])
                                    self.fourthtube.append(
                                        f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                                    self.fourthtube.append(
                                        f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.thirdcheck.append(
                                        self.firstcheck[len(self.firstcheck) - 1])
                                    self.thirdtube.append(
                                        f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                                    self.thirdtube.append(
                                        f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.fourthcheck.append(
                                        self.firstcheck[len(self.firstcheck) - 1])
                                    self.fourthtube.append(
                                        f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                                    self.fourthtube.append(
                                        f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                                countofcolor = 0
                                for i in self.thirdcheck:
                                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.thirdcheck.append(
                                        self.firstcheck[len(self.firstcheck) - 1])
                                    previous = eval(
                                        self.thirdtube[len(self.thirdtube) - 1])
                                    self.thirdtube.append(
                                        f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.firstcheck) == 1:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                        self.firsttube.pop()
                                    else:
                                        self.firstcheck.pop()
                                        self.firsttube.pop()
                                elif countofcolor != 0:
                                    countofcolor = 0
                                    for i in self.fourthcheck:
                                        if i != self.firstcheck[len(self.firstcheck) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        self.fourthcheck.append(
                                            self.firstcheck[len(self.firstcheck) - 1])
                                        previous = eval(
                                            self.fourthtube[len(self.fourthtube) - 1])
                                        self.fourthtube.append(
                                            f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(self.firstcheck) == 1:
                                            self.firstcheck.pop()
                                            self.firsttube.pop()
                                            self.firsttube.pop()
                                        else:
                                            self.firstcheck.pop()
                                            self.firsttube.pop()
                                    else:
                                        if self.secondcheck[len(self.secondcheck) - 1] == self.firstcheck[len(self.firstcheck) - 1]:
                                            self.secondcheck.append(
                                                self.firstcheck[len(self.firstcheck) - 1])
                                            previous = eval(
                                                self.secondtube[len(self.secondtube) - 1])
                                            self.secondtube.append(
                                                f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(self.firstcheck) == 1:
                                                self.firstcheck.pop()
                                                self.firsttube.pop()
                                                self.firsttube.pop()
                                            else:
                                                self.firstcheck.pop()
                                                self.firsttube.pop()
        elif len(self.firstcheck) < len(self.secondcheck) and len(self.firstcheck) != 0:
            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.fourthcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4=1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                else:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                else:
                    append4 = 1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                elif countofcolor!=0:
                    countofcolor = 0
                    for i in self.fourthcheck:
                        if i != self.firstcheck[len(self.firstcheck) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(self.firstcheck) == 1:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                            self.firsttube.pop()
                        else:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                    elif countofcolor!=0:
                        countofcolor = 0
                        for i in self.secondcheck:
                            if i != self.firstcheck[len(self.firstcheck) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            self.secondcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                            previous = eval(self.secondtube[len(self.secondtube) - 1])
                            self.secondtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.firstcheck) == 1:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                                self.firsttube.pop()
                            else:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                        elif self.firstcheck[len(self.firstcheck)-1]==self.secondcheck[len(self.secondcheck)-1] and self.secondcheck[len(self.secondcheck) - 2] == self.firstcheck[len(self.firstcheck) - 1] :
                            self.secondcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                            previous = eval(self.secondtube[len(self.secondtube) - 1])
                            self.secondtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.firstcheck) == 1:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                                self.firsttube.pop()
                            else:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                        else:
                            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                                countofcolor = 0
                                for i in self.fourthcheck:
                                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append4=1
                                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                else:
                                    append3 = 1
                                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                                countofcolor = 0
                                for i in self.thirdcheck:
                                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                else:
                                    append4 = 1
                                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                                randomnumber = random.randint(0, 1)
                                if randomnumber == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                if randomnumber == 1:
                                    append4 = 1
                                    self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                                countofcolor = 0
                                for i in self.thirdcheck:
                                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                                        countofcolor += 1
                                if countofcolor == 0:
                                    append3 = 1
                                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                    if len(self.secondcheck) == 1:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                        self.secondtube.pop()
                                    else:
                                        self.secondcheck.pop()
                                        self.secondtube.pop()
                                elif countofcolor!=0:
                                    countofcolor = 0
                                    for i in self.fourthcheck:
                                        if i != self.secondcheck[len(self.secondcheck) - 1]:
                                            countofcolor += 1
                                    if countofcolor == 0:
                                        append4 = 1
                                        self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                        if len(self.secondcheck) == 1:
                                            self.secondcheck.pop()
                                            self.secondtube.pop()
                                            self.secondtube.pop()
                                        else:
                                            self.secondcheck.pop()
                                            self.secondtube.pop()
                                    else:
                                        if self.secondcheck[len(self.secondcheck) - 1] == self.firstcheck[len(self.firstcheck) - 1]:
                                            self.firstcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                            previous = eval(self.firsttube[len(self.firsttube) - 1])
                                            self.firsttube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                            if len(self.secondcheck) == 1:
                                                self.secondcheck.pop()
                                                self.secondtube.pop()
                                                self.secondtube.pop()
                                            else:
                                                self.secondcheck.pop()
                                                self.secondtube.pop()
        elif len(self.firstcheck)==len(self.secondcheck):
            randomnumber=random.randint(0,1)
            if randomnumber==0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.fourthcheck:
                        if i != self.firstcheck[len(self.firstcheck) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(self.firstcheck) == 1:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                            self.firsttube.pop()
                        else:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                    else:
                        countofcolor = 0
                        for i in self.thirdcheck:
                            if i != self.secondcheck[len(self.secondcheck) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                            previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                            self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.secondcheck) == 1:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                                self.secondtube.pop()
                            else:
                                self.secondcheck.pop()
                                self.secondtube.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in self.fourthcheck:
                                if i != self.secondcheck[len(self.secondcheck) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(self.secondcheck) == 1:
                                    self.secondcheck.pop()
                                    self.secondtube.pop()
                                    self.secondtube.pop()
                                else:
                                    self.secondcheck.pop()
                                    self.secondtube.pop()
                            else:
                                self.firstcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                                previous = eval(self.firsttube[len(self.firsttube) - 1])
                                self.firsttube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(self.secondcheck) == 1:
                                    self.secondcheck.pop()
                                    self.secondtube.pop()
                                    self.secondtube.pop()
                                else:
                                    self.secondcheck.pop()
                                    self.secondtube.pop()
            elif randomnumber==1:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.fourthcheck:
                        if i != self.secondcheck[len(self.secondcheck) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fourthcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(self.secondcheck) == 1:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                            self.secondtube.pop()
                        else:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                    else:
                        countofcolor = 0
                        for i in self.thirdcheck:
                            if i != self.firstcheck[len(self.firstcheck) - 1]:
                                countofcolor += 1
                        if countofcolor == 0:
                            append3 = 1
                            self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                            previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                            self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            if len(self.firstcheck) == 1:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                                self.firsttube.pop()
                            else:
                                self.firstcheck.pop()
                                self.firsttube.pop()
                        elif countofcolor != 0:
                            countofcolor = 0
                            for i in self.fourthcheck:
                                if i != self.firstcheck[len(self.firstcheck) - 1]:
                                    countofcolor += 1
                            if countofcolor == 0:
                                append4 = 1
                                self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                                self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(self.firstcheck) == 1:
                                    self.firstcheck.pop()
                                    self.firsttube.pop()
                                    self.firsttube.pop()
                                else:
                                    self.firstcheck.pop()
                                    self.firsttube.pop()
                            else:
                                self.secondcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                                previous = eval(self.secondtube[len(self.secondtube) - 1])
                                self.secondtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                                if len(self.firstcheck) == 1:
                                    self.firstcheck.pop()
                                    self.firsttube.pop()
                                    self.firsttube.pop()
                                else:
                                    self.firstcheck.pop()
                                    self.firsttube.pop()
        elif len(self.secondcheck)==0 and self.unique2!=1:
            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.fourthcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4=1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                else:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                else:
                    append4 = 1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.thirdtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    self.fourthtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.firstcheck[len(self.firstcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.firstcheck) == 1:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                        self.firsttube.pop()
                    else:
                        self.firstcheck.pop()
                        self.firsttube.pop()
                elif countofcolor!=0:
                    countofcolor = 0
                    for i in self.fourthcheck:
                        if i != self.firstcheck[len(self.firstcheck) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fourthcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                        previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                        self.fourthtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(self.firstcheck) == 1:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                            self.firsttube.pop()
                        else:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                    else:
                        self.secondtube.append(f'pygame.draw.circle(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",(476, 438),21)')
                        self.secondtube.append(f'pygame.draw.rect(screen,"{self.firstcheck[len(self.firstcheck) - 1]}",pygame.Rect(453.9, 415, 45, 23))')
                        self.secondcheck.append(self.firstcheck[len(self.firstcheck) - 1])
                        if len(self.firstcheck) == 1:
                            self.firstcheck.pop()
                            self.firsttube.pop()
                            self.firsttube.pop()
                        else:
                            self.firstcheck.pop()
                            self.firsttube.pop()
        elif len(self.firstcheck)==0 and self.unique1!=1:
            if len(self.thirdcheck) == 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.fourthcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append4 = 1
                    self.fourthcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.fourthtube[len(self.fourthtube) - 1])
                    self.fourthtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                else:
                    append3 = 1
                    self.thirdcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    self.thirdtube.append(
                        f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) == 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                else:
                    append4 = 1
                    self.fourthcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    self.fourthtube.append(
                        f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) == 0 and len(self.fourthcheck) == 0:
                randomnumber = random.randint(0, 1)
                if randomnumber == 0:
                    append3 = 1
                    self.thirdcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    self.thirdtube.append(
                        f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(276, 438),21)')
                    self.thirdtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(253.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                if randomnumber == 1:
                    append4 = 1
                    self.fourthcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    self.fourthtube.append(
                        f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(576, 438),21)')
                    self.fourthtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(553.9, 415, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
            elif len(self.thirdcheck) != 0 and len(self.fourthcheck) != 0:
                countofcolor = 0
                for i in self.thirdcheck:
                    if i != self.secondcheck[len(self.secondcheck) - 1]:
                        countofcolor += 1
                if countofcolor == 0:
                    append3 = 1
                    self.thirdcheck.append(
                        self.secondcheck[len(self.secondcheck) - 1])
                    previous = eval(self.thirdtube[len(self.thirdtube) - 1])
                    self.thirdtube.append(
                        f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                    if len(self.secondcheck) == 1:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                        self.secondtube.pop()
                    else:
                        self.secondcheck.pop()
                        self.secondtube.pop()
                elif countofcolor != 0:
                    countofcolor = 0
                    for i in self.fourthcheck:
                        if i != self.secondcheck[len(self.secondcheck) - 1]:
                            countofcolor += 1
                    if countofcolor == 0:
                        append4 = 1
                        self.fourthcheck.append(
                            self.secondcheck[len(self.secondcheck) - 1])
                        previous = eval(
                            self.fourthtube[len(self.fourthtube) - 1])
                        self.fourthtube.append(
                            f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        if len(self.secondcheck) == 1:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                            self.secondtube.pop()
                        else:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                    else:
                        self.firsttube.append(f'pygame.draw.circle(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",(376, 438),21)')
                        self.firsttube.append(f'pygame.draw.rect(screen,"{self.secondcheck[len(self.secondcheck) - 1]}",pygame.Rect(353.9, 415, 45, 23))')
                        self.secondcheck.append(self.secondcheck[len(self.secondcheck) - 1])
                        if len(self.secondcheck) == 1:
                            self.secondcheck.pop()
                            self.secondtube.pop()
                            self.secondtube.pop()
                        else:
                            self.secondcheck.pop()
                            self.secondtube.pop()
    def calculating(self):
        self.unique2 = 0
        self.unique1 = 0
        if len(self.secondcheck) != 0:
            self.unique1 = 1
            unique1array = []
            check1 = self.secondcheck[len(self.secondcheck) - 1]
            for i in self.secondcheck:
                if check1 != i and i not in unique1array:
                    self.unique1 += 1
                    unique1array.append(i)
        if len(self.firstcheck) != 0:
            self.unique2 = 1
            unique2array = []
            check2 = self.firstcheck[len(self.firstcheck) - 1]
            for i in self.firstcheck:
                if check2 != i and i not in unique2array:
                    self.unique2 += 1
                    unique2array.append(i)
        if len(self.thirdcheck) != 0:
            self.unique5 = 1
            unique5array = []
            check5 = self.thirdcheck[len(self.thirdcheck) - 1]
            for i in self.thirdcheck:
                if check5 != i and i not in unique5array:
                    self.unique5 += 1
                    unique5array.append(i)
        if len(self.fourthcheck) != 0:
            self.unique6 = 1
            unique6array = []
            check6 = self.fourthcheck[len(self.fourthcheck) - 1]
            for i in self.fourthcheck:
                if check6 != i and i not in unique6array:
                    self.unique6 += 1
                    unique6array.append(i)


# Variables
unique1=1
unique2=1
unique3=1
unique4=1
unique5=0
unique6=0
exceedingcolorcountlimit=0
a=1
countofreds=0
countofyellows=0
countofblues=0
countoforanges=0
countofgreens=0
countofpurples=0
countofpinks=0
countofbrowns=0
countofblacks=0
countofgreys=0
countofwhites=0
countofbeiges=0
mode=0
count=0
easytubecheck3=[]
easytubecheck4=[]
easytubecheck2=[]
exceeding=0
cursor_color='White'
coloreasy1='red'
easytubecheck1=[]
easytubecheck5=[]
easytubecheck6=[]
gameover=0
easytube1=[]
easytube2=[]
easytube3=[]
easytube4=[]
easytube5=[]
easytube6=[]
redcolor='black'
yellowcolor='black'
bluecolor='white'
orangecolor='black'
greencolor='black'
purplecolor='black'
pinkcolor='black'
browncolor='white'
blackcolor='white'
greycolor='black'
whitecolor='black'
beigecolor='black'
gamemode=0
tube1firstpos='376'
tube1secondpos='353.9'
tube2firstpos='476'
tube2secondpos='453.9'
tube3firstpos='576'
tube3secondpos='553.9'
tube4firstpos='676'
tube4secondpos='653.9'
constraint=0




# Easy Mode Page
colorlist = pygame.image.load('user color.png')
tube = pygame.image.load('water_tube__1_-removebg-preview.png')
background1=pygame.image.load('background.jpg')
selecttextt = pygame.font.Font(None, 32)
rules = pygame.font.Font(None, 25)
text5 = selecttextt.render('Rules Of Easy Mode', False, 'Red')
text6 = rules.render('- User May Enter Only 3 Distinct Colors', False, 'Red')
text7 = rules.render('- User Must Not Input More Than 10 Colors From the 3 Distinct Colors', False, 'Red')
text8 = rules.render('- List Of Colors For Your Reference :', False, 'Red')
tubefull=rules.render('Tubes are Full Now!!!',False,'red')
notfollowingconstraint=selecttextt.render('Violating Constraint!!!', False, 'Red')
gameended=selecttextt.render('Sorted Game Over!!!', False, 'Red')
starteasy=pygame.font.Font(None,23)
playeasy=starteasy.render('Start',True,'red')
color=pygame.font.Font(None,18)
red=color.render('RED',True,redcolor,(255,51,51))
yellow=color.render('YELLOW',True,yellowcolor,'yellow')
blue=color.render('BLUE',True,bluecolor,(0,76,153))
orange=color.render('ORANGE',True,orangecolor,(255,153,51))
green=color.render('GREEN',True,greencolor,(102,204,0))
purple=color.render('PURPLE',True,purplecolor,(204,153,255))
pink=color.render('PINK',True,pinkcolor,(255,204,255))
brown=color.render('BROWN',True,browncolor,(102,0,0))
black=color.render('BLACK',True,blackcolor,(32,32,32))
grey=color.render('GREY',True,greycolor,(160,160,160))
white=color.render('WHITE',True,whitecolor,'white')
beige=color.render('BEIGE',True,beigecolor,(255,204,153))
watermusic=pygame.mixer.Sound('Mountain-stream-sounds.wav')

# Hard Mode Page
text13=rules.render('- Atleast One Tube Must Be Unique', False, 'Red')
text10 = selecttextt.render('Rules Of Hard Mode', False, 'Red')
text11 = rules.render('- User May Enter Only 4 Distinct Colors', False, 'Red')
text12 = rules.render('- User Must Not Input More Than 12 Colors From the 4 Distinct Colors', False, 'Red')

# Screen
screen=pygame.display.set_mode((900, 600))
pygame.display.set_caption('Water Color Sorter')
icon=pygame.image.load('sorter icon.png')
pygame.display.set_icon(icon)

# HomePage
music = pygame.mixer.Sound('Autumn-lullaby.wav')
music.play(-1)
music.set_volume(0.7)
selecttext1=pygame.font.Font(None,27)
selecttext=pygame.font.Font(None,23)
home=selecttext.render('Home',True,'red')
text2=selecttext1.render('Select Level Of Difficulty',True,'Red')
text3=selecttext.render('  Easy  ',True,coloreasy1)
text4=selecttext.render('  Hard  ',True,coloreasy1)
background=pygame.image.load('water.png')
button=pygame.image.load('Buttons image (2).png')


while True:
    x=pygame.event.get()
    mouse=pygame.mouse.get_pos()
    # print(x)
    # print(mouse)

    if a==1:

        screen.blit(background, (0, 0))
        screen.blit(text2, (60, 490))
        screen.blit(button, (80, 530))
        screen.blit(button, (180, 530))
        screen.blit(text3, (80, 539))
        screen.blit(text4, (180, 539))
        pygame.display.update()
        clock.tick(30)

    if a==0:

        screen.blit(background1, (0, 0))
        screen.blit(button, (5, 5))
        screen.blit(home,(10,13))
        screen.blit(text5, (350, 50))
        screen.blit(text6, (100, 110))
        screen.blit(text7, (100, 140))
        screen.blit(text8, (100, 170))
        screen.blit(colorlist, (100, 210))
        screen.blit(tube, (350, 210))
        screen.blit(tube, (450, 210))
        screen.blit(red,(111,217))
        screen.blit(yellow,(111,241))
        screen.blit(blue,(111,265))
        screen.blit(orange, (111, 289))
        screen.blit(green, (111, 313))
        screen.blit(purple, (111, 337))
        screen.blit(pink, (111, 361))
        screen.blit(brown, (111, 385))
        screen.blit(black, (111, 409))
        screen.blit(grey, (111, 433))
        screen.blit(white, (111, 457))
        screen.blit(beige, (111, 481))

        if len(easytubecheck2) == 4 and count == 2:
            text9 = rules.render('  You are missing another unique color!!! ', False, 'Red')
            screen.blit(text9, (450, 190))
        if exceeding==1:
            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
            screen.blit(text9,(450,190))
        if exceedingcolorcountlimit==1:
            text9 = rules.render('  You must have 5 colors of a color!!! ', False, 'Red')
            screen.blit(text9, (450, 190))
        if len(easytube1)>0:
            for i in range(len(easytube1)):
                if i == 0:
                    eval(easytube1[1])
                    eval(easytube1[0])
                elif i==1:
                    continue
                else:
                    eval(easytube1[i])
        if len(easytube2)>0:
            for i in range(len(easytube2)):
                if i == 0:
                    eval(easytube2[1])
                    eval(easytube2[0])
                elif i==1:
                    continue
                else:
                    eval(easytube2[i])

        if len(easytubecheck1)==5 and len(easytubecheck2)==5:
            exceedingcolorcountlimit=0
            screen.blit(tubefull, (320, 523))
            screen.blit(button, (520, 518))
            screen.blit(playeasy,(526,525))

        pygame.display.update()
        clock.tick(30)
    if a==2:
        screen.blit(background1, (0, 0))
        screen.blit(button, (5, 5))
        screen.blit(home, (10, 13))
        screen.blit(text10, (350, 40))
        screen.blit(text13, (100, 80))
        screen.blit(text11, (100, 110))
        screen.blit(text12, (100, 140))
        screen.blit(text8, (100, 170))
        screen.blit(colorlist, (100, 210))
        screen.blit(tube, (350, 210))
        screen.blit(tube, (450, 210))
        screen.blit(tube, (550, 210))
        screen.blit(tube, (650, 210))
        screen.blit(red, (111, 217))
        screen.blit(yellow, (111, 241))
        screen.blit(blue, (111, 265))
        screen.blit(orange, (111, 289))
        screen.blit(green, (111, 313))
        screen.blit(purple, (111, 337))
        screen.blit(pink, (111, 361))
        screen.blit(brown, (111, 385))
        screen.blit(black, (111, 409))
        screen.blit(grey, (111, 433))
        screen.blit(white, (111, 457))
        screen.blit(beige, (111, 481))
        if len(easytubecheck4) == 2 and count == 2:
            text9 = rules.render('  You are missing another unique color!!! ', False, 'Red')
            screen.blit(text9, (450, 190))
        if len(easytubecheck4) == 3 and count == 3:
            text9 = rules.render('  You are missing another unique color!!! ', False, 'Red')
            screen.blit(text9, (450, 190))
        if exceedingcolorcountlimit==1:
            text9 = rules.render('  You must have 4 colors of a color!!! ', False, 'Red')
            screen.blit(text9, (450, 190))
        if exceeding==1:
            text9 = rules.render('  Only 4 Distinct Colors!!! ', False, 'Red')
            screen.blit(text9,(450,190))
        if len(easytube1)>0:
            for i in range(len(easytube1)):
                if i == 0:
                    eval(easytube1[1])
                    eval(easytube1[0])
                elif i==1:
                    continue
                else:
                    eval(easytube1[i])
        if len(easytube2)>0:
            for i in range(len(easytube2)):
                if i == 0:
                    eval(easytube2[1])
                    eval(easytube2[0])
                elif i==1:
                    continue
                else:
                    eval(easytube2[i])
        if len(easytube3)>0:
            for i in range(len(easytube3)):
                if i == 0:
                    eval(easytube3[1])
                    eval(easytube3[0])
                elif i==1:
                    continue
                else:
                    eval(easytube3[i])
        if len(easytube4)>0:
            for i in range(len(easytube4)):
                if i == 0:
                    eval(easytube4[1])
                    eval(easytube4[0])
                elif i==1:
                    continue
                else:
                    eval(easytube4[i])
        if len(easytubecheck1)==4 and len(easytubecheck2)==4 and len(easytubecheck3)==4 and len(easytubecheck4)==4:
            exceedingcolorcountlimit=0
            screen.blit(tubefull, (350, 523))
            screen.blit(button, (520, 518))
            screen.blit(playeasy, (526, 525))
        pygame.display.update()
        clock.tick(30)
    if a==3:
        screen.blit(background1, (0, 0))
        if mode==0:
            watermusic.stop()
            music.set_volume(0.7)
            if gamemode==0 or gamemode==1 or gamemode==2:
                screen.blit(tube, (250, 210))
                screen.blit(tube, (350, 210))
                screen.blit(tube, (450, 210))
                screen.blit(tube, (550, 210))
                if len(easy.firsttube) > 0:
                    for i in range(len(easy.firsttube)):
                        if i == 0:
                            eval(easy.firsttube[1])
                            eval(easy.firsttube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(easy.firsttube[i])
                if len(easy.secondtube) > 0:
                    for i in range(len(easy.secondtube)):
                        if i == 0:
                            eval(easy.secondtube[1])
                            eval(easy.secondtube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(easy.secondtube[i])
                if len(easy.thirdtube) > 0:
                    for i in range(len(easy.thirdtube)):
                        if i == 0:
                            eval(easy.thirdtube[1])
                            eval(easy.thirdtube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(easy.thirdtube[i])
                if len(easy.fourthtube) > 0:
                    for i in range(len(easy.fourthtube)):
                        if i == 0:
                            eval(easy.fourthtube[1])
                            eval(easy.fourthtube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(easy.fourthtube[i])
            if gamemode==3 or gamemode==4 or gamemode==5 or gamemode==6 or gamemode==7 or gamemode==8 or gamemode==9 or gamemode==10 or gamemode==11 or gamemode==12 or gamemode==13 or gamemode==14:
                screen.blit(tube, (150, 210))
                screen.blit(tube, (250, 210))
                screen.blit(tube, (350, 210))
                screen.blit(tube, (450, 210))
                screen.blit(tube, (550, 210))
                screen.blit(tube, (650, 210))
                if len(hard.firsttube) > 0:
                    for i in range(len(hard.firsttube)):
                        if i == 0:
                            eval(hard.firsttube[1])
                            eval(hard.firsttube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(hard.firsttube[i])
                if len(hard.secondtube) > 0:
                    for i in range(len(hard.secondtube)):
                        if i == 0:
                            eval(hard.secondtube[1])
                            eval(hard.secondtube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(hard.secondtube[i])
                if len(hard.thirdtube) > 0:
                    for i in range(len(hard.thirdtube)):
                        if i == 0:
                            eval(hard.thirdtube[1])
                            eval(hard.thirdtube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(hard.thirdtube[i])
                if len(hard.fourthtube) > 0:
                    for i in range(len(hard.fourthtube)):
                        if i == 0:
                            eval(hard.fourthtube[1])
                            eval(hard.fourthtube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(hard.fourthtube[i])
                if len(hard.fifthtube) > 0:
                    for i in range(len(hard.fifthtube)):
                        if i == 0:
                            eval(hard.fifthtube[1])
                            eval(hard.fifthtube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(hard.fifthtube[i])
                if len(hard.sixthtube) > 0:
                    for i in range(len(hard.sixthtube)):
                        if i == 0:
                            eval(hard.sixthtube[1])
                            eval(hard.sixthtube[0])
                        elif i == 1:
                            continue
                        else:
                            eval(hard.sixthtube[i])
            if gameover==0:
                mode += 1
                pygame.display.update()
                clock.tick(1)
            else:
                if constraint==1:
                    screen.blit(notfollowingconstraint, (350, 50))
                    screen.blit(button, (5, 5))
                    screen.blit(home, (10, 13))
                    mode=0
                    pygame.display.update()
                    clock.tick(30)
                else:
                    screen.blit(gameended, (350, 50))
                    screen.blit(button, (5, 5))
                    screen.blit(home, (10, 13))
                    mode=0
                    pygame.display.update()
                    clock.tick(30)
        elif mode==1:
            if gamemode == 0 or gamemode == 1 or gamemode == 2:
                if ((easy.unique1 == 1 and easy.unique2 == 0 and easy.unique5 == 1 and easy.unique6 == 1) or (easy.unique1 == 0 and easy.unique2 == 1 and easy.unique5 == 1 and easy.unique6 == 1) or (easy.unique1 == 1 and easy.unique2 == 1 and easy.unique5 == 0 and easy.unique6 == 1) or (easy.unique1 == 1 and easy.unique2 == 1 and easy.unique5 == 1 and easy.unique6 == 0)):
                    gameover = 1
            if gamemode==3 or gamemode==4 or gamemode==6 or gamemode==5 or gamemode==7 or gamemode==8 or gamemode==9 or gamemode==11 or gamemode==12 or gamemode==13 or gamemode==10 or gamemode==14:
                if ((hard.unique1==1 and len(hard.secondcheck)==4) and (hard.unique2==1 and len(hard.firstcheck)==4) and (hard.unique3==0 and len(hard.thirdcheck)==0) and (hard.unique4==0 and len(hard.fourthcheck)==0) and (hard.unique5==1 and len(hard.fifthcheck)==4) and (hard.unique6==1 and len(hard.sixthcheck)==4)) or ((hard.unique1==0 and len(hard.secondcheck)==0) and (hard.unique2==0 and len(hard.firstcheck)==0) and (len(hard.thirdcheck)==4 and hard.unique3==1) and (len(hard.fourthcheck)==4 and hard.unique4==1) and (len(hard.fifthcheck)==4 and hard.unique5==1) and (len(hard.sixthcheck)==4 and hard.unique6==1)) or ((hard.unique1==1 and len(hard.secondcheck)==4) and (hard.unique2==0 and len(hard.firstcheck)==0) and (len(hard.fourthcheck)==0 and hard.unique4==0) and (len(hard.thirdcheck)==4 and hard.unique3==1) and (len(hard.fifthcheck)==4 and hard.unique5==1) and (len(hard.sixthcheck)==4 and hard.unique6==1)) or ((hard.unique1==1 and len(hard.secondcheck)==4) and (hard.unique2==0 and len(hard.firstcheck)==0) and (len(hard.fourthcheck)==4 and hard.unique4==1) and (len(hard.thirdcheck)==0 and hard.unique3==0) and (len(hard.fifthcheck)==4 and hard.unique5==1) and (len(hard.sixthcheck)==4 and hard.unique6==1)) or ((hard.unique1==0 and len(hard.secondcheck)==0) and (hard.unique2==1 and len(hard.firstcheck)==4) and (len(hard.fourthcheck)==0 and hard.unique4==0) and (len(hard.thirdcheck)==4 and hard.unique3==1) and (len(hard.fifthcheck)==4 and hard.unique5==1) and (len(hard.sixthcheck)==4 and hard.unique6==1)) or ((hard.unique1==0 and len(hard.secondcheck)==0) and (hard.unique2==1 and len(hard.firstcheck)==4) and (len(hard.fourthcheck)==4 and hard.unique4==1) and (len(hard.thirdcheck)==0 and hard.unique3==0) and (len(hard.fifthcheck)==4 and hard.unique5==1) and (len(hard.sixthcheck)==4 and hard.unique6==1)):
                    gameover = 1
            if gameover==0:
                if gamemode==0:
                    # print('first unique and second not unique')
                    easy.firstunique_secondnotunique()
                    easy.calculating()
                    mode=0
                elif gamemode==1:
                    # print('second unique and first not unique')
                    easy.firstnotunique_secondunique()
                    easy.calculating()
                    mode=0
                elif gamemode==2:
                    easy.both_not_unique()
                    easy.calculating()
                    mode=0
                    # print('first not unique and second not unique')
                elif gamemode==3:
                    hard.twounique_twonotunique(hard.thirdcheck,hard.thirdtube,hard.fourthcheck,hard.fourthtube,hard.unique3,hard.unique4)
                    hard.calculating()
                    mode=0
                elif gamemode==4:
                    hard.twounique_twonotunique(hard.firstcheck,hard.firsttube,hard.secondcheck,hard.secondtube,hard.unique2,hard.unique1)
                    hard.calculating()
                    mode=0
                elif gamemode==5:
                    hard.twounique_twonotunique(hard.firstcheck,hard.firsttube,hard.fourthcheck,hard.fourthtube,hard.unique2,hard.unique4)
                    hard.calculating()
                    mode=0
                elif gamemode==6:
                    hard.twounique_twonotunique(hard.firstcheck,hard.firsttube,hard.thirdcheck,hard.thirdtube,hard.unique2,hard.unique3)
                    hard.calculating()
                    mode=0
                elif gamemode==7:
                    hard.twounique_twonotunique(hard.secondcheck,hard.secondtube,hard.thirdcheck,hard.thirdtube,hard.unique1,hard.unique3)
                    hard.calculating()
                    mode=0
                elif gamemode==8:
                    hard.twounique_twonotunique(hard.secondcheck,hard.secondtube,hard.fourthcheck,hard.fourthtube,hard.unique1,hard.unique4)
                    hard.calculating()
                    mode=0
                elif gamemode==9:
                    hard.three_not_unique(hard.thirdcheck,hard.thirdtube,hard.fourthcheck,hard.fourthtube,hard.secondcheck,hard.secondtube,hard.unique3,hard.unique4,hard.unique1,tube3firstpos,tube3secondpos,tube4firstpos,tube4secondpos,tube2firstpos,tube2secondpos)
                    hard.calculating()
                    mode=0
                elif gamemode==14:
                    hard.three_not_unique(hard.firstcheck,hard.firsttube,hard.secondcheck,hard.secondtube,hard.thirdcheck,hard.thirdtube,hard.unique2,hard.unique1,hard.unique3,tube1firstpos,tube1secondpos,tube2firstpos,tube2secondpos,tube3firstpos,tube3secondpos)
                    hard.calculating()
                    mode=0
                elif gamemode==11:
                    hard.three_not_unique(hard.firstcheck,hard.firsttube,hard.thirdcheck,hard.thirdtube,hard.fourthcheck,hard.fourthtube,hard.unique2,hard.unique3,hard.unique4,tube1firstpos,tube1secondpos,tube3firstpos,tube3secondpos,tube4firstpos,tube4secondpos)
                    hard.calculating()
                    mode=0
                elif gamemode==12:
                    hard.three_not_unique(hard.firstcheck,hard.firsttube,hard.secondcheck,hard.secondtube,hard.fourthcheck,hard.fourthtube,hard.unique2,hard.unique1,hard.unique4,tube1firstpos,tube1secondpos,tube2firstpos,tube2secondpos,tube4firstpos,tube4secondpos)
                    hard.calculating()
                    mode=0
            else:
                mode=0

    for i in x:

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 213<=mouse[1]<=233 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"red",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"red",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('red')
                    count += 1
                    countofreds+=1
                else:
                    if 'red' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('red')
                        exceeding = 0
                        countofreds += 1
                    elif count <= 2:
                        if 'red' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('red')
                        count += 1
                        countofreds += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'red' in easytubecheck1 and countofreds<5:
                        easytube2.append(f'pygame.draw.circle(screen,"red",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"red",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('red')
                        countofreds += 1
                        exceeding=0
                        exceedingcolorcountlimit = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofreds<5:
                        easytube2.append(f'pygame.draw.circle(screen,"red",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"red",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('red')
                        count+=1
                        countofreds += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('red' in easytubecheck2 or 'red' in easytubecheck1):
                            pass
                        elif ('red' in easytubecheck1 or 'red' in easytubecheck2) and countofreds<5:
                            if 'red' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('red')
                            exceeding = 0
                            countofreds += 1
                            exceedingcolorcountlimit = 0

                        elif count <= 2 and countofreds<5:
                            if 'red' not in easytubecheck2:
                                unique2 += 1
                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('red')
                            count += 1
                            countofreds += 1
                            exceedingcolorcountlimit = 0
                        elif countofreds == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofreds==5:
                            exceedingcolorcountlimit=1

                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))


        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 213<=mouse[1]<=233:
            redcolor='green'
            red=color.render('RED',True,redcolor,(255,51,51))
        else:
            redcolor='black'
            red = color.render('RED', True, redcolor, (255, 51, 51))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 237<=mouse[1]<=257:
            yellowcolor='green'
            yellow=color.render('YELLOW',True,yellowcolor,'yellow')
        else:
            yellowcolor='black'
            yellow=color.render('YELLOW',True,yellowcolor,'yellow')
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 261<=mouse[1]<=281:
            bluecolor='green'
            blue=color.render('BLUE',True,bluecolor,(0,76,153))
        else:
            bluecolor='white'
            blue=color.render('BLUE',True,bluecolor,(0,76,153))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 285<=mouse[1]<=305:
            orangecolor='green'
            orange=color.render('ORANGE',True,orangecolor,(255,153,51))
        else:
            orangecolor='black'
            orange=color.render('ORANGE',True,orangecolor,(255,153,51))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 309<=mouse[1]<=329:
            greencolor='green'
            green=color.render('GREEN',True,greencolor,(102,204,0))
        else:
            greencolor='black'
            green=color.render('GREEN',True,greencolor,(102,204,0))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 333<=mouse[1]<=353:
            purplecolor='green'
            purple = color.render('PURPLE', True, purplecolor, (204, 153, 255))
        else:
            purplecolor='black'
            purple=color.render('PURPLE',True,purplecolor,(204,153,255))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 357<=mouse[1]<=377:
            pinkcolor='green'
            pink=color.render('PINK',True,pinkcolor,(255,204,255))
        else:
            pinkcolor='black'
            pink = color.render('PINK', True, pinkcolor, (255, 204, 255))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 381<=mouse[1]<=401:
            browncolor='green'
            brown=color.render('BROWN',True,browncolor,(102,0,0))
        else:
            browncolor='white'
            brown=color.render('BROWN',True,browncolor,(102,0,0))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 405<=mouse[1]<=425:
            blackcolor='green'
            black=color.render('BLACK',True,blackcolor,(32,32,32))
        else:
            blackcolor='white'
            black=color.render('BLACK',True,blackcolor,(32,32,32))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 429<=mouse[1]<=449:
            greycolor='green'
            grey=color.render('GREY',True,greycolor,(160,160,160))
        else:
            greycolor='black'
            grey=color.render('GREY',True,greycolor,(160,160,160))
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 453<=mouse[1]<=473:
            whitecolor='green'
            white = color.render('WHITE', True, whitecolor, 'white')
        else:
            whitecolor='black'
            white=color.render('WHITE',True,whitecolor,'white')
        if i.type==pygame.MOUSEMOTION and 102<=mouse[0]<=251 and 477<=mouse[1]<=497:
            beigecolor='green'
            beige=color.render('BEIGE',True,beigecolor,(255,204,153))
        else:
            beigecolor='black'
            beige=color.render('BEIGE',True,beigecolor,(255,204,153))




        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 237<=mouse[1]<=257 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"yellow",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('yellow')
                    count+=1
                    countofyellows += 1
                else:
                    if 'yellow' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('yellow')
                        exceeding = 0
                        countofyellows += 1
                        exceedingcolorcountlimit = 0
                    elif count<=2:
                        if 'yellow' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('yellow')
                        count+=1
                        countofyellows += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            else:
                if len(easytubecheck2) != 5:
                    if len(easytube2) == 0 and 'yellow' in easytubecheck1 and countofyellows<5:
                        easytube2.append(f'pygame.draw.circle(screen,"yellow",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('yellow')
                        exceedingcolorcountlimit=0
                        countofyellows+=1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofyellows<5:
                        easytube2.append(f'pygame.draw.circle(screen,"yellow",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('yellow')
                        count+=1
                        countofyellows += 1
                        exceedingcolorcountlimit=0
                    else:

                        if len(easytubecheck2) == 4 and count == 2 and ('yellow' in easytubecheck2 or 'yellow' in easytubecheck1):
                            pass
                        elif ('yellow' in easytubecheck2 or 'yellow' in easytubecheck1) and countofyellows<5:
                            if 'yellow' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('yellow')
                            exceeding = 0
                            countofyellows += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 2 and countofyellows<5:
                            if 'yellow' not in easytubecheck2:
                                unique2 += 1
                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('yellow')
                            count += 1
                            countofyellows += 1
                            exceedingcolorcountlimit = 0
                        elif countofyellows == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofyellows==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 261<=mouse[1]<=281 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"blue",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('blue')
                    count += 1
                    countofblues += 1
                else:
                    if 'blue' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('blue')
                        exceeding = 0
                        countofblues += 1

                    elif count <= 2:
                        if 'blue' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('blue')
                        count += 1
                        countofblues += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'blue' in easytubecheck1 and countofblues<5:
                        easytube2.append(f'pygame.draw.circle(screen,"blue",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('blue')
                        exceedingcolorcountlimit=0
                        countofblues+=1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofblues<5:
                        easytube2.append(f'pygame.draw.circle(screen,"blue",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('blue')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofblues += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('blue' in easytubecheck2 or 'blue' in easytubecheck1):
                            pass
                        elif ('blue' in easytubecheck2 or 'blue' in easytubecheck1) and countofblues<5:
                            if 'blue' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('blue')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofblues += 1
                        elif count <= 2 and countofblues<5:
                            if 'blue' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('blue')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofblues += 1

                        elif countofblues == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofblues==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 285<=mouse[1]<=305 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"orange",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('orange')
                    count += 1
                    countoforanges += 1
                else:
                    if 'orange' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('orange')
                        exceeding = 0
                        countoforanges += 1

                    elif count <= 2:
                        if 'orange' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('orange')
                        count += 1
                        countoforanges += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'orange' in easytubecheck1 and countoforanges<5:
                        easytube2.append(f'pygame.draw.circle(screen,"orange",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('orange')
                        exceedingcolorcountlimit = 0
                        countoforanges += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countoforanges<5:
                        easytube2.append(f'pygame.draw.circle(screen,"orange",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('orange')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countoforanges += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('orange' in easytubecheck2 or 'orange' in easytubecheck1):
                            pass
                        elif ('orange' in easytubecheck1 or 'orange' in easytubecheck2) and countoforanges<5:
                            if 'orange' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('orange')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countoforanges += 1
                        elif count <= 2 and countoforanges<5:
                            if 'orange' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('orange')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countoforanges += 1
                        elif countoforanges == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countoforanges==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 309<=mouse[1]<=329 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"green",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"green",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('green')
                    count += 1
                    countofgreens += 1
                else:
                    if 'green' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('green')
                        exceeding = 0
                        countofgreens += 1
                    elif count <= 2:
                        if 'green' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('green')
                        count += 1
                        countofgreens += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'green' in easytubecheck1 and countofgreens<5:
                        easytube2.append(f'pygame.draw.circle(screen,"green",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"green",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('green')
                        exceedingcolorcountlimit = 0
                        countofgreens += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofgreens<5:
                        easytube2.append(f'pygame.draw.circle(screen,"green",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"green",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('green')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofgreens += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('green' in easytubecheck2 or 'green' in easytubecheck1):
                            pass
                        elif ('green' in easytubecheck1 or 'green' in easytubecheck2) and countofgreens<5 :
                            if 'green' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('green')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofgreens += 1
                        elif count <= 2 and countofgreens<5:
                            if 'green' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('green')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofgreens += 1
                        elif countofgreens == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofgreens==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 333<=mouse[1]<=353 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"purple",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('purple')
                    count += 1
                    countofpurples += 1
                else:
                    if 'purple' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('purple')
                        exceeding = 0
                        countofpurples += 1
                    elif count <= 2:
                        if 'purple' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('purple')
                        count += 1
                        countofpurples += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'purple' in easytubecheck1 and countofpurples<5:
                        easytube2.append(f'pygame.draw.circle(screen,"purple",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('purple')
                        exceedingcolorcountlimit = 0
                        countofpurples += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofpurples<5:
                        easytube2.append(f'pygame.draw.circle(screen,"purple",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('purple')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofpurples += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('purple' in easytubecheck2 or 'purple' in easytubecheck1):
                            pass
                        elif ('purple' in easytubecheck1 or 'purple' in easytubecheck2) and countofpurples<5:
                            if 'purple' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('purple')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofpurples += 1
                        elif count <= 2 and countofpurples<5:
                            if 'purple' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('purple')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofpurples += 1
                        elif countofpurples == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofpurples==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 357<=mouse[1]<=377 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"pink",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('pink')
                    count += 1
                    countofpinks += 1
                else:
                    if 'pink' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('pink')
                        exceeding = 0
                        countofpinks += 1
                    elif count <= 2:
                        if 'pink' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('pink')
                        count += 1
                        countofpinks += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'pink' in easytubecheck1 and countofpinks<5:
                        easytube2.append(f'pygame.draw.circle(screen,"pink",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('pink')
                        exceedingcolorcountlimit = 0
                        countofpinks += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofpinks<5:
                        easytube2.append(f'pygame.draw.circle(screen,"pink",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('pink')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofpinks += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('pink' in easytubecheck2 or 'pink' in easytubecheck1):
                            pass
                        elif ('pink' in easytubecheck1 or 'pink' in easytubecheck2) and countofpinks<5:
                            if 'pink' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('pink')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofpinks += 1
                        elif count <= 2 and countofpinks<5:
                            if 'pink' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('pink')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofpinks += 1
                        elif countofpinks == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofpinks==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))
        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 381<=mouse[1]<=401 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"brown",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('brown')
                    count += 1
                    countofbrowns += 1
                else:
                    if 'brown' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                        f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('brown')
                        exceeding = 0
                        countofbrowns += 1
                    elif count <= 2:
                        if 'brown' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('brown')
                        count += 1
                        countofbrowns += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'brown' in easytubecheck1 and countofbrowns<5:
                        easytube2.append(f'pygame.draw.circle(screen,"brown",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('brown')
                        exceedingcolorcountlimit = 0
                        countofbrowns += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofbrowns<5:
                        easytube2.append(f'pygame.draw.circle(screen,"brown",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('brown')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofbrowns += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('brown' in easytubecheck2 or 'brown' in easytubecheck1):
                            pass
                        elif ('brown' in easytubecheck1 or 'brown' in easytubecheck2) and countofbrowns<5:
                            if 'brown' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('brown')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofbrowns += 1
                        elif count <= 2 and countofbrowns<5:
                            if 'brown' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('brown')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofbrowns += 1
                        elif countofbrowns == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofbrowns==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 405<=mouse[1]<=425 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"black",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"black",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('black')
                    count += 1
                    countofblacks += 1
                else:
                    if 'black' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('black')
                        exceeding = 0
                        countofblacks += 1
                    elif count <= 2:
                        if 'black' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('black')
                        count += 1
                        countofblacks += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'black' in easytubecheck1 and countofblacks<5:
                        easytube2.append(f'pygame.draw.circle(screen,"black",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"black",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('black')
                        exceedingcolorcountlimit = 0
                        countofblacks += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofblacks<5:
                        easytube2.append(f'pygame.draw.circle(screen,"black",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"black",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('black')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofblacks += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('black' in easytubecheck2 or 'black' in easytubecheck1):
                            pass
                        elif ('black' in easytubecheck1 or 'black' in easytubecheck2) and countofblacks<5:
                            if 'black' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('black')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofblacks += 1
                        elif count <= 2 and countofblacks<5:
                            if 'black' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('black')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofblacks += 1
                        elif countofblacks == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofblacks==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))
        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 429<=mouse[1]<=449 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"grey",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('grey')
                    count += 1
                    countofgreys += 1
                else:
                    if 'grey' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('grey')
                        exceeding = 0
                        countofgreys += 1
                    elif count <= 2:
                        if 'grey' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('grey')
                        count += 1
                        countofgreys += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'grey' in easytubecheck1 and countofgreys<5:
                        easytube2.append(f'pygame.draw.circle(screen,"grey",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('grey')
                        exceedingcolorcountlimit = 0
                        countofgreys += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofgreys<5:
                        easytube2.append(f'pygame.draw.circle(screen,"grey",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('grey')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofgreys += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('grey' in easytubecheck2 or 'grey' in easytubecheck1):
                            pass
                        elif ('grey' in easytubecheck1 or 'grey' in easytubecheck2) and countofgreys<5:
                            if 'grey' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('grey')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofgreys += 1
                        elif count <= 2 and countofgreys<5:
                            if 'grey' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('grey')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofgreys += 1
                        elif countofgreys == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofgreys==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))
        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 453<=mouse[1]<=473 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"white",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"white",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('white')
                    count += 1
                    countofwhites += 1
                else:
                    if 'white' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('white')
                        exceeding = 0
                        countofwhites += 1
                    elif count <= 2:
                        if 'white' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('white')
                        count += 1
                        countofwhites += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'white' in easytubecheck1 and countofwhites<5:
                        easytube2.append(f'pygame.draw.circle(screen,"white",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"white",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('white')
                        exceedingcolorcountlimit = 0
                        countofwhites += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofwhites<5:
                        easytube2.append(f'pygame.draw.circle(screen,"white",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"white",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('white')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofwhites += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('white' in easytubecheck2 or 'white' in easytubecheck1):
                            pass
                        elif ('white' in easytubecheck1 or 'white' in easytubecheck2) and countofwhites<5:
                            if 'white' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('white')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofwhites += 1
                        elif count <= 2 and countofwhites<5:
                            if 'white' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('white')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofwhites += 1
                        elif countofwhites == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofwhites==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))
        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 477<=mouse[1]<=497 and a==0:
            if len(easytubecheck1) != 5:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"beige",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('beige')
                    count += 1
                    countofbeiges += 1

                else:
                    if 'beige' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('beige')
                        exceeding = 0
                        countofbeiges += 1
                    elif count<=2:
                        if 'beige' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('beige')
                        count+=1
                        countofbeiges += 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            else:
                if len(easytubecheck2) != 5:
                    if len(easytubecheck2) == 0 and 'beige' in easytubecheck1 and countofbeiges<5:
                        easytube2.append(f'pygame.draw.circle(screen,"beige",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('beige')
                        exceedingcolorcountlimit = 0
                        countofbeiges += 1
                        exceeding = 0
                    elif len(easytubecheck2) == 0 and count<=2 and countofbeiges<5:
                        easytube2.append(f'pygame.draw.circle(screen,"beige",(476, 438),21)')
                        easytube2.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(453.9, 415, 45, 23))')
                        easytubecheck2.append('beige')
                        count+=1
                        exceedingcolorcountlimit = 0
                        countofbeiges += 1
                    else:
                        if len(easytubecheck2) == 4 and count == 2 and ('beige' in easytubecheck2 or 'beige' in easytubecheck1):
                            pass
                        elif ('beige' in easytubecheck1 or 'beige' in easytubecheck2) and countofbeiges<5:
                            if 'beige' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('beige')
                            exceeding = 0
                            exceedingcolorcountlimit = 0
                            countofbeiges += 1
                        elif count <= 2 and countofbeiges<5:
                            if 'beige' not in easytubecheck2:
                                unique2 += 1

                            previous = eval(easytube2[len(easytube2) - 1])
                            easytube2.append(
                                f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck2.append('beige')
                            count += 1
                            exceedingcolorcountlimit = 0
                            countofbeiges += 1
                        elif countofbeiges == 5 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding=0
                        elif countofbeiges==5:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 2 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 213<=mouse[1]<=233 and a==2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"red",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"red",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('red')
                    count += 1
                    countofreds += 1
                else:
                    if 'red' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('red')
                        exceeding = 0
                        countofreds += 1

                    elif count <= 3:
                        if 'red' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(
                            f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('red')
                        count += 1
                        countofreds += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'red' in easytubecheck1 and countofreds<4:
                    easytube2.append(f'pygame.draw.circle(screen,"red",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"red",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('red')
                    countofreds += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofreds<4:
                    easytube2.append(f'pygame.draw.circle(screen,"red",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"red",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('red')
                    count += 1
                    countofreds += 1
                    exceedingcolorcountlimit = 0
                else:
                    # print('happening')
                    if ('red' in easytubecheck1 or 'red' in easytubecheck2) and countofreds<4:
                        if 'red' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('red')
                        exceeding = 0
                        countofreds += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofreds<4:
                        if 'red' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('red')
                        count += 1
                        countofreds += 1
                        exceedingcolorcountlimit = 0
                    elif countofreds == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofreds == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('red' in easytubecheck1 or 'red' in easytubecheck2) and countofreds<4:
                    easytube3.append(f'pygame.draw.circle(screen,"red",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"red",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('red')
                    countofreds += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofreds<4:
                    easytube3.append(f'pygame.draw.circle(screen,"red",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"red",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('red')
                    count += 1
                    countofreds += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('red' in easytubecheck1 or 'red' in easytubecheck2 or 'red' in easytubecheck3) and countofreds<4:
                        if 'red' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('red')
                        exceeding = 0
                        countofreds += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofreds<4:
                        if 'red' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('red')
                        count += 1
                        countofreds += 1
                        exceedingcolorcountlimit = 0
                    elif countofreds == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofreds == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('red' in easytubecheck1 or 'red' in easytubecheck2 or 'red' in easytubecheck3) and countofreds<4:
                        easytube4.append(f'pygame.draw.circle(screen,"red",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"red",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('red')
                        countofreds += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count<=3 and countofreds<4:
                        easytube4.append(f'pygame.draw.circle(screen,"red",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"red",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('red')
                        count+=1
                        countofreds += 1
                        exceedingcolorcountlimit = 0
                    else:
                        # print(count)
                        if len(easytubecheck4) == 2 and count == 2 and ('red' in easytubecheck2 or 'red' in easytubecheck1 or 'red' in easytubecheck3 or 'red' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('red' in easytubecheck2 or 'red' in easytubecheck1 or 'red' in easytubecheck3 or 'red' in easytubecheck4 ):
                            pass
                        elif ('red' in easytubecheck1 or 'red' in easytubecheck2 or 'red' in easytubecheck3 or 'red' in easytubecheck4) and countofreds<4:
                            if 'red' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('red')
                            exceeding = 0
                            countofreds += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofreds<4:
                            if 'red' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"red",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('red')
                            count += 1
                            countofreds += 1
                            exceedingcolorcountlimit = 0
                        elif countofreds == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofreds==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))
                        # print(count)

        if i.type==pygame.MOUSEBUTTONDOWN and 102<=mouse[0]<=251 and 237<=mouse[1]<=257 and a==2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"yellow",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('yellow')
                    count+=1
                    countofyellows += 1

                else:
                    if 'yellow' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('yellow')
                        exceeding = 0
                        countofyellows += 1

                    elif count<=3:
                        if 'yellow' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('yellow')
                        count+=1
                        countofyellows += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))
            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'yellow' in easytubecheck1 and countofyellows<4:
                    easytube2.append(f'pygame.draw.circle(screen,"yellow",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('yellow')
                    countofyellows += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofyellows<4:
                    easytube2.append(f'pygame.draw.circle(screen,"yellow",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('yellow')
                    count += 1
                    countofyellows += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('yellow' in easytubecheck2 or 'yellow' in easytubecheck1) and countofyellows<4:
                        if 'yellow' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('yellow')
                        exceeding = 0
                        countofyellows += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofyellows<4:
                        if 'yellow' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('yellow')
                        countofyellows += 1
                        exceedingcolorcountlimit = 0
                        count += 1
                    elif countofyellows == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofyellows == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('yellow' in easytubecheck1 or 'yellow' in easytubecheck2) and countofyellows<4:
                    easytube3.append(f'pygame.draw.circle(screen,"yellow",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('yellow')
                    countofyellows += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofyellows<4:
                    easytube3.append(f'pygame.draw.circle(screen,"yellow",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('yellow')
                    count += 1
                    countofyellows += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('yellow' in easytubecheck2 or 'yellow' in easytubecheck1 or 'yellow' in easytubecheck3) and countofyellows<4:
                        if 'yellow' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('yellow')
                        exceeding = 0
                        countofyellows += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofyellows<4:
                        if 'yellow' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('yellow')
                        count += 1
                        countofyellows += 1
                        exceedingcolorcountlimit = 0
                    elif countofyellows == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofyellows == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('yellow' in easytubecheck1 or 'yellow' in easytubecheck2 or 'yellow' in easytubecheck3) and countofyellows<4:
                        easytube4.append(f'pygame.draw.circle(screen,"yellow",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('yellow')
                        countofyellows += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofyellows<4:
                        easytube4.append(f'pygame.draw.circle(screen,"yellow",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"yellow",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('yellow')
                        count += 1
                        countofyellows += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('yellow' in easytubecheck2 or 'yellow' in easytubecheck1 or 'yellow' in easytubecheck3 or 'yellow' in easytubecheck4 ):
                            pass
                        if len(easytubecheck4) == 3 and count == 3 and ('yellow' in easytubecheck2 or 'yellow' in easytubecheck1 or 'yellow' in easytubecheck3 or 'yellow' in easytubecheck4 ):
                            pass
                        elif ('yellow' in easytubecheck1 or 'yellow' in easytubecheck2 or 'yellow' in easytubecheck3 or 'yellow' in easytubecheck4) and countofyellows<4:
                            if 'yellow' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('yellow')
                            exceeding = 0
                            countofyellows += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofyellows<4:
                            if 'yellow' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"yellow",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('yellow')
                            count += 1
                            countofyellows += 1
                            exceedingcolorcountlimit = 0
                        elif countofyellows == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofyellows==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 261 <= mouse[1] <= 281 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"blue",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('blue')
                    count+=1
                    countofblues += 1

                else:
                    if 'blue' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('blue')
                        exceeding = 0
                        countofblues += 1

                    elif count<=3:
                        if 'blue' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('blue')
                        count+=1
                        countofblues += 1
                    elif countofblues == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'blue' in easytubecheck1 and countofblues<4:
                    easytube2.append(f'pygame.draw.circle(screen,"blue",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('blue')
                    countofblues += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofblues<4:
                    easytube2.append(f'pygame.draw.circle(screen,"blue",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('blue')
                    count += 1
                    countofblues += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('blue' in easytubecheck2 or 'blue' in easytubecheck1) and countofblues<4:
                        if 'blue' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('blue')
                        exceeding = 0
                        countofblues += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofblues<4:
                        if 'blue' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('blue')
                        count += 1
                        countofblues += 1
                        exceedingcolorcountlimit = 0
                    elif countofblues == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofblues == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('blue' in easytubecheck1 or 'blue' in easytubecheck2) and countofblues<4:
                    easytube3.append(f'pygame.draw.circle(screen,"blue",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('blue')
                    countofblues += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofblues<4:
                    easytube3.append(f'pygame.draw.circle(screen,"blue",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('blue')
                    count += 1
                    countofblues += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('blue' in easytubecheck2 or 'blue' in easytubecheck1 or 'blue' in easytubecheck3) and countofblues<4:
                        if 'blue' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('blue')
                        exceeding = 0
                        countofblues += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofblues<4:
                        if 'blue' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('blue')
                        count += 1
                        countofblues += 1
                        exceedingcolorcountlimit = 0
                    elif countofblues == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofblues == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('blue' in easytubecheck1 or 'blue' in easytubecheck2 or 'blue' in easytubecheck3) and countofblues<4:
                        easytube4.append(f'pygame.draw.circle(screen,"blue",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('blue')
                        countofblues += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofblues<4:
                        easytube4.append(f'pygame.draw.circle(screen,"blue",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"blue",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('blue')
                        count += 1
                        countofblues += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('blue' in easytubecheck2 or 'blue' in easytubecheck1 or 'blue' in easytubecheck3 or 'blue' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('blue' in easytubecheck2 or 'blue' in easytubecheck1 or 'blue' in easytubecheck3 or 'blue' in easytubecheck4 ):
                            pass
                        elif ('blue' in easytubecheck1 or 'blue' in easytubecheck2 or 'blue' in easytubecheck3 or 'blue' in easytubecheck4) and countofblues<4:
                            if 'blue' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('blue')
                            exceeding = 0
                            countofblues += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofblues<4:
                            if 'blue' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"blue",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('blue')
                            countofblues += 1
                            exceedingcolorcountlimit = 0
                            count += 1
                        elif countofblues == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofblues==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 285 <= mouse[1] <= 305 and a == 2:
            if len(easytubecheck1) != 4:
                # print(count)
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"orange",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('orange')
                    count+=1
                    countoforanges += 1

                else:
                    if 'orange' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('orange')
                        exceeding = 0
                        countoforanges += 1

                    elif count<=3:
                        if 'orange' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('orange')
                        count+=1
                        countoforanges += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and ('orange' in easytubecheck1) and countoforanges<4:
                    easytube2.append(f'pygame.draw.circle(screen,"orange",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('orange')
                    countoforanges += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countoforanges<4:
                    easytube2.append(f'pygame.draw.circle(screen,"orange",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('orange')
                    count += 1
                    countoforanges += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('orange' in easytubecheck2 or 'orange' in easytubecheck1) and countoforanges<4:
                        if 'orange' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('orange')
                        exceeding = 0
                        countoforanges += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countoforanges<4:
                        if 'orange' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('orange')
                        count += 1
                        countoforanges += 1
                        exceedingcolorcountlimit = 0
                    elif countoforanges == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countoforanges == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('orange' in easytubecheck1 or 'orange' in easytubecheck2) and countoforanges<4:
                    easytube3.append(f'pygame.draw.circle(screen,"orange",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('orange')
                    countoforanges += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countoforanges<4:
                    easytube3.append(f'pygame.draw.circle(screen,"orange",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('orange')
                    count += 1
                    countoforanges += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('orange' in easytubecheck2 or 'orange' in easytubecheck1 or 'orange' in easytubecheck3) and countoforanges<4:
                        if 'orange' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('orange')
                        exceeding = 0
                        countoforanges += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countoforanges<4:
                        if 'orange' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('orange')
                        count += 1
                        countoforanges += 1
                        exceedingcolorcountlimit = 0
                    elif countoforanges == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countoforanges == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    # print(count)
                    if len(easytubecheck4) == 0 and ('orange' in easytubecheck1 or 'orange' in easytubecheck2 or 'orange' in easytubecheck3 ) and countoforanges<4:
                        easytube4.append(f'pygame.draw.circle(screen,"orange",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('orange')
                        countoforanges += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countoforanges<4:
                        easytube4.append(f'pygame.draw.circle(screen,"orange",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"orange",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('orange')
                        count += 1
                        countoforanges += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('orange' in easytubecheck2 or 'orange' in easytubecheck1 or 'orange' in easytubecheck3 or 'orange' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('orange' in easytubecheck2 or 'orange' in easytubecheck1 or 'orange' in easytubecheck3 or 'orange' in easytubecheck4 ):
                            pass
                        elif ('orange' in easytubecheck1 or 'orange' in easytubecheck2 or 'orange' in easytubecheck3 or 'orange' in easytubecheck4) and countoforanges<4:
                            if 'orange' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('orange')
                            exceeding = 0
                            countoforanges += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countoforanges<4:
                            if 'orange' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"orange",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('orange')
                            count += 1
                            countoforanges += 1
                            exceedingcolorcountlimit = 0
                        elif countoforanges == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countoforanges==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 309 <= mouse[1] <= 329 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"green",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"green",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('green')
                    count+=1
                    countofgreens += 1

                else:
                    if 'green' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('green')
                        exceeding = 0
                        countofgreens += 1

                    elif count<=3:
                        if 'green' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('green')
                        count+=1
                        countofgreens += 1
                    elif countofgreens == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'green' in easytubecheck1 and countofgreens<4:
                    easytube2.append(f'pygame.draw.circle(screen,"green",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"green",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('green')
                    countofgreens += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofgreens<4:
                    easytube2.append(f'pygame.draw.circle(screen,"green",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"green",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('green')
                    count += 1
                    countofgreens += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('green' in easytubecheck2 or 'green' in easytubecheck1) and countofgreens<4:
                        if 'green' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('green')
                        exceeding = 0
                        countofgreens += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofgreens<4:
                        if 'green' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('green')
                        count += 1
                        countofgreens += 1
                        exceedingcolorcountlimit = 0
                    elif countofgreens == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofgreens == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('green' in easytubecheck1 or 'green' in easytubecheck2) and countofgreens<4:
                    easytube3.append(f'pygame.draw.circle(screen,"green",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"green",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('green')
                    countofgreens += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofgreens<4:
                    easytube3.append(f'pygame.draw.circle(screen,"green",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"green",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('green')
                    count += 1
                    countofgreens += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('green' in easytubecheck2 or 'green' in easytubecheck1 or 'green' in easytubecheck3) and countofgreens<4:
                        if 'green' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('green')
                        exceeding = 0
                        countofgreens += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofgreens<4:
                        if 'green' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('green')
                        count += 1
                        countofgreens += 1
                        exceedingcolorcountlimit = 0
                    elif countofgreens == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofgreens == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('green' in easytubecheck1 or 'green' in easytubecheck2 or 'green' in easytubecheck3) and countofgreens<4:
                        easytube4.append(f'pygame.draw.circle(screen,"green",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"green",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('green')
                        countofgreens += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofgreens<4:
                        easytube4.append(f'pygame.draw.circle(screen,"green",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"green",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('green')
                        count += 1
                        countofgreens += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('green' in easytubecheck2 or 'green' in easytubecheck1 or 'green' in easytubecheck3 or 'green' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('green' in easytubecheck2 or 'green' in easytubecheck1 or 'green' in easytubecheck3 or 'green' in easytubecheck4 ):
                            pass
                        elif ('green' in easytubecheck1 or 'green' in easytubecheck2 or 'green' in easytubecheck3 or 'green' in easytubecheck4) and countofgreens<4:
                            if 'green' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('green')
                            exceeding = 0
                            countofgreens += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofgreens<4:
                            if 'green' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"green",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('green')
                            count += 1
                            countofgreens += 1
                            exceedingcolorcountlimit = 0
                        elif countofgreens==4 and exceeding==1:
                            exceedingcolorcountlimit=1
                            exceeding=0
                        elif countofgreens==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 333 <= mouse[1] <= 353 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"purple",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('purple')
                    count+=1
                    countofpurples += 1

                else:
                    if 'purple' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('purple')
                        exceeding = 0
                        countofpurples += 1

                    elif count<=3:
                        if 'purple' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('purple')
                        count+=1
                        countofpurples += 1

                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'purple' in easytubecheck1 and countofpurples<4:
                    easytube2.append(f'pygame.draw.circle(screen,"purple",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('purple')
                    countofpurples += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofpurples<4:
                    easytube2.append(f'pygame.draw.circle(screen,"purple",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('purple')
                    count += 1
                    countofpurples += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('purple' in easytubecheck2 or 'purple' in easytubecheck1) and countofpurples<4 :
                        if 'purple' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('purple')
                        exceeding = 0
                        countofpurples += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofpurples<4:
                        if 'purple' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('purple')
                        countofpurples += 1
                        exceedingcolorcountlimit = 0
                        count += 1
                    elif countofpurples == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofpurples == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('purple' in easytubecheck1 or 'purple' in easytubecheck2) and countofpurples<4:
                    easytube3.append(f'pygame.draw.circle(screen,"purple",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('purple')
                    countofpurples += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofpurples<4:
                    easytube3.append(f'pygame.draw.circle(screen,"purple",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('purple')
                    count += 1
                    countofpurples += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('purple' in easytubecheck2 or 'purple' in easytubecheck1 or 'purple' in easytubecheck3) and countofpurples<4:
                        if 'purple' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('purple')
                        exceeding = 0
                        countofpurples += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofpurples<4:
                        if 'purple' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('purple')
                        count += 1
                        countofpurples += 1
                        exceedingcolorcountlimit = 0
                    elif countofpurples == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofpurples == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('purple' in easytubecheck1 or 'purple' in easytubecheck2 or 'purple' in easytubecheck3) and countofpurples<4:
                        easytube4.append(f'pygame.draw.circle(screen,"purple",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('purple')
                        countofpurples += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofpurples<4:
                        easytube4.append(f'pygame.draw.circle(screen,"purple",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"purple",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('purple')
                        countofpurples += 1
                        exceedingcolorcountlimit = 0
                        count += 1
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('purple' in easytubecheck2 or 'purple' in easytubecheck1 or 'purple' in easytubecheck3 or 'purple' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('purple' in easytubecheck2 or 'purple' in easytubecheck1 or 'purple' in easytubecheck3 or 'purple' in easytubecheck4 ):
                            pass
                        elif ('purple' in easytubecheck1 or 'purple' in easytubecheck2 or 'purple' in easytubecheck3 or 'purple' in easytubecheck4) and countofpurples<4:
                            if 'purple' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('purple')
                            exceeding = 0
                            countofpurples += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofpurples<4:
                            if 'purple' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"purple",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('purple')
                            count += 1
                            countofpurples += 1
                            exceedingcolorcountlimit = 0
                        elif countofpurples == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofpurples==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 357 <= mouse[1] <= 377 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"pink",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('pink')
                    countofpinks += 1
                    count+=1
                else:
                    if 'pink' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('pink')
                        exceeding = 0
                        countofpinks += 1

                    elif count<=3:
                        if 'pink' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('pink')
                        count+=1
                        countofpinks += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'pink' in easytubecheck1 and countofpinks<4:
                    easytube2.append(f'pygame.draw.circle(screen,"pink",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('pink')
                    countofpinks += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofpinks<4:
                    easytube2.append(f'pygame.draw.circle(screen,"pink",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('pink')
                    count += 1
                    countofpinks += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('pink' in easytubecheck2 or 'pink' in easytubecheck1) and countofpinks<4:
                        if 'pink' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('pink')
                        exceeding = 0
                        countofpinks += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofpinks<4:
                        if 'pink' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('pink')
                        count += 1
                        countofpinks += 1
                        exceedingcolorcountlimit = 0
                    elif countofpinks == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofpinks == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('pink' in easytubecheck1 or 'pink' in easytubecheck2) and countofpinks<4:
                    easytube3.append(f'pygame.draw.circle(screen,"pink",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('pink')
                    countofpinks += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofpinks<4:
                    easytube4.append(f'pygame.draw.circle(screen,"pink",(576, 438),21)')
                    easytube4.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('pink')
                    count += 1
                    countofpinks += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('pink' in easytubecheck2 or 'pink' in easytubecheck1 or 'pink' in easytubecheck3) and countofpinks<4:
                        if 'pink' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('pink')
                        exceeding = 0
                        countofpinks += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofpinks<4:
                        if 'pink' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('pink')
                        count += 1
                        countofpinks += 1
                        exceedingcolorcountlimit = 0
                    elif countofpinks == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofpinks == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('pink' in easytubecheck1 or 'pink' in easytubecheck2 or 'pink' in easytubecheck3) and countofpinks<4:
                        easytube4.append(f'pygame.draw.circle(screen,"pink",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('pink')
                        countofpinks += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofpinks<4:
                        easytube4.append(f'pygame.draw.circle(screen,"pink",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"pink",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('pink')
                        count += 1
                        countofpinks += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('pink' in easytubecheck2 or 'pink' in easytubecheck1 or 'pink' in easytubecheck3 or 'pink' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('pink' in easytubecheck2 or 'pink' in easytubecheck1 or 'pink' in easytubecheck3 or 'pink' in easytubecheck4 ):
                            pass
                        elif ('pink' in easytubecheck1 or 'pink' in easytubecheck2 or 'pink' in easytubecheck3 or 'pink' in easytubecheck4) and countofpinks<4:
                            if 'pink' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('pink')
                            exceeding = 0
                            countofpinks += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofpinks<4:
                            if 'pink' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"pink",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('pink')
                            count += 1
                            countofpinks += 1
                            exceedingcolorcountlimit = 0
                        elif countofpinks == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofpinks==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))


        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 381 <= mouse[1] <= 401 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"brown",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('brown')
                    count+=1
                    countofbrowns+=1

                else:
                    if 'brown' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('brown')
                        exceeding = 0
                        countofbrowns += 1

                    elif count<=3:
                        if 'brown' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('brown')
                        count+=1
                        countofbrowns += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'brown' in easytubecheck1 and countofbrowns<4:
                    easytube2.append(f'pygame.draw.circle(screen,"brown",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('brown')
                    countofbrowns += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofbrowns<4:
                    easytube2.append(f'pygame.draw.circle(screen,"brown",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('brown')
                    count += 1
                    countofbrowns += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('brown' in easytubecheck2 or 'brown' in easytubecheck1) and countofbrowns<4:
                        if 'brown' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('brown')
                        exceeding = 0
                        countofbrowns += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofbrowns<4:
                        if 'brown' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('brown')
                        count += 1
                        countofbrowns += 1
                        exceedingcolorcountlimit = 0
                    elif countofbrowns == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofbrowns == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('brown' in easytubecheck1 or 'brown' in easytubecheck2) and countofbrowns<4:
                    easytube3.append(f'pygame.draw.circle(screen,"brown",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('brown')
                    countofbrowns += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofbrowns<4:
                    easytube3.append(f'pygame.draw.circle(screen,"brown",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('brown')
                    count += 1
                    countofbrowns += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('brown' in easytubecheck2 or 'brown' in easytubecheck1 or 'brown' in easytubecheck3) and countofbrowns<4:
                        if 'brown' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('brown')
                        exceeding = 0
                        countofbrowns += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofbrowns<4:
                        if 'brown' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('brown')
                        count += 1
                        countofbrowns += 1
                        exceedingcolorcountlimit = 0
                    elif countofbrowns == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofbrowns == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('brown' in easytubecheck1 or 'brown' in easytubecheck2 or 'brown' in easytubecheck3) and countofbrowns<4:
                        easytube4.append(f'pygame.draw.circle(screen,"brown",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('brown')
                        countofbrowns += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofbrowns<4:
                        easytube4.append(f'pygame.draw.circle(screen,"brown",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"brown",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('brown')
                        count += 1
                        countofbrowns += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('brown' in easytubecheck2 or 'brown' in easytubecheck1 or 'brown' in easytubecheck3 or 'brown' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('brown' in easytubecheck2 or 'brown' in easytubecheck1 or 'brown' in easytubecheck3 or 'brown' in easytubecheck4 ):
                            pass
                        elif ('brown' in easytubecheck1 or 'brown' in easytubecheck2 or 'brown' in easytubecheck3 or 'brown' in easytubecheck4) and countofbrowns<4:
                            if 'brown' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('brown')
                            exceeding = 0
                            countofbrowns += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofbrowns<4:
                            if 'brown' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"brown",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('brown')
                            count += 1
                            countofbrowns += 1
                            exceedingcolorcountlimit = 0
                        elif countofbrowns == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofbrowns==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 405 <= mouse[1] <= 425 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"black",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"black",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('black')
                    count+=1
                    countofblacks += 1

                else:
                    if 'black' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('black')
                        exceeding = 0
                        countofblacks += 1

                    elif count<=3:
                        if 'black' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('black')
                        count+=1
                        countofblacks += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'black' in easytubecheck1 and countofblacks<4:
                    easytube2.append(f'pygame.draw.circle(screen,"black",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"black",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('black')
                    countofblacks += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofblacks<4:
                    easytube2.append(f'pygame.draw.circle(screen,"black",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"black",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('black')
                    count += 1
                else:
                    if ('black' in easytubecheck2 or 'black' in easytubecheck1) and countofblacks<4:
                        if 'black' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('black')
                        exceeding = 0
                        countofblacks += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofblacks<4:
                        if 'black' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('black')
                        count += 1
                        countofblacks += 1
                        exceedingcolorcountlimit = 0
                    elif countofblacks == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofblacks == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('black' in easytubecheck1 or 'black' in easytubecheck2) and countofblacks<4:
                    easytube3.append(f'pygame.draw.circle(screen,"black",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"black",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('black')
                    countofblacks += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofblacks<4:
                    easytube3.append(f'pygame.draw.circle(screen,"black",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"black",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('black')
                    count += 1
                    countofblacks += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('black' in easytubecheck2 or 'black' in easytubecheck1 or 'black' in easytubecheck3) and countofblacks<4:
                        if 'black' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('black')
                        exceeding = 0
                        countofblacks += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofblacks<4:
                        if 'black' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('black')
                        count += 1
                        countofblacks += 1
                        exceedingcolorcountlimit = 0
                    elif countofblacks == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofblacks == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('black' in easytubecheck1 or 'black' in easytubecheck2 or 'black' in easytubecheck3) and countofblacks<4:
                        easytube4.append(f'pygame.draw.circle(screen,"black",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"black",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('black')
                        countofblacks += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofblacks<4:
                        easytube4.append(f'pygame.draw.circle(screen,"black",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"black",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('black')
                        countofblacks += 1
                        exceedingcolorcountlimit = 0
                        count += 1
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('black' in easytubecheck2 or 'black' in easytubecheck1 or 'black' in easytubecheck3 or 'black' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('black' in easytubecheck2 or 'black' in easytubecheck1 or 'black' in easytubecheck3 or 'black' in easytubecheck4 ):
                            pass
                        elif ('black' in easytubecheck1 or 'black' in easytubecheck2 or 'black' in easytubecheck3 or 'black' in easytubecheck4) and countofblacks<4:
                            if 'black' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('black')
                            exceeding = 0
                            countofblacks += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofblacks<4:
                            if 'black' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"black",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('black')
                            count += 1
                            countofblacks += 1
                            exceedingcolorcountlimit = 0
                        elif countofblacks == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofblacks==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 429 <= mouse[1] <= 449 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"grey",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('grey')
                    countofgreys += 1
                    count+=1
                else:
                    if 'grey' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('grey')
                        exceeding = 0
                        countofgreys += 1

                    elif count<=3:
                        if 'grey' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('grey')
                        count+=1
                        countofgreys += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'grey' in easytubecheck1 and countofgreys<4:
                    easytube2.append(f'pygame.draw.circle(screen,"grey",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('grey')
                    countofgreys += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofgreys<4:
                    easytube2.append(f'pygame.draw.circle(screen,"grey",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('grey')
                    count += 1
                    countofgreys += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('grey' in easytubecheck2 or 'grey' in easytubecheck1) and countofgreys<4:
                        if 'grey' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('grey')
                        exceeding = 0
                        countofgreys += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofgreys<4:
                        if 'grey' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('grey')
                        count += 1
                        countofgreys += 1
                        exceedingcolorcountlimit = 0
                    elif countofgreys == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofgreys == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('grey' in easytubecheck1 or 'grey' in easytubecheck2) and countofgreys<4:
                    easytube3.append(f'pygame.draw.circle(screen,"grey",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('grey')
                    countofgreys += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofgreys<4:
                    easytube3.append(f'pygame.draw.circle(screen,"grey",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('grey')
                    count += 1
                    countofgreys += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('grey' in easytubecheck2 or 'grey' in easytubecheck1 or 'grey' in easytubecheck3) and countofgreys<4:
                        if 'grey' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('grey')
                        exceeding = 0
                        countofgreys += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofgreys<4:
                        if 'grey' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('grey')
                        count += 1
                        countofgreys += 1
                        exceedingcolorcountlimit = 0
                    elif countofgreys == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofgreys == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('grey' in easytubecheck1 or 'grey' in easytubecheck2 or 'grey' in easytubecheck3) and countofgreys<4:
                        easytube4.append(f'pygame.draw.circle(screen,"grey",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('grey')
                        countofgreys += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofgreys<4:
                        easytube4.append(f'pygame.draw.circle(screen,"grey",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"grey",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('grey')
                        count += 1
                        countofgreys += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('grey' in easytubecheck2 or 'grey' in easytubecheck1 or 'grey' in easytubecheck3 or 'grey' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('grey' in easytubecheck2 or 'grey' in easytubecheck1 or 'grey' in easytubecheck3 or 'grey' in easytubecheck4 ):
                            pass
                        elif ('grey' in easytubecheck1 or 'grey' in easytubecheck2 or 'grey' in easytubecheck3 or 'grey' in easytubecheck4) and countofgreys<4:
                            if 'grey' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('grey')
                            exceeding = 0
                            countofgreys += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofgreys<4:
                            if 'grey' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"grey",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('grey')
                            count += 1
                            countofgreys += 1
                            exceedingcolorcountlimit = 0
                        elif countofgreys == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofgreys==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 453 <= mouse[1] <= 473 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"white",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"white",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('white')
                    count+=1
                    countofwhites += 1

                else:
                    if 'white' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('white')
                        exceeding = 0
                        countofwhites += 1

                    elif count<=3:
                        if 'white' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('white')
                        count+=1
                        countofwhites += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2) != 4:
                if len(easytubecheck2) == 0 and 'white' in easytubecheck1 and countofwhites<4:
                    easytube2.append(f'pygame.draw.circle(screen,"white",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"white",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('white')
                    countofwhites += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofwhites<4:
                    easytube2.append(f'pygame.draw.circle(screen,"white",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"white",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('white')
                    count += 1
                    countofwhites += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('white' in easytubecheck2 or 'white' in easytubecheck1) and countofwhites<4:
                        if 'white' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('white')
                        exceeding = 0
                        countofwhites += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofwhites<4:
                        if 'white' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('white')
                        count += 1
                        countofwhites += 1
                        exceedingcolorcountlimit = 0
                    elif countofwhites == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofwhites == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('white' in easytubecheck1 or 'white' in easytubecheck2) and countofwhites<4:
                    easytube3.append(f'pygame.draw.circle(screen,"white",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"white",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('white')
                    countofwhites += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofwhites<4:
                    easytube3.append(f'pygame.draw.circle(screen,"white",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"white",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('white')
                    count += 1
                    countofwhites += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('white' in easytubecheck2 or 'white' in easytubecheck1 or 'white' in easytubecheck3) and countofwhites<4:
                        if 'white' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('white')
                        exceeding = 0
                        countofwhites += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofwhites<4:
                        if 'white' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('white')
                        count += 1
                        countofwhites += 1
                        exceedingcolorcountlimit = 0

                    elif countofwhites == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofwhites == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('white' in easytubecheck1 or 'white' in easytubecheck2 or 'white' in easytubecheck3) and countofwhites<4:
                        easytube4.append(f'pygame.draw.circle(screen,"white",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"white",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('white')
                        countofwhites += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofwhites<4:
                        easytube4.append(f'pygame.draw.circle(screen,"white",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"white",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('white')
                        count += 1
                        countofwhites += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('white' in easytubecheck2 or 'white' in easytubecheck1 or 'white' in easytubecheck3 or 'white' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('white' in easytubecheck2 or 'white' in easytubecheck1 or 'white' in easytubecheck3 or 'white' in easytubecheck4 ):
                            pass
                        elif ('white' in easytubecheck1 or 'white' in easytubecheck2 or 'white' in easytubecheck3 or 'white' in easytubecheck4) and countofwhites<4:
                            if 'white' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('white')
                            exceeding = 0
                            countofwhites += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofwhites<4:
                            if 'white' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"white",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('white')
                            count += 1
                            countofwhites += 1
                            exceedingcolorcountlimit = 0
                        elif countofwhites == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofwhites==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))

        if i.type == pygame.MOUSEBUTTONDOWN and 102 <= mouse[0] <= 251 and 477 <= mouse[1] <= 497 and a == 2:
            if len(easytubecheck1) != 4:
                if len(easytubecheck1) == 0:
                    easytube1.append(f'pygame.draw.circle(screen,"beige",(376, 438),21)')
                    easytube1.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(353.9, 415, 45, 23))')
                    easytubecheck1.append('beige')
                    count+=1
                    countofbeiges += 1

                else:
                    if 'beige' in easytubecheck1:
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('beige')
                        exceeding = 0
                        countofbeiges += 1

                    elif count<=3:
                        if 'beige' not in easytubecheck1:
                            unique1 += 1
                        previous = eval(easytube1[len(easytube1) - 1])
                        easytube1.append(f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck1.append('beige')
                        count+=1
                        countofbeiges += 1

                    else:
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9,(450,190))

            elif len(easytubecheck2)!= 4:
                if len(easytubecheck2) == 0 and 'beige' in easytubecheck1 and countofbeiges<4:
                    easytube2.append(f'pygame.draw.circle(screen,"beige",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('beige')
                    countofbeiges += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck2) == 0 and count <= 3 and countofbeiges<4:
                    easytube2.append(f'pygame.draw.circle(screen,"beige",(476, 438),21)')
                    easytube2.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(453.9, 415, 45, 23))')
                    easytubecheck2.append('beige')
                    count += 1
                    countofbeiges += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('beige' in easytubecheck2 or 'beige' in easytubecheck1) and countofbeiges<4:
                        if 'beige' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(
                            f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('beige')
                        exceeding = 0
                        countofbeiges += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofbeiges<4:
                        if 'beige' not in easytubecheck2:
                            unique2 += 1
                        previous = eval(easytube2[len(easytube2) - 1])
                        easytube2.append(f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck2.append('beige')
                        count += 1
                        countofbeiges += 1
                        exceedingcolorcountlimit = 0
                    elif countofbeiges == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofbeiges == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            elif len(easytubecheck3) != 4:
                if len(easytubecheck3) == 0 and ('beige' in easytubecheck1 or 'beige' in easytubecheck2) and countofbeiges<4:
                    easytube3.append(f'pygame.draw.circle(screen,"beige",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('beige')
                    countofbeiges += 1
                    exceedingcolorcountlimit = 0
                    exceeding = 0
                elif len(easytubecheck3) == 0 and count <= 3 and countofbeiges<4:
                    easytube3.append(f'pygame.draw.circle(screen,"beige",(576, 438),21)')
                    easytube3.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(553.9, 415, 45, 23))')
                    easytubecheck3.append('beige')
                    count += 1
                    countofbeiges += 1
                    exceedingcolorcountlimit = 0
                else:
                    if ('beige' in easytubecheck2 or 'beige' in easytubecheck1 or 'beige' in easytubecheck3) and countofbeiges<4:
                        if 'beige' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('beige')
                        exceeding = 0
                        countofbeiges += 1
                        exceedingcolorcountlimit = 0
                    elif count <= 3 and countofbeiges<4:
                        if 'beige' not in easytubecheck3:
                            unique3 += 1
                        previous = eval(easytube3[len(easytube3) - 1])
                        easytube3.append(
                            f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                        easytubecheck3.append('beige')
                        count += 1
                        countofbeiges += 1
                        exceedingcolorcountlimit = 0
                    elif countofbeiges == 4 and exceeding == 1:
                        exceedingcolorcountlimit = 1
                        exceeding = 0
                    elif countofbeiges == 4:
                        exceedingcolorcountlimit = 1
                    else:
                        if count > 3 and exceedingcolorcountlimit == 1:
                            exceedingcolorcountlimit = 0
                        exceeding = 1
                        text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                        screen.blit(text9, (450, 190))
            else:
                if len(easytubecheck4) != 4:
                    if len(easytubecheck4) == 0 and ('beige' in easytubecheck1 or 'beige' in easytubecheck2 or 'beige' in easytubecheck3) and countofbeiges<4:
                        easytube4.append(f'pygame.draw.circle(screen,"beige",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('beige')
                        countofbeiges += 1
                        exceedingcolorcountlimit = 0
                        exceeding = 0
                    elif len(easytubecheck4) == 0 and count <= 3 and countofbeiges<4:
                        easytube4.append(f'pygame.draw.circle(screen,"beige",(676, 438),21)')
                        easytube4.append(f'pygame.draw.rect(screen,"beige",pygame.Rect(653.9, 415, 45, 23))')
                        easytubecheck4.append('beige')
                        count += 1
                        countofbeiges += 1
                        exceedingcolorcountlimit = 0
                    else:
                        if len(easytubecheck4) == 2 and count == 2 and ('beige' in easytubecheck2 or 'beige' in easytubecheck1 or 'beige' in easytubecheck3 or 'beige' in easytubecheck4 ):
                            pass
                        elif len(easytubecheck4) == 3 and count == 3 and ('beige' in easytubecheck2 or 'beige' in easytubecheck1 or 'beige' in easytubecheck3 or 'beige' in easytubecheck4 ):
                            pass
                        elif ('beige' in easytubecheck1 or 'beige' in easytubecheck2 or 'beige' in easytubecheck3 or 'beige' in easytubecheck4) and countofbeiges<4:
                            if 'beige' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('beige')
                            exceeding = 0
                            countofbeiges += 1
                            exceedingcolorcountlimit = 0
                        elif count <= 3 and countofbeiges<4:
                            if 'beige' not in easytubecheck4:
                                unique4 += 1
                            previous = eval(easytube4[len(easytube4) - 1])
                            easytube4.append(
                                f'pygame.draw.rect(screen,"beige",pygame.Rect({previous.topleft[0]}, {previous.topleft[1] - 22}, 45, 23))')
                            easytubecheck4.append('beige')
                            count += 1
                            countofbeiges += 1
                            exceedingcolorcountlimit = 0
                        elif countofbeiges == 4 and exceeding == 1:
                            exceedingcolorcountlimit = 1
                            exceeding = 0
                        elif countofbeiges==4:
                            exceedingcolorcountlimit=1
                        else:
                            if count > 3 and exceedingcolorcountlimit == 1:
                                exceedingcolorcountlimit = 0
                            exceeding = 1
                            text9 = rules.render('  Only 3 Distinct Colors!!! ', False, 'Red')
                            screen.blit(text9,(450,190))
        if i.type==pygame.MOUSEBUTTONDOWN and 83<=mouse[0]<=129 and 531<=mouse[1]<=559 and a==1:
            a=0

        if i.type==pygame.MOUSEBUTTONDOWN and 181<=mouse[0]<=231 and 531<=mouse[1]<=559 and a==1:
            a=2



        if i.type== pygame.MOUSEMOTION and 83<=mouse[0]<=129 and 531<=mouse[1]<=559:
            coloreasy1='green'
            text3 = selecttext.render('  Easy  ', True, coloreasy1)

        else:
            coloreasy1='red'
            text3 = selecttext.render('  Easy  ', True, coloreasy1)

        if i.type==pygame.MOUSEMOTION and 7<=mouse[0]<=52 and 7<=mouse[1]<=31 and (a==0 or a==2 or a==3):
            home = selecttext.render('Home', True, 'green')
        else:
            home=selecttext.render('Home', True, 'red')

        if i.type==pygame.MOUSEBUTTONDOWN and 7<=mouse[0]<=52 and 7<=mouse[1]<=31 and (a==0 or a==2) :
            easytube1=[]
            screen.blit(tube, (350, 210))
            easytubecheck1=[]
            easytubecheck2=[]
            easytubecheck3=[]
            easytubecheck4=[]
            easytubecheck5=[]
            easytubecheck6=[]
            easytube5 = []
            easytube6 = []
            easytube3=[]
            easytube4=[]
            exceedingcolorcountlimit = 0
            exceeding=0
            count=0
            unique1=1
            unique2=1
            unique3=1
            unique4=1
            unique5=0
            unique6=0
            countofreds = 0
            countofyellows = 0
            countofblues = 0
            countoforanges = 0
            countofgreens = 0
            countofpurples = 0
            countofpinks = 0
            countofbrowns = 0
            countofblacks = 0
            countofgreys = 0
            countofwhites = 0
            countofbeiges = 0
            easytube2=[]
            a=1

        if i.type == pygame.MOUSEMOTION and 523 <= mouse[0] <= 569 and 520 <= mouse[1] <= 547 and (a == 0 or a == 2):
            playeasy = starteasy.render('Start', True, 'green')
        else:
            playeasy = starteasy.render('Start', True, 'red')

        if i.type == pygame.MOUSEBUTTONDOWN and 7<=mouse[0]<=52 and 7<=mouse[1]<=31 and a == 3:
            easytube1 = []
            screen.blit(tube, (350, 210))
            constraint=0
            easytubecheck1 = []
            easytubecheck2 = []
            easytubecheck3 = []
            easytubecheck4 = []
            easytubecheck5 = []
            easytubecheck6 = []
            easytube5=[]
            easytube6=[]
            easytube3 = []
            easytube4 = []
            exceedingcolorcountlimit = 0
            exceeding = 0
            count = 0
            unique1 = 1
            unique2 = 1
            unique3 = 1
            unique4 = 1
            unique5 = 0
            unique6 = 0
            countofreds = 0
            countofyellows = 0
            countofblues = 0
            countoforanges = 0
            countofgreens = 0
            countofpurples = 0
            countofpinks = 0
            countofbrowns = 0
            countofblacks = 0
            countofgreys = 0
            countofwhites = 0
            countofbeiges = 0
            easytube2 = []
            gameover=0
            a = 1

        if i.type == pygame.MOUSEBUTTONDOWN and 523 <= mouse[0] <= 569 and 520 <= mouse[1] <= 547 and a == 0:
            easy=Easymode(easytubecheck1,easytube1,easytubecheck2,easytube2,easytubecheck3,easytube3,easytubecheck4,easytube4,unique1,unique2,unique5,unique6)
            if unique1 == 1 and unique2 != 1:
                gamemode = 0
            elif unique1 != 1 and unique2 == 1:
                gamemode = 1
            else:
                gamemode = 2
            a=3
        if i.type == pygame.MOUSEBUTTONDOWN and 523 <= mouse[0] <= 569 and 520 <= mouse[1] <= 547 and a == 2:
            hard=Hardmode(easytubecheck1,easytube1,easytubecheck2,easytube2,easytubecheck3,easytube3,easytubecheck4,easytube4,easytubecheck5,easytube5,easytubecheck6,easytube6,unique1,unique2,unique5,unique6,unique4,unique3)
            if unique1==1 and unique2==1 and unique3==1 and unique4==1:
                gameover=1
                gamemode=10
            elif unique1==1 and unique2==1 and unique3!=1 and unique4!=1:
                gamemode=3
            elif unique1!=1 and unique2!=1 and unique3==1 and unique4==1:
                gamemode=4  
            elif unique1!=1 and unique2==1 and unique3==1 and unique4!=1:
                gamemode=5
            elif unique1==1 and unique2!=1 and unique3!=1 and unique4!=1:
                gamemode=9
            elif unique1!=1 and unique2!=1 and unique3!=1 and unique4==1:
                gamemode=14
            elif unique1!=1 and unique2==1 and unique3!=1 and unique4!=1:
                gamemode=11
            elif unique1!=1 and unique2!=1 and unique3==1 and unique4!=1:
                gamemode=12
            elif unique1!=1 and unique2==1 and unique3!=1 and unique4==1:
                gamemode=6
            elif unique1==1 and unique2!=1 and unique3!=1 and unique4==1:
                gamemode=7
            elif unique1==1 and unique2!=1 and unique3==1 and unique4!=1:
                gamemode=8              
            elif unique1!=1 and unique2!=1 and unique3!=1 and unique4!=1:
                gameover=1
                constraint=1
                gamemode=13 
            a=3

        if i.type== pygame.MOUSEMOTION and 181<=mouse[0]<=231 and 531<=mouse[1]<=559:
            coloreasy1='green'
            text4 = selecttext.render('  Hard  ', True, coloreasy1)

        else:
            coloreasy1='red'
            text4 = selecttext.render('  Hard  ', True, coloreasy1)

        if i.type == pygame.QUIT:
            pygame.quit()
            exit()


