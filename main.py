import streamlit as st
import PyPDF2
import os
import google.generativeai as genai


genai.configure(api_key="YOUR_API_KEY")
#replace YOUR_API_KEY with your google gemini api key
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def extract_text_from_pdfs(pdf_files):
    all_text = ""
    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            all_text += pdf_reader.pages[page_num].extract_text()
    return all_text.strip()

@st.cache_data(show_spinner=False)
def generate_response(prompt):
    try:
       
        response = model.generate_content([prompt])
        if response.candidates:
            generated_text = response.candidates[0].content.parts[0].text
            return generated_text
        else:
            return "No content found in the response."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("Chat with your PDFs using Google Gemini LLM")
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        text = extract_text_from_pdfs(uploaded_files)
        st.write("PDF text extracted successfully!")
        st.text_area("Extracted Text", text, height=200)
        query = st.text_input("Ask a question about the PDFs:")

        if query:
            prompt = f"The following is extracted from the PDF documents:\n{text}\n\nUser question: {query}"
            response = generate_response(prompt)
            st.write(response)

if __name__ == "__main__":
    main()
