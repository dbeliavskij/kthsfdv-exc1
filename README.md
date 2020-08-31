# Excersice 1 of KTH Formula Student - Driverlees, Software Skill Training

## Visualisation

Below, plot of data posted in topics /Beliavskij and /kthfs/result can be found:
![alt text](https://github.com/dbeliavskij/kthsfdv-exc1/blob/master/2020-08-31_17-37-52_01_plot.png "Data visualisation")

Below, ROS network graph performed with rqt_graph, can be found:

![alt text](https://github.com/dbeliavskij/kthsfdv-exc1/blob/master/rosgraph.png "ROS Network visualisation")

## Questions

1. Task stated: "Additionally it shall be noted that you have limited network traffic capacity and are happily reducing every bit from your network throughput.". Was it required to use as small datatype as possible? Smaller data type was possible for node_a, but it would result in maximum number of 255, that's why UInt16 were choosen
2. Task stated: "First output your data, between each new coding step, respectively newly added feature and adhere to modular code development. You can use rostopic echo and rostopic list to visualise output." It is unclear what exact visualisation is required and at which steps it should be performed

## Instalation
No additional packages were used