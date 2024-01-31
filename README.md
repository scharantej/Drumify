## Flask Application Design: Online Drum Lessons Website

## HTML Files
- **index.html**:
  - Serves as the homepage, containing information about the website's purpose and tutorials.
  - Consists of sections for intermediate and advanced drummers, each with tailored content.


- **lessons.html**:
  - Contains the actual drum lessons, divided into separate sections for intermediate and advanced learners.
  - Each section includes text explanations, interactive drum set images, and video demonstrations.


- **quiz.html**:
  - Features interactive quizzes to test the user's progress and reinforce learning.
  - Consists of multiple-choice questions covering various drumming techniques and concepts.


## Routes
- **/**:
  - Route for the homepage, served by the `index.html` template.


- **/lessons**:
  - Routes to the lessons page, serving the `lessons.html` template.


- **/quiz**:
  - Routes to the quiz page, serving the `quiz.html` template.


- **/about**:
  - Route for the about page, containing information about the website's creators and objectives.
  - Served by a dedicated `about.html` template.


- **/contact**:
  - Route for the contact page, allowing users to submit queries and feedback.
  - Served by the `contact.html` template and includes a contact form for user input.