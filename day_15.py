numbers = [
    0,1,2,3,4,5,6,7,8,9,

    10,11,12,13,14,15,16,17,18,19,
    20,30,
    40,50,60,70,80,90,
    100,1000,
    1000000,1000000000
    ]

words = ['zero', 'one', 'two','three', 'four', 'five', 'six', 'seven', 'eight',
         'nine', 
         'ten', 'elevn', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen',
         'seventeen','eighteen','nineteen', 'twenty','thirty', 'forty', 'fifty','sixty',
         'seventy', 'eighty', 'ninty', 'hundred', 'thousand', 'million', 'billion'
         ]

def ones(number):
   ans = words[numbers.index(int(number))]
   return ans

def tens(number):
    ans = ""
    if number[0] == '1':
        ans = words[numbers.index(int(number))]
    elif number[0] == '0':
        ans = words[numbers.index(int(number[1]))]
    else:
        if number[1] == '0':
            ans = f"{words[numbers.index(int(number))]}"
        else: 
            ans = f"{words[numbers.index(int(number[0] + '0'))]} {words[numbers.index(int(number[1]))]}"

    return ans

def hundreds(number):
    ans = ""
    if number[-1:] == "00":
        ans = ones(number[-1])
    elif number[0] == "0":
        ans = tens(number[1:])
    elif number[1:] == "00":
        ans = f"{ones(number[0])} hundred"
    else:
        ans = f"{ones(number[0])} hundred and {tens(number[1:])}"
    return ans 

def thousands(number):
    ans = ""
    # if number[-1:] == "00":
    #     ans = ones(number[-1])
    # elif number[0] == "0":
    #     ans = hundreds(number[1:])
    # elif number[:-2] == "00":
    #     ans = hundreds(number[1:])
    if number[1:] == "000":
       ans = f"{ones(number[0])} thousand"
    # else: 
        # ans = f"{ones(number[0])} thousand {hundreds(number[1:2])} and {ones(number[-1])}"
        # ans = f'{hundreds(number[1:2])}'

    return ans

    








    
# def numbers_words(number):
#     # ONES
#     ones(number)

#     # TENS
#     tens(number)

#     # HUNDREDS
#     hundreds(number)
    
    

while True: 
    input_num = input("Enter a number: ")
    print (thousands(input_num))
    