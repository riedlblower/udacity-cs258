import random
import math

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""


def fuzzit(content):
        num_tests = 10000
        FuzzFactor = 113
        list_of_strings = []
        buf = bytearray(content)
       #print buf
        #print len(buf)
        for i in range(num_tests):
            numwrites=random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1
            #print numwrites
            for j in range(numwrites):
                rbyte = random.randrange(256)
                rn = random.randrange(len(buf))
                buf[rn] = "%c"%(rbyte)
                list_of_strings.append(str(buf))
        return list_of_strings
