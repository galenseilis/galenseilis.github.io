---
title: Gutsick Gibbon and Dr. Carter on Normality and Weighted Averages
date: 2024-06-20 04:51:15
categories: [statistics]
tags: [statistics,probability,normal-distribution,mathematical-statistics,math,maths,moments,expectation,expected-value,average,weighted-average,weighted-arithmetic-mean,arithmetic-mean]
math: true
mermaid: true
---

This post was prompted by the following video by the YouTube channel Gutsick Gibbon:

<iframe width="560" height="315" src="https://www.youtube.com/embed/zzkYmKJ6Sk8?si=WJL1G98hEJaMhzZt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## How good was the sample?

I won't try to cover every aspect of the sample that was under discussion, but both Roohif (embedded below) and Gutsick Gibbon (embedded above) give extensive critiques of various aspects of the studies by Tomkins.

<iframe width="560" height="315" src="https://www.youtube.com/embed/j9XbeckuzwY?si=KKtSOg9vFC6V_rNo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I will just echo that it is imperative that the right statistical population has been sampled from (or at least close enough) in order for the accurate inferences to be made.

### Statistical Precision

According to the univariate [DKW(M) inequality](https://en.wikipedia.org/wiki/Dvoretzky%E2%80%93Kiefer%E2%80%93Wolfowitz_inequality), an [IID](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) sample of size $n$ has a bounded probability of exceeding a given absolute difference between the [empirical cumulative distribution](https://en.wikipedia.org/wiki/Empirical_distribution_function) and the (population) [cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function).

$$\Pr \left( \sup_{x \in \mathbb{R}} \left| F_n(x) - F(x) \right| > \epsilon \right) \leq 2 e^{-2n\epsilon^2}$$

We can convert from this [survival function](https://en.wikipedia.org/wiki/Survival_function) (i.e. the probability of exceedance) to the cumulative probability that the error will not exceed $\epsilon$ by simply taking the complement. This complement rule is a logical consequence of [Kolmogorov's axioms of probability](https://en.wikipedia.org/wiki/Probability_axioms#Kolmogorov_axioms).

$$\Pr \left( \sup_{x \in \mathbb{R}} \left| F_n(x) - F(x) \right| > \epsilon \right) \leq 2 e^{-2n\epsilon^2} \iff 1 - 2 e^{-2n\epsilon^2}  \leq \Pr \left( \sup_{x \in \mathbb{R}} \left| F_n(x) - F(x) \right| \leq \epsilon \right)$$


Here is the calculation, taking $\epsilon := \frac{1}{100}$ for the sake of example:

```python
# Python 3.10.12 [GCC 11.4.0] on linux
>>> import numpy as np
>>> 2 * np.exp(-2 * (18000) * (1 / 100)**2)
0.05464744489458512
>>> 1 - _
0.9453525551054149
```

So when the univariate DKW(M) inequality holds, we can say that a sample size of 18 000 would tells us the probability of our estimate of the cumulative distribution function anywhere being within 1% absolute difference from the population cumulative distribution function is no less than 94.54%.

However, the key assumption that may not hold here is the sample variables being [IID](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables).


## Averages

A part of the what was discussed in the video linked by Gutsick Gibbon was about averages.

### Is the average of a ratio the same as the ratio of the averages?

In short, no, the average of a ratio is not the same as the ratio of an average in general.

$$\mathbb{E} \left[ \frac{Y}{X} \right] \neq \frac{\mathbb{E}[Y]}{\mathbb{E}[X]}$$

Both of these quantities are mathematically valid as long as the expectations are defined and we do not divide by zero.

Even more generally, if $g$ is a non-linear measurable function of the outcome space, then $$\mathbb{E}[f(X)] \neq f(\mathbb{E}[X]).$$ 

### Weighted Average

#### What are weighted averages?

A [weighted (arithmetic) mean](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean#Mathematical_definition) is a [convex combination](https://en.wikipedia.org/wiki/Convex_combination) which we can write in vector form as 

$$\bar x_{\vec w} \triangleq \frac{\vec w \cdot \vec x}{\Vert \vec w \Vert_1}$$

where I have used a [1-norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#Taxicab_norm_or_Manhattan_norm) to collapse the weights vector in the denominator into a scalar. Indeed, we can recognize this as being a [scalar projection](https://en.wikipedia.org/wiki/Scalar_projection#Definition_in_terms_of_a_and_b).

#### Are weighted averages about non-normality?

Given a sample of real numbers $x_1, \ldots, x_n$ and (non-negative) weights $w_1, \ldots, w_n$ the quantity is always defined. It doesn't matter if we're talking about normal distributions, Poisson distributions, or some other distribution whose support is a subset of the real numbers.

Such a quantity may not be defined in the population for similar reasons that the ordinary average may not exist in the population: lack of convergence. The [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy_distribution) and [Pareto distribution](https://en.wikipedia.org/wiki/Pareto_distribution) are examples of distributions where the average does not exist in the population, and I suspect that under mild assumptions that a weighted mean would not either.

Beyond the edge/corner cases, weighted averages are often well-defined. In general they are not about non-normality. In fact, due to normal distributions being [Lévy alpha-stable](https://en.wikipedia.org/wiki/Stable_distribution), weighted averages of independent normal variables has a change of variables that gives us a new normal variable (e.g. see [The Book of Statistical Proofs](https://statproofbook.github.io/P/norm-lincomb.html)).

#### What are weighted averages good for?

The primary reason I would use a weighted average is to produce a [shrunk estimate](https://en.wikipedia.org/wiki/Shrinkage_(statistics)) of the parameter of interest. Wikipedia gives a nice informal description:

> A shrinkage estimator is an estimator that, either explicitly or implicitly, incorporates the effects of shrinkage. In loose terms this means that a naive or raw estimate is improved by combining it with other information. The term relates to the notion that the improved estimate is made closer to the value supplied by the 'other information' than the raw estimate. In this sense, shrinkage is used to regularize ill-posed inference problems.

Additionally, special cases of weighted averaging can formulated as the [law of total expectation](https://en.wikipedia.org/wiki/Law_of_total_expectation), which is sometimes useful.