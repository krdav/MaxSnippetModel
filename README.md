### Forked from [here](https://github.com/jostmey/MaxSnippetModel)

Changed a few things mainly in `dataplumbing.py`.
The input file format is simply a tab separated file with three columns:
```CDR3	subject_id	diagnose_0_or_1

No header should be provided e.g.:
```
CASSLEGYTEAFF   HIP04511        1
CAISTGTAAGANGLTF        HIP15861        1
CASRGTAYNSPLHF  HIP01004        0
CASSSQGVSGDEQYF HIP04511        1
CASSEARNSPLHF   HIP01004        0
CASSLGATEAFF    HIP04511        1
CASSQGGPDTQYF   HIP17723        1
CAWSLSNYQPQHF   HIP17723        1
CASSSGRADTQYF   HIP15861        1
CAWSGLAGEQFF    HIP14238        0
```

