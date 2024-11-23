# Volleyball Coordination Tool :volleyball: :palm_tree: :sunny:

Automate coordination for your volleyball group by managing polls, schedules, and communication seamlessly through WhatsApp. This project leverages **Waha Dev Pro**, **Python**, **Selenium**, and **Beautiful Soup** to automate group activities efficiently.

## :books: Table of Contents 
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [License](#license)
- [Contributing](#contributing)

---

## :mechanical_arm: Features 
- **Automated Poll Creation:** Parse messages to generate and post polls directly in the group chat.
- **Message Parsing:** Use Beautiful Soup for extracting structured data from group messages.
- **Seamless Integration:** Operates via WhatsApp Web using Selenium for automation.
- **Scalable:** Built to handle a 20-member volleyball group, with potential for larger scalability.

---

## :computer: Technologies Used 
- **Waha Dev Pro** (via Docker): Environment for WhatsApp Web automation.
- **Python**: Core programming language for the automation logic.
- **Selenium**: Browser automation for WhatsApp Web interactions.
- **Beautiful Soup**: Data parsing from WhatsApp messages.

---

## :wrench: Installation 
### Prerequisites
- Docker installed on your machine.
- Follow NoWeb installation guide from [Waha Dev Pro Install & Update](https://waha.devlike.pro/docs/how-to/install/) to get Docker image running on your local machine and linking your phone with WhatsApp Web
- Python 3.9 or above.
- Selenium, Beautiful Soup, and Requests installed on your local/virutal machine.
- Google Chrome and ChromeDriver (ensure version compatibility with Selenium).

### :ladder: Steps 
1. Clone the repository:
   ```bash
   git clone https://github.com/https://github.com/annemarieb215/VballPolling.git
   cd VballPolling
   python3 send_poll.py
