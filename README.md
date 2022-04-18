## Recent Form App
### Project Brief
<details>
<summary>"Summary of Project brief requirements"</summary>

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
![ERD](link)  
The database relationship is modelled here with the green tables being tables that have been implemented and red being tables that are set to be implemented in the future. The green databases (Teams and Games) are linked through a one mandatory (Teams) to many optional (Games) as each team may play many games, but exist whether they have had game entries or not, and no game can exist without there being a team (and the game entry cannot include more than one team at a time). In the future, there may also be a new table (Game Type) that models a similar relationship towards Games, but that has a many optional to many optional relationship towards teams as both Teams and Game Types can contain multiple of each other, or none.  

### Trello Board
Here is a screenshot of the kanban board used in my project to demonstrate the progression that has occured.  
Here is a link to the full Trello Board:  
https://trello.com/b/UJVoEN6i/first-flask-project  
![Trello Board](Link2)  
The project tracks progress from start to finish using the following headings that mark the position:
* User Stories - a set of parameters I have designed to implement the application from the point of view as a user. The user stories have been colour coded according to at which point in my to do list the tasks related to it occur (green='completed', yellow='doing', red='to do') 
* To Do - the original state of each task (no development having been completed in any task under this heading)
* Doing - an 'in progress' state of being (some development has occured)
* Completed - a completely finished task/feature
* Testing - tracks any tests that have been set up (has no progression but is useful to track)

### Application Front-End Demonstration
The following paragraph demostrates the way in which the application works and how the user may interact with it. It is also the expected outcome for anyone looking to clone down this repository.  
The url itself takes the user to the homepage (index):  
![Homepage](link3)  

From here you may navigate the page. To enter a new game you need to navigate to the 'Add Game' section of the navigation bar.  
This will show the following page:  
![Add Game](link4)  
Games that have been entered will then be sorted into their appropriate html pages to allow for easy viewing for the user. All database entries will be included in the 'All Entries' section, from which the user can choose to include or delete any entry.  
![All Entries](link5)  
The games will also be sorted into a page for each of the team entries, for example all Arsenal game entries are included in the 'Arsenal' page:  
![Arsenal](link6)  
If the games 'included' value is set to true (as is default), the most recent 5, in date order and for each team, will be included in the 'included entries' page.  
![Included Entries](link7)  
Of the game entries that are 'included', the points values will be summed and displayed on the 'Table' page as follows:  
![Table](link8)  

### Testing
The application uses pytest to unit-test for server responses on each of the web pages and tests that the 'create' function of the application (adding a game entry) works as it should. Jenkins automates these tests and produces detailed coverage reports. The reports recieved in this application detail a high level of coverage, with room for improvement detailed in the 'missing' lines element.  
![Tests](link9)  

### CI Pipeline
The CI pipeline for this application details the automated integration process that Jenkins utilises. Code is uploaded from a local machine to github (or work is taken from the kanban board) where it is then pushed to the CI server through a webhook, tested using pytest, and returned back through github and out to the virtual machine. As such, it automates the integration process and produces detailed reports as they occur.  
![CI Pipeline](link10)

### Risk Assessment
Here is a screenshot of the risk assessment with a link to a larger version available here:  (link...)

### Known Issues
There are currently two known errors that can cause issues with the application:  
* Deletion error - in some instances of large amounts of data deletion, the application will display an error page. This can be rectified by returning back to the original URL and the app will operate as normal.
* Database error - if there is no information in certain elements of the database, the application will not run and will have to be completely reset in order to fix. 

### Future Improvements
In the future there is several things that could be changed and improved that have been detailed in the Kanban board associated with this project and are as follows:
* Having the ability to sort out the 'Table' data to display in order of the value of total points (to display more like a league table)
* Adding a third table with 'Game Type'
* From this creating 'recent form' pages for each respective game type (and allow the user to display whichever team they may choose)




