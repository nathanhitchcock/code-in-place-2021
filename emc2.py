def main():
    '''E = mc^2'''
    #use a constant value for the speed of light -- C = 299792458 m/s.
    C = 299792458

    #  ask the user for mass (m) in kilograms 
    mass = input("Enter kilos of mass: ")
    mass = float(mass)

    # call math function
    E = go_go_gadget_einstein(C, mass)
    print_results(E, C, mass)

    # perform calculation
def go_go_gadget_einstein(C, mass):
    return mass * (C ** 2)

    #print result
def print_results(E, C, mass):
    print('e = m * C^2...')
    print('m = ' + str(mass) + ' m/s')
    print('C = ' + str(C) + 'm/s')
    print(str(E) + 'joulles of energy!')


if __name__ == "__main__":
    main()
