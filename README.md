# Precision Health Challenge 2021-22

**DOCFLIX** - Recommends medical specialists. With the help of coputer vision, it makes it easier for people with less knowledge about medical domain. 

# Problem Statement
As the majority of people aren't aware of exactly what kind of illness, pain or discomfort they are facing, we tend to provide them a better perspective about it. Our solution works on identifying the pin-point location where our user is experiencing pain or discomfort as they point their finger towards it, using Computer Vision.

Further, we ask a couple of questions customized to the affected area pointed by the user, to get a better understanding of the cause of the pain. Then by using Machine Learning Algorithm i.e., Decision Tree Classifier, we recommend possible medical issue(s) our user might be suffering with. Our star module, is to predict the best suited medical specialist for the disease diagnosed by the symptoms incurred. We also provide a document / report to the Doctor / Medical Specialist (if selected) by our user and to the user as well, which contains the Basic Details, Symptoms, Disease Predicted, and the other optional message, our user wants to convey to the Doctor beforehand.

# Key Value Proposition

 - Explicit medical care for the users is prioritised by **DOCFLIX**.
 - **DOCFLIX** offers the precise medical specialist for the specified affected area of the user.
 - Our Dataset involves **160+** Diseases and **450+** symptoms. 
 - Machine Learning Algorithm i.e., Decision Tree Classifier is preferred which offers higher accuracy on the non-linear dataset considered for **DOCFLIX**.
 - Computer Vision providing the pin-point recognition of the discomfort region of the user.
 - Simplicity is favoured as the user just needs to point at the area of discomfort.
 - Waiting time for patients / users is drastically reduced for consultation by General Physicians / Doctors and at Hospitals OPD's.
 - **DOCFLIX** bridges the communication gap between Doctors and Patients.
 - Efficient usage of Time and Money as a potential resource in the field of medical facilities.
 - Ready Home Preparedness and Bilingual Support for the users.

# Target Customer
### Our website has something for everybody. We specifically target,

  - Uneducated people who find it difficult to identify their specific point of care, and subsequently the medical specialist required for the treatment. 
  - People having less knowledge and are unaware about the medicinal terms.
  - Doctors – For the efficient utilisation of their appointment times.
  - Medical Organisations – To cut on the chain of Physicians / Doctors and thereby reducing corruption down the line.
  - People who aren’t comfortable with English. (Our website provides bilingual support - English & Hindi language).

# Proposed solution

Our software solution has the following components:

- **Computer Vision**\
   Our website gives the user the option to open his/her webcam and point their index finger at the area where there is discomfort. Then, with the help of computer vision, we will be identifying the pointed body part, thus deriving meaningful information through visual inputs.
- **Machine Learning**
   - **Disease Prediction**\
     After gathering the symptoms from the user, the symptoms are matched with the trained model in order to get the accurate disease prediction. For training the dataset, we used Decision Tree Classifiier. Dataset link: https://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html
   - **Medical Practitioner Recommendation**
     In order to get the correct Medical Practitioner, the diseases are mapped to their respective Medical Practitioners, thus solving the problem of 'Which doctor to consult?'

-  **Report Generation**
   Our website also has the feature of generating report after filling the form to make an appointment with the doctor. The generated report has the following content:\
      a. Name\
      b. Email\
      c. Contact No.\
      d. Date\
      e. Department\
      f. Doctor\
      g. Message\
      h. Symptoms 
  
    This will help the user as it will give prior information regarding the disease as well as for the doctor since the generated report will reduce consultancy time and will be time saving solution.
- **Language**\
   As, India is a diversified country and a home of various cultures and languages.\
   Our website is bilingual, which tends for everyone irrespective of their native language. DOCFLIX supports both English and Hindi.

# Work Flow Diagram

![Screenshot](https://github.com/shourya-gupta/VIT_JMI_Phoenix/blob/main/WORKFLOW_DIAGRAM.png?raw=true)

# Technology Stack Used
### DOCFlix works involving varied Technologies – 

#### Frontend – 
 - HTML5 for the structure
 - CSS3 for designing
 - JavaScript for interactivity.
 - Bootstrap Framework is used to enhance User Interface.
#### Backend –
- Python Language is used as it provided large library support
- Framework – Django is used for Integration with frontend requests.
- OpenCV captures the user video.
- Mediapipe module helps in the identification of the specific body part.
- Django_crispy_forms is used for user authentication and login database
- Fpdf module is used for PDF processing.
- Pandas, numpy, and sklearn is used for handling CSV files and data analysis.

# Implementation Screenshots


![Screenshot](https://github.com/shourya-gupta/VIT_JMI_Phoenix/blob/main/1_image.PNG?raw=true)

![Screenshot](https://github.com/shourya-gupta/VIT_JMI_Phoenix/blob/main/2_image.PNG?raw=true)

![Screenshot](https://github.com/shourya-gupta/VIT_JMI_Phoenix/blob/main/3_image.PNG?raw=true)

![Screenshot](https://github.com/shourya-gupta/VIT_JMI_Phoenix/blob/main/4_image.PNG?raw=true)

# Video Link 
## Explaining the problem statement and the proposed solution

https://drive.google.com/file/d/1V7j-U6YndexWF2_1Iv2ppdBqHo4fxuZc/view?usp=sharing

# Demo Link
## Demonstration of the project

https://drive.google.com/file/d/1yaX9mTNBSg-xewcY3npYkMOErq8cvHfl/view?usp=sharing

# Step by Step Procedure to run the project on your Local Machine

 1. Download the project through the below mentioned link or as a ZIP file from GitHub. https://github.com/shourya-gupta/VIT_JMI_Phoenix
 2.	Extract the Downloaded ZIP to a folder.
 3.	Download and Install Python on your platform through this link https://www.python.org/downloads/
 4.	Switch on to your favourite Integrated Development Environment (IDE) as the project is platform independent (Windows / Linux / MacOSX) as well as IDE independent (PyCharm, VS Code). We have preferred Visual Studio Code (VS Code) as our IDE.
 5.	Download and Installation link for Visual Studio Code – https://code.visualstudio.com/download
 6.	Open VS Code on your Platform and Navigate to File Button at the Top Corner
 7.	Click Open Folder, browse to your extracted folder and select that folder.
 8.	Navigate to required_modules.txt file from the left pane in the folder and install the mentioned modules.
 9.	To install a specific module. For example – Django. Follow the below steps –

     I.   In VS Code, Press Ctrl+` (for windows) to open the terminal\
     II.  Type the following command pip install django --user\
     III. VS Code will automatically install the Django and its subsidiary modules.\
     IV.  Once done, you will see a successful installation message\
     V.   Similarly, install other mentioned modules following I, II, III and IV steps

 10.	Now, enter the following command in the terminal – python manage.py runserver
 11.	If you encounter with an error, file not found. Right Click on the manage.py file in the left side bar, click on copy path, and replace manage.py with the path in the above command.
 12.	Now, you will see Starting Development Server stating the link of the website.


# Thank you :)
## TEAM PHOENIX
### Shourya, Ritik, Ridhika, Kshitij
