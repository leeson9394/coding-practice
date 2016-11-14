import sys

input_num=int(raw_input(""))

if 1 <= input_num <= 1000000000:
    bin_input=bin(input_num)[2:]
    for i in xrange(len(bin_input)):
        tmp_list=list(bin_input)
    tmp_list.reverse()
    bin_output=''.join(tmp_list)
    output_num=int(bin_output,2)
    print output_num
else:
    sys.exit()