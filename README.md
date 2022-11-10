# ComputerVision

Chrome Dino autoplayer implemented using Opencv and Pillow in order to demonstrate Computer Vision concepts

## Key Notes

This app has been set to HD resolution  (1360x768) for greater compatibility.

### Looking for Dinosaur and Enemies

To found the dino and enemies on the screen, we compare a template against overlapped image regions with the matchTemplate() method using the TM_CCOEFF_NORMED template match mode. With this, we can see that in the player's place there is a bright white spot - the peak of normalized cross-correlation.

#### Normalized cross-correlation

> Correlation is similarity of two signals,vectors etc. Suppose you have vectors:
> 
> ```
>  template=[0 1 0 0 1 0 ]   A=[0 1 1 1 0 0] B =[ 1 0 0 0 0 1]  
> ```
> 
> If you perform correlation between vectors and template to get which one is more similar, you will see A is similar to template more than B because 1's are placed in corresponding indexes.This means the more nonzero elements corresponds the more correlation between vectors is.
> 
> In grayscale images the values are in the range of 0-255.Let's do that :
> 
> ```
> template=[10 250 36 30] A=[10 250 36 30] B=[220 251 240 210] .
> ```
> 
> Here it is clear that A is the same as template but correlation between B and template is bigger than A and template.In normalized cross correlation denumerator part of formula is solving this problem. If you check the formula below you can see that denumerator for B(x)template will be much bigger than A(x)template.
> 
> Formula as stated in opencv documentation :
>
> ![TM_CCOEFF_NORMED](<https://github.com/willkennedyo/ComputerVision/blob/Master/TM_CCOEFF_NORMED.png?raw=true>)

```
See the coeff_norm_test.py file for more details
```

## References

[Reference 1](<https://stackoverflow.com/a/28540675>)

[Reference 2](<https://v-hramchenko.medium.com/normalized-cross-correlation-with-alpha-masked-templates-for-object-detection-c5eb76b16479>)

[Reference app](<https://www.youtube.com/watch?v=mIojvoMRerU&ab_channel=AmritAryal>)