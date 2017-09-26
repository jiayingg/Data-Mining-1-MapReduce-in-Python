# Data Mining 1 MapReduce in Python

## Problem 1 Social network: finding connections

In this problem, consider a social graph where nodes are people and edges represent their friendship. You are to write a MapReduce program to find indirect connection between two people.

There is an indirect connection between two persons X and Y if X and Y are connected via a third person Z. In other words, there exist edges (X, Z) and (Z, Y). For example, there is an indirect connection between “john” and “david” since both are connected to “mary”. Note that in this problem, we assume that X and Y may also be directly connected (i.e., there is an edge between X and Y) even though there
may exist some indirect connections between X and Y.

For every indirect connection, say X and Y connected via Z as described above, output: [X, Y, Z]. Notethat there may be multiple indirect connections between X and Y, e.g., [X, Y, W]. You need to output all connections via a different third person, e.g., Z and W. But you should only output once for every unique connection. That is, either [X, Y, Z] or [Y, X, Z] but not both.

The input will be provided as a JSON document where each line represents an edge on the graph. For example:

[“john”, “mary”]
[“mary”, “david”] 

## Problem 2 Descriptive statistics: variance

In this problem, you are provided with a large number of integers, pre-divided into chunks, with each chunk stored as a line (an JSON array) in the input file (see below). Your task is to compute the variance of the integers using MapReduce. Recall that the variance can be computed as the average of X2 minus the square of the average of X, as show below. 
 widehat{ab} 

Here is the sample input: 

[3, 5, 11, 2, 5]
[2, 8, 22, 92, 123, 78] 
