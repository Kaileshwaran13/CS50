def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    ans = d.replace('$','')
    return (float(ans))


def percent_to_float(p):
    ans = p.replace('%','')
    return float(ans)/100

main()