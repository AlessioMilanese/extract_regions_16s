# Extract regions from 16s gene sequences

This tool extract variable regions from the 16S rRNA gene.

Summary
--------------
* [Installation](https://github.com/AlessioMilanese/extract_regions_16s#installation)
* [Simple example](https://github.com/AlessioMilanese/extract_regions_16s#simple-example)
* [Mode 1: extract variable regions](https://github.com/AlessioMilanese/extract_regions_16s#mode-1-extract-variable-regions)
* [Mode 2: extract from primers](https://github.com/AlessioMilanese/extract_regions_16s#mode-2-extract-from-primers)
* [Notes and advance usage](https://github.com/AlessioMilanese/extract_regions_16s#notes-and-advance-usage)
* [Details of implementation](https://github.com/AlessioMilanese/extract_regions_16s#details-of-implementation)
* [Options list](https://github.com/AlessioMilanese/extract_regions_16s#options-list)

Installation
--------------
```bash
git clone https://github.com/AlessioMilanese/extract_regions_16s.git
cd extract_regions_16s
```

Note: in the following examples we assume that the python script ```extract_regions``` is in the system path.

**Pre-requisites:**
* cmalign ([Infernal](http://eddylab.org/infernal/))

Simple example
--------------
The expected input is a fasta file with one (or more) 16S sequences, example:
```bash
cat my_16S_seq.fasta
>seq1
CAGTATTAGCGGGGATCATCGATCGATTACGATCGAGCTAGC....
>seq2
CAGTATGATCGCGGATCATCGATCGATTACGATCCAGCTAGG....
```

Running:
```
extract_regions -i my_16S_seq.fasta
```

results is:
```
>seq1__V1
ACACAGCAUGCAUAACACGAGCUAUCGACGACUACGACGGCA
>seq1__V2
CAUCAGUACCGAUCAUCGGAAUCAGCGAGGCAGGCGAAGGCGAGAGAGCAUAC
...
>seq1__V8
ACUACGUGCACGAGUACGUAUACGGACAUCGAUUUACGAGCAGCGA
>seq1__V9
ACAGAUCGGAUUCGAUCGGCAUCGGACCCAUCAGGAGGAUCGUCAAUCAUG
```

Mode 1: extract variable regions
--------------
If you don't specify any primer (with `-f` and `-r`), then all the variable regions will be extracted.
We extract the variable regions defined in [Yarza et al. Nat. Rev. Microbiol. (2014)](https://www.nature.com/articles/nrmicro3330):

| Variable region | Start | End |
| :---: | :---: | :---: |
| V1 | 69 | 99 |
| V2 | 137 | 242 |
| V3 | 433 | 497 |
| V4 | 576 | 682 |
| V5 | 822 | 879 |
| V6 | 986 | 1043 |
| V7 | 1117 | 1173 |
| V8 | 1243 | 1294 |
| V9 | 1435 | 1465 |

These positions refers to the 16S rRNA gene of *Escherichia coli* str. K-12.
The output is a fasta file with 9 times more sequences (one for each variable region) than the input fasta file.

The regions are indicated with `__V[1-9]` at the end of the fasta header (see also [Simple example](https://github.com/AlessioMilanese/extract_regions_16s#simple-example)).

Mode 2: extract from primers
--------------

| For Primer | Start | End | Relative position | | Rev Primer | Start | End | Relative position |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 8F | 8 | 27 | before V1 | | 338R | 338 | 355 | after V2 |
| 27F | 8 | 27 | before V1 | | 519R | 519 | 536 | after V3 |
| 68F | 49 | 68 | before V1 | | 785R | 785 | 805 | after V4 |
| 341F | 341 | 357 | before V3 | | 806R | 787 | 806 | after V4 |
| 515F | 515 | 533 | before V4 | | 907R | 907 | 926 | after V5 |
| 967F | 967 | 985 | before V6 | | 926R | 907 | 926 | after V5 |
| 1237F | 1220 | 1237 | before V8 | | 1100R | 1100 | 1115 | after V6 |
| | | | | | 1391R | 1391 | 1407 | after V8 |
| | | | | | 1492R | 1492 | 1510 | after V9 |


Notes and advance usage
--------------


Details of implementation
--------------


Options list
--------------
