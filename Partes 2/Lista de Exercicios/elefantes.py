def incomodam(n, num_elefantes=2, elefantes='incomodam '):
    if n < 1:
        return ''
    if num_elefantes > n:
        return elefantes
    else:
        elefantes += 'incomodam '
        return incomodam(n, num_elefantes+1, elefantes)
    
def elefantes(n, num_elefantes=2, elefantes_s=''):
    if n < 1:
        return ''
    elif n == 1:
        return 'Um elefante incomoda muita gente'
    else:
        if elefantes_s == '':
            elefantes_s = 'Um elefante incomoda muita gente\n'
        if num_elefantes <= n:
            elefantes_s += str(num_elefantes) + ' elefantes ' + incomodam(num_elefantes) + 'muito mais'
            if num_elefantes < n:
                elefantes_s += '\n' + str(num_elefantes) + ' elefantes ' + 'incomodam ' + 'muita gente\n'
            if num_elefantes == n:
                return elefantes_s
            return elefantes(n, num_elefantes+1, elefantes_s)
