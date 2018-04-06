"""
python implementation of Information Geometry Causal Inference
Python 2.7.12

P. Daniusis, D. Janzing, J. Mooij, J. Zscheischler, B. Steudel,
K. Zhang, B. Scholkopf:  Inferring deterministic causal relations.
Proceedings of the 26th Annual Conference on Uncertainty in Artificial 
Intelligence (UAI-2010).  
http://event.cwi.nl/uai2010/papers/UAI2010_0121.pdf

Shoubo (shoubo.sub AT gmail.com)
08/12/2016

Inputs:
x 			L x 1 observations of x
y 			L x 1 observations of y
refMeasure 	reference measure to use:
			1: uniform
			2: Gaussian
estimator 	estimator to use:
			1: entropy (eq. (12) in [1]),
			2: integral approximation (eq. (13) in [1]).

Outputs: 
f < 0:		the method prefers the causal direction x -> y
f > 0:		the method prefers the causal direction y -> x
"""

from __future__ import division
import numpy as np
from scipy.special import psi

def igci(x, y, refMeasure=1, estimator=2):
	xi = np.real(x)
	yi = np.real(y)

	Lx, dimx = xi.shape
	Ly, dimy = yi.shape

	# ----- input data check -----
	if dimx != 1:
		print 'Dimensionality of x must be 1'
		return None

	if Lx < 20:
		print 'Not enough observations in x (must be > 20)'
		return None

	if dimy != 1:
		print 'Dimensionality of x must be 1'
		return None

	if Ly < 20:
		print 'Not enough observations in y (must be > 20)'
		return None

	if Lx != Ly:
		print 'Lenghts of x and y must be equal'
		return None
	# ----- -----

	if refMeasure == 1:
		xi = (xi - np.min(xi)) / (np.max(xi) - np.min(xi))
		yi = (yi - np.min(yi)) / (np.max(yi) - np.min(yi))
	elif refMeasure == 2:
		xi = (xi - np.mean(xi)) / np.std(xi)
		yi = (yi - np.mean(yi)) / np.std(yi)
	else:
		print 'Warning: unknown reference measure - no scaling applied'

	if estimator == 1:
		x1 = np.sort(xi, axis = 0)
		y1 = np.sort(yi, axis = 0)

		n1 = x1.shape[0]
		hx = 0
		for i in range(0, n1-1):
			delta = x1[i+1,0] - x1[i,0]
			if delta:
				hx = hx + np.log(np.abs(delta))

		hx = hx / (n1 - 1) + psi(n1) - psi(1)

		n2 = y1.shape[0]
		hy = 0
		for i in range(0, n2-1):
			delta = y1[i+1,0] - y1[i,0]
			if delta:
				hy = hy + np.log(np.abs(delta))

		hy = hy / (n2 - 1) + psi(n2) - psi(1)

		f = hy - hx
		return f

	elif estimator == 2:
		a = 0
		b = 0

		ind1 = np.argsort(xi, axis=0)
		ind2 = np.argsort(yi, axis=0)

		for i in range(0, Lx-1):
			X1 = xi[ind1[i,0], 0]
			X2 = xi[ind1[i+1,0], 0]
			Y1 = yi[ind1[i,0], 0]
			Y2 = yi[ind1[i+1,0], 0]
			if (X1!=X2) & (Y1!=Y2):
				a += np.log( np.abs((Y2 - Y1) / (X2 - X1)) )

			X1 = xi[ind2[i,0], 0]
			X2 = xi[ind2[i+1,0], 0]
			Y1 = yi[ind2[i,0], 0]
			Y2 = yi[ind2[i+1,0], 0]
			if (X1!=X2) & (Y1!=Y2):
				b += np.log( np.abs((X2 - X1) / (Y2 - Y1)) )

		f = (a-b) / Lx
		return f

	else:
		print 'Unknown estimator'
		return None
