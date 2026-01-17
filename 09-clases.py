class OperaBas:
    # declaración del constructor
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
        self.res = 0

    # declaración de métodos
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))

    def resta(self):
        self.res = self.num1 - self.num2
        print("La resta es: {}".format(self.res))


def main():
    obj = OperaBas(5, 3)
    obj.suma()
    obj.resta()


if __name__ == "__main__":
    main()
