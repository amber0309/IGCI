# Information Geometric Causal Inference (IGCI)

Python version of the original MATLAB code of [Information Geometric Causal Inference](http://event.cwi.nl/uai2010/papers/UAI2010_0121.pdf) (IGCI).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* NumPy
* SciPy

We test the code using **Anaconda 4.3.30 64-bit for python 2.7** on windows. Any later version should still work perfectly.

## Apply on your data

### Usage

Import IGCI using

```
from IGCI import igci
```

Apply IGCI on your data
```
f = igci(x, y, refMeasure=1, estimator=2)
```

### Description

Input of function **igci()**

| Argument  | Description  |
|---|---|
|x | Obeservations of the first variable. L by 1 numpy array.|
|y | Obeservations of the second variable. L by 1 numpy array.|
|refMeasure | 1 - uniform reference measure;<br/> 2 - Gaussian reference measure |
|estimator | 1 - entropy;<br/> 2 - integral approximation |

Output of function **igci()**

| Argument  | Description  |
|---|---|
|f  |f < 0 - x causes y;<br/> f > 0 - y causes x;<br/> None - incorrect inputs|

## Authors

* **Shoubo Hu** - shoubo DOT sub AT gmail DOT com

See also the list of [contributors](https://github.com/amber0309/IGCI/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
