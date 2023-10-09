# Betting-Trends

This project takes all of the Odds per NFL game (once a day) and displays them on a graph. This 
tool can be used to track odds movement between NFL games throughout the week to see the odds 
movement/direction. This can be useful to handicappers/bettors to move with or against the public 
and have that data handed to them in one centralized place.

This project uses python lambda funstions to pull the data and put all the data
in AWS Dynamo databases. This NoSQL DB is useful because of how easy and least overhead 
is needed to build and manage this DB. Then, more lambda functions will read from the DB
twice a data and create a graph based on each game. The graph is posted to a static 
HTML file hosted in AWS S3. On this webpage is The game, odds graph, and logged data of when
the odds were recorded. Happy betting !

![image](https://github.com/Daniel-Higgins/Betting-Trends/assets/32625437/df68ea25-bb2b-472e-87ba-2a9d8088e970)
