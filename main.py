import linear_algebra as la
import statistics as st
import probability_theory as pt
import matplotlib.pyplot as plt
import gradient_descent as gd

def task(xs, ps):
    print(pt.expected_value(xs,ps))
    print(pt.variance(xs,ps))
    pt.draw(xs,ps)

    for i in ps:
        print(i)

def binominal(xs, p):
    n = len(xs)
    return [pt.binominal_distribution(x, n - 1, p) for x in xs]

def draw_binominal(xs, p):
    ps = binominal(xs, p)
    pt.draw(xs, ps)

def f(x):
    if x < 0:
        return 0
    if x > 3:
        return 1
    return (x ** 2) / 9

def deriviative(x):
    return 2 * x

def square(x):
    return x * x


xs = [x for x in range(-10, 11)]
actuals = [deriviative(x) for x in xs]
estimates = [gd.difference_quotient(square, x, 0.0001) for x in xs]

estimate = gd.estimate_gradient(square, xs, 0.0001)

print(xs)
print(actuals)
print(estimates)

print(estimate)




