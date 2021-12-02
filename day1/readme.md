# Day 1

## a)
### Count how often the current number is smaller than the previous one.

one dragger is used to reference the value before, then the current element is compared to the dragger (1 is added to the counter if current>dragger) and dragger is set to the current element.

## b)
### Count how often the sum of the current 3 elements is smaller than the sum of the next 3 elements (going only one, not three elements forward)

now we use 3 draggers and the current element. Then two sums are computed and compared.


## Problems I had to tackle:
Remember to cast to int!

"998">"1004" but 998<1004
