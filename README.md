# Brainfuck Suite

Use:
```console
$ python bfTranslator.py
$ Filename: test
$ Translate: This is a test
```
This will save the following code to test.bf
```brainfuck
++++++++++[>
	++++++++>
	++++++++++>
	++++++++++>
	+++++++++++>
	+++>
	++++++++++>
	+++++++++++>
	+++>
	+++++++++>
	+++>
	+++++++++++>
	++++++++++>
	+++++++++++>
	+++++++++++>
<<<<<<<<<<<<<<<-]>
++++.>
++++.>
+++++.>
+++++.>
++.>
+++++.>
+++++.>
++.>
+++++++.>
++.>
++++++.>
+.>
+++++.>
++++++.>
```


```console
$ python compressor.py
$ (c)ompress / d(e)compress: c
$ Filename: test
$ Filename: testc
```
This will read the content of test.bf and compress it into testc.bfc:
```
i10f+ki1f[ki1f>ki8f+ki1f>ki10f+ki1f>ki10f+ki1f>ki11f+ki1f>ki3f+ki1
f>ki10f+ki1f>ki11f+ki1f>ki3f+ki1f>ki9f+ki1f>ki3f+ki1f>ki11f+ki1f>
ki10f+ki1f>ki11f+ki1f>ki11f+ki1f>ki15f<ki1f-ki1f]ki1f>ki4f+ki1f.k
i1f>ki4f+ki1f.ki1f>ki5f+ki1f.ki1f>ki5f+ki1f.ki1f>ki2f+ki1f.ki1f>k
i5f+ki1f.ki1f>ki5f+ki1f.ki1f>ki2f+ki1f.ki1f>ki7f+ki1f.ki1f>ki2f+k
i1f.ki1f>ki6f+ki1f.ki1f>ki1f+ki1f.ki1f>ki5f+ki1f.ki1f>ki6f+ki1f.k
```


```console
$ python compressor.py
$ (c)ompress / d(e)compress: d
$ Filename: testc
$ Filename: testd
```
This will read the content of testc.bfc and decompress it into testd.bf


```console
$ python brainfuck.py
$ Filename: testd.bf
```
This will run testd.bf
```console
$ This is a test
```
