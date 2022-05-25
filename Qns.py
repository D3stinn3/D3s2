class Developer:

    def __init__(self, __seniority, skills):
        self.__seniority = 'Junior'
        self.skills = 'python'

    def display(self):
        print('Welcome to D3stinn3 with {seniority} developer with skill in {skills}'.format(seniority=self.__seniority,
                                                                                             skills=self.skills))


class NodeJs(Developer):

    def __init__(self):
        super().__init__()
        self.__seniority = 'Senior'
        self.skills = 'NodeJs'

    def display2(self):
        print('Welcome to Destinne the place with great{level} and awesome'.format(level=self.__seniority))


lst2 = Developer('Junior', 'Python')
lst2.display()
