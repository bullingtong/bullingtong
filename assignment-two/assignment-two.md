# Requirement Analysis
## Graeson Bullington

### Users

* Students
    * Students should be able to login to the software to identify the user's of the system
        * Entites: sID, studentPass
    * Students should be able to access the assignments the instructor/TA has assigned to the class
        * Entites: sID, assignID, instrucID, taID, classID
    * Students should be able to turn in files that are required by the assignment and reject files that aren't accepted by the assignment.
        * Entites: accepFiles, rejFiles, sID, classID, assignID
* Teaching Assistants
    * Teaching Assistants should be able to download the files that the students submit for the assignment that pertain to the class or group of the class that they're assigned.
        * * Entites: taID, sID, assignID, groupID, classID
    * They should also be able to give grades according to the work that the students give
        * Entites: sID, sGrade, assignID, classID, groupID, taID
    * They should be able to comment on their submission's if there are any issues with the program.
        * Entites: sID, assignID, classID, groupID, taID
    * They should be allowed to create, delete, and ammend assignments based on instructor permissions for the teaching assistants.
        * Entites: instrucID, classID, assignID, groupID, taID

* Teachers
    * Teachers should be allowed to create, delete, and ammend assignments
        * Entites: instrucID, classID, assignID, groupID
    * They should also be able to grade student's assignments and give them comments based on their grades.
        * Entites: sID, sGrade, classID, assignID, groupID, taID
    * They should be able to assign teaching assistants to groups within the classes if needed.
        * Entites: taID, classID, instrucID, groupID
    * They should be able to assign students to groups within the class if class size is big enough.
        * Entites: sID, classID, groupID, taID
    * They should be able to ammend students grades up until the last day for grades of the semester.
        * Entites: sID, sGrade, classID, instrucID, groupID, assignID

* System Administrators
    * SysAdmins should be allowed to assign students to classes based on the classes that they signed up for.
        * Entites: adminID, sID, classID, instrucID
    * They should be allowed to assign teachers to the classes that they are teaching.
        * Entites: adminID, classID, instrucID
    * They should be allowed to configure the permissions for all of the necessities needed from students, teachers, and teaching assistants. All without violating the FERPA privacy laws.
        * Entites: adminID, sID, instrucID, taID, classID
    * They should be able to ammend system configurations if the instructor 
    needs any changes made to them.
        * Entites: adminID, instrucID, classID@Delrod69


#### System constraints
* Web-Server to allow the students to access the website from the internet and domain name that will allow the students to type in a static string to access IP address for website.
* Database to allow the storage of student projects and student information. Also, allow the storage of assignments and information needed from instructor or teaching assistants.
* Machine compatible with accessing internet and being able to create programming files










