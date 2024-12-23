# IPA to SynthV Converter Backend

This project converts input language text to IPA (International Phonetic Alphabet) symbols using the ChatGPT API, and then converts those IPA symbols to pronunciation symbols supported by the SynthV program.

## Features

- Converts input language text to IPA symbols using the ChatGPT API
- Converts IPA symbols to SynthV pronunciation symbols

## Installation and Running

### Requirements

- Python 3.x
- Virtual environment (recommended)

### Installation

1. Clone the repository.

   ```bash
   git clone https://github.com/yourusername/ipa-synthV-converter.git
   cd ipa-synthV-converter/backend
   ```

2. Create and activate a virtual environment.

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Install the required packages.

   ```bash
   pip install -r requirements.txt
   ```

### Running

1. Run the server.

   ```bash
   python app.py
   ```

## Usage

Use the API endpoints to input language text and get the converted results. Refer to the API documentation for detailed usage instructions.

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.
