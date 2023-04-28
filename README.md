# Welcome to PDFPilot!

PDFPilot is a powerful AI-driven React web application that helps users find relevant answers to their questions from PDF documents. By utilizing advanced natural language processing techniques, the application can provide concise answers and highlight the exact location of the information within the PDF. This makes it a valuable tool for businesses and organizations that work with many handouts and often spend a lot of time going through them.

PDFPilot was developed as a project during a hackathon and is an evolved prototype that we will continue to work on after the hackathon. We're very proud of what we've achieved so far and believe that PDFPilot represents a promising solution to the problem of time-consuming handout reviews.

In this README file, you'll find detailed information on how to install and use PDFPilot. We hope you find the application useful and welcome any feedback and suggestions for improvement. Thank you for trying out PDFPilot!



![](https://github.com/nixknameee/pdf_pilot/blob/main/pdfpilot/public/ezgif.com-video-to-gif.gif)

                                                              First Steps

Before installing the project, it is important to note that you will need to provide your keys for AI21lab and OpenAI.

These keys can be found in the HandoutAssistant file under the OpenAI and AI21Segmentation classes, respectively the AI21_Key, under the "headers" section:

> Key = <your_OpenAi_key>

> Authorization: Bearer 'Your_AI21_Key'

Please make sure to include these keys in the appropriate files after the installation.

## Installation

To install PDFPilot on your computer, you first need to make sure you have Node.js and npm installed. You can do this by typing the following commands in your terminal:

> node -v

> npm -v

If you see the versions of Node.js and npm, you're ready to install PDFPilot.

Clone this repository to your computer:


> git clone https://github.com/nixknameee/pdfpilot.git

Navigate to the project folder:


> cd pdfpilot

Install the required dependencies:

> npm install

Start the application:

> npm start

    The application should now be available in your web browser at http://localhost:3000.

That's it! You should now have PDFPilot installed on your computer and be ready to search PDF documents. Thank you for using PDFPilot!

### How to start the Server
After starting the Webpage you have to start the server.py with the command.

> pyhton3 server.py

![](https://github.com/nixknameee/pdf_pilot/blob/main/pdfpilot/public/IMG_0232.png)

## server.py


This file contains a Flask web application that serves as the backend for a chatbot that processes PDF handouts and answers user questions based on their content.

The server provides two API endpoints:

    '/chatbot' (POST) - Receives a user's question and a PDF file, processes the PDF using the HandoutAssistant class,
    and returns the answer along with a highlighted PDF containing the relevant segment.

    '/download_highlighted_pdf' (GET) - Allows the user to download the highlighted PDF generated by the '/chatbot' endpoint.

To use this application, send a POST request to the '/chatbot' endpoint with a user's question and a PDF file. The server will process the PDF and return the answer to the user's question along with a highlighted PDF containing the relevant segment. The PDF file should be sent as a form-data file attachment with the key 'file', and the user's question should be sent as a form-data field with the key 'question'.

If the request is successful, the server will return a JSON object with the answer and the path to the highlighted PDF file. If the request fails due to missing parameters, the server will return a JSON object with an error message and a 400 status code.

To download the highlighted PDF file, send a GET request to the '/download_highlighted_pdf' endpoint with the 'pdf_path' parameter set to the path of the highlighted PDF file returned by the '/chatbot' endpoint. The server will return the highlighted PDF file as an attachment with the filename 'highlighted.pdf'. If the file is not found, the server will return a JSON object with an error message and a 404 status code.

The Flask app uses CORS to handle cross-origin resource sharing, allowing requests to be made from different domains, and communicates with the HandoutAssistant to process the PDFs and answer the questions.




## HandoutAssistant.py


This file contains the HandoutAssistant class, designed to process PDF handouts and answer questions based on their content.

The HandoutAssistant class is responsible for:


1. Converting PDF to text.
2. Segmenting the text using AI21 Studio's API.
3. Loading the segmented questions.
4. Identifying relevant segments based on user questions using Hugging Face's Transformers.
5. Generating a prompt for OpenAI's GPT-3.
6. Extracting answers and segment IDs from GPT-3's response.

The file also includes a PDFHandler class responsible for highlighting relevant segments in the input PDF.

The NLP class defines a function using Hugging Face's Transformers for the question-answering model, and the OpenAIAPI class defines functions for using OpenAI's GPT-3 to generate answers.

The AI21Segmentation class uses AI21 Studio's API for text segmentation. The "segment_text" function requires an API key to be provided by the user.

To use the HandoutAssistant class:

        Create an instance of the HandoutAssistant class.
        Call the "process_pdf_and_get_answer" method and provide the path to the PDF file and the question as parameters.
        The method returns the answer from GPT-3 and the ID of the segment that generated the answer.

Note: Before using the class, you need to configure the API keys for AI21 and OpenAI. You also need to install the "fitz", "requests", "transformers", and "openai" libraries.
