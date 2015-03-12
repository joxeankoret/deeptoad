# Introduction #

"DeepToad" is designed, mainly, to work with directories. When you run the command "deeptoad directory", by default, the tool calculates the [DHA](Algorithms.md) hash and tries to clusterize all the files with the best signature for a group of files.

# Example #

Let imagine that we have a directory with various modified images:

```
$ ls -ltr
total 3224
-rw-r--r-- 1 joxean joxean 1449217 2009-12-21 20:53 test1.jpg
-rw-r--r-- 1 joxean joxean   23825 2009-12-21 20:55 test2.jpg
-rw-r--r-- 1 joxean joxean   47618 2009-12-21 20:56 test3.jpg
-rw-r--r-- 1 joxean joxean   24577 2009-12-21 20:57 test4.jpg
-rw-r--r-- 1 joxean joxean   23809 2009-12-21 20:58 test5.jpg
-rw-r--r-- 1 joxean joxean   23809 2009-12-21 20:59 test6.jpg
-rw-r--r-- 1 joxean joxean   23809 2009-12-28 11:50 voices.jpg
-rw-r--r-- 1 joxean joxean   23809 2009-12-30 20:22 reverse.jpg
-rw-r--r-- 1 joxean joxean 1640474 2010-01-03 11:47 marginal.jpg
$ md5sum *
b0e427ff390e26557fdf4115a4d9b81c  marginal.jpg
8dc0af8bfcfed780b6600005630000e1  reverse.jpg
d20b09a96a75e9ef0301ea815318cca4  test1.jpg
bb5b8e1e593b8155bf547780ca83031b  test2.jpg
3119e54115db7061178700d418999f8b  test3.jpg
48cca8820898addf59e8bbf12935606d  test4.jpg
893c166092fe25e10915c01b3533974c  test5.jpg
06c1dc530fa503d7a122949847ea31e0  test6.jpg
6d981bd87565cfa0dd0913a88eff92a4  voices.jpg
```

If we execute the command "deeptoad ." we get the following result:

```
$ deeptoad .
FumIFnmIO3kWO+IWgeKAgQiAvghsvsFs;./marginal.jpg
FumIFnmIO3kWO+IWgeKAgQiAvghsvsFs;./test3.jpg
h9O2HIUByx9AidzXInvpoKkwk2/hohWf;./test6.jpg
xn2llp2gVKW8ztssbApeYdvcpG/KwW4K;./reverse.jpg
xn2llp2gVKW8ztssbApeYdvcpG/KwW4K;./test4.jpg
xn2llp2gVKW8ztssbApeYdvcpG/KwW4K;./test5.jpg
xn2llp2gVKW8ztssbApeYdvcpG/KwW4K;./voices.jpg
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;./test1.jpg
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;./test2.jpg
```

We clearly see 3 groups and one file (test6.jpg) which seems to be very different. Now, I will compare the image files to know how closer they are from the deeptoad's perspective:

```
$ deeptoad -c .
File './test3.jpg' matches './test1.jpg' (100.00%)
File './test3.jpg' matches './voices.jpg' (100.00%)
File './test3.jpg' matches './test2.jpg' (68.75%)
File './test3.jpg' matches './marginal.jpg' (100.00%)
File './test3.jpg' matches './test4.jpg' (100.00%)
File './test3.jpg' matches './test5.jpg' (100.00%)
File './test1.jpg' matches './voices.jpg' (100.00%)
File './test1.jpg' matches './test2.jpg' (68.75%)
File './test1.jpg' matches './test4.jpg' (100.00%)
File './test1.jpg' matches './test5.jpg' (100.00%)
File './reverse.jpg' matches './voices.jpg' (100.00%)
File './reverse.jpg' matches './test2.jpg' (100.00%)
File './reverse.jpg' matches './marginal.jpg' (100.00%)
File './reverse.jpg' matches './test4.jpg' (100.00%)
File './reverse.jpg' matches './test5.jpg' (93.75%)
File './voices.jpg' matches './test3.jpg' (100.00%)
File './voices.jpg' matches './test1.jpg' (100.00%)
File './voices.jpg' matches './test2.jpg' (68.75%)
File './voices.jpg' matches './test4.jpg' (100.00%)
File './voices.jpg' matches './test5.jpg' (100.00%)
File './test2.jpg' matches './test3.jpg' (68.75%)
File './test2.jpg' matches './test1.jpg' (68.75%)
File './test2.jpg' matches './reverse.jpg' (100.00%)
File './test2.jpg' matches './test4.jpg' (68.75%)
File './test2.jpg' matches './test5.jpg' (68.75%)
File './marginal.jpg' matches './test3.jpg' (100.00%)
File './test4.jpg' matches './test3.jpg' (100.00%)
File './test4.jpg' matches './test1.jpg' (100.00%)
File './test4.jpg' matches './reverse.jpg' (56.25%)
File './test4.jpg' matches './voices.jpg' (100.00%)
File './test4.jpg' matches './test5.jpg' (100.00%)
File './test5.jpg' matches './test3.jpg' (100.00%)
File './test5.jpg' matches './test1.jpg' (100.00%)
File './test5.jpg' matches './reverse.jpg' (93.75%)
File './test5.jpg' matches './voices.jpg' (100.00%)
File './test5.jpg' matches './test2.jpg' (68.75%)
```

In many cases the image files, although modified, are so similar that "deeptoad" classified them as equals (100.00%).

# Working with big batteries #

The [DHA](Algorithms.md) algorithm is a bit slow and, for big batteries, it may take a very long while. If you just want to see how similar a battery of samples is (i.e., malware files) you may run the tool passing the argument `-`f in order to use the faster version of the algorithm. The time difference is really notable:

```
$ time deeptoad /a/25/samples/battery
(...)
real    0m32.029s
user    0m30.066s
sys     0m0.512s
$ time deeptoad -f /a/25/samples/battery
(...)

real    0m1.396s
user    0m0.820s
sys     0m0.460s
```

# Generating reports #

The default output of deeptoad when working with directories is the best signature to clusterize the files and the filenames (in CSV format), however, we may want to see the complete signature for all the files and also see how different the results are using different block sizes, algorithms or signature's sizes. For this purpose, you may use many different arguments to "deeptoad" to generate reports. In example, the following command prints out the signatures for a directory using the default hashing algorithm, the faster version and the experimental version:

```
$ deeptoad -p -echo="DHA" . -f -echo="FHA" . -x -echo="XHA" . > report.csv
Processing file (...) ...
$ cat report.csv
DHA
===
Signature;Simple Signature;Reverse Signature;Filename
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;fcalfZalnZagnVSgpVS8pc68284s22ws;FumIFnmIO3kWO+IWgeKAgQiAvghsvsFs;./test3.jpg
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;fcalfZalnZagnVSgpVS8pc68284s22ws;LGTOLPzOEfyGEe2G5e3S5QTSNQQMNWAM;./test1.jpg
6Yrp6RbpFhaIFoiIeYh5eTt5OzsWOxYW;6RaIeTsW4oGACL5swVR4GGd1hX2kGtpd;xn2llp2gVKW8ztssbApeYdvcpG/KwW4K;./reverse.jpg
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;xn2llp2gVKW8ztssbApeYdvcpG/KwW4K;6RaIeTsW4oGACL5swVR4GGd1hX2kGtpd;./voices.jpg
xjvGxn3GfX2lfaWllqWWlrqWurrBusHB;xn2llrrBDkavaNITErprC9IP+14S65r3;6RaIeTsW4oGACL5swVR4GGd1hX2kGtpd;./test2.jpg
6Yrp6RbpFhaIFoiIeYh5eTt5OzsWOxYW;FumIFnmIO3kWO+IWgeKAgQiAvghsvsFs;3Fy93Oa9T+YBT10BTF3xTLPxwrNHwpZH;./marginal.jpg
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;xn2llp2gVKW8ztssbAo//ToUhZsou26I;6RaIeTsW4oGACL5swVR4GGd1hX2kGtpd;./test4.jpg
xjvGxn3GfX2lfaWllqWWlp2WnZ2gnaCg;xn2llp2gVKW8ztssbApeYdvcpG/KwW5L;6RYyZdAZieACeFTfyveAGfSJEffJaNpd;./test5.jpg
WOpYWG5Ybm5cblxcYlxiYrpiurrAusDA;WG5cYrrAA5AfYkeU/aMLMt0yJ+xJyxjs;h9O2HIUByx9AidzXInvpoKkwk2/hohWf;./test6.jpg
FHA
===
Signature;Simple Signature;Reverse Signature;Filename
YaClxp0KLM7bVJY7Xn28bA;gAqWnaClpCYsO7y/wUrGys5U29zfXmFg;gYCFiIuKFpkYmxoipKgIO72+wdJU2l3i;./test3.jpg
YaClxp0KLM7bVJY7Xn28bA;gAqWnaClpCYsO7y/wUrGys5U29zfXmFg;wQSGDBGTFpsdLJE1uLw/QcfO0lVaYOVk;./test1.jpg
gYDi6YiKbBjBCFQWeXg7vg;gYCFiIuKFpkYmxoipKgIO72+wdJU2l3i;gAqWnaClpCYsO7y/wUrGys5U29zfXmFg;./reverse.jpg
YaClxp0KLM7bVJY7Xn28bA;gAqWnaClpCYsO7y/wUrGys5U29zfXmFg;gYCFiIuKFpkYmxoipKgIO72+wdJU2l3i;./voices.jpg
waXGaGtGrw4T0pYSO7p9Cw;BgsPDhMSlpojpadGr7M7usF3x8bI0l5o;gYCFiIuKFpkYmxoipKgIO72+wdJU2l3i;./test2.jpg
gYDi6YiKbBjBCFQWeXg7vg;gYCFiIuKFpkYmxoipKgIO72+wdJU2l3i;AZYYGxpcszQ5ur3AwsVHRspNTE/P113c;./marginal.jpg
oKXGnQoszv3bVJY7fbw/bA;hYgKDawUlpudoKOlKEatLLs6vD/GzlTb;gYCFiIuKFpkYGiKkqAg7vaK+wcrSVNpd;./test4.jpg
YaClxp0KLM7bVJY7Xn28bA;AwqOEZadoKWkLLc7OrzBxkvKzlTb3F5h;gAKJi4oRmRYZmyKoMr3JytDSVNpd3+Bl;./test5.jpg
wANiRwvqo26QMpRYuv1cHw;AwuQlBiaH6MnpjEytri6vsBHScvMU1jd;AYWHiQqTFRidHB+gIqkwn7ZAIMvP06LX;./test6.jpg
XHA
===
Signature;Simple Signature;Reverse Signature;Filename
V4G57GlGn7uE1W+gdz/35evG4BnE3R1+;V/UKDfpdKyqsTEfHStYgqPu/4ToCr6wZ;o43hwBpf8lQuHCe7VSustKRZIb0sgNEx;./test3.jpg
V+UpiYcULPPFJh9UmIfAEYZL4bEEMvEN;V9YeoRL2OMlQiJezLmlHqxiFPFBkX8WQ;gZp0UJuPx4yVwzu5nDP3k+azBuRHri3h;./test1.jpg
oxljBfUbJSVPybMVJx479S43JYqTgfSQ;o4ONROFxwLYaPl8D8rdUhS6LHKcn97vX;V2v14wqIDe767l1ZK80qTKy5TAVHnceA;./reverse.jpg
V2Tn17657ddtNml5xKgqn0s+1dSEDfPm;V2v14wqIDe767l1ZK80qTKy5TAVHnceA;o4ONROFxwLYaPl8D8rdUhS6LHKcn97vX;./voices.jpg
V2Tn1765Jt/+jmHdsrxWIBwQcKDIHr/q;V2v14wqIo+JIvwNccrPx5AWNxviGzoNZ;o4ONROFxwLYaPl8D8rdUhS6LHKcn97vX;./test2.jpg
oyYCHy9JoJtgzBfOuXAXSCp2q5O8hniR;o03HVdog6NPfd1D53SGTUGQsuTVrK0B1;8rjBCmIrDX8QziZa5v7h72COzBPVjsCT;./marginal.jpg
V2Tn17657ddtNml5xKgqn0zFcNgasvS7;V2v14wqIDe767l1ZK80qTEx0yLvltECN;o4ONROFxwLYaPl8D8rdUhS6LHKcn97vX;./test4.jpg
V2Tn17657ddtNml5xKgqn0s+1dSEDfPm;V2v14wqIDe767l1ZK80qTKy5TAVHnceA;o4ONREGYstWn0yOXs04UM/Y8XKE+BjQm;./test5.jpg
wHK7pUdeYlHdse4/a5EChY1x5IgHYhv1;wOyHr2l1bxk79Fi3KSQUD8jTpg7SJtoa;ATfFwjCpgQdDay3zedyoHhD1hPFvs/LT;./test6.jpg
```