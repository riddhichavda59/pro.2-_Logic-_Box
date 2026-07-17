#Logic Box

print("Welcome to the Pattern Generator and Number Analyzer")

while True:
    print("Select an option:")
    print("1.Generate a pattern:")
    print("2.Analayze a Range of Numbers")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        rows=int(input("Enter the number of rows for the pattern:"))

        for i in range(1,rows+1):
            for j in range(i):
                print("*",end="")
            print()
           
    elif choice==2:

        start=int(input("\nEnter the start of the range:"))
        end=int(input("Enter the end of the range:"))

        total=0
        
        for i in range(start,end+1):
            if i%2==0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")

            total +=i
                
        print(f"Sum of all numbers from {start} to {end} is:{total}")

    elif choice==3:
        print("Exiting the program.Goodbye!")

        break
    
    else:
        print("Invalide choice")
           
     

