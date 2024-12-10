Discord Bot for University Information
This is a Discord bot designed to provide useful information about a university, including tuition details, campus maps, department details, clubs, and notices. It also includes a feature to display department-specific educational roadmaps.

Features
Help Command (/도움말)
Displays all available commands and their descriptions.

Tuition Details (/등록금)
Provides tuition details for different departments with paginated images.

Campus Map (/캠퍼스지도)
Shows a map of the university campus.

Grade Ratio (/학점비율)
Displays the grade distribution ratios for the 2025 academic year.

Clubs Information (/분과정보)
Provides information about various clubs categorized by their type.

University Notices (/공지사항)
Fetches and displays the latest notices from the university's official website.

College and Department Information (/단과대학)
Allows users to explore colleges and their respective departments. Users can also view department-specific educational roadmaps as images.

Setup Instructions
Prerequisites
Python 3.8 or later installed
Discord Bot token
Required Python libraries installed:
bash
코드 복사
pip install nextcord aiohttp beautifulsoup4 requests
Project Structure
bash
코드 복사
project/
├── bot.py              # Main bot script
├── 이미지/             # Directory for educational roadmap images
│   ├── 기계시스템디자인공학과.jpg
│   ├── 컴퓨터공학과.png
│   └── ...             # Additional images
└── README.md           # Project description file
Running the Bot
Clone this repository or copy the code files into a project folder.
Replace YOUR_BOT_TOKEN in bot.py with your Discord bot token.
Ensure the 이미지/ folder contains the educational roadmap images for each department.
Run the bot:
bash
코드 복사
python bot.py
Invite the bot to your Discord server using its OAuth2 link.
Commands
Command	Description
/도움말	Lists all available commands.
/등록금	Shows tuition details with pagination for images.
/캠퍼스지도	Displays the campus map.
/학점비율	Shows grade distribution ratios for the 2025 academic year.
/분과정보	Provides categorized club information.
/공지사항	Fetches and displays the latest university notices.
/단과대학	Displays colleges, departments, and educational roadmaps.
Educational Roadmap Images
Each department has an associated image file stored in the 이미지/ folder. The bot dynamically loads these images when the user selects a department.

Example
Path: 이미지/기계시스템디자인공학과.jpg
Displayed when: The user selects the "기계시스템디자인공학과" department under the "공과대학".
Contribution
Feel free to contribute to this project by adding new features or improving the existing ones. Create a pull request or open an issue to discuss changes.

License
This project is open-source and available under the MIT License.

Contact
For questions or suggestions, please contact the project maintainer at your_email@example.com.
