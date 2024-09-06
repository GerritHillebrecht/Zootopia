# 🐾 Animal Data Explorer

Welcome to **Animal Data Explorer**! This project allows you to look up fascinating information about various animals
using the [API-Ninjas Animals API](https://api.api-ninjas.com/v1/animals) and generates a beautiful HTML template to
display the data.

## 🌟 Features

- **Dynamic Animal Lookup**: Enter the name of any animal to fetch detailed information.
- **Beautiful HTML Templates**: Automatically generates visually appealing HTML pages.
- **Easy to Use**: Simple and intuitive interface for seamless user experience.
- **Responsive Design**: HTML templates are mobile-friendly and look great on any device.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- An API key from API-Ninjas

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GerritHillebrecht/Zootopia.git
    cd zootopia
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your API key:
    ```python
    # In .env file
    API_KEY = 'your_api_key_here'
    ```

### Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Enter the name of the animal you want to look up.

3. View the generated HTML file in your browser.

## 📂 Project Structure

```plaintext
animal-data-explorer/
├── ...
├── animal_template.html
├── main.py
├── README.md
└── requirements.txt

animal_template.html: Contains the HTML template used for displaying animal data.
main.py: The main script to fetch data and generate HTML.
README.md: This file.
requirements.txt: List of required Python packages.

🛠️ Built With
Python
Requests
!Animal Data Explorer Screenshot

🤝 Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
For any questions or suggestions, feel free to reach out:

GitHub: GerritHillebrecht
Happy Exploring! 🐾