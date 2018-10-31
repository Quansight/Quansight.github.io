---
layout: post
title: Open Source Directions Episode 3: SymPy
---

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [SymPy](www.sympy.org)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Aaron Meurer, lead developer of the SymPy project and currently based in Albuquerque New Mexico

### Project Overview

SymPy has about 5,100 stars on GitHub and was downloaded from PyPy about 190,000 times last month.

SymPy was started by Ondrej Certik back in 2005, to help him with his work as a physics graduate student.  He primarily needed the ability to work with symbolics in Python.  More and more people contributed things to it to fit their needs, and it has grown into a full featured computer algebra system.

SymPy fills the “symbolic computation” slot of the scientific Python ecosystem. Most libraries in the ecosystem work with numerics, but SymPy works with symbolics.  Symbolic computation is very powerful and can be used in virtually any field that wants a system that can deal with mathematical expressions in a way that the computer actually knows the mathematics of the what is being computed. This is as opposed to “numeric computation”, where the computer simply manipulates numbers without a higher level understanding of the algebraic expressions it is computing.

There are some popular proprietary systems such as Maple and Mathematica, but these can have very expensive licenses, and are closed source, so it can often be opaque as to how it works. These programs also work outside the Python ecosystem.  In terms of Python SymPy is pretty much it.  There are other open source systems written languages like Sage. What makes SymPy unique among the alternatives aside from being written in Python is that it is designed to be used as a library and not just for interactive use. So you can use SymPy interactively like a calculator, but you can also write programs and other libraries that import SymPy and manipulate expressions programmatically.

That programmatic aspect is a key part about what makes SymPy useful for doing things with it downstream.  

SymPy is written in pure Python. It’s only dependency is a library called mpmath, which is a pure Python library for doing arbitrary precision numerics.

Aaron is the lead maintainer, but we have about a dozen people with push access who make and review pull requests. We also have many smaller contributors who contribute maybe once a year or once every few months. In total, SymPy has had 750 people who have contributed at least one patch to the project.

Most of the contributers are from the Scientific Python world.  Most people who are using SymPy are also likely to be using other parts of the scientific stack like NumPy or SciPy.  There are a lot of academic researchers from a variety of fields that make use of SymPy to help them model their domain specific problems mathematically.  One reason for this is that SymPy is very useful for modeling domain specific problems. Quite often these people will contribute back to the project to make it better for the problems they are trying to solve. 

### Demo

The demo functionality is available on the website here: live.sympy.org 

### Roadmap Items

You can find the [roadmap here](www.quansight.com/projects)

1. **The assumptions system:**  The assumptions system handles how SymPy makes assumptions on expressions and does logical inference and simplification based on those assumptions (for instance, assuming an expression is "positive" or "integer"). The SymPy assumptions system currently is inconsistent, as there is a "new" system and an "old" system that need to be properly merged. However, because assumptions affect every part of the codebase, this is a challenging task.  This could be a 6 month to a year project, so we could really use some contributions or funding for this. 

So is the idea here then that the old system would go away, or are there different use cases for this?

We have had an evolving view on this as they develop.  The current view is that the best outcome would be for them to merge in such a way that they can both understand each other.  We would want both syntaxes to remain, and right now this new assumptions is using completely different code than what the old assumptions is using.  If we were to pursue this, there would be a lot of duplication work.  There has been some effort put forth to make it so that the new assumptions can read the old assumptions but not the other way around.  

It looks like in both of these cases you build up a set of assumptions that apply across a number of expressions, but is there a way to try and evaluate within different sets of assumptions?

Another difference with these new assumptions is that the assumptions are separate from the symbol.  With the old way, the assumptions were on the symbol itself.  Something that is possible with the new assumptions is that is easier is deduction.  

2. **Code Generation:** basically this is taking Sumpy expressions and generating C or Fortran or whatever language you want from that expression.   You start with a high level of representation of the expression and work this in Sympy then you use code generation to work down to the numeric code.  Basically, the idea here is to make that pipeline as seamless as possible.  Right now this requires a lot of work to be done in between, and ideally, Sympy could get to the point where it only requires a high-level input.

You can also make mathematical optimizations because Sympy knows your expressions and it can make optimizations that are potentially smarter than a compiler would be able to do because compilers are limited.  This goes beyond common subexpression eliminations, one example would be the simplification function.

3. **Performance:** Sympy is written entirely in Python, so sometimes that can make it slower than desired and this roadmap item is about finding ways to improve performance to overcome that. There are many different avenues to approach this issue, one is benchmarking and profiling to find inefficiency.  Another optimization technique would be to develop more efficient algorithms. There is also a Simengine project that is a very fast symbolic core library written in C++ and the idea here would be that the core engine of Sympy could be swapped out for Simengine.  

4. **SymPy Live and SymPy Gamma:** [SymPy Live](http://live.sympy.org/ ) is a web application that runs a full SymPy Python session in the browser. It can be used standalone and is also used in the [SymPy documentation](http://docs.sympy.org/latest/index.html) to allow readers to interactively evaluate the documentation examples. The backend of SymPy Live needs modernization, and there are several possible improvements for the frontend as well, it is currently run in the Google app engine.  One big limitation of this current setup is the fact that although it acts as a persistent shell, it is not.

[SymPy Gamma](http://gamma.sympy.org/) is a web application that takes a mathematical formula and performs many useful calculations on it, such as plotting, solving, simplifying, and symbolic integration. The goal of SymPy Gamma is to be an open source competitor to products such as like [WolframAlpha](http://wolframalpha.com/). We aim to improve SymPy Gamma by adding more useful computations to the output, and by improving the parsing so that users do not need to know SymPy syntax to use it.

### Viewer Questions

**Q.** Any thoughts on if/how MatchPy (used in a previous GSOC for Rubi integration) can be useful to SymPy?

**A.** Yes, so for those who may not know, Ruby is a mathematical library that does symbolic integration by having a very large table of integrals and then it uses Mathematica's pattern matching abilities to match the input to the table to produce an output.  The goal for the past three years of Google’s summer code projects was to port this to SymPy.  So far the MatchPy library has been very helpful with this.  One of the challenges with MatchPy is finding someone to maintain it because the person who started it has moved on..

---

**Q.** I need to evaluate a Sympy lambda function in parallel using multiprocessing.Pool. Is there a way that the Sympy lambda function could be pickled by default to work when used in Pool?

**A.** Pickling has not been tested recently, but LambdaPhi was refactored a little bit and it no longer gennerates a Lambda function, it now generates a real function.  This update may help with the pickling, but since it is untested we cannot say for sure.  The one thing we do know is that you can recreate the lambda function in each pool rather than pickling it, and that should work without impacting performance.

---

**Q.** Is there a canonical way of declaring a function by parts in Sympy?

**A.** SymPy functions are Python objects, so essentially you can assign expressions to variables. The way you would then build an expression by parts through the assignment of Python variables.  So if there is a right way to do it, then it would be by building an expression using variables that you have assigned and combining those.

---

**Q.** Is there a robust way of finding functional parameters in a Sympy expression?

**A.** To try and find the variables in an expression the best way to do that is by using the free_symbols attribute.  By using that you can see all the variables in the expression listed.

---

**Q.** I would love to know about the status of new-style assumptions and if there's a planned effort to systematically go over the "Wrong Result" tag on GitHub.

**A.** The status of the new assumptions is still somewhat experimental.  It would be recommended to use the old assumptions for now with whatever you are trying to do unless you are willing to try out the new assumptions experimentally.  With the wrong result tag, there haven’t been any plans to implement that, but it would be a good idea and maybe it will be added to the plan.

---

**Q.** Have any security reviews been done on SymPy?

**A.** No, simply because for the most part SymPy does not really have security implications.  There is one function called sympify which takes a string and turns it into a SymPy expression and it is recommended that users only employ this with trusted input because it uses the eval-Python construct underneath and is not secure.  There has been some work done to try and make this safer, but that is not finished yet.

---

**Q.** SymPy is growing a lot in feature surface, for instance, the Physics package. Have you ever considered splitting it into packages?

**A.** There have been discussions about this specifically with the physics package, but there are other modules that this would be very difficult to do that with.  The reason it is possible with physics is that there aren't other parts of SymPy that rely on the physics module.  So far the consensus has been that as long as the code is in SymPy, it will be updated with everything else.  As long as this is the case then any conflicts can be identified once a pull request is made since the physics module is part of what gets pulled, but if it were separate then this would not be the case.  If someone wanted to become a maintainer of a subpackage, then that is an option and making a module independent would be more plausible. 

---

**Q.** Are Graph Algorithms implemented in SymPy so that they always return symbolic expressions, like graph algorithms do in Mathematica?

**A.** There is no graph theory in SymPy, so it is recommended to use Network X or another library like that.  Graph theory is kind of out of the scope of SymPy because it already exists in these other libraries and it does not mesh with the other symbolic parts of SymPy.  If people were able to demonstrate that this is not the case, then it is open for opportunities.  

### Footnotes & Links

* You can find [the current SymPy roadmap here.](www.quansight.com/projects)
* [The SymPy online shell](www.live.sympy.org)
* [SymPy Website](www.sympy.org/en/index.html)
* [GitHub page](https://github.com/sympy/sympy)
