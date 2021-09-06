unless_imported_from_other_file_everything_within_this_file_can_access_me = 'variable'


def global_variable():
    global my_global_variable


class MyClass:
    variable_my_class_has = 'my class variable'
    kwargs = 'key word arguments'

    def __init__(self, parameter1, *args_list_of_params, **kwargs_dictionary_of_params):
        print('This shit is executed first')
        self.parameter1 = parameter1
        self.args_list_of_params = args_list_of_params
        self.kwargs_dictionary_of_params = kwargs_dictionary_of_params

    def list_my_args(self):
        value = 0 # local variable value
        for i in self.args_list_of_params:
            print(f'Param: {i} is in index {value}')
            value += 1

    def list_my_kwargs(self):
        value = 0 # local variable value
        for i in self.kwargs_dictionary_of_params['key1']:
            print(f'Param: {i} is in index {value} for key1')
            value += 1

    @staticmethod  # required if you want function here allows it to exist without 'self' param. - called decorator, but DW about that
    def this_stupid_method_is_static():
        """
        Because it doesn't use any of the self. thing.
        It could even be placed outside of the class ^^^^^^
        :return:
        """
        print('because it doesn\'t use other shit')
        print("because it doesn't use other shit")
        print('''because ""it"" doesn't use other shit''')

    def wtf_is_my_param(self):
        print(self.parameter1)
        print(unless_imported_from_other_file_everything_within_this_file_can_access_me)

    def need_to_return_string(self):
        return MyClass.variable_my_class_has

    def need_to_return_list(self):
        return [MyClass.variable_my_class_has, self.variable_my_class_has, 'same shit']

    def do_it_all(self, method_argument):
        self.list_my_args()
        self.list_my_kwargs()
        self.wtf_is_my_param()
        print(f"My class variable is {self.variable_my_class_has}")
        self.need_to_return_string()
        for i in self.need_to_return_list():
            print(i)

        self.this_stupid_method_is_static()

# TODO: Add sub/child class
