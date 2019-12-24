class A:
    student = 'Tom'
    pass

class B:
    def tellwho(self, A_obj):
        return A_obj.student
    pass

def main():
    a = A()
    a.student = 'jane'
    b = B()
    print(b.tellwho(a))

if __name__ == '__main__':
    main()

