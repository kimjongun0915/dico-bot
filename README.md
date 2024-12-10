# Discord Bot for University Information

This is a Discord bot designed to provide useful information about a university, including tuition details, campus maps, department details, clubs, and notices. It also includes a feature to display department-specific educational roadmaps.

---

## Features

### Help Command (`/도움말`)
Displays all available commands and their descriptions.

### Tuition Details (`/등록금`)
Provides tuition details for different departments with paginated images.

### Campus Map (`/캠퍼스지도`)
Shows a map of the university campus.

### Grade Ratio (`/학점비율`)
Displays the grade distribution ratios for the 2025 academic year.

### Clubs Information (`/분과정보`)
Provides information about various clubs categorized by their type.

### University Notices (`/공지사항`)
Fetches and displays the latest notices from the university's official website.

### College and Department Information (`/단과대학`)
Allows users to explore colleges and their respective departments. Users can also view department-specific educational roadmaps as images.

---

## Setup Instructions

### Prerequisites

1. **Python 3.8 or later**
   - Ensure that Python 3.8 or a later version is installed on your system.
   - Download Python from the [official Python website](https://www.python.org/).

2. **Discord Bot Token**
   - Create a bot in the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy the bot token and replace `"YOUR_BOT_TOKEN"` in the `bot.run()` line of the code.

3. **Required Python Libraries**
   - Install the necessary Python libraries using the following command:
     ```bash
     pip install nextcord aiohttp beautifulsoup4 requests
     ```
   - **Library Descriptions**:
     - `nextcord`: Library for interacting with Discord's API.
     - `aiohttp`: Handles asynchronous HTTP requests.
     - `beautifulsoup4`: Parses HTML for web scraping.
     - `requests`: Makes HTTP requests.

4. **Educational Roadmap Images**
   - Prepare images for department-specific educational roadmaps.
   - Save the images in the `이미지/` directory and map them in the `college_data` dictionary.
     - Example:
       ```plaintext
       이미지/
       ├── 기계시스템디자인공학과.jpg
       ├── 컴퓨터공학과.png
       └── ...
       ```

---

### Running the Bot

1. **Create a Bot in Discord Developer Portal**
   - Visit the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on "New Application" and provide a name for your bot.
   - Navigate to the "Bot" tab and click "Add Bot" to create a bot user.

2. **Get the Bot Token**
   - Copy the bot token from the "Bot" tab.
   - Replace `"YOUR_BOT_TOKEN"` in the `bot.run()` line of the code with the copied token.

3. **Set Bot Permissions**
   - Go to the "OAuth2" tab in the Discord Developer Portal.
   - Select "URL Generator" and check the following permissions under the "Scopes" and "Bot Permissions" sections:
     - **Scopes**: `bot`
     - **Bot Permissions**: `Send Messages`, `Embed Links`, `Read Message History`, and any other permissions your bot needs.
   - Copy the generated OAuth2 URL.

4. **Invite the Bot to Your Server**
   - Open the copied OAuth2 URL in your web browser.
   - Select your Discord server and invite the bot.

5. **Run the Bot**
   - Open a terminal and navigate to the folder containing `seoultech.py`.
   - Run the following command to start the bot:
     ```bash
     python seoultech.py
     ```
   - The bot should now be online and ready to use.

---

Now your bot should be set up and running on your Discord server. If you encounter any issues, feel free to ask for help!

## License

This project is licensed under the MIT License
