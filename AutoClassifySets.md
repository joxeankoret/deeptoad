# Introduction #

So many times, AV and malware researchers receive big sets of files to classify where there is no easy way to know if they are close or not. DeepToad helps performing a 1st pass to classify files according to their binary similiraty.

# Details #

DeepToad, as of 2011-May-05, can classify files copying them to subdirectories according to their binary similarity. To do it use the option "-o=directory" as in the following example.

## Example ##

Let's use this new feature with this file's set:

```
$ ls -l
total 10060
-rw-r--r-- 1 joxean joxean 1257472 2011-05-03 09:52 0109e34c137e006c65010759206d09077dad3a4433898a2eeae68f1f06cc56f5
-rw-r--r-- 1 joxean joxean  364032 2011-05-03 09:52 0da88b1bae34c357e5357d17d8b8e0d01dcf6c7dbb85e9ea3e908757793730c4
-rw-r--r-- 1 joxean joxean  536064 2011-05-03 09:52 138cc1fa7637b883118c7b05abd925c9b2a10f67e880e2f1380d15b7808e0eba
-rw-r--r-- 1 joxean joxean  244034 2011-05-03 09:52 206f57cfdfacd5a56522eaed5984d4e110ba56b44d09fe110dc9277eeddefb40
-rw-r--r-- 1 joxean joxean  242688 2011-05-03 09:52 316222ff39afcca10b683ee64a49fccbbdc24dd52af7680318028f2c97781fcb
-rw-r--r-- 1 joxean joxean  286720 2011-05-03 09:52 31b41d1e03f89a1f1e6289d0af8d117c3de3dea9f1cbbc26cfb6744612c64e81
-rw-r--r-- 1 joxean joxean  636928 2011-05-03 09:52 31e8fe8d10f2bac15bcf1922cee073955f1bd520d8175355b2703fa8a1bee2ba
-rw-r--r-- 1 joxean joxean   54272 2011-05-03 09:52 528cb2043ec0e2b7abcf29e0bf50143bd1a764912ecdc9201c302b089a27ad39
-rw-r--r-- 1 joxean joxean  112128 2011-05-03 09:52 5c745ff177295e297293603e8a0aa80ec83565d3caca7a499cf9f744f61011c0
-rw-r--r-- 1 joxean joxean  402432 2011-05-03 09:52 5f8246ef7e459c8d639bc50f3fb0c1ed79e5f1606460936fbe9a2cbfcc6402a1
-rw-r--r-- 1 joxean joxean  291328 2011-05-03 09:52 86ea6ed67b0f779ed5d9a98e284c61dec028f463d67f56089e3a8a2b3760288e
-rw-r--r-- 1 joxean joxean   69891 2011-05-03 09:52 8e282e22dd5f3502b5d6d53acc952472eae0286987da187ab7fe203a2582e50a
-rw-r--r-- 1 joxean joxean  266240 2011-05-03 09:52 9f6037e7e5d0443e61adcb80a4709bab01cbc90ccce5c4e5b4417d4ce78ad21d
-rw-r--r-- 1 joxean joxean   16384 2011-05-03 09:52 a90ee0d6c840d1a053fec9f72d89b828574253dd9a350be2db8cf9c220478176
-rw-r--r-- 1 joxean joxean   44981 2011-05-03 09:52 ab909c15998b7da7f2ce4b5cb5f08572a63e5e86a844b4830ceda6fab07798d1
-rw-r--r-- 1 joxean joxean  213779 2011-05-03 09:52 aeedc4921db82d20137514728d7ab89a52c2e1c8d91a66a426433c0a40e988a1
-rw-r--r-- 1 joxean joxean 2576942 2011-05-03 09:52 b135739f4101e17c3d746c6df9ce7472a8d0a0a6d3c3a1ee6aa8d053f26f6be3
-rw-r--r-- 1 joxean joxean  273920 2011-05-03 09:52 b3b7aae358ac74f9153e13d791ae6a476e1c738de0ff823db49d6fbdd68300fa
-rw-r--r-- 1 joxean joxean  434176 2011-05-03 09:52 cbac6d0aced4c7f1799775bc8877a5d998c9ab007d1f5d3f167746bc6cfbf649
-rw-r--r-- 1 joxean joxean  352256 2011-05-03 09:52 ce7e768c5b090cc0a0fa494eb5d793a2ca70cdfd3f52ae8ec902a97941c77982
-rw-r--r-- 1 joxean joxean   44300 2011-05-03 09:52 d6d68b770129f28b35bf8e88dbe3eebd53ab4759767d516f4235029fa97a7f69
-rw-r--r-- 1 joxean joxean  622344 2011-05-03 09:52 de562c359d97bbb1cfd94473269a6fcef71229215a262d057a863e5e3ca6bf38
-rw-r--r-- 1 joxean joxean  438272 2011-05-03 09:52 df2bd3f8342fe43566925d5be0926ed93dae136268a90f9b5d475d4fdb436e12
-rw-r--r-- 1 joxean joxean  242176 2011-05-03 09:52 e693b862346af09b578f3552680141a15c487050b5d31fe605ebbb76d3c92efb
-rw-r--r-- 1 joxean joxean  239104 2011-05-03 09:52 f9435b601162478a476be141d460e8f13bd612725e9a917d5a8b94b9159997ac
```

We have 25 different files and we know nothing about them. Let's check how close they are with deeptoad:

```
$ deeptoad .
ysq/v1hYS0vi4sLCxMR1dQoKZWWSkkZG;./cbac6d0aced4c7f1799775bc8877a5d998c9ab007d1f5d3f167746bc6cfbf649
pqYZGUVFPz9vb0pK/v6lpfT0GRkkJF9f;./8e282e22dd5f3502b5d6d53acc952472eae0286987da187ab7fe203a2582e50a
ZGRmZouL7OzS0l9feHiHh5CQcHCNjcTE;./aeedc4921db82d20137514728d7ab89a52c2e1c8d91a66a426433c0a40e988a1
z89kZFlZ2dnv75CQ9fVoaDk55+cQEAcH;./528cb2043ec0e2b7abcf29e0bf50143bd1a764912ecdc9201c302b089a27ad39
traysq6ut7cSEo6Om5s6OlFRcnJgYLKy;./5c745ff177295e297293603e8a0aa80ec83565d3caca7a499cf9f744f61011c0
Li709PT07Ozs7M7Ozs77+/v73t7e3ggI;./f9435b601162478a476be141d460e8f13bd612725e9a917d5a8b94b9159997ac
bW3z8yAgnZ3Hx42Nvr5jY319zc0tLQ0N;./206f57cfdfacd5a56522eaed5984d4e110ba56b44d09fe110dc9277eeddefb40
yclmZmZmyMjIyO/v7++WlpaWfX19feLi;./ab909c15998b7da7f2ce4b5cb5f08572a63e5e86a844b4830ceda6fab07798d1
rKxkZH9/x8f5+efndHQfH1paGxsiIsjI;./0109e34c137e006c65010759206d09077dad3a4433898a2eeae68f1f06cc56f5
MTESEhISU1NTU1VVVVXw8PDwFBQUFL29;./b135739f4101e17c3d746c6df9ce7472a8d0a0a6d3c3a1ee6aa8d053f26f6be3
jo6Tk1JSCgr6+uLigIAcHAsLPT2QkNfX;./de562c359d97bbb1cfd94473269a6fcef71229215a262d057a863e5e3ca6bf38
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./ce7e768c5b090cc0a0fa494eb5d793a2ca70cdfd3f52ae8ec902a97941c77982
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./86ea6ed67b0f779ed5d9a98e284c61dec028f463d67f56089e3a8a2b3760288e
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./5f8246ef7e459c8d639bc50f3fb0c1ed79e5f1606460936fbe9a2cbfcc6402a1
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./b3b7aae358ac74f9153e13d791ae6a476e1c738de0ff823db49d6fbdd68300fa
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./9f6037e7e5d0443e61adcb80a4709bab01cbc90ccce5c4e5b4417d4ce78ad21d
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./31e8fe8d10f2bac15bcf1922cee073955f1bd520d8175355b2703fa8a1bee2ba
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./316222ff39afcca10b683ee64a49fccbbdc24dd52af7680318028f2c97781fcb
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./138cc1fa7637b883118c7b05abd925c9b2a10f67e880e2f1380d15b7808e0eba
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./31b41d1e03f89a1f1e6289d0af8d117c3de3dea9f1cbbc26cfb6744612c64e81
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./e693b862346af09b578f3552680141a15c487050b5d31fe605ebbb76d3c92efb
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./df2bd3f8342fe43566925d5be0926ed93dae136268a90f9b5d475d4fdb436e12
JycuLh4e8fHLyxkZX1/OzgUFoaFdXVZW;./0da88b1bae34c357e5357d17d8b8e0d01dcf6c7dbb85e9ea3e908757793730c4
w8MNDTAw8/Pu7mJiv78NDXV1JiaamoCA;./d6d68b770129f28b35bf8e88dbe3eebd53ab4759767d516f4235029fa97a7f69
```

Using the default block size (512 bytes) DeepToad says many files are very similar. Let's change the block size to something smaller to see if the tool can group by similiraties more files:

```
$ deeptoad -b=32 .
Processing file ./0da88b1bae34c357e5357d17d8b8e0d01dcf6c7dbb85e9ea3e908757793730c4 ...
vb2ysrS0QkIwMNzcvLxmZkJCHh6wsLy8;./ab909c15998b7da7f2ce4b5cb5f08572a63e5e86a844b4830ceda6fab07798d1
jY1fX3d3LS2GhtPTLy+NjSkp9fWVlcrK;./0109e34c137e006c65010759206d09077dad3a4433898a2eeae68f1f06cc56f5
cnJjY2NjNzc3N9LS0tJ5eXl51tbW1vb2;./aeedc4921db82d20137514728d7ab89a52c2e1c8d91a66a426433c0a40e988a1
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;./ce7e768c5b090cc0a0fa494eb5d793a2ca70cdfd3f52ae8ec902a97941c77982
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;./b3b7aae358ac74f9153e13d791ae6a476e1c738de0ff823db49d6fbdd68300fa
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;./9f6037e7e5d0443e61adcb80a4709bab01cbc90ccce5c4e5b4417d4ce78ad21d
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;./d6d68b770129f28b35bf8e88dbe3eebd53ab4759767d516f4235029fa97a7f69
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;./8e282e22dd5f3502b5d6d53acc952472eae0286987da187ab7fe203a2582e50a
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;./df2bd3f8342fe43566925d5be0926ed93dae136268a90f9b5d475d4fdb436e12
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;./0da88b1bae34c357e5357d17d8b8e0d01dcf6c7dbb85e9ea3e908757793730c4
gIB9fQ8P6uoYGFBQt7e1tSYm9PR1deTk;./5c745ff177295e297293603e8a0aa80ec83565d3caca7a499cf9f744f61011c0
n59/f39/mZmZmaWlpaWPj4+Pfn5+fsTE;./206f57cfdfacd5a56522eaed5984d4e110ba56b44d09fe110dc9277eeddefb40
ODjIyMjIfX19fQ8PDw/Q0NDQLCwsLKOj;./528cb2043ec0e2b7abcf29e0bf50143bd1a764912ecdc9201c302b089a27ad39
ODjIyMjIfX19fQ8PDw/Q0NDQLCwsLKOj;./a90ee0d6c840d1a053fec9f72d89b828574253dd9a350be2db8cf9c220478176
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;./86ea6ed67b0f779ed5d9a98e284c61dec028f463d67f56089e3a8a2b3760288e
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;./5f8246ef7e459c8d639bc50f3fb0c1ed79e5f1606460936fbe9a2cbfcc6402a1
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;./31e8fe8d10f2bac15bcf1922cee073955f1bd520d8175355b2703fa8a1bee2ba
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;./316222ff39afcca10b683ee64a49fccbbdc24dd52af7680318028f2c97781fcb
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;./138cc1fa7637b883118c7b05abd925c9b2a10f67e880e2f1380d15b7808e0eba
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;./31b41d1e03f89a1f1e6289d0af8d117c3de3dea9f1cbbc26cfb6744612c64e81
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;./e693b862346af09b578f3552680141a15c487050b5d31fe605ebbb76d3c92efb
ODjw8PDwfX19fQ8PDw/f39/feXl5ecjI;./cbac6d0aced4c7f1799775bc8877a5d998c9ab007d1f5d3f167746bc6cfbf649
ODjw8PDwfX19fQ8PDw/f39/feXl5ecjI;./f9435b601162478a476be141d460e8f13bd612725e9a917d5a8b94b9159997ac
ubmvr2Bg6Oj19SkpcXFdXW1thIS1tbm5;./b135739f4101e17c3d746c6df9ce7472a8d0a0a6d3c3a1ee6aa8d053f26f6be3
ODgRERERfX19fQ8PDw+vr6+v3t7e3rm5;./de562c359d97bbb1cfd94473269a6fcef71229215a262d057a863e5e3ca6bf38
```

And more groups appeared! OK, so we have the perfect block size for this sample's set. Now, let's copy and group them in subdirectories using the newly added feature:

```
$ deeptoad -b=32 -o=../grouped_samples .
$ ls -l ../grouped_samples/
total 44
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set1
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set10
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set11
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set2
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set3
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set4
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set5
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set6
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set7
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set8
drwxr-xr-x 2 joxean joxean 4096 2011-05-05 09:43 set9
$ find ../grouped_samples/ -type f
../grouped_samples/set1/ab909c15998b7da7f2ce4b5cb5f08572a63e5e86a844b4830ceda6fab07798d1
../grouped_samples/set10/b135739f4101e17c3d746c6df9ce7472a8d0a0a6d3c3a1ee6aa8d053f26f6be3
../grouped_samples/set5/5c745ff177295e297293603e8a0aa80ec83565d3caca7a499cf9f744f61011c0
../grouped_samples/set8/86ea6ed67b0f779ed5d9a98e284c61dec028f463d67f56089e3a8a2b3760288e
../grouped_samples/set8/5f8246ef7e459c8d639bc50f3fb0c1ed79e5f1606460936fbe9a2cbfcc6402a1
../grouped_samples/set8/31e8fe8d10f2bac15bcf1922cee073955f1bd520d8175355b2703fa8a1bee2ba
../grouped_samples/set8/316222ff39afcca10b683ee64a49fccbbdc24dd52af7680318028f2c97781fcb
../grouped_samples/set8/138cc1fa7637b883118c7b05abd925c9b2a10f67e880e2f1380d15b7808e0eba
../grouped_samples/set8/31b41d1e03f89a1f1e6289d0af8d117c3de3dea9f1cbbc26cfb6744612c64e81
../grouped_samples/set8/e693b862346af09b578f3552680141a15c487050b5d31fe605ebbb76d3c92efb
../grouped_samples/set6/206f57cfdfacd5a56522eaed5984d4e110ba56b44d09fe110dc9277eeddefb40
../grouped_samples/set9/cbac6d0aced4c7f1799775bc8877a5d998c9ab007d1f5d3f167746bc6cfbf649
../grouped_samples/set9/f9435b601162478a476be141d460e8f13bd612725e9a917d5a8b94b9159997ac
../grouped_samples/set7/528cb2043ec0e2b7abcf29e0bf50143bd1a764912ecdc9201c302b089a27ad39
../grouped_samples/set7/a90ee0d6c840d1a053fec9f72d89b828574253dd9a350be2db8cf9c220478176
../grouped_samples/set2/0109e34c137e006c65010759206d09077dad3a4433898a2eeae68f1f06cc56f5
../grouped_samples/set11/de562c359d97bbb1cfd94473269a6fcef71229215a262d057a863e5e3ca6bf38
../grouped_samples/set4/ce7e768c5b090cc0a0fa494eb5d793a2ca70cdfd3f52ae8ec902a97941c77982
../grouped_samples/set4/b3b7aae358ac74f9153e13d791ae6a476e1c738de0ff823db49d6fbdd68300fa
../grouped_samples/set4/9f6037e7e5d0443e61adcb80a4709bab01cbc90ccce5c4e5b4417d4ce78ad21d
../grouped_samples/set4/d6d68b770129f28b35bf8e88dbe3eebd53ab4759767d516f4235029fa97a7f69
../grouped_samples/set4/8e282e22dd5f3502b5d6d53acc952472eae0286987da187ab7fe203a2582e50a
../grouped_samples/set4/df2bd3f8342fe43566925d5be0926ed93dae136268a90f9b5d475d4fdb436e12
../grouped_samples/set4/0da88b1bae34c357e5357d17d8b8e0d01dcf6c7dbb85e9ea3e908757793730c4
../grouped_samples/set3/aeedc4921db82d20137514728d7ab89a52c2e1c8d91a66a426433c0a40e988a1

```

OK! We have the files grouped by similarity in new directories. Now, we can perform further analysis of the subsets, instead of analyzing by hand every file.

We can double-check the sets are created as expected with DeepToad:

```
$ deeptoad -b=32 ../grouped_samples/
vb2ysrS0QkIwMNzcvLxmZkJCHh6wsLy8;../grouped_samples/set1/ab909c15998b7da7f2ce4b5cb5f08572a63e5e86a844b4830ceda6fab07798d1
jY1fX3d3LS2GhtPTLy+NjSkp9fWVlcrK;../grouped_samples/set2/0109e34c137e006c65010759206d09077dad3a4433898a2eeae68f1f06cc56f5
cnJjY2NjNzc3N9LS0tJ5eXl51tbW1vb2;../grouped_samples/set3/aeedc4921db82d20137514728d7ab89a52c2e1c8d91a66a426433c0a40e988a1
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;../grouped_samples/set4/ce7e768c5b090cc0a0fa494eb5d793a2ca70cdfd3f52ae8ec902a97941c77982
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;../grouped_samples/set4/9f6037e7e5d0443e61adcb80a4709bab01cbc90ccce5c4e5b4417d4ce78ad21d
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;../grouped_samples/set4/d6d68b770129f28b35bf8e88dbe3eebd53ab4759767d516f4235029fa97a7f69
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;../grouped_samples/set4/8e282e22dd5f3502b5d6d53acc952472eae0286987da187ab7fe203a2582e50a
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;../grouped_samples/set4/df2bd3f8342fe43566925d5be0926ed93dae136268a90f9b5d475d4fdb436e12
ODjg4ODgfX19fQ8PDw9QUFBQdHR0dIaG;../grouped_samples/set4/0da88b1bae34c357e5357d17d8b8e0d01dcf6c7dbb85e9ea3e908757793730c4
gIB9fQ8P6uoYGFBQt7e1tSYm9PR1deTk;../grouped_samples/set5/5c745ff177295e297293603e8a0aa80ec83565d3caca7a499cf9f744f61011c0
n59/f39/mZmZmaWlpaWPj4+Pfn5+fsTE;../grouped_samples/set6/206f57cfdfacd5a56522eaed5984d4e110ba56b44d09fe110dc9277eeddefb40
ODjIyMjIfX19fQ8PDw/Q0NDQLCwsLKOj;../grouped_samples/set7/528cb2043ec0e2b7abcf29e0bf50143bd1a764912ecdc9201c302b089a27ad39
ODjIyMjIfX19fQ8PDw/Q0NDQLCwsLKOj;../grouped_samples/set7/a90ee0d6c840d1a053fec9f72d89b828574253dd9a350be2db8cf9c220478176
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;../grouped_samples/set8/86ea6ed67b0f779ed5d9a98e284c61dec028f463d67f56089e3a8a2b3760288e
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;../grouped_samples/set8/5f8246ef7e459c8d639bc50f3fb0c1ed79e5f1606460936fbe9a2cbfcc6402a1
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;../grouped_samples/set8/31e8fe8d10f2bac15bcf1922cee073955f1bd520d8175355b2703fa8a1bee2ba
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;../grouped_samples/set8/316222ff39afcca10b683ee64a49fccbbdc24dd52af7680318028f2c97781fcb
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;../grouped_samples/set8/138cc1fa7637b883118c7b05abd925c9b2a10f67e880e2f1380d15b7808e0eba
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;../grouped_samples/set8/31b41d1e03f89a1f1e6289d0af8d117c3de3dea9f1cbbc26cfb6744612c64e81
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;../grouped_samples/set8/e693b862346af09b578f3552680141a15c487050b5d31fe605ebbb76d3c92efb
lJQkJJWVMzO8vLCwzc2VlaWlZ2dvb87O;../grouped_samples/set4/b3b7aae358ac74f9153e13d791ae6a476e1c738de0ff823db49d6fbdd68300fa
ODjw8PDwfX19fQ8PDw/f39/feXl5ecjI;../grouped_samples/set9/cbac6d0aced4c7f1799775bc8877a5d998c9ab007d1f5d3f167746bc6cfbf649
ODjw8PDwfX19fQ8PDw/f39/feXl5ecjI;../grouped_samples/set9/f9435b601162478a476be141d460e8f13bd612725e9a917d5a8b94b9159997ac
ubmvr2Bg6Oj19SkpcXFdXW1thIS1tbm5;../grouped_samples/set10/b135739f4101e17c3d746c6df9ce7472a8d0a0a6d3c3a1ee6aa8d053f26f6be3
ODgRERERfX19fQ8PDw+vr6+v3t7e3rm5;../grouped_samples/set11/de562c359d97bbb1cfd94473269a6fcef71229215a262d057a863e5e3ca6bf38
```