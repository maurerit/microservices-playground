# microservices-playground

I simple playground to build microservices while learning what I like and dislike and how to handle what I dislike or
 rather... what will end up becoming the support nightmares/headaches.

The database ddl is in the *-model projects src/main/resources folder as mysql-schema.sql.  Import these, start the 
discovery-server projects app and then spawn the remainder of the services.

## shopping-cart-dao-spi

This project is the basic demand of the actual dao projects.  It's existence only came about because I wanted to be 
able ot easily play around with raw jdbc using springs JdbcTemplate and JPA using spring-data-jpa

## shopping-cart-*-dao projects

One project for each implementation of jdbc and jpa.  This provides for easily swapping out the underyling 
implementation at run time using the two profiles in the shopping-cart project ;).

## shopping-cart-model

Should be self explanatory.  This was broken out due to not wanting circular references \*-dao\* projects and the 
shopping-cart project. 
