# Day 2

## a)
### Return the minimum sum of the distances to any specific position

Try to align for every position, calculate the sum of distances and return the minimum


## b)
### This time the distance are not linear. Each step is 1 more expensive than the step before.

$$c(1)= 1$$
$$c(2)= 1+2=3$$
$$c(3)= 1+2+3=6$$

the current distance is now no calculated linear, but instead the gaussian sum is used.

$$ \sum_{i=1}^n i= n * (n+1) /2$$