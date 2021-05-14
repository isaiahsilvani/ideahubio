# IDEAHUBI, AN IDEA SHARING APP
### Thank you for checking out my application!
## Create and share your next startup idea [now!](https://ideahubio.herokuapp.com/)

## Description
The purpose of this app is to allow users to have a platform to not only create and store their business ideas for future reference, but also to bring innovators together to discuess these ideas. The social application allows users to make their ideas public, have those ideas liked, and even further discuss the idea in a real time chatroom using Web Sockets.
## Wireframe
![IdeaHubIO Wireframe](https://i.imgur.com/3hgYLzA.png)

## User Story and Pseudo-Code
[Whimsicla Link](https://whimsical.com/ideahub-io-user-stories-Gi7jRbEqxxAhGjMZMpj36i)
## Instructions
In order to use the full functionality of this app, users must be signup an account, no email verification required. Users then have the option to create a new idea, and are prompted with a form to input basic details. From there, users can also upload photos for a logo and additional photos as they see fit. Users will have the option to either make their idea public, or private. If public, the idea is displayed in the "Public Ideas" thread, which can be reached using the navigation bar at the top of the screeen. Users can also like ideas, and enter a chatroom specific to that idea to have a real time discussion about it.


 ## User Persona
 Todd just graduated from a Coding Bootcamp, and is now thinking about a creating a startup company. But, before Todd invests time and money into making his dreams a reality, he would like to gain some honest feedback from people other than friends and family. So, Todd goes on IdeaHubIO, creates his idea using the New Idea form, and sets his idea to public so others can see it. Todd now sees that 20 people liked his idea, and there is an active discussion in his idea's chatroom. With all the positive feedback recieved from the users of IdeaHubIO, Todd knows he has a great idea and is now ready to truly pursue it.

## Application Screenshots
![Application Screenshot 1](https://i.imgur.com/F7lvqgy.png)
![Application Screenshot 2](https://i.imgur.com/8MegUfr.png)
![Application Screenshot 3](https://i.imgur.com/z2G2xjQ.png)
## Technologies Used
Django, Python, Postgresql, JavaScript, Django Channels, HTML5, CSS3

## Technologies Used for Deployment
Heroku, Daphne, Docker, Redis

## Accessiblity
This web application features a Mobile Responsiveness so that anyone with a web browser and internet connection can share their startup ideas to the internet. 

## Unresolved Chatroom Database Connection Issue
Due to the fact that the Django ORM is a synchronous package, it cannot be used traditionally inside the asynchrnous consumer file which makes the chatroom. According to Django Channels documentation, there is a @database_sync_to_async decorator which can be imported to convert the Django ORM to an asynchronous process. However, when implementing this functionality, the Django ORM does indeed become asynchronous, but it is still unable to create new model instances to the database. I plan to look into this and fix this functionality so I can develop a real time, persistent chatroom 

## Next Steps
- Fix chatroom database connection issue
- Add usernames to disconnect and connect message web socket events
- Further develop mobile responsiveness


## Credits
#### Styling
[Text Typing Animation](https://codepen.io/raubaca/pen/rxLwPq)


