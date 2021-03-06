## Recent Form App

Link to Video Presentation: https://drive.google.com/file/d/1pn2Sm2EMzdhXzKW5r8MyGPq-a1r4ljug/view?usp=sharing  
*Please note there is a small error on the video @ 10:20, the foreign key talked about is in the GAMES table, not TEAMS (it is the primary key of TEAMS)

### Project Brief
<details>
<summary>Summary of Project brief requirements</summary>

The project brief issues the following requirements:  
* To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.    

In order to have the MVP the project requires (summarised):  
* A Trello Board
* A relational database with at least 2 tables
* Clear Documentation at all stages
* A Python CRUD application
* Tests (including automated tests)
* Front-end website
* Code integrated into version control system
</details>

Following the project brief, I have set about to create a recent form
application that allows the user to keep track of whichever football games they see fit. In the current stage of application the user may only choose from the 'top 6' teams within the Premier League, but the games that can be entered can currently be from any league, giving the user flexibility in their records. The application comes with several features:  
* Create a game entry (satisfies 'Create') in which the user is able to input records of football games with the following information:  
  * Team Name (out of a choice of 6 from the Teams table)
  * Game Date
  * Home or away
  * Result (Win/Draw/Loss)
  * Points (3/1/0)
  * Opponent (can be from any league/cup currently)
  * Comment (to allow the user to have extra information about the game
  * Included (True/False)
    * the default option will be 'included'
    * if a user wishes to not include a game, (for whatever reason but an example could be "there were 2 red cards" or "young team starting") then they can do so through updating this value (satisfies 'Update').
* Multiple Html pages that display different database information (satisfies 'Read'):  
  * Arsenal  
  * Chelsea 
  * Liverpool
  * Manchester City
  * Manchester United
  * Tottenham
  * Team Information
  * All Entries
  * Included Entries (entries with the included value set to true) 
  * Recent Form (a page that displays a sum of the 5 most recent included=True entries)
* Delete Feature (satisfies 'Delete'):
  * Any games that have been entered into the system come with a delete button that allows the user to remove it from database.  

### Entity Relationship Diagram
Here is the ERD relationship diagram, modelling the interactions between my databases:    
![picture9](https://user-images.githubusercontent.com/101715863/163982727-f56a640e-0d89-4ea3-a054-325fbb0b41ff.png)
Link to image: https://drive.google.com/file/d/1mlSpFh55QYBSEO9k5Oy9ZFDWR9EUFu5b/view?usp=sharing  
The database relationship is modelled here with the green tables being tables that have been implemented and red being tables that are set to be implemented in the future. The green databases (Teams and Games) are linked through a one mandatory (Teams) to many optional (Games) as each team may play many games, but exist whether they have had game entries or not, and no game can exist without there being a team (and the game entry cannot include more than one team at a time). In the future, there may also be a new table (Game Type) that models a similar relationship towards Games, but that has a many optional to many optional relationship towards teams as both Teams and Game Types can contain multiple of each other, or none.  

### Trello Board
Here is a screenshot of the kanban board used in my project to demonstrate the progression that has occured.  
Here is a link to the full Trello Board:  
https://trello.com/b/UJVoEN6i/first-flask-project  
![2022-04-19 (18)](https://user-images.githubusercontent.com/101715863/163982907-b2c54317-b922-4098-bb85-666b20ae3426.png)
Link to image: https://drive.google.com/file/d/1D1OAN2PYvpsMsk08xewifjz91pF92Ej1/view?usp=sharing  
The project tracks progress from start to finish using the following headings that mark the position:
* User Stories - a set of parameters I have designed to implement the application from the point of view as a user. The user stories have been colour coded according to at which point in my to do list the tasks related to it occur (green='completed', yellow='doing', red='to do') 
* To Do - the original state of each task (no development having been completed in any task under this heading)
* Doing - an 'in progress' state of being (some development has occured)
* Completed - a completely finished task/feature
* Testing - tracks any tests that have been set up (has no progression but is useful to track)

### Application Front-End Demonstration
The following paragraph demostrates the way in which the application works and how the user may interact with it. It is also the expected outcome for anyone looking to clone down this repository.  
The url itself takes the user to the homepage (index):  
![Picture3](https://user-images.githubusercontent.com/101715863/163983236-2f5454d5-f60d-4da7-aa49-2f7af97e0e8e.png)   
Link to image: https://drive.google.com/file/d/10gu-X84RmqKHuyFhznJeQ-h_JmQg0UoW/view?usp=sharing  

From here you may navigate the page. To enter a new game you need to navigate to the 'Add Game' section of the navigation bar.  
This will show the following page:  
![picture](https://user-images.githubusercontent.com/101715863/163984147-733eeb85-9b86-43c5-93f4-c2eead066797.png)  
Link to image: https://drive.google.com/file/d/1V_9Pk8cVZN0wTJok25iWvVe8u4bwfJKu/view?usp=sharing  
Games that have been entered will then be sorted into their appropriate html pages to allow for easy viewing for the user. All database entries will be included in the 'All Entries' section, from which the user can choose to include or delete any entry.  
![picture4](https://user-images.githubusercontent.com/101715863/163985026-67021511-cd5e-4e5a-bac9-f90998f78cc9.png) 
Link to image: https://drive.google.com/file/d/1V5pHekIigHKKlXaNIIyHvmj8jXg_GDSq/view?usp=sharing  
The games will also be sorted into a page for each of the team entries, for example all Arsenal game entries are included in the 'Arsenal' page:  
![picture5](https://user-images.githubusercontent.com/101715863/163986104-9da5ddfd-c17a-46c5-8825-d8f374a085df.png)  
Link to image: https://drive.google.com/file/d/10WaayqvwmSfYNDefcpK45XlpOZWc2L_p/view?usp=sharing   
If the games 'included' value is set to true (as is default), the most recent 5, in date order and for each team, will be included in the 'included entries' page.  
![picture6](https://user-images.githubusercontent.com/101715863/163987019-9025ed65-cdd2-4d83-bd96-efd50a542959.png) 
Link to image:  https://drive.google.com/file/d/1RShkBvw5kBRsIIqVyN0dGRM80jZ3Pqsg/view?usp=sharing
Of the game entries that are 'included', the points values will be summed and displayed on the 'Table' page as follows:  
![picture7](https://user-images.githubusercontent.com/101715863/163987314-64702fa3-7676-4dbd-9d5e-2e449223c1ef.png)
Link to image:  https://drive.google.com/file/d/126XKGZt79ykeldU4mLHOPvyQq2uDSAkt/view?usp=sharing

### Testing
The application uses pytest to unit-test for server responses on each of the web pages and tests that the 'create' function of the application (adding a game entry) works as it should. Jenkins automates these tests and produces detailed coverage reports. The reports recieved in this application detail a high level of coverage, with room for improvement detailed in the 'missing' lines element.  
![Picture2](https://user-images.githubusercontent.com/101715863/163987438-ec55a7a1-3760-46ae-9e61-f00843f313cc.png)
Link to image:  https://drive.google.com/file/d/19CCr2DEPxCQL8RdMNwpO4R21ny0zz4gc/view?usp=sharing  

### CI Pipeline
The CI pipeline for this application details the automated integration process that Jenkins utilises. Code is uploaded from a local machine to github (or work is taken from the kanban board) where it is then pushed to the CI server through a webhook, tested using pytest, and returned back through github and out to the virtual machine. As such, it automates the integration process and produces detailed reports as they occur.  
![2022-04-19 (9)](https://user-images.githubusercontent.com/101715863/163987925-6cf32343-bf0f-41bc-84a5-cf3330cee701.png)  
Link to image:  https://drive.google.com/file/d/1yy0EFIUoe_P1vOmKv06UjJ4qDOurB5Gj/view?usp=sharing

### Risk Assessment
Here is a link to my risk assessment: https://docs.google.com/spreadsheets/d/1AS53x9t-2XX8800BTLzhhC-bXG4_zt8z/edit?usp=sharing&ouid=103462476978780985311&rtpof=true&sd=true

### Known Issues
There are currently two known errors that can cause issues with the application:  
* Deletion error - in some instances of large amounts of data deletion, the application will display an error page. This can be rectified by returning back to the original URL and the app will operate as normal.
* Database error - if there is no information in certain elements of the database, the application will not run and will have to be completely reset in order to fix. 

### Future Improvements
In the future there is several things that could be changed and improved that have been detailed in the Kanban board associated with this project and are as follows:
* Having the ability to sort out the 'Table' data to display in order of the value of total points (to display more like a league table)
* Adding a third table with 'Game Type'
* From this creating 'recent form' pages for each respective game type (and allow the user to display whichever team they may choose)




