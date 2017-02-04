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
        self.normalize_data()

    def runhypothesis(self, theta0, theta1, bool_print):
        self.predicted = []

        if bool_print:
            print("Θ₀ = " + str(theta0) + ", Θ₁ = " + str(theta1))
            print('\nactual, predicted')

        for row in self.data:
            predicted = theta0 + theta1 * row[0]
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
        theta0, theta1 = 10, 10

        while runs >= 0:
            result0 = 0
            result1 = 0
            for val in self.normalized:
                result0 += (theta0 + theta1 * val[0]) - val[1]
                result0 = theta0 - alpha * (1/(2*float(len(self.normalized)))) * result0
            for val in self.normalized:
                result1 += ((theta0 + theta1 * val[0]) - val[1]) * val[0]
                result1 = theta1 - alpha * (1/(2*float(len(self.normalized)))) * result1

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
            raw_x = raw_input("Enter an input value predict output using the best predictor function: ")
            if raw_x in ["quit", "q"]:
                sys.exit()
            elif raw_x in ["guess", "g"]:
                self.guess_loop()
            x = float(raw_x)
            y = self.best[2] + self.best[3] * x
            print(str(x) + " -> " + str(y))

    def normalize_data(self):
        self.normalized = []
        x = [row[0] for row in self.data]
        y = [row[1] for row in self.data]

        max_x = max(x)
        min_x = min(x)
        diff_x = max_x - min_x

        max_y = max(y)
        min_y = min(y)
        diff_y = max_y - min_y

        for idx, val in enumerate(self.data):
            self.normalized.append([(val[0] - min_x) / diff_x, (val[1] - min_y) / diff_y])
            # print(str(self.normalized[idx][0]) + "\t" + str(self.normalized[idx][1]))
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

                raw_n = raw_input("Amount of learning iterations (default 400): ")
                if raw_n in ["quit", "q"]:
                    print('')
                    sys.quit()
                elif hasbest and raw_alpha in ["done", "d"]:
                    self.predict()
                if raw_n == "":
                    n = 400
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
