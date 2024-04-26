# validation_component.py
from flask import Blueprint, jsonify
import pytesseract
from PIL import Image

validation_blueprint = Blueprint('validation', __name__)

@validation_blueprint.route('/validate', methods=['POST'])
def validate_invoice():
    if 'file' not in validate_invoice.files:
        return jsonify({'error': 'No file part'})
    
    file = validate_invoice.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        text = extract_text(file)
        extracted_data = parse_invoice_text(text)
        if extracted_data:
            return jsonify({'message': 'Invoice validated successfully', 'data': extracted_data})
        else:
            return jsonify({'error': 'Failed to extract information from the invoice'})
    else:
        return jsonify({'error': 'File type not allowed'})

def extract_text(image_file):
    text = pytesseract.image_to_string(Image.open(image_file))
    return text

def parse_invoice_text(text):
    # Implement logic to parse key information from the extracted text
    # For demonstration purposes, we're returning dummy data
    return {
        'school_name': 'Sample School',
        'invoice_amount': '1000 USD',
        'parent_name': 'John Doe',
        'school_account_number': '1234567890'
    }

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_file
