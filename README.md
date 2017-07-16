### Univariate Linear Regression in Python

Building simple machine-learning assisted predictor functions has never been so fun, or hacky!


#### Example csv training set
```
x,y
18.4591171940333,102.295585970166
5.31230719747555,36.5615359873778
82.5034903621521,422.51745181076
21.5405894435364,117.702947217682
42.8181377673104,224.090688836552
```

#### Example usage

```
python univariate_linear_regression.py plus2mult5.csv
```

#### Explanation
The csv file above contains some randomly generated numbers and the corresponding result of adding 2 to each input and multiplying by 5.

By running the regression program against the csv with an `alpha` value of `0.0001` and the default amount of iterations (10000000), we see the following result:

```
actual, predicted
102.29558597, 102.29558597
36.5615359874, 36.5615359874
422.517451811, 422.517451811
117.702947218, 117.702947218
224.090688837, 224.090688837
```

From these results we can see that we have built a function that can very accurately recreate our original data transformation. We can type `done` to enter prediction mode and generate expected output for novel input values, e.g.
```
Enter an input value to predict output using the best predictor function: 100
100.0 -> 510.0
Enter an input value to predict output using the best predictor function: 93618235.12352193
93618235.1235 -> 468091185.618
```
