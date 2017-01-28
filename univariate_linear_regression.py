# -*- coding: utf-8 -*-

import csv
import sys

class UnivarLinearRegression(object):

    def __init__(self, filepath):
        if filepath == "":
            raise Exception("No csv file path given")
        raw = csv.reader(open(filepath), delimiter = ',')
        self.header = raw.next()
        self.data = []
        for row in raw:
            self.data.append([float(row[0]), float(row[1])])

    def runhypothesis(self, theta0, theta1, bool_print):
        self.predicted = []
        print("Θ₀ = " + str(theta0) + ", Θ₁ = " + str(theta1))
        print('\nactual, predicted')
        for row in self.data:
            x = row[0]
            y = row[1]

            predicted = theta0 + theta1 * x
            self.predicted.append(predicted)
            if bool_print:
                print(', '.join([str(y), str(predicted)]))

        result = 0

        for idx, val in enumerate(self.data):
            result += (self.predicted[idx] - self.data[idx][1]) ** 2

        result = result * 0.5 * len(self.data)

        if bool_print:
            print("\nJ(Θ₀, Θ₁): " + str(result))

        return result

    # def rungradientdescent(self, squarederror):
        # TODO

    def printdata(self):
        print(', '.join(self.header))
        for row in self.data:
            stringrow = [str(row[0]), str(row[1])]
            print(', '.join(stringrow))
        print('')

if (len(sys.argv)) < 2:
    print("No file path given for csv data file")
    sys.exit()

univar = UnivarLinearRegression(sys.argv[1])
univar.printdata()

print("Follow prompts to create and compute a hypothesis function over values in " + sys.argv[1] + ". Type \"quit\" at any point to quit.")

while True:
    try:
        rawtheta0 = raw_input("\nΘ₀: ")
        if rawtheta0 in ["quit", "q"]:
            sys.exit()
        theta0 = float(rawtheta0)

        rawtheta1 = raw_input("Θ₁: ")
        if rawtheta1 in ["quit", "q"]:
            print('')
            sys.quit()
        theta1 = float(rawtheta1)

        univar.runhypothesis(theta0, theta1, True)
    except EOFError:
        print("")
        sys.exit()
    except ValueError:
        print('Please enter a number or type \"quit\" to exit')
