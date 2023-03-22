ones ={
    1: 'one', 2: 'two',  3: 'three', 4: 'four', 5: 'five',
    6:'six', 7:'seven', 8:'eight', 9:'nine', 0:'zero',
    }

tens  ={
    10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 
    14:'forteen', 15:'fifteen', 16:'sixteen',17:'seventeen',
    18:'eighteen', 19:'nineteen',20: "twenty", 30:'thirty', 
    40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 
    90:'ninety',
}

hun_tho_mil_bil_tri ={
    100:'hundred', 
    1000:'thousand',
    1000000:'million',
    1000000000:'billion', 
    1000000000000:'trillion'
    }

while True: 
    input_num = input("Enter a number: ")

    # Ones
    if len(input_num) == 1:
        print(ones[int(input_num)])
       
    # Tens
    elif len(input_num) ==2:
        if int(input_num[0]) == 1:
            print(tens[int(input_num)])
        elif int(input_num[0]) == 0:
            print(f'{ones[int(input_num[1])]}')
        elif int(input_num[0]) > 1 and int(input_num[1]) != 0 :
            print(f"{tens[int(input_num[0] + '0')]} {ones[int(input_num[1])]} ")
        else:
            print(f"{tens[int(input_num[0] + '0')]}")

    # Hundreds
    elif len(input_num) == 3:
        if int(input_num[0]) == 0:
            if int(input_num[1]) > 1 and int(input_num[2]) != 0:
                print(f"{tens[int(input_num[1] + '0')]} {ones[int(input_num[2])]} ")
            else:
                print(f"{tens[int(input_num[1] + '0')]} ")

        elif int(input_num[1]) == 0 and int(input_num[2]) == 0:
            print(f'{ones[int(input_num[0])]} hundred')

        elif int(input_num[1]) == 0:
            print(f'{ones[int(input_num[0])]} hundred and {ones[int(input_num[2])]}')

        elif int(input_num[1]) > 1 and int(input_num[2]) != 0:
            print(f"{ones[int(input_num[0])]} hundred and {tens[int(input_num[1] + '0')]} {ones[int(input_num[2])]} ")

        elif int(input_num[1]) > 1 and int(input_num[2]) == 0:
            print(f"{ones[int(input_num[0])]} hundred and {tens[int(input_num[1] + '0')]} ")

        elif int(input_num[1]) != 0:
            if int(input_num[1]) == 1:
                print(f'{ones[int(input_num[0])]} hundred and {tens[int(input_num[1]+input_num[2])]}')

    # input_num=""

#thousands


    


# print(words[int(input_num)])

'''5467
5000
five thousand four hundred sixty seven'''


# word = ''
# print(f'{input_num} ==> {word} ')