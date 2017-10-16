Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/manaswineebezbaruah/Desktop/Junk.py ============
length limt: 0
Is iteration faster? False
length limt: 10
Is iteration faster? False
length limt: 20
Is iteration faster? False
length limt: 30
Is iteration faster? False
length limt: 40
Is iteration faster? False
length limt: 50
Is iteration faster? False
length limt: 60
Is iteration faster? True
length limt: 70
Is iteration faster? True
length limt: 80
Is iteration faster? False
length limt: 90
Is iteration faster? True
length limt: 100
Is iteration faster? True
length limt: 110
Is iteration faster? True
length limt: 120
Is iteration faster? True
length limt: 130
Is iteration faster? True
length limt: 140
Is iteration faster? True
length limt: 150
Is iteration faster? True
length limt: 160
Is iteration faster? True
length limt: 170
Is iteration faster? True
length limt: 180
Is iteration faster? True
length limt: 190
Is iteration faster? True
length limt: 200
Is iteration faster? True
length limt: 210
Is iteration faster? True
length limt: 220
Is iteration faster? True
length limt: 230
Is iteration faster? True
length limt: 240
Is iteration faster? True
length limt: 250
Is iteration faster? True
length limt: 260
Is iteration faster? True
length limt: 270
Is iteration faster? True
length limt: 280
Is iteration faster? True
length limt: 290
Is iteration faster? True
length limt: 300
Is iteration faster? True
length limt: 310
Is iteration faster? True
length limt: 320
Is iteration faster? True
length limt: 330
Is iteration faster? True
length limt: 340
Is iteration faster? True
length limt: 350
Is iteration faster? True
length limt: 360
Is iteration faster? True
length limt: 370
Is iteration faster? True
length limt: 380
Is iteration faster? True
length limt: 390
Is iteration faster? True
length limt: 400
Is iteration faster? True
length limt: 410
Is iteration faster? True
length limt: 420
Is iteration faster? True
length limt: 430
Is iteration faster? True
length limt: 440
Is iteration faster? True
length limt: 450
Is iteration faster? True
length limt: 460
Is iteration faster? True
length limt: 470
Is iteration faster? True
length limt: 480
Is iteration faster? True
length limt: 490
Is iteration faster? True
length limt: 500
Is iteration faster? True
length limt: 510
Is iteration faster? True
length limt: 520
Is iteration faster? True
length limt: 530
Is iteration faster? True
length limt: 540
Is iteration faster? True
length limt: 550
Is iteration faster? True
length limt: 560
Is iteration faster? True
length limt: 570
Is iteration faster? True
length limt: 580
Is iteration faster? True
length limt: 590
Is iteration faster? True
length limt: 600
Is iteration faster? True
length limt: 610
Is iteration faster? True
length limt: 620
Is iteration faster? True
length limt: 630
Is iteration faster? True
length limt: 640
Is iteration faster? True
length limt: 650
Is iteration faster? True
length limt: 660
Is iteration faster? True
length limt: 670
Is iteration faster? True
length limt: 680
Is iteration faster? True
length limt: 690
Is iteration faster? True
length limt: 700
Is iteration faster? True
length limt: 710
Is iteration faster? True
length limt: 720
Is iteration faster? True
length limt: 730
Is iteration faster? True
length limt: 740
Is iteration faster? True
length limt: 750
Is iteration faster? True
length limt: 760
Is iteration faster? True
length limt: 770
Is iteration faster? True
length limt: 780
Is iteration faster? True
length limt: 790
Is iteration faster? True
length limt: 800
Is iteration faster? True
length limt: 810
Is iteration faster? True
length limt: 820
Is iteration faster? True
length limt: 830
Is iteration faster? True
length limt: 840
Is iteration faster? True
length limt: 850
Is iteration faster? True
length limt: 860
Is iteration faster? True
length limt: 870
Is iteration faster? True
length limt: 880
Is iteration faster? True
length limt: 890
Is iteration faster? True
length limt: 900
Is iteration faster? True
length limt: 910
Is iteration faster? True
length limt: 920
Is iteration faster? True
length limt: 930
Is iteration faster? True
Traceback (most recent call last):
  File "/Users/manaswineebezbaruah/Desktop/Junk.py", line 95, in <module>
    time_comparison()
  File "/Users/manaswineebezbaruah/Desktop/Junk.py", line 82, in time_comparison
    split(species_list,limit)
  File "/Users/manaswineebezbaruah/Desktop/Junk.py", line 68, in split
    split(species_list,limit)
  File "/Users/manaswineebezbaruah/Desktop/Junk.py", line 68, in split
    split(species_list,limit)
  File "/Users/manaswineebezbaruah/Desktop/Junk.py", line 68, in split
    split(species_list,limit)
  [Previous line repeated 979 more times]
  File "/Users/manaswineebezbaruah/Desktop/Junk.py", line 55, in split
    species1 = species.new_child()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/DendroPy-4.3.0-py3.6.egg/dendropy/datamodel/treemodel.py", line 1671, in new_child
    node = self.__class__(**kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/DendroPy-4.3.0-py3.6.egg/dendropy/datamodel/treemodel.py", line 1005, in __init__
    length=kwargs.pop("edge_length", None))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/DendroPy-4.3.0-py3.6.egg/dendropy/datamodel/treemodel.py", line 746, in __init__
    basemodel.DataObject.__init__(self, label=kwargs.pop("label", None))
RecursionError: maximum recursion depth exceeded
>>> 
