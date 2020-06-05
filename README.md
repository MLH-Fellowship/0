# Welcome to TL;DR:!
TL;DR: a web app that summarizes texts of any size to help users save time, powered by Flask, jinja2, NLP libraries, text-to-speech, and more.

![screenshot of TL;DR website](tldr_screenshot.png?raw=true )


## Why TL;DR:?
We wanted to find ways to let people summarize anything - be it an article, a school essay, or a Reddit comment - to help them save time and become more productive. We decided to create an app that made use of the latest findings in NLP to summarize web pages and read it aloud. We especially focused on helping kids struggling with reading long texts because of dyslexia, and blind people that deal with unnecessarily long web pages every day by adding text-to-speech functionality.

## What it does
This web app uses Natural Language Processing algorithms to transform long texts into short paragraphs while still preserving the most relevant information. Users can summarize any content they like by pasting it into a text field or by entering a web page URL. If they enter an URL, the web app uses the BeautifulSoup library to scrape most websites’ content,

We implemented multiple NLP algorithms, such as TF-IDF and TextRank, to get the best summary out of any text. By default, the web app uses a TextRank algorithm (inspired by PageRank) to select the most important sentences based on their similarity to the rest of the text.

When the summary is displayed on the user interface, users can choose to copy the text into the clipboard or use the “Listen” button powered by the Microsoft Text-to-Speech API to read the summary out loud. Finally, we added some algorithms to inform users about how much the text was reduced, and how much time they saved by using the tool.

## What we learned
On the text summarization side, we learnt that sometimes it’s hard to get research models to do what their papers say they can do (we were unsuccessful at getting OpenAI’s GPT-2 to summarize). On the other hand, we learned a lot about extractive models and the challenges of the text summarization task. On the frontend side, we learnt that Flask can be an incredible tool to build powerful web applications. We were able to easily run the NLP Python scripts within Flask and serve the content through API routes and Jinja2. We also experimented with using Issues and Milestones to track project progress in Github.

## Open Source Projects
We used several Open Source libraries in our project to create the best user experience possible for our users. Flask is used to serve the API endpoints and the web page users can interact with. Jinja2, which is part of Flask, was used to render the content into HTML pages. spaCy, a Natural Language Processing library, made it easy for us to get the summary out of any text. If the user enters a website URL, we use BeautifulSoup to scrape the website contents by creating a dictionary containing the page headings as for the keys, and the paragraphs for the values.

## Individual Contributors

* Katherine ([@kbanc](https://github.com/kbanc)) worked on building and testing the NLP algorithms and providing default examples in the web app
* Mwiza ([@mwizasimbeye11](https://github.com/mwizasimbeye11)) implemented text-to-speech using the Microsoft Text-to-Speech API
* Cesare ([@csr](https://github.com/csr)) worked on creating the web application with Flask, serving the API endpoints, providing users with an intuitive user interface, and scraping any website contents with BeautifulSoup.

## On choosing the right NLP algorithm

To summarize the text, we explored three extractive text summarization models that don’t require training. Within those models, we experimented with retaining the original text order instead of displaying the most highly ranked sentence first. 

The models: 
1. Sentence scoring based on word frequency
* Assign weights to each word in the text depending on how frequently they appear. Using weights assigned to the words, score the sentence. Pick top sentences.
Referenced from this [tutorial](https://medium.com/better-programming/extractive-text-summarization-using-spacy-in-python-88ab96d1fd97).
2. TextRank
    1. Using semantic word vectors (GloVe)
    2. Using word occurrence vectors 
* TextRank is based on the PageRank notion that important sentences will be similar to other sentences in the text. To find similar sentences, we create a vector representation of each sentence, and create a matrix of the cosine similarity between every sentence in the text. The sentences that have the highest cumulative cosine similarity scores are the most important sentences.
Referenced from these tutorials: [GloVe vector tutorial](https://appliedmachinelearning.blog/2019/12/31/extractive-text-summarization-using-glove-vectors/), [occurrence tutorial](https://towardsdatascience.com/text-summarization-in-python-3f5a25418606)

Model variations were empirically compared. The final product uses TextRank with word occurrence vectors, and retains the original sentence order from the text. 

## Run the project

## What's next
We’re always looking for ways to improve. We’re very happy to have hacked something users can use from day 1, and we’ll be continuously looking for user feedback. We’re specifically looking into adding markup support and building a Chrome extension to summarize the entire Internet. Feel free to open an issue here to provide feedback or contribute.

## License
This project is under the [MIT License](/LICENSE)
