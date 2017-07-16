# -*- coding: utf-8 -*-

import csv
import sys
import math

class UnivarLinearRegression(object):

    def __init__(self, filepath):
        if filepath == "":
            raise Exception("No csv file path given")
        raw = csv.reader(open(filepath), delimiter = ',')
        self.header = raw.next()
        self.data = []
        self.best = None
        for row in raw:
            self.data.append([float(row[0]), float(row[1])])

    def runhypothesis(self, theta0, theta1, bool_print):
        self.predicted = []

        if bool_print:
            print("Θ₀ = " + str(theta0) + ", Θ₁ = " + str(theta1))
            print('\nactual, predicted')

        for row in self.data:
            x = row[0]
            predicted = theta0 + (theta1 * x)
            self.predicted.append(predicted)
            if bool_print:
                print(', '.join([str(row[1]), str(predicted)]))

        result = 0

        for idx, val in enumerate(self.data):
            result += (self.predicted[idx] - self.data[idx][1]) ** 2

        result = result * 0.5 * float(len(self.data))

        if bool_print:
            print("\nJ(Θ₀, Θ₁): " + str(result))

        return result

    def run_gradient_descent(self, runs, alpha):
        theta0, theta1 = 0, 0
        m = (float(len(self.data)))

        while runs >= 0:
            total_error = 0
            for val in self.data:
                x = val[0]
                y = val[1]
                hypothesis = theta0 + (theta1 * x)
                total_error += hypothesis - y

            result0 = theta0 - (alpha * (1.0/m) * total_error)

            total_error = 0
            for val in self.data:
                x = val[0]
                y = val[1]
                hypothesis = theta0 + (theta1 * x)
                total_error += (hypothesis - y) * x

            result1 = theta1 - (alpha * (1.0/m) * total_error)

            runs -= 1
            theta0 = result0
            theta1 = result1

        result = self.runhypothesis(theta0, theta1, True)
        if not math.isnan(result):
            if self.best is None or self.best[0] > result:
                self.best = [result, alpha, theta0, theta1]

    def predict(self):
        print("Entering prediction mode. To continue function generation, type \"guess\": ")
        while True:
            raw_x = raw_input("Enter an input value to predict output using the best predictor function: ")
            if raw_x in ["quit", "q"]:
                sys.exit()
            elif raw_x in ["guess", "g"]:
                self.guess_loop()
            x = float(raw_x)
            y = self.best[2] + self.best[3] * x
            print(str(x) + " -> " + str(y))

    def printdata(self):
        print(', '.join(self.header))
        for row in self.data:
            stringrow = [str(row[0]), str(row[1])]
            print(', '.join(stringrow))
        print('')

    def guess_loop(self):
        print("Follow prompts to find the best prediction function over values in " + sys.argv[1] + ". Type \"quit\" at any point to quit.")

        while True:
            hasbest = self.best is not None
            if hasbest:
                print("Best guess for learning rate so far: " + str(self.best[1]))
                print("Type \"done\" at any point to use the best guess to make predictions.")
            try:
                raw_alpha = raw_input("\nα (learning rate): ")
                if raw_alpha in ["quit", "q"]:
                    sys.exit()
                elif hasbest and raw_alpha in ["done", "d"]:
                    self.predict()
                alpha = float(raw_alpha)

                raw_n = raw_input("Amount of learning iterations (default 10000000): ")
                if raw_n in ["quit", "q"]:
                    print('')
                    sys.quit()
                elif hasbest and raw_alpha in ["done", "d"]:
                    self.predict()
                if raw_n == "":
                    n = 10000000
                else:
                    n = int(raw_n)

                univar.run_gradient_descent(n, alpha)
            except EOFError:
                print("")
                sys.exit()
            except ValueError:
                print('Please enter a number or type \"quit\" to exit')
            except OverflowError:
                print('Please choose smaller numbers')

if (len(sys.argv)) < 2:
    print("No file path given for csv data file")
    sys.exit()

univar = UnivarLinearRegression(sys.argv[1])
univar.printdata()
univar.guess_loop()
