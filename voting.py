'''
International voting age
Write a program which asks a user for their age and lets them know if they can 
or can't vote in the following three fictional countries.

Around the world, different countries have different voting ages. 
In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, 
the voting ages are very different:

the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, 
for example, Scotland, Ethiopia, and Austria)

the voting age in Stanlau is 25 (in real life this is the voting age in the 
United Arab Emirates)

the voting age in Mayengua is 48 (in real life, as far as we can tell, 
this isn't the voting age anywhere)

Your code should prompt the for their age and print whether or not they can vote 
in Peturksbouipo, Stanlau, or Mayengua.
'''

voting_age_peturks = 16
voting_age_stanlau = 25
voting_age_mayengua = 48


def main():
    age = input("How old are you? ")
    age = int(age)
    if (age >= voting_age_peturks):
        print("You can vote in Peturksbouipo where the voting age is " + str(voting_age_peturks) + ".")
    else: 
        print("You cannot vote in Peturksbouipo where the voting age is " + str(voting_age_peturks) + ".")
    if (age >= voting_age_stanlau):
        print("You can vote in Stanlau where the voting age is " + str(voting_age_stanlau) + ".")
    else: 
        print("You cannot vote in Stanlau where the voting age is " + str(voting_age_peturks) + ".")
    if (age >= voting_age_mayengua):
        print("You can vote in Mayengua where the voting age is " + str(voting_age_mayengua) + ".")
    else: 
        print("You cannot vote in Mayengua where the voting age is " + str(voting_age_peturks) + ".")

if __name__ == "__main__":
    main()
