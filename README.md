# AIDA
Artificially Intelligent Dialogic Reading Aid

# Quick navigation
[Background](#background)  
[Data](#data)  
[Models](#models)  
[Timeline](#timeline)  
[Repo Structure](#repo-structure)  
[Logistics](#project-logistics)  
[Resources](#resources)  
[Contact](#contact-info)

# Goal
Create an AI-based dialogic question generating system to support parents of young readers. See [AIDA Notes](https://docs.google.com/document/d/1Roy4C3PgQ76B8761KBR9-KcFoJn6NJhB0z3mOo4xJng/edit) for more information. 

# Background  

**An overview of Dialogic Reading:**

Introduced by Whitehurst et al. (1988), dialogic reading ("DR") endeavors to turn shared book reading into a conversation about the story. To do this, parents are taught a sequence to follow while engaging with a book. 

<img width="551" alt="Screen Shot 2023-06-04 at 2 06 57 PM" src="https://github.com/vanderbilt-data-science/AIDA/assets/62776902/fcd9a81b-2ec3-4e1d-a511-622377f280f0">

The first step is prompting the child to talk about something in the book by asking a question. There are, of course, many different questions a parent could ask. To help parents remember these, parents are taught to use the acronym “CROWD,” with the letters standing for different types of prompts. 

“C” is for completion prompts: these are fill-in-the-blank questions, where the parent creates the sentence frame, setting the child up to complete it (e.g., “When we eat soup, we use a .....")

“R” is for recall prompts: these are questions that require the child to remember aspects of the book (e.g., "Can you remember some of the things that Sally did at school?"). 

“O” is for open-ended questions: these are statements that encourage the child to respond to the book in his or her own words (e.g., "Now it’s your turn to tell about this page” or “What do you think will happen next?”). 

“W” is for who, what, where, when, and why questions (e.g., "What is this called?" or "Why did Peter stay home from school?"). 

"D” is for distancing prompts: these are questions that require the child to relate the content of the book to aspects of life outside of the book (e.g., "Did you ever stay home from school like Peter did?"). 

The child might not always answer the prompts – perhaps because they do not know the answer, or they just are not used to talking while reading a book. When this happens, parents are encouraged to try easier questions to get the child started – or to just answer their own questions and see if the child will repeat what they say. But, when the child does answer the parent’s questions, parents are encouraged to respond to keep the conversation flowing. Whitehurst and colleagues also developed tips to help parents do this, creating the acronym “PEER” to help parents remember the sequence. 

“P” stands for prompt: for this step, parents are encouraged to use any of the CROWD prompts. 

“E” stands for evaluate: parents are encouraged to evaluate their child’s responses to the prompts by praising a correct answer or gently correcting one that is not quite right (e.g., “That’s right! We use a spoon to eat soup!” or ‘Hmm, I don’t think we eat soup with a fork – we use a spoon to eat soup!”). 

“E” also stands for expand: parents are encouraged to expand on their child’s response in a way that provides more information (e.g., after saying “That's right, we use a spoon to eat soup!” the parent could add “We also can use a spoon to eat ice cream.”).

“R” stands for repeat: if the child is willing, parents are encouraged to have them repeat the expanded response (e.g., “Yes, we use a spoon to eat soup and ice cream. Can you say that?”). Additionally, dialogic reading emphasizes the value of reading the same book again later, and to keep coming back to it again and again. 

** Here is Margaret's Dissertation manuscript (with more information about DR): http://hdl.handle.net/1803/18172

# Repo Structure
When applicable, this repository contains numbered jupyter notebooks, which correspond to different stages of project development and final products. The numbering system is as-follows:
* 10-series notebooks (10-19) will correspond to prompt development.
* 20-series notebooks (20-29) cover handling of the database of childrens books and the book API.
* 30-series notebooks (30-39) handle WHISPER and audio-related components.
* 50-series notebooks (50-59) are for development of the full pipeline and front-end.

When possible, notebooks within a numbered series roughly follow each other - i.e. the first notebook in a series should be labeled 10,20,30,etc, with notebooks that build off of that work being labeled 11,12, etc. Within the correct numbering scheme, notebooks titles contain short descriptions of the task that the notebook covers, separated by dashes, i.e (33-whisper-basic-inferencing.ipynb)

# Timeline

Outline the desired timeline of the project and any explicit deadlines.


# Project logistics

**Sprint planning**: Mondays at 11:30am Central

**Retrospective**: Fridays at 11:30am Central

**Demo**: Fridays at 3:00pm on Zoom []


**Slack channel**:  https://datasciencetip.slack.com/archives/C04NE3C2525

**Zoom link**: https://vanderbilt.zoom.us/j/95130287754?pwd=bkpwamkxKzZvV0I4eklVNzNGOGh6dz09


# Resources 

**Free online e-book repositories:**

- **Open Library's Student Library**, a School Library designed for a k-12 audience: https://openlibrary.org/collections/k-12
- **Children's Library Internet Archive**, books for children from around the world: https://archive.org/details/iacl
- **University of Maryland's International Children's Digital Library**, a Library for the World's Children: http://en.childrenslibrary.org/
- **StoryWeaver**, a free library of books in different languages: https://storyweaver.org.in/
- **ReadConmigo**, https://www.readconmigo.org/
- **Unite for Literacy** has a library of many digital children's books, which can include narration (in multiple languages): https://www.uniteforliteracy.com/
- **BookSpring** has a library of books and activities for different reading levels/ages: https://www.bookspring.org/en/weekly-themes-lessons/


# Contact Info

Add contact information for any project stakeholders. Include name, email and title. 

*Name, position, role, email*

Prof. Amy Booth, , Co-PI, amy.booth@vanderbilt.edu

Prof. Georgene Troseth, Co-PI, georgene.troseth@vanderbilt.edu

Dr. Margaret Shavik, , Co-PI, margaret.e.shavlik@vanderbilt.edu

Dr. Abbie Petulante, DSI Postdoctoral Fellow, staff data scientist lead, abigail.petulante@vanderbilt.edu

Dr. Jesse Spencer-Smith, DSI Chief Data Scientiat, team member, jesse.spencer-smith@vanderbilt.edu 
