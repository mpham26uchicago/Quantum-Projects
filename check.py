### Building the circuit

def check(x1, x2, x3, z1, z2, z3):
    
    circ = q(1)
    circ.h(0)
    circ.t(0)

    ### 1
    if x1 ==1:
        circ.x(0)
    if z1 ==1:
        circ.z(0)

    circ.tdg(0)
    circ.h(0)

    ### 2
    if x2 ==1:
        circ.x(0)
    if z2 ==1:
        circ.z(0)

    circ.t(0)

    ### 3
    if x3 ==1:
        circ.x(0)
    if z3 ==1:
        circ.z(0)

    circ.tdg(0)

    ### 2
    if x2 ==1:
        circ.x(0)
    if z2 ==1:
        circ.z(0)

    circ.t(0)

    ### 3
    if x3 ==1:
        circ.x(0)
    if z3 ==1:
        circ.z(0)

    circ.tdg(0)

    circ.h(0)
    circ.t(0)

    ### 1
    if x1 ==1:
        circ.x(0)
    if z1 ==1:
        circ.z(0)

    circ.tdg(0)
    circ.h(0)

    return circ
  
  
  for elem in product([0, 1], repeat = 6):
    
    x1, x2, x3, z1, z2, z3 = elem
    
    circ = check(x1, x2, x3, z1, z2, z3)
    
    print(f'{x1 = } , {x2 = } , {x3 = } , {z1 = } , {z2 = } , {z3 = }')
    #get(circ)
    c1 = zx.qasm(circ.qasm())
    
    print('Full Circuit')
    zx.draw(c1)

    c2 = zx.optimize.basic_optimization(c1)
    print('Reduced Circuit')
    zx.draw(c2)
    print('\n')
    
    '''verify = input('Is the circuit correct: ')
    if verify == 'y':
        correct +=1'''
