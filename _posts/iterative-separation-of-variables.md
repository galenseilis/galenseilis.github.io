---
title: Iterated Separation of Variables
date: 2023-02-20 13:29:02
categories: [math,differential-equations,separation-of-variables]
tags: [math,differential-equations,separation-of-variables,product-differential-equation,chain-rule,fundamental-theorem-of-calculus]
math: true
---

The following is something I developed during my MSc thesis, which was motived by the Agnesian operators I defined there. It probably isn't novel, and comes about from well-known results. But it may be novel to someone new to differential equations.

> **Proposition** (Iterated Separation of Variables)
>
> Suppose we have a product differential equation of the form
>
> $$\prod_{j=1}^n \frac{dx_j}{dt} = F(x_1, \ldots, x_n, t)$$
>
> which can be written in the form of 
>
$$\prod_{j=1}^n \frac{dx_j}{dt} = h(x_1, \ldots, x_n)g(t)$$ 
> 
> where $h$ and $g$ are suitably-integrable. Let us suppose that $h(x_1, \ldots, x_n) \neq 0$. Then we can obtain the following rearrangement 
>
>$$\frac{1}{h(x_1, \ldots, x_n)} dx_1 \ldots dx_n = g(t) \underbrace{dt \ldots dt}_{n}.$$
>
> **Proof**
>
> Begin by supposing that the expression $$\prod_{j=1}^n \frac{dx_j}{dt} = h(x_1, \ldots, x_n)g(t)$$ has been obtained.
>
>Assuming $h(x_1, \ldots, x_n) \neq 0$, then we can obtain 
>
> $$\frac{1}{h(x_1, \ldots, x_n)} \prod_{j=1}^n \frac{dx_j}{dt}  = g(t).$$
>
> Integrating with respect to $t$ iteratively $n$ times we obtain 
> 
> $$\underbrace{\int \cdots \int}_{n} \frac{1}{h(x_1, \ldots, x_n)} \prod_{j=1}^n \frac{dx_j}{dt} \underbrace{dt \ldots dt}_{n} = \underbrace{\int \cdots \int}_{n} g(t) \underbrace{dt \ldots dt}_{n}.$$
>
> Taking $H(x_1, \ldots, x_n)$ to be the $n$th [antiderivative](https://en.wikipedia.org/wiki/Antiderivative) of $h(x_1, \ldots, x_n)^{-1}$, and using the [chain rule of derivatives](https://en.wikipedia.org/wiki/Chain_rule) then 
>
> $$\frac{d^n}{dt^n} H(x_1, \ldots, x_n) = \frac{1}{h(x_1, \ldots, x_n)} \Xi (x_1, \ldots, x_n) \prod_{j=1}^n \frac{dx_j}{dt}$$
> 
> where $\Xi (x_1, \ldots, x_n)$ is a factor that fills in the rest of [Faà di Bruno's formula](https://en.wikipedia.org/wiki/Fa%C3%A0_di_Bruno%27s_formula) generalized to multiple arguments.
>
> So the left-hand integral is 
>
> $$\underbrace{\int \cdots \int}_{n} \frac{1}{h(x_1, \ldots, x_n)} \Xi (x_1, \ldots, x_n) \prod_{j=1}^n \frac{dx_j}{dt} \underbrace{dt \ldots dt}_{n} = \underbrace{\int \cdots \int}_{n} \frac{d^n}{dt^n} H(x_1, \ldots, x_n) \underbrace{dt \ldots dt}_{n} = $$
>
> which by the [fundamental theorem of calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus) entails that
>
> $$\underbrace{\int \cdots \int}_{n} \frac{1}{h(x_1, \ldots, x_n)} dx_1 \ldots dx_n = H(x_1, \ldots, x_n) + C$$
>
> where $C$ is a [constant of integration](https://en.wikipedia.org/wiki/Constant_of_integration). 
> 
> This finally gives us
>
>$$\underbrace{\int \cdots \int}_{n} \frac{1}{h(x_1, \ldots, x_n)} dx_1 \ldots dx_n = \underbrace{\int \cdots \int}_{n} g(t) \underbrace{dt \ldots dt}_{n}.$$ $\blacksquare$

I believe using substitution can acheive a more general result starting from the form

$$\prod_{j=1}^n \frac{dx^k_j}{dt^k} = h(x_1, \ldots, x_n) g(t)$$

but I will leave that as an exercise for the reader.

# Citation

```latex
@MISC {seilis20230220,
    TITLE = {Iterated Separation of Variables},
    AUTHOR = {Galen Seilis (https://galenseilis.github.io/about/)},
    HOWPUBLISHED = {Galen's Blog},
    NOTE = {URL:https://galenseilis.github.io/posts/iterative-separation-of-variables/},
    EPRINT = {https://galenseilis.github.io/posts/iterative-separation-of-variables/},
    URL = {https://galenseilis.github.io/posts/iterative-separation-of-variables/}
}
```