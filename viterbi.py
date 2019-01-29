import sys;
import numpy;

def viterbi(a, b, ip):
    op = []
    p = numpy.zeros(shape=(2, len(ip)), dtype=float)
    pr = numpy.zeros(shape=(2, len(ip)), dtype=int)
    for i in range(2):
        p[i][0] = a[2][i] * b[i][ip[0]-1]
    for i in range(1, len(ip)):
        for j in range(2):
            p[j][i] = max(p[0][i-1]*a[0][j]*b[j][ip[i]-1], p[1][i-1]*a[1][j]*b[j][ip[i]-1])
            if(p[0][i-1]*a[0][j] >= p[1][i-1]*a[1][j]):
                pr[j][i] = 0
            else:
                pr[j][i] = 1
    c = 0
    l = len(ip)-1;
    if(p[0][l]*a[0][0] > p[1][l]*a[1][1]):
        c = 0
    else:
        c = 1
    op.append(c)
    for i in range(1, len(ip)):
        op.insert(0,pr[c][l])
        c = pr[c][l]
        l = l-1
    return(convert_op(op))

def convert_op(op):
    output_list = []
    for i in op:
        if i==0:
            output_list.append("H")
        else:
            output_list.append("F")
    output_string = ' '.join(output_list)
    return output_string

def convert_ip(input_string):
    ip = list(input_string)
    input_list = []
    for char in ip:
        if(char == 'N'):
            input_list.append(1);
        elif(char == 'C'):
            input_list.append(2);
        else:
            input_list.append(3);
    return(input_list)


# Probability table: transition probability
t_p = numpy.array([ [0.7, 0.3, 0],
                    [0.5, 0.5, 0],
                    [0.6, 0.4, 0]])

# Probability table: observation probability
o_p = numpy.array([ [0.1, 0.4, 0.5],
                    [0.6, 0.3, 0.1]])

# read input
ip = sys.argv[1];
# run algorithm
output_string = viterbi(t_p, o_p, convert_ip(ip));
#print to console
print(output_string);
#print to file
myfile = open('output.txt', 'w+');
myfile.write(output_string);

