# Cab_Hippo (Tax Hippokampoi)

## Introduction
Tax Hippocampoi is a company dedicated to great service in the city of Barranquilla; As the mighty Poseidon who was always traveling the seven seas on a carriage pulled by Hippokapoies, we want every customer to feel like a god with our outstanding service.

## Current Situation
Currently, the company has multiple taxi stations around the city of Barranquilla, each one in a strategic location to cover the whole city and provide fast and efficient service. Each Station is operated by a single person, who registers each Taxi when they arrive, and dispatches a Service when a Passenger arrives according to their needs and the Taxi number in line.

Our biggest challenge is with some locations where Passengers require a large trunk for storing groceries or baggage from a trip, the Station Operator, needs to go Cab by Cab, asking who has a large trunk for Passengers with baggage, which takes a lot of time when there are dozens of taxis, and gives our customers an impression of bad service.

## Vision
Our main goal for this project is to optimize the Response Time, Service Quality and overall experience for our customers. Being able to assign a Taxi Service to a customer according to their needs and keeping the Taxi Station Operator informed about the status of the Taxis available is the main reason for this project.

## Rules:
* The team must deliver a library, we only need the Logic to handle multiple taxis and multiple customers for a single taxi station
* The team must add a test directory with multiple tests of different situations
* The messages for the Station Operator must be en English
* The maximum amount of taxis per Taxi Station is 73
* When a customer needs a Taxi with a trunk, the system must find the first available taxi with a trunk and assign the * service, skipping the waiting line.
* When a new taxi arrives, it must be added to the waitlist
* The Station Operator must know the remaining amount of taxis after each Service Assignation
* When the Taxi Wait Line only has 10 Taxis, a message should be returned saying: “Please request more Taxis to this location”

