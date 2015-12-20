
def dayTen():
    startMember = [1, 1, 1, 3, 1, 2, 2, 1, 1, 3]
    iterations = 50

    currentMember = startMember
    for i in range(iterations):
        newMember = []
        number = currentMember[0]
        count = 0
        for s in currentMember:
            if s != number:
                newMember.append(count)
                newMember.append(number)
                count = 0
                number = s

            count += 1

        newMember.append(count)
        newMember.append(number)
        currentMember = newMember
        print len(newMember) 

dayTen()

