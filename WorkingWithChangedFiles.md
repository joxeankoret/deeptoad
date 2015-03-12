# Usage #
## Working with files ##

"DeepToad" is a command line tool that receives at least one parameter: a directory or a file to be scanned. The following is a sample output:

```
$ deeptoad voices.jpg
OzvGxsbGfX19faWlpaWWlpaWnZ2dnaCg;xsZ9faWllpadnaCgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;voices.jpg
```

In the output, we see that the signature is divided in 4 fields separated by the character ';'. The fields are (in order): [Signature](Signature.md), [Simple Signature](SimpleSignature.md), [Reverse Signature](ReverseSignature.md) and the filename (the corresponding signature's meaning are explained more in depth in their corresponding wiki pages).

Now, I will generate a somewhat modified version of the file:

```
$ cp voices.jpg test1.jpg
$ cat /dev/urandom >> test.jpg
Ctrl+C
$ ls -l
total 884
-rw-r--r-- 1 joxean joxean 875777 2009-12-29 21:21 test.jpg
-rw-r--r-- 1 joxean joxean  23809 2009-12-29 21:21 voices.jpg
$ deeptoad voices.jpg test.jpg
OzvGxsbGfX19faWlpaWWlpaWnZ2dnaCg;xsZ9faWllpadnaCgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;voices.jpg
OzvGxsbGfX19faWlpaWWlpaWnZ2dnaCg;xsZ9faWllpadnaCgVFSlpby8zs7b2yws;7e18fKCgvr5ZWQkJlJQnJ6CgGxuenqSk;test.jpg
$ md5sum *
9517f6dca6a7be39d68c5f73952124d4  test.jpg
6d981bd87565cfa0dd0913a88eff92a4  voices.jpg
```

The new generated file is different to the first one (the MD5 sums are different), however, the signature and simple signature of both files are equals so, deeptoad found that they are very similar. At this point ssdeep generated signatures are quite different and doesn't work right:

```
$ ssdeep -b *
ssdeep,1.0--blocksize:hash:hash,filename
24576:bLPF+T8sHDpcHOGeuKVPYHvLiBEH2Si4QQ+:bLNh3LKRYjQBIQQ+,"test.jpg"
384:fGDuCLgwoO9TMF9DuqJmwNRyOGLHUoywdDs9X6Zd41622uamR0Xu4GALul:+7hoFF9uqx4ooq9g4329yN1l,"voices.jpg"
$ ssdeep -d *
```

Now, I will make a tiny change with an hexadecimal editor to a new copy of the "voices.jpg" file:

```
$ cp voices.jpg test2.jpg
$ radare -w test2.jpg
(...)
[0x00000000]> s 1000
[0x000003E8]> wx 414141414141414141414141414141414141414141
[0x000003E8]> q
Do you want save these changes? (Y/n) Y
```

And recheck with both tools to see what happens:

```
$ deeptoad voices.jpg test2.jpg
OzvGxsbGfX19faWlpaWWlpaWnZ2dnaCg;xsZ9faWllpadnaCgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;voices.jpg
OztOTk5OfX19faWlpaWWlpaWnZ2dnaCg;Tk59faWllpadnaCgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;test2.jpg
$ ssdeep voices.jpg test2.jpg
ssdeep,1.0--blocksize:hash:hash,filename
384:fGDuCLgwoO9TMF9DuqJmwNRyOGLHUoywdDs9X6Zd41622uamR0Xu4GALul:+7hoFF9uqx4ooq9g4329yN1l,"voices.jpg"
384:fGDtCLgwoO9TMF9DuqJmwNRyOGLHUoywdDs9X6Zd41622uamR0Xu4GALul:+ghoFF9uqx4ooq9g4329yN1l,"test2.jpg"
```

Both tools works more or less OK. The "signature" of deeptoad changes various bytes, the simple signature only changes one byte (because just one block was changed) and the reverse signature is equal.

Now, another change: I will take a big block from the beginning and move it to another offset closer to the end of the file and check what happens with both ssdeep and deeptoad:

```
$ deeptoad voices.jpg test3.jpg
OzvGxsbGfX19faWlpaWWlpaWnZ2dnaCg;xsZ9faWllpadnaCgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;voices.jpg
wcGLi4uLDQ0NDfv7+/vr6+vrFxcXF6Cg;i4sNDfv76+sXF6CgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;test3.jpg
$ ssdeep voices.jpg test3.jpg
ssdeep,1.0--blocksize:hash:hash,filename
384:fGDuCLgwoO9TMF9DuqJmwNRyOGLHUoywdDs9X6Zd41622uamR0Xu4GALul:+7hoFF9uqx4ooq9g4329yN1l,"voices.jpg"
384:LCLlGD9woO9TMF9DuqJmwNRyOGLHUoywdDs9X6Zd41622uamR0Xu4GALul:io6oFF9uqx4ooq9g4329yN1l,"test3.jpg"
```

In this case, ssdeep works better than deeptoad (although both tools say the files are very similar). One more test: I will insert a bunch of "a"-s (512) at offset 0x1EC0 and compare the newly generated files:

```
$ deeptoad voices.jpg test4.jpg
OzvGxsbGfX19faWlpaWWlpaWnZ2dnaCg;xsZ9faWllpadnaCgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;voices.jpg
OzvGxsbGfX19faWlpaWWlpaWnZ2dnaCg;xsZ9faWllpadnaCgVFSlpby8zs7b2yws;6ekWFoiIeXk7OxYW4uKBgYCACAi+vmxs;test4.jpg
$ ssdeep voices.jpg test4.jpg -b
ssdeep,1.0--blocksize:hash:hash,filename
384:fGDuCLgwoO9TMF9DuqJmwNRyOGLHUoywdDs9X6Zd41622uamR0Xu4GALul:+7hoFF9uqx4ooq9g4329yN1l,"voices.jpg"
384:fGDuCLgwoO9TMF9DuqJmwaRyOGLHUoywdDs9X6Zd41622uamR0Xu4GALul:+7hoFF9uq+4ooq9g4329yN1l,"test4.jpg"
```

In both cases the generated file's signatures are equals.