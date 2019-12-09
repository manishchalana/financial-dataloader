# financial-dataloader

A folder containing the historical data corresponding to various attributes

e.g. let's assume the folder has open (fopen.csv), high (fhigh.csv), low (flow.csv), close (fclose.csv) historical data on futures.

The data in each file is stored in the following format. Let's say below is the close price for a few tickers.

| Dates  | RANBAXY  | VIJAYABANK  | BAJAJHIND  | MPHASIS  |
|---|---|---|---|---|
| 1/2/2007  | 402.3|47.75|183.77|305.65|
| 1/3/2007 | 414.15|48.45|184.06|317.55|
| 1/4/2007  | 414.45|49.3|182.46|312.1|
| 1/5/2007  | 414.95|48.5|173.13|304.25|

The dataloader object will read all the data in the above format and produce a dataloader (a generator object) which can yield the data by stock or by specific number of datapoints. 



