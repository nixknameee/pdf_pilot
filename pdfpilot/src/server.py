"""
server.py

This file contains a Flask web application that serves as the backend for a chatbot that processes PDF handouts and answers user questions based on their content. 

The server provides the following API endpoints:

1. '/chatbot' (POST) - Receives a user's question and a PDF file, processes the PDF using the HandoutAssistant class, 
    and returns the answer along with a highlighted PDF containing the relevant segment.
    
2. '/download_highlighted_pdf' (GET) - Allows the user to download the highlighted PDF generated by the '/chatbot' endpoint.

The Flask app uses CORS to handle cross-origin resource sharing and communicates with the HandoutAssistant to process the PDFs and answer the questions.
"""


from flask import Flask, request, jsonify, send_file, make_response
from flask_cors import CORS
from HandoutAssistant import HandoutAssistant, PDFHandler
import os
import uuid

app = Flask(__name__)
CORS(app)

os.makedirs('pdf_backup', exist_ok=True)
os.makedirs('static/pdf', exist_ok=True)

assistant = HandoutAssistant()

@app.route('/chatbot', methods=['POST'])
def chatbot():
    print("Request received.")
    question = request.form.get('question')
    file = request.files.get('file')

    if not question or not file:
        return jsonify({"error": "Missing question or file"}), 400

    pdf_path = 'temp_pdf_file.pdf'
    file.save(pdf_path)

    answer, segment_id, segment_text = assistant.process_pdf_and_get_answer(pdf_path, question)
    print("process_pdf_and_get_answer")

    if answer and segment_id:
        highlighted_pdf_path = f'static/pdf/highlighted_{uuid.uuid4().hex}.pdf'
        PDFHandler.highlight_text(pdf_path, highlighted_pdf_path, segment_text)

        print("OpenAI API Response:", answer)
        print("Answer: ", answer)
        os.remove(pdf_path)

        return jsonify({
            'answer': answer,
            'highlighted_pdf_path': highlighted_pdf_path
        })
    else:
        os.remove(pdf_path)
        print("No answer found.")
        return jsonify({"answer": "No answer found"})

@app.route('/download_highlighted_pdf', methods=['GET'])
def download_highlighted_pdf():
    pdf_path = request.args.get('pdf_path')
    if not pdf_path:
        return jsonify({"error": "Missing pdf_path parameter"}), 400

    try:
        return send_file(pdf_path, as_attachment=True, attachment_filename='highlighted.pdf')
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(port=5001)
