---
layout: post
title: Episode 17 - TensorFlow - Open Source Directions
author: bsodenkamp
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/-fiEzhva2ZY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [TensorFlow](https://www.tensorflow.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** Carol Willing
* **Guest 1:** Paige Bailey: is a TensorFlow developer advocate at Google.  

### Project Overview

Tensor flow is an open source machine learning library for research and production.
It has 123,000+ stars on Github and about 41 million downloads/month across PyPI and conda as reported at the TensorFlow Dev Summit February 2019.

TensorFlow has been used in different iterations at Google for about 15 years. It used to affectionately be called disbelief which eventually evolved into TensorFlow.  Every application that you are using that incorporates AI in some way from Google then you are basically guaranteed that the algorithm being used is from TensorFlow.  It was very valuable from the beginning and was fun to use as well.  It has remained a stable production system for deploying machine learning models.  About three years ago there was a guy named Jeff Dean, known as the Chuck Norris of deep learning, who came on the scene as director of Google AI and Google Brain and decided to make TensorFlow an open source software.  They had to make sure that it was disconnected from sensitive Google systems but were eventually successful in bringing TensorFlow into the open source world. Nobody was quite able to anticipate the level of excitement which came when it was released to the public, but it grew into a mainstream software overnight.  If you want to use it for boosted trees, logistic regression, linear regression, or ODE linear regression modeling, then the option is available with TensorFlow. There was a desire for Google to share this project with the world because of how helpful it has been to them.


There are some similar projects out there which help with machine learning, but the TensorFlow organization on GitHub has about 70 sub-repos.  With this in mind you could then say that while there are a lot of projects out there, many of them are under the TensorFlow umbrella.  You have core TensorFlow which is the heart of the numerical modeling, then you have projects like TensorFlow.js which is more for deep learning in browsers or even servers now.  There is also TensorFlow Light which allows you to deploy models to mobile devices and embedded devices.  Things like TF Federated and Probability just help to fill in more of the space and the list goes on.  The point of explaining this is that there are likely other tools that people have made to address parts of what TensorFlow can do, but nothing that is the entire big box.  Some of these would be things like PyTorch, Chainer, MXNet, Scikit-Learn, or even some packages in R.  There are a lot of great projects out there with fantastic capabilities and communities, but nothing that specifically covers all the parts that TensorFlow does with its “big box”.

TensorFlow is not just for deep learning, but it also allows you to construct neural networks in straight forward ways.  Keras was a high-level API that was created by someone named François Chollet, who now works at Google, and now that tooling he created is enabled in TensorFlow which has enabled the creation of neural networks with as little as ten lines of code.  There is also a Python API which enables the user to do the functionality, and that works alongside C++ API but it is recommended to use the Python API if possible.  If a user is ever confused about which API to use, they are encouraged to reach out to Paige on [Twitter](https://twitter.com/DynamicWebPaige) and she can point you in the right direction.  Anyone who is familiar with Python should be pretty happy, but it is compatible with a number of other languages.  It is set up to work with anything from Rust to Javascript, Java to C++.

It is very difficult to maintain this project, and it is an effort between internal teams and the ever-growing open community.  Something that was started last year came from the Kubernetes community and they are called RFCs.  Any changes to the API require the submission of a design document that is announced and posted to GitHub for open review during a couple of weeks.  There are also special interest groups, mailing lists, and forum spaces where people can meet to talk about the different functionalities for different aspects of the TensorFlow sphere.  Having a multiplicity of discourse channels allows for community organization and has promoted interconnectivity and effectiveness. 

[TensorFlow.org](https://www.tensorflow.org/) is the best place to stay up to date on the latest developments, and it was actually recently re-vamped.  There is an [announcement section](https://medium.com/tensorflow/tagged/announcements) and you can also subscribe to the mailing list to keep up to date as well.  

Within the last three years and partially thanks to the availability of TensorFlow, there has been a large expansion of adoption for people in many areas of development to begin using machine learning and deep learning tools.  App developers have become part of this increase, and even kids are able to use this to build autonomous cars, so the horizon of users has broadened greatly.  Everything from academic writing to application developers have found ways to make use of this new software access.  This is great because a lot of effort has gone into making things more useful through TF Light and TF.js.  Scientists are benefiting but artists and musicians have even started to use this to generate things like synthetic rose petals or generated instrumental accompaniment to guitar music.  It has even been used to write blog articles based on sample text.

Since TensorFlow is used globally, there is some natural diversity which has come to the community.  There are users on every continent including Antarctica, and so reps from TensorFlow can go and participate in conferences in all kinds of places including China and Africa.  Speaking of Africa, Google just opened a new Google Brain office there as well, which is added to the list of India and Europe locations.  Google is also pursuing an AI ethics policy called [PAIR](https://twitter.com/StanfordHAI/status/1107627992816275456): people in AI research.  This is a program that every Google AI project must conform to.  The “what if” tool is another way that a project can be audited to see if there are any groups which are underrepresented or biased.  

### Demo

[Demo at timestamp 31:04](https://youtu.be/-fiEzhva2ZY?t=1864)
[TensorFlow introduction](https://www.tensorflow.org/learn)

### Roadmap Discussion

Just recently a new version of TensorFlow 2.0 was just announced and it is focused on developer productivity, ease of use, and building machine learning models that you can deploy anywhere.  You should be able to train it on any sort of hardware architecture.  If, for example, you tried to use TensorFlow in 2015 when it first went open source it was pretty painful to use.  At that time it took about 300 lines of boilerplate code to do anything useful.  TensorFlow was essentially left without the higher level tooling that you could find with Scikit-Learn or Pandas.  Since that time TensorFlow has moved to Keras which has dramatically improved things.  It is currently the recommendation for any user as the higher level API.  In addition to the ten line programming, users also have the option to subclass which gives more control and granularity.  If people need access to even lower level operations, then the raw operations are also exposed.

Another area of development is the building out of performance for CPUs, GPUs, and TPUs.  There is not TPU support for TensorFlow 2.0 at the moment, so that will be a major part of the work going forward.  As TensorFlow is used on small devices and in browsers, there will also be more work to expand its usefulness in those unexpected spaces.  This will mean building out TensorFlow.js and TensorFlow Light.  They have the ability to embed tensorboard within collaboration notebooks in Jupyter notebooks now, so instead of having to use local hosting as an improvisation, you can just have it in an environment that you are familiar with.  

Anybody is welcome to help in any of these areas, and the TensorFlow team would be delighted to have helpers.  They would never turn down an open source contributor.  To get in contact and begin helping out with the TensorFlow project, you can visit their GitHub [community page](https://github.com/tensorflow/community).  Code contribution is great, but documentation and graphic design or any other contributions are also welcome.  

 ### Viewer Questions

**Q.** Are there plans to support Metal, or officially support ROCm (the latter of which has already been upstreamed) so as not to force people to use CUDA?

**A.**  I don’t have an exact answer for that, but checking GitHub, this is something that others have expressed interest in.  There is a merged pull request to introduce support for the ROCM platform, but that is the idea behind it.  If you notice a gap, especially on popular, external platforms then feel free to file an issue.

### Footnotes & Links

* TensorFlow Forum [here](https://www.tensorflow.org/community/forums)
* [TensorFlow Website](https://www.tensorflow.org/)
* [GitHub page](https://github.com/tensorflow)
* [Gitter Channel](https://gitter.im/tensorflow/)

