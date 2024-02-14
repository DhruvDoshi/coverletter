import requests
import json

def upload_resume_to_gemini(file_path, api_key):
    # Endpoint for uploading resume to Gemini
    endpoint = "https://api.gemini.ai/v1/parse/resume"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    files = {
        "resume": open(file_path, "rb")
    }
    response = requests.post(endpoint, headers=headers, files=files)
    return response.json()

def save_to_json(data, json_file):
    # Save the extracted information to a JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    # Input PDF file
    pdf_file = "Resume.pdf"
    # API key for Gemini
    api_key = "AIzaSyDrUNBZxCBze5T_39ZN9WAgKzus8AsXWpY"
    
    # Step 1: Upload Resume to Gemini
    gemini_response = upload_resume_to_gemini(pdf_file, api_key)
    if "data" in gemini_response:
        extracted_info = gemini_response["data"]
        
        # Step 2: Extract Structured Data
        # Extracted information will be in 'extracted_info'
        
        # Step 3: Save Extracted Information to JSON file
        json_file = "resume_info.json"
        save_to_json(extracted_info, json_file)
        print("Information extracted from the resume has been saved to", json_file)
    else:
        print("Error: Failed to extract information from the resume.")

if __name__ == "__main__":
    main()
