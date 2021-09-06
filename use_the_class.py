from my_class_file import MyClass, unless_imported_from_other_file_everything_within_this_file_can_access_me

list_of_shit = ['one', 'two', 'three']

# MyClass.do_it_all('method_argument') # wrong sort of. General mistake when calling a class.
#
# MyClass().do_it_all() # better, but needs params

MyClass('PARAMTER_ONE', args=list_of_shit, key1=list_of_shit, key2='nothing but can be here').do_it_all('method_argument')

# MyClass(unless_imported_from_other_file_everything_within_this_file_can_access_me, args=['one', 'two', 'three', 'four'], kwargs=dict_of_shit).do_it_all('method_argument')

