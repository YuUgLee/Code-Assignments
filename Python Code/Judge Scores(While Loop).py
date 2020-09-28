i=2
while i<4:
    one=int(input("Enter the judge #1's score:"))
    if one>10:
        print('Please enter a range from 0-10')
        i=2
    else:
        two=int(input("Enter the judge #2's score:"))
        if two>10:
            print('Please enter a range from 0-10')
            i=2
        else:
            three=int(input("Enter the judge #3's score:"))
            if three>10:
                print('Please enter a range from 0-10')
                i=2
            else:
                four=int(input("Enter the judge #4's score:"))
                if four>10:
                    print('Please enter a range from 0-10')
                    i=2
                else:
                    five=int(input("Enter the judge #5's score:"))
                    if five>10:
                        print('Please enter a range from 0-10')
                        i=2
                    else:
                        if one>10 or two>10 or three>10 or four>10 or five>10:
                            print('Please enter a range from 0-10')
                            i=2
                        if (10>one>0) and (10>two>0) and (10>three>0) and (10>four>0) and (10>five>0):
                            avg=(one+two+three+four+five)/5
                            print('The average score is','%0.2f' %(avg))
                            i=6


