
 Chat with Your PDF

 Overview

"Chat with Your PDF" is a proof-of-concept web application that allows users to interact with the content of PDF documents using a language model (LLM) integrated with a user-friendly Streamlit interface. The application supports multiple PDF documents, extracts and processes their text, and generates contextually relevant responses to user queries. Additionally, the application highlights relevant portions of the PDF text that relate to the LLM's response.


 Live :https://jithendhar1435-chat-with-your-pdf-main-branch-8x9neu.streamlit.app/
 Features

- Multiple PDF Support: Upload multiple PDF files in a single session. The application extracts and combines text from all PDFs for comprehensive querying.
- Text Extraction and Preprocessing: Extracts text from PDF files using PyPDF2 and preprocesses it for interaction.
- LLM Integration: Integrates with the Google Gemini language model to generate responses based on user queries.
- Highlighted Text: Highlights relevant portions of the PDF text that match the generated response.
- User-Friendly Interface: Built with Streamlit, providing an intuitive and interactive experience for users.
-Implemented basic caching to reduce API calls for repeated or similar queries.

 Installation

 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

 Step-by-Step Installation

1. Clone the Repository
 
   git clone https://github.com/jithendhar1435/Chat-with-your-pdf.git
   cd chat-with-pdf
 

2. Create a Virtual Environment
   
   python -m venv venv
   source venv/bin/activate    On Windows use: venv\Scripts\activate
  

3. Install the Required Packages
  	pip install -r requirements.txt
  

4. Set Up Google Gemini API Key
   - Obtain your Google Gemini API key from the [Google Cloud Console](https://console.cloud.google.com/).

   - Add the API key to your environment:
     
     export GOOGLE_API_KEY='your-google-api-key'    On Windows use: set GOOGLE_API_KEY=your-google-api-key
    

5. Run the Application
  
   streamlit run app.py
   

 Usage

 Running the Application

1. Launch the Application
   - Run the application using the command `streamlit run app.py`.
   - The application will open in your default web browser.

2. Upload PDFs
   - Click on "Choose PDF files" to upload one or more PDF documents.
   - The text from the PDFs will be extracted and displayed.

3. Ask Questions
   - Enter your query in the text input field.
   - The application will generate a response based on the extracted text and display it.

4. View Highlighted Text
   - Relevant portions of the PDF text that match the LLM's response will be highlighted.







 Example Queries

- "What are the key components of a neural network?"
- "Explain the methodology used in this research paper."
- "Summarize the findings of the document."

 Approach and Design Decisions

 Text Extraction and Preprocessing

The application uses PyPDF2 to extract text from PDF documents. The text is cleaned and combined into a single string if multiple PDFs are uploaded. This allows the language model to access the entire content for generating responses.

 LLM Integration

The application integrates with the Google Gemini language model through the `google.generativeai` library. The LLM is tasked with generating responses based on user queries and the extracted PDF content.

 Handling Multiple PDFs

Support for multiple PDFs was implemented to provide a more comprehensive analysis. The text from all uploaded PDFs is combined, allowing the LLM to generate responses that consider the content of all documents.

 Highlighting Relevant Text

The application highlights relevant portions of the PDF text by matching phrases from the LLM-generated response with the extracted content. This helps users easily see where the information in the response originates.

 Challenges and Solutions

- Multiple PDF Support: Handling multiple PDFs required combining text from various documents into a single source, which was achieved using an efficient text extraction loop.
- Text Highlighting: Ensuring that the highlighted text accurately reflects the LLM's response required careful string matching and handling of edge cases where the text might be slightly different.



 Potential Improvements

- Handling Hallucinations: Future versions could implement more robust checks to verify that the LLM's responses are grounded in the provided PDF content, reducing the risk of hallucinations.
- PDF Structure Recognition: Enhancing the application to recognize and display the structure of the PDF content, such as headers and paragraphs, would improve navigation and readability.
- Expanded Model Support: Adding support for other language models or custom-trained models could make the application more versatile.


 Contact

For any questions or feedback, please contact 
[Jithendhar Reddy]
(jithendharreddy304@gmail.com).

---

This README file provides a comprehensive guide to the project, covering everything from installation and usage to the approach and potential improvements.

