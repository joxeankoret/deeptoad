# Basic Usage #

DeepToad is a command line tool. It expects to receive, at least, one file or directory. Given a file, the tool prints out the generated signature:

```
$ deeptoad voices.jpg 
OzvGxsbGfX19faWlpaWWlpaWnZ2dnaCg;xsZ9faWllpadnaCgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;voices.jpg
```

The generated signature has 4 fields: the signature, the simple signature, the reverse signature and the filename. Now, I will execute the tool passing the current directory as argument:

```
$ deeptoad .
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;./voices.jpg
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;./test.jpg
```

Now we see only one "signature". What happened? When running deeptoad in directory mode (i.e., passing as argument a directory) deeptoad tries to clusterize all the files found (recursively) and shows the signature that best clusterizes them all. If you just want to get the 3 signatures of every file pass the command line argument -p:

```
$ deeptoad -p .
Signature;Simple Signature;Reverse Signature;Filename
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;fcalfZalnZagnVSgpVS8pc68284s22ws;fO2gfL6gWb4JWZQJJ5SgJxugnhuknlek;./test.jpg
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;xn2llp2gVKW8ztssbApeYdvcpG/KwW4K;6RaIeTsW4oGACL5swVR4GGd1hX2kGtpd;./voices.jpg
```

If you just want to compare all the files in a directory pass the argument "-c":

```
$ deeptoad -c .
File './test.jpg' matches './voices.jpg' (100.00%)
```

The percent shown is relative to the [Levenshtein distance](http://en.wikipedia.org/wiki/Levenshtein_distance) between the hashes.

## Working with malware samples ##

The tool deeptoad was created, mainly, to clusterize big malware batteries so, it's time now to start working with them ;) I will use, in example, a bunch of malwares called by some AV companies as "Packer Krap". I will use deeptoad just to see how similars are them:

```
$ deeptoad kraps/
gJeAgCCAICDlIOXlaeVpadVp1dU+1T4+;./26ec20d25d1df6d84557304931d9e253.file
Ye9hYdNh09Om06ami6aLizGLMTEDMQMD;./268ea7eff324470892c91cea4cd3b408.file
Ye9hYdNh09Om06ami6aLizGLMTEDMQMD;./2624ffb6c9edc1ed34168eadc366e7b5.file
XP5cXBVcFRVJFUlJEkkSEn4Sfn5bfltb;./6a9fd93f48e81ecbaf14b84a28b58db5.file
XP5cXBVcFRVJFUlJEkkSEn4Sfn5bfltb;./5cf77cb17d24ff935ce37116a78042de.file
XP5cXBVcFRVJFUlJEkkSEn4Sfn5bfltb;./647a25e96e9bce5d13c20d1d0ec1fd6c.file
XP5cXBVcFRVJFUlJEkkSEn4Sfn5bfltb;./5d7bbb216e430fdad7cc9697d7e8427c.file
XP5cXBVcFRVJFUlJEkkSEn4Sfn5bfltb;./60287028061fbdb5591aaead0ccfb34d.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./32d7d334fc95b38aa4079d86e624c534.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./2a2cec153f07ebd07f8ba250a8cd19b6.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./296368123a71e873bc03b7a0d0f1d1bb.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./a0d0f55fbd412de49f17b9f21d5470e2.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./b2cec72ba2c13018bd0b529ee14effbc.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./b39915b0075908b203d6020c13a67621.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./89e5159f8fe45ebffc77c0ac3729a5a0.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./83470ee9856d33f11dd01f5d9468d13e.file
zPRkzOhkfujzflvzy1vwy63wda1AdaZA;./585442eaec327654a5b87770896f1c33.file
HX9YHYpYJoqXJmWXI2VYI1VYSVUuSdYu;./27761d6676940c51232dcc51139002eb.file
HX9YHYpYJoqXJmWXI2VYI1VYSVUuSdYu;./eff5b36bd4e48c3bc4d2f192c6f30c0d.file
HX9YHYpYJoqXJmWXI2VYI1VYSVUuSdYu;./4e9db696938b817da5153f08f9be920b.file
HX9YHYpYJoqXJmWXI2VYI1VYSVUuSdYu;./27e2c599d01e84765fad7145b55c2a61.file
HX9YHYpYJoqXJmWXI2VYI1VYSVUuSdYu;./7bc969a74937cadf9fa21fdf282ecf30.file
m3Uzm/czs/dYs/tYDPuzDJmzwpn3wuH3;./d5ab3f4161ab49f4f51c1e1d92fb098a.file
pGKkpGakZmbcZtzcX9xfXyNfIyNhI2Fh;./89447f6a6fe74cb9ed0e75e6aaabaed9.file
pGKkpGakZmbcZtzcX9xfXyNfIyNhI2Fh;./6e34bfe984b342a7211287d74116a888.file
```

We clearly see that almost all the 25 samples can be grouped in 5 groups so it seems that they are very similars. It will not be very hard to write a detection code for them ;)

I will play a bit with the samples just to show you more options of deeptoad. By default, all available algorithms used in deeptoad operate over 512 bytes blocks, however, we may want to change the block size. To change it pass the parameter "-b=" and the desired block size as in the following example:

```
$ deeptoad -b=32 .
ProcProcessing file ./6e34bfe984b342a7211287d74116a888.file ...    
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./32d7d334fc95b38aa4079d86e624c534.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./26ec20d25d1df6d84557304931d9e253.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./6a9fd93f48e81ecbaf14b84a28b58db5.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./5cf77cb17d24ff935ce37116a78042de.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./89447f6a6fe74cb9ed0e75e6aaabaed9.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./d5ab3f4161ab49f4f51c1e1d92fb098a.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./27761d6676940c51232dcc51139002eb.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./647a25e96e9bce5d13c20d1d0ec1fd6c.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./eff5b36bd4e48c3bc4d2f192c6f30c0d.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./2a2cec153f07ebd07f8ba250a8cd19b6.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./296368123a71e873bc03b7a0d0f1d1bb.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./4e9db696938b817da5153f08f9be920b.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./27e2c599d01e84765fad7145b55c2a61.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./7bc969a74937cadf9fa21fdf282ecf30.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./a0d0f55fbd412de49f17b9f21d5470e2.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./b2cec72ba2c13018bd0b529ee14effbc.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./b39915b0075908b203d6020c13a67621.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./89e5159f8fe45ebffc77c0ac3729a5a0.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./5d7bbb216e430fdad7cc9697d7e8427c.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./60287028061fbdb5591aaead0ccfb34d.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./83470ee9856d33f11dd01f5d9468d13e.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./268ea7eff324470892c91cea4cd3b408.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./2624ffb6c9edc1ed34168eadc366e7b5.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./585442eaec327654a5b87770896f1c33.file
ASABAcIBwsLswuzsleyVla6Vrq58rnx8;./6e34bfe984b342a7211287d74116a888.file
```

Uhmm... Changing the block size to 32 bytes we get a hash that clusterizes all the files. I will try now with other algorithms. By default, deeptoad uses the "default hashing algorithm" but there are other 3 algorithms very similars available. Let's suppose we want to hash gigabytes of malware samples, it would take a very long while with the default algorithm so we may want to try to clusterize the files using the fastest (but weaker) "fast version" of the algorithm:

```
ASDMwoBDHatv7M+ukXCVYb183z4;./32d7d334fc95b38aa4079d86e624c534.file
ASDMwoBDHatv7M+ukXCVYb183z4;./2a2cec153f07ebd07f8ba250a8cd19b6.file
ASDMwoBDHatv7M+ukXCVYb183z4;./296368123a71e873bc03b7a0d0f1d1bb.file
ASDMwoBDHatv7M+ukXCVYb183z4;./a0d0f55fbd412de49f17b9f21d5470e2.file
ASDMwoBDHatv7M+ukXCVYb183z4;./b2cec72ba2c13018bd0b529ee14effbc.file
ASDMwoBDHatv7M+ukXCVYb183z4;./b39915b0075908b203d6020c13a67621.file
ASDMwoBDHatv7M+ukXCVYb183z4;./89e5159f8fe45ebffc77c0ac3729a5a0.file
ASDMwoBDHatv7M+ukXCVYb183z4;./83470ee9856d33f11dd01f5d9468d13e.file
ASDMwoBDHatv7M+ukXCVYb183z4;./585442eaec327654a5b87770896f1c33.file
ASDCgMkIywrsj3EzQfQ;./26ec20d25d1df6d84557304931d9e253.file
ASDCgMkIywrsj3EzQfQ;./6a9fd93f48e81ecbaf14b84a28b58db5.file
ASDCgMkIywrsj3EzQfQ;./5cf77cb17d24ff935ce37116a78042de.file
ASDCgMkIywrsj3EzQfQ;./89447f6a6fe74cb9ed0e75e6aaabaed9.file
ASDCgMkIywrsj3EzQfQ;./d5ab3f4161ab49f4f51c1e1d92fb098a.file
ASDCgMkIywrsj3EzQfQ;./27761d6676940c51232dcc51139002eb.file
ASDCgMkIywrsj3EzQfQ;./647a25e96e9bce5d13c20d1d0ec1fd6c.file
ASDCgMkIywrsj3EzQfQ;./eff5b36bd4e48c3bc4d2f192c6f30c0d.file
ASDCgMkIywrsj3EzQfQ;./4e9db696938b817da5153f08f9be920b.file
ASDCgMkIywrsj3EzQfQ;./27e2c599d01e84765fad7145b55c2a61.file
ASDCgMkIywrsj3EzQfQ;./7bc969a74937cadf9fa21fdf282ecf30.file
ASDCgMkIywrsj3EzQfQ;./5d7bbb216e430fdad7cc9697d7e8427c.file
ASDCgMkIywrsj3EzQfQ;./60287028061fbdb5591aaead0ccfb34d.file
ASDCgMkIywrsj3EzQfQ;./268ea7eff324470892c91cea4cd3b408.file
ASDCgMkIywrsj3EzQfQ;./2624ffb6c9edc1ed34168eadc366e7b5.file
ASDCgMkIywrsj3EzQfQ;./6e34bfe984b342a7211287d74116a888.file
```

Pretty similar results. Now, I will use the "simplified" version of the "default hashing algorithm":

```
$ deeptoad -simple -b=32
bX8GJuRBPft6hWIZRIeRk0JYD8/6Gn74;./268ea7eff324470892c91cea4cd3b408.file
bX8GJuRBPft6hWIZRIeRk0JYD8/6Gn74;./2624ffb6c9edc1ed34168eadc366e7b5.file
vsdV1+lgKSaDRK34A3RHaVHk9zf4WcEo;./d5ab3f4161ab49f4f51c1e1d92fb098a.file
bccVzVcVt2pULe/DnCRbYKeuaJIP0Kyt;./26ec20d25d1df6d84557304931d9e253.file
bRtUZBFEFXqSdDlWqCsuzyZjKvtXToXW;./89447f6a6fe74cb9ed0e75e6aaabaed9.file
bRtUZBFEFXqSdDlWqCsuzyZjKvtXToXW;./eff5b36bd4e48c3bc4d2f192c6f30c0d.file
bRtUZBFEFXqSdDlWqCsuzyZjKvtXToXW;./4e9db696938b817da5153f08f9be920b.file
bRtUZBFEFXqSdDlWqCsuzyZjKvtXToXW;./7bc969a74937cadf9fa21fdf282ecf30.file
bRtUZBFEFXqSdDlWqCsuzyZjKvtXToXW;./6e34bfe984b342a7211287d74116a888.file
1bFyOcqkEYKvMdJ2rxLmbLEJPkGTZy98;./27761d6676940c51232dcc51139002eb.file
1bFyOcqkEYKvMdJ2rxLmbLEJPkGTZy98;./27e2c599d01e84765fad7145b55c2a61.file
bVcrRSOTqT80FMdU3pA5VlWwYbDwFkqs;./6a9fd93f48e81ecbaf14b84a28b58db5.file
bVcrRSOTqT80FMdU3pA5VlWwYbDwFkqs;./5cf77cb17d24ff935ce37116a78042de.file
bVcrRSOTqT80FMdU3pA5VlWwYbDwFkqs;./647a25e96e9bce5d13c20d1d0ec1fd6c.file
bVcrRSOTqT80FMdU3pA5VlWwYbDwFkqs;./5d7bbb216e430fdad7cc9697d7e8427c.file
bVcrRSOTqT80FMdU3pA5VlWwYbDwFkqs;./60287028061fbdb5591aaead0ccfb34d.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./32d7d334fc95b38aa4079d86e624c534.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./2a2cec153f07ebd07f8ba250a8cd19b6.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./296368123a71e873bc03b7a0d0f1d1bb.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./a0d0f55fbd412de49f17b9f21d5470e2.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./b2cec72ba2c13018bd0b529ee14effbc.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./b39915b0075908b203d6020c13a67621.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./89e5159f8fe45ebffc77c0ac3729a5a0.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./83470ee9856d33f11dd01f5d9468d13e.file
bbY+o+gKfNH31+i2lIt5EhA14BM6Ha2w;./585442eaec327654a5b87770896f1c33.file
```

The simplified version of the algorithm works "good" but is weaker than the default hashing algorithm. But, there is another algorithm, the experimental one:

```
$ deeptoad -x -b=32 .
SJoA8wo+PPmqycZzRn+KWRwumPqC4S/J;./d5ab3f4161ab49f4f51c1e1d92fb098a.file
qFlfQuA1NF6rM317mcfKbkAlRs08ORSN;./27e2c599d01e84765fad7145b55c2a61.file
iU1G/cwEZ6eEL2I/0LMWsNZxQU5O2x7Z;./26ec20d25d1df6d84557304931d9e253.file
INbUZKPYp5HCqnX2N0yeAIoxj99e2GBj;./6a9fd93f48e81ecbaf14b84a28b58db5.file
INbUZKPYp5HCqnX2N0yeAIoxj99e2GBj;./5cf77cb17d24ff935ce37116a78042de.file
INbUZKPYp5HCqnX2N0yeAIoxj99e2GBj;./647a25e96e9bce5d13c20d1d0ec1fd6c.file
INbUZKPYp5HCqnX2N0yeAIoxj99e2GBj;./5d7bbb216e430fdad7cc9697d7e8427c.file
INbUZKPYp5HCqnX2N0yeAIoxj99e2GBj;./60287028061fbdb5591aaead0ccfb34d.file
IKRswOnyu7ixD9qSapn6CB3S9ys0+blr;./89447f6a6fe74cb9ed0e75e6aaabaed9.file
IKRswOnyu7ixD9qSapn6CB3S9ys0+blr;./eff5b36bd4e48c3bc4d2f192c6f30c0d.file
IKRswOnyu7ixD9qSapn6CB3S9ys0+blr;./4e9db696938b817da5153f08f9be920b.file
IKRswOnyu7ixD9qSapn6CB3S9ys0+blr;./7bc969a74937cadf9fa21fdf282ecf30.file
IKRswOnyu7ixD9qSapn6CB3S9ys0+blr;./6e34bfe984b342a7211287d74116a888.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./32d7d334fc95b38aa4079d86e624c534.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./2a2cec153f07ebd07f8ba250a8cd19b6.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./296368123a71e873bc03b7a0d0f1d1bb.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./a0d0f55fbd412de49f17b9f21d5470e2.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./b2cec72ba2c13018bd0b529ee14effbc.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./b39915b0075908b203d6020c13a67621.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./89e5159f8fe45ebffc77c0ac3729a5a0.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./83470ee9856d33f11dd01f5d9468d13e.file
IPaELqqfBbpUU1oiWN3mCQJDKsgFYsel;./585442eaec327654a5b87770896f1c33.file
IHXNlIlv3+2TOVzQk6k84vcIwe12hGVX;./27761d6676940c51232dcc51139002eb.file
IFKaHSr4VsvlyOQwMcpqPTJ617kTtS+2;./268ea7eff324470892c91cea4cd3b408.file
IFKaHSr4VsvlyOQwMcpqPTJ617kTtS+2;./2624ffb6c9edc1ed34168eadc366e7b5.file
```

Very similar results but this algorithm is, as of December 2009, the slowest one.