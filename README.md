# Calculate Faulhaber's formula figuratively

## Background   
The following message is picked up from the wikipedia:
> ## Faulhaber's formula
>In mathematics, Faulhaber's formula, named after Johann Faulhaber, expresses the sum of the p-th powers of the first n positive integers.https://en.wikipedia.org/wiki/Faulhaber%27s_formula

>![](https://wikimedia.org/api/rest_v1/media/math/render/svg/cdfa28bc350e73f808fc51da16d427df1a45fd28)

> ## Figurate number
>The term figurate number is used by different writers for members of different sets of numbers, generalizing from triangular numbers to different shapes (polygonal numbers) and different dimensions (polyhedral numbers). https://en.wikipedia.org/wiki/Figurate_number

>![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Nicomachus_theorem_3D.svg/220px-Nicomachus_theorem_3D.svg.png)

## My method
My English is poor,but it's luckily what I am going to explain are mostly shown by pictures.

## Express regcursively
> S3(n) means the sum of the p-th powers which p equals -3

S3(n) = [(1+3*n)*S2(n)]/(4) + 0.125*S1 + 0.125*S2

S4(n) = [(1+4*n)*S3(n)]/(5) + 0.200*S1 + 0.400*S2 + 0.200*S3

S5(n) = [(1+5*n)*S4(n)]/(6) + 0.194*S1 + 0.667*S2 + 0.722*S3 + 0.250*S4

S6(n) = [(1+6*n)*S5(n)]/(7) + 0.143*S1 + 0.786*S2 + 1.429*S3 + 1.071*S4 + 0.286*S5

S7(n) = [(1+7*n)*S6(n)]/(8) + 0.104*S1 + 0.750*S2 + 2.021*S3 + 2.500*S4 + 1.438*S5 + 0.312*S6

S8(n) = [(1+8*n)*S7(n)]/(9) + 0.111*S1 + 0.704*S2 + 2.333*S3 + 4.148*S4 + 3.889*S5 + 1.815*S6 + 0.333*S7

S9(n) = [(1+9*n)*S8(n)]/(10) + 0.130*S1 + 0.800*S2 + 2.600*S3 + 5.600*S4 + 7.420*S5 + 5.600*S6 + 2.200*S7 + 0.350*S8
