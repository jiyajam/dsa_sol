total =0.0

while True:
    user_input=input()

    try:
        number=float(user_input)
        if number==0:
            break
        total +=number
        print(f'The total is now {total}')
    except ValueError:
        print(f"That was not a number")
print (f'The grand total is {total}')

