#!/usr/bin/python3

#########################################################################################
#                           Program by Mohammed Faisal Khan                             #
#                           00598949                                                    #
#                           mkhan8@unh.newhaven.edu                                     #
#########################################################################################

# Initial response parameter for the PRIMARY while loop asking user if they want to check another sequence
res = 'Yes'

# Primary while loop to ask user to input sequence to process
while res != 'No' or res != 'no' or res != 'n' or res != 'N':

    # Initial response parameter for the secondary while loop asking user if they want to try entering the code again
    response = 'Yes'
    # Flag to track error and prompt user if he wants to try again
    flag = '1'

    # Input while loop to continuously ask for input until it is entered correctly
    while response != 'No' or response != 'no' or response != 'n' or response != 'N':

        # Data Input
        data = input("Please enter the transmitted data: ")

        # To check if the length of the input is 12 bits
        if len(data) == 12:
            print("Correct length of data... length = ", len(data), " Proceeding...")
            # For loop to check if the digits entered are either 1 or 0 and to display error if not.
            for var in data:
                if var != '1' and var != '0':
                    print("Wrong data entered, please enter a binary string of 12 bits ")
                    flag = '0'
                    break
            else:
                print("Binary data received -", data, "- Processing...")
                break

        # To check if the length of the input is less than 12 bits
        elif len(data) < 12:
            print("Data entered is too short ")
            flag = '0'

        # To check if the length of the input is more than 12 bits
        else:
            print("Data entered is too long ")
            flag = '0'

        # Condition check for error and then ask user if they want to try again.
        if flag == '0':
            print("Do you want to try again? [Y/N]")
            response = input("")
            if response == 'No' or response == 'no' or response == 'n' or response == 'N':
                print("You chose NOT to try again... Exiting program!...")
                break
            else:
                print("You chose to try again")
                continue
    else:
        # If loop exits unexpectedly display error
        print("Oops! something is wrong with the input loop!")

    if flag == '0':
        break

    #########################################################################################

    # Slicing the string into individual bits
    c1 = data[0:1]
    c2 = data[1:2]
    d1 = data[2:3]
    c4 = data[3:4]
    d2 = data[4:5]
    d3 = data[5:6]
    d4 = data[6:7]
    c8 = data[7:8]
    d5 = data[8:9]
    d6 = data[9:10]
    d7 = data[10:11]
    d8 = data[11:12]

#    print(c1, c2, d1, c4, d2, d3, d4, c8, d5, d6, d7, d8)

    #########################################################################################

    # Initial declaration of the sum to calculate the error bit position
    sum = 0

    # Count for the first sequence to deduce even and odd bit
    count = int(d1) + int(d2) + int(d4) + int(d5) + int(d7)

#    print("First sequence is: ", int(d1), int(d2), int(d4), int(d5), int(d7))
#    print("Count for the first sequence is: ", count)

    # To check even and odd count
    if (count % 2) == 0:
        # If count is even
#        print("First set count is even")
        # To check value mismatch
        if c1 != '0' :
#            print("Error: Mismatch in the value of c1, value: ", c1)
            sum += 1
#        else:
#            print("c1 is correct, value: ", c1)

    else:
        #  If count is odd
#        print("First set count is odd")
        # To check value mismatch
        if c1 != '1':
#            print("Error: Mismatch in the value of c1, value: ", c1)
            sum += 1
#        else:
#            print("c1 is correct, value: ", c1)


    #########################################################################################

    # Count for the second sequence to deduce even and odd bit
    count = int(d1) + int(d3) + int(d4) + int(d6) + int(d7)

#    print("Second sequence is: ", int(d1), int(d3), int(d4), int(d6), int(d7))
#    print("Count for the second sequence is: ", count)

    # To check even and odd count
    if (count % 2) == 0:
        # If count is even
#        print("Second set count is even")
        # To check value mismatch
        if c2 != '0':
#            print("Error: Mismatch in the value of c2, value: ", c2)
            sum += 2
#        else:
#            print("c2 is correct, value: ", c2)

    else:
        # If count is odd
#        print("Second set count is odd")
        # To check value mismatch
        if c2 == '1':
#            print("Error: Mismatch in the value of c2, value: ", c2)
            sum += 2
#        else:
#            print("c2 is correct, value: ", c2)

    #########################################################################################

    # Count for the third sequence to deduce even and odd bit
    count = int(d2) + int(d3) + int(d4) + int(d8)

#    print("Third sequence is: ", int(d2), int(d3), int(d4), int(d8))
#    print("Count for the third sequence is: ", count)

    # To check even and odd count
    if (count % 2) == 0:
        # If count is even
#        print("Third set count is even")
        # To check value mismatch
        if c4 == '0':
#            print("Error: Mismatch in the value of c4, value: ", c4)
            sum += 4
#        else:
#            print("c4 is correct, value: ", c4)

    else:
        # If count is odd
#        print("Third set count is odd")
        # To check value mismatch
        if c4 == '1':
#            print("Error: Mismatch in the value of c4, value: ", c4)
            sum += 4
#        else:
#            print("c4 is correct, value: ", c4)

    #########################################################################################

    # Count for the fourth sequence to deduce even and odd bit
    count = int(d5) + int(d6) + int(d7) + int(d8)

#    print("Fourth sequence is: ", int(d5), int(d6), int(d7), int(d8))
#    print("Count for the fourth sequence is: ", count)

    # To check even and odd count
    if (count % 2) == 0:
        # If count is even
#        print("Fourth set count is even")
        # To check value mismatch
        if c8 == '0':
#            print("Error: Mismatch in the value of c8, value: ", c8)
            sum += 8
#        else:
#            print("c8 is correct, value: ", c8)

    else:
        # If count is odd
#        print("Fourth set count is odd")
        # To check value mismatch
        if c8 == '1':
#            print("Error: Mismatch in the value of c8, value: ", c8)
            sum += 8
#        else:
#            print("c8 is correct, value: ", c8)

    #########################################################################################

    # Final output of the sum
#    print("Final sum = ", sum)

    #########################################################################################

    # To check if error detected
    if sum == 0 :
        print("No error in the data!")
    elif sum > 12:
        print("More than 1 error occurred!")
    else:
        print("Received data: ", int(data))
        print("Bit ", sum, " was corrupted!")

#        print("Value to change : ", int(data[sum - 1:sum]))

        # Correct the wrong bit
        if int((data[sum - 1:sum])) == 0 :
            newdata = data[0:sum - 1] + '1' + data[sum:]
        else:
            newdata = data[0:sum - 1] + '0' + data[sum:]

        print("Corrected data : ", newdata)
        print("Hurray! Code corrected!!!")

    #########################################################################################

    # Check to process another sequence
    print("Do you want to check another 12 bit data [Y/N]")
    res = input("")
    if res == 'No' or res == 'no' or res == 'n' or res == 'N':
        print("You chose NOT to continue... Exiting program!...")
        break
    else:
        print("You chose to continue")
        continue

else:
    # If loop exits unexpectedly display error
    print("Oops! something is wrong!")

    #########################################################################################
    #                                   End of Program                                      #
    #########################################################################################