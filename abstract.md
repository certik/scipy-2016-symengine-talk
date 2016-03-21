# Title

SymEngine, a fast symbolic manipulation library

# Authors

Ondřej Čertík, Isuru Fernando

# The Brief Description

The goal of [SymEngine](https://github.com/symengine/symengine) is to be the
fastest C++ symbolic manipulation library (opensource or commercial),
compatible with SymPy, that can be used from many languages (Python, Ruby,
Julia, ...). We will present the current status of development, how things are
implemented internally, why we chose C++, benchmarks, and examples of usage
from Python (SymPy and Sage), Ruby and Julia.

# The Detailed Abstract

## Motivation

SymPy is a widely used symbolic manipulation library in Python, which
implements most of the features that are expected in a mature computer algebra
system. While SymPy turns out to be very useful for many applications, one of
the long term problems with SymPy is that the speed might be insufficient when
handling of very large expressions is required (and for this reason Sage uses
SymPy for many features, but uses a modification of the GiNaC library for basic
symbolics). Another problem with SymPy is that due to being written in Python,
it can be cumbersome to use from other languages like Julia, Ruby, JavaScript
or C++, because it requires, say, a Python to Julia bridge, which might not
always be robust and which inflicts additional overhead.

For these reasons, we implemented an open source C++ symbolic manipulation
library called SymEngine, with the goal of being the fastest library for
symbolic manipulation (opensource or commercial), and allowing natural wrappers
to other languages like Python (the most mature wrapper), Ruby, Julia and
others.

## Methods

SymEngine takes advantage of C++ to be able to customize data structures and
memory accesses.

## Results

We show benchmarks against other computer algebra systems (opensource and
commercial) as well as examples of usage from Python (SymPy and Sage), Ruby and
Julia. We will present a roadmap how to port SymPy on top of SymEngine.

## Conclusion

SymEngine should fix the slowness of SymPy, while providing a familiar
interface, and at the same time allows many languages to naturaly use it.

## Resources

* SymEngine C++ library: https://github.com/symengine/symengine
* SymEngine Python wrappers (with SymPy and Sage integration): https://github.com/symengine/symengine.py
* SymEngine Ruby wrappers: https://github.com/symengine/symengine.rb
* SymEngine Julia wrappers: https://github.com/symengine/symengine.jl
* SymPy: http://sympy.org/

Evidence of public speaking ability: The first author has given talks at SciPy
2007 and 2009, EuroSciPy 2008 and other conferences (PMAA'08, CSE09, FEMTEC
2009, ESCO 2010, APS California-Nevada Section 2011, ...), we held a SymPy
tutorial at SciPy 2013, and he has given other talks, tutorials and seminars at
various places (Los Alamos National Lab, Lawrence Berkeley National Lab, Lawrence Livermore National Lab, CU Denver, University of Nevada Reno, ...).
