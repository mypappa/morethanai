# more thAn I  
an interactive installation where humans and artificial intelligences collaborate in unprecedented ways to co-create a story.  

## concept  
we wonder..  
- What happens if we revert The roles between the users and the servers?  
- How can I become the assistant of an AI? then who is the master of whom?  

this project aims to materialise and embody the ways in which artificial intelligences (AI) affect the creation of stories and how human inputs together with nonhuman processing (AI) give us a more-than-human outcome.   


## hands-on  
we will create an interface that records speech, transcribes it to text and feeds it into a language model (which in this case is GPT). Then the AI starts generating a story. The story always ends with a question to the participants for new human input. The answer is then integrated to the story from the AI, live-projected and ends with another question. this continues until we reach an x amount of words

## What we did (and did not do(ourselves)) in technical terms. 
knowing relatively nothing about coding and how to build digital interfaces was an interesting starting point for our project “more thAn I” that includes a complex structure of code and (strange) languages. With a lot of help we made our scaffold and can work on the understandable interface set up without that much of knowledgeable minds. Great thanks to Pietro, Mikel, Xavier, Victor, and Aurel (@FabLab, I know you know BUT woman power is definitely needed here!) 

### technicalities
we want to enable a human and an AI (our vision a visual and text generating AI) to collaborate on writing a fictional story. We use a “LangChain” framework for developing applications that deal with language models, we use a “GPT” language model by “OpenAI” with the “davinci” configuration, we use the open-source web framework “Flask” that is written in “python” to make our application a responsive webpage and we use “SpeechRecognition” which is a pre-built interface of “javascript” to transform audio (speech) to text. In our coding environment we use python, javascript, HTML and CSS. We work with open-source software and have our codes in a repo for everyone to access. 

## what we came across and we learned to understand: 
Interface: term used in programming; describes a set of rules that define how different software components (will) interact with each other. It is the “cover” / the interface allows the user to interact with software, without exposing the internal workings of the underlying code.

**API:** Application Programming Interface, so this speaks specifically about how applicatioins communicate with each other. API are offered by platform like facebook, services like paypal, or providers like googlemaps to allow cross-linkages and integration in bigger (software) systems. 

**Visual generating AI:** uses algorithms and models trained on large datasets to create new visual content based on the patterns and information it has learned.

**text generating AI:** uses natural language processing techniques, deep learning models, and language models (@LLMs) trained on large datasets to generate coherent (and relevant) written content-

**LLMs:** large language models that are made to understand and generate human-like text. They are trained on large datasets to learn human languages. 

**python:** programming language often used in web development and data analysis. It comes with a big set of pre-built modules and functions for a lot of tasks and has an easy system to import external libraries and frameworks for specific domains. 

**HTML:** Hypertext Markup Language, a standard markup language used to create web pages [markup: practice of adding special annotations and tags to text to provide structure and formatting instructions]. It often creates a set of instructions that tells web browsers how to display content.

**markdown:** another language to apply markup to text. Simpler and more intuitive way to format text. 

**CSS:** Cascading Style Sheet, a style sheet language the describes the presentation and visual formatting of HTML and other text-structured documents. 

**javascript:** a programming language that runs directly in a web browser (one of the few). It allows to add interactive and dynamic elements and behaviour to websites, e.g. it enables websites to respond to user actions, manipulate content, and interact with external resources. Similarly to python, it comes with a big set of pre-built modules and functions for a lot of tasks and has an easy system to import external libraries and frameworks for specific domains. 
 
Running code in a **local (on my computer) environment** vs. in an **online environment:** local allows full control over development setup and I have offline access but need to install all libraries and necessary languages on my disk. Online is convenient when working together and I can store the necessary additional datasets online.

**GPT:** Generative Pre-trained Transformer. A type of language model developed by OpenAI that has exists in different versions (GPT-2, GPT-3, GPT-4 ect.). 

**Davinci:** a name that OpenAI has given to SPECIFIC configurations of their language models (a very capable and large variation) e.g. GPT-3 and GPT-4 are having these configurations.

#### We installed: 

**OpenAI** (python library): needed to access the OpenAI APIs (interfaces). When having an account to use ChatGPT for example, I can ask for my API key which I need to integrate OpenAI services into my system. In OpenAI I have “tokens” (because it is not open-source anymore) that I need to use the API. If my tokes are used up I can only buy new ones. 

**Flask** (library): open-source web framework that is written in python. It is like a foundation / structure that helps to make a python code a web application. You can create routes that define how applications are responding to different URLs. It is a way to make a website out of your code. 

**LangChain** (library): is a python library that provides open-source frameworks to develop applications that deal with (large) language models. Its idea is to “chain” together different components to create more advanced use cases around LLMs like chatbots and generative question-answering. 

**SpeechRecognition** (library): is a javascript library that serves as a Web Speech API (interface). It enable to record, detect, and transcribe audio (speech) into written text. 

## References:

• [replit](https://replit.com/~ ); allows programming code in collaboration in an online environment

• [LangChain](https://python.langchain.com/en/latest/index.html) by python; a open-source framework to develop applications that deal with language models

• [SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) by javascript; a open-source Web Speech API

• [Flask](https://flask.palletsprojects.com/en/2.3.x/) by python; a open-source web framework we use to stream and show the (inter)actions

• the best [to look everything up related to the digital interface languages](https://www.w3schools.com/html/default.asp)

• [OpenAI](https://platform.openai.com/docs/models/overview) overview of their models






