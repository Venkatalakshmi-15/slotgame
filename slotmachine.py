import random
def spin():
    symbols=['🍒','🍉','🍋','🔔','⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    return " ".join(row)

def pay_out(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*2
        elif row[0]=='🍉':
            return bet*3
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='🔔':
            return bet*10
        elif row[0]=='⭐':
            return bet*20
    return 0

def decorator():
    print("**************************")

def main():
    balance=100
    decorator()
    print("Welcome to play slot")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    decorator()
    while balance>0:
        print(f"Your balance amount is {balance}")
        bet=int(input("Enter your bet amount:"))
        balance-=bet
        if bet>balance:
            print("Insufficient funds.")
            break
        row=spin()
        p_rint=print_row(row)
        print(p_rint)
        payout=pay_out(row,bet)
        
        if payout>0:
            decorator()
            print(f"you won {payout}")
            decorator()
        else:
            decorator()
            print(f"Sorry you lost!!")
            decorator()
        balance+=payout
        play_again=input("Enter you want to play again or not(y/n):").lower()
        if play_again!='y':
            break
            
    

if __name__=='__main__':
    main()

    
    
    
    