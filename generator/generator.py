the_list = [ x+x for x in range(3)]

print(type(the_list), the_list)


the_gen = ( x+x for x in range(3) )

print(type(the_gen), the_gen)