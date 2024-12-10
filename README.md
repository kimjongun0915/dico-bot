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

## 코드 설명 및 구현 화면

---

### 명령어: `/도움말`

```python
@bot.slash_command(name="도움말",description="봇의 명령어를 알려준다")

#### 설명
- 이 명령어는 봇에 등록된 모든 명령어를 보여줍니다.
- 명령어의 이름과 그 설명이 포함된 임베드 메시지를 출력합니다.

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

---

## 실행 요건

1. **Python 3.8 이상**
   - Python 3.8 또는 그 이상의 버전이 필요합니다.
   - [Python 공식 웹사이트](https://www.python.org/)에서 다운로드하여 설치할 수 있습니다.

2. **필수 라이브러리 설치**
   - 다음 명령어를 실행하여 필요한 Python 라이브러리를 설치하세요:
     ```bash
     pip install nextcord aiohttp beautifulsoup4 requests
     ```
   - 각 라이브러리의 역할:
     - `nextcord`: 디스코드 API와 상호작용하기 위한 라이브러리.
     - `aiohttp`: 비동기 HTTP 요청을 처리하기 위한 라이브러리.
     - `beautifulsoup4`: HTML 파싱 및 크롤링에 사용.
     - `requests`: HTTP 요청을 처리하기 위한 라이브러리.
     - `os`: 파일 및 디렉토리 경로 관리를 하기 위한 라이브러리.
3. **이미지 폴더 설정**
   - 프로젝트 디렉토리에 `이미지/` 폴더를 생성합니다.
   - 해당 폴더에 **학과별 교육 연계도 이미지**와 **등록금 이미지**를 추가합니다.
     - 예시:
       ```plaintext
       프로젝트/
       ├── seoultech.py
       ├── 이미지/
       │   ├── 등록금1.png
       │   ├── 등록금2.png
       │   ├── 컴퓨터공학과.png
       │   └── 기계시스템디자인공학과.jpg
       ```
.

---

## License

This project is licensed under the MIT License
