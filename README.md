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
```

#### 설명
- 이 명령어는 봇에 등록된 모든 명령어를 보여줍니다.
- 명령어의 이름과 그 설명이 포함된 임베드 메시지를 출력합니다.

### 명령어: `/등록금`

```python
@bot.slash_command(name="등록금", description="학과별 등록금을 알려줍니다.")
```

#### 설명
- 학과별 등록금 정보를 페이지별로 보여줍니다.
- "이전", "다음" 버튼으로 페이지를 이동할 수 있습니다.
- 버튼 정의 및 콜백 연결
   - `next_page_callback`: 다음 페이지를 표시
   - `prev_page_callback`: 이전 페이지를 표시
- 페이지 순환 로직: 페이지 번호를 배열 길이로 모듈러 연산하여 순환
- 버튼 뷰: `View`객체를 사용해 버튼을 생성하고 메시지에 추가

### 명령어: `/캠퍼스지도`

```python
@bot.slash_command(name="캠퍼스지도", description="서울과학기술대학교의 캠퍼스 지도를 보여줍니다.")
```

#### 설명
- 서울과학기술대학교 캠퍼스 지도를 이미지로 보여줍니다.
- `nextcord.File`: 이미지를 Discord 메시지에 첨부할 때 사용됩니다.

### 명령어: `/학점비율`

```python
@bot.slash_command(name="학점비율", description="2025학년 학점 비율을 보여줍니다.")
```

#### 설명
- 2025학년 학점 비율에 대한 정보를 보여줍니다.
- 상대평가 및 절대평가 기준과 주의사항을 임베드 메시지로 출력합니다.
- 임베드 메시지 생성: 학점 비율 정보는 `Embed`에 추가.
- 상대평가/영어수 필드: 가독성을 위해 각각의 기준을 필드로 분리.

### 명령어: `/분과정보`

```python
@bot.slash_command(name="분과정보", description="분과별 동아리 정보를 보여줍니다.")
```

#### 설명
- 서울과학기술대학교의 분과별 동아리 정보를 제공합니다.
- 각 분과에 포함된 동아리의 이름, 위치, 그리고 목적을 임베드 메시지로 출력합니다.
- "이전 분과", "다음 분과" 버튼을 통해 페이지를 이동하며 정보를 확인할 수 있습니다.
- 페이지 구조화
  - 동아리 정보를 분과별로 나눠 페이지로 구성.
  - 각 분과에는 이름, 위치, 목적 정보가 포함.
- 페이지 렌더링
   - `render_page(page_index)`: 현재 페이지의 동아리 정보를 임베드에 추가.
-버튼 네비게이션
   - `next_page_callback`: 다음 분과로 이동.
   - `prev_page_callback`: 이전 분과로 이동.
   - 버튼을 사용해 순활적으로 페이지 이동 가능.

### 명령어: `/공지사항`

```python
@bot.slash_command(name="공지사항", description="학교의 최신 공지사항을 보여줍니다.")
```

#### 설명
- 공지사항 크롤링
  - `fetch_notices()` 함수에서 공지사항 데이터(제목, 링크, 부서, 작성일)를 가져옵니다.
  - 최대 15개의 공지사항만 표시합니다.
-페이지 렌더링
  - `render_page(page_index)`: 현재 페이지에 해당하는 공지사항 데이터를 임베드에 추가합니다.
- 버튼 네비게이션
  - `next_page_callback`: 다음 페이지로 이동
  - `prev_page_callback`: 이전 페이지로 이동
  - 페이지는 순환 구조로 마지막 페이지에서 첫 번째 페이지로 이동 가능.
-임베드 메시지
  - 공지사항 제목과 링크, 부서, 작성일 정보를 포함.

### 명령어: `/단과대학`

```python
@bot.slash_command(name="단과대학", description="단과대학과 학과 정보를 보여줍니다.")
```

#### 설명

- 단과대학 선택
  - 사용자가 선택 메뉴에서 단과대학을 선택하면 해당 단과대학의 학과 목록이 표시됩니다.
- 학과 선택
  - 학과 선택 시, 해당 학과의 교육 연계도 이미지가 전송됩니다.
  - `os.path.exists()`로 이미지 파일의 존재 여부를 확인합니다.
- 선택 메뉴
  - `Select`: 단과대학 및 학과 선택을 위한 드롭다운 메뉴를 생성.
  - `callback`: 사용자가 선택한 항목에 따라 동작을 정의.
- 이미지 전송
  - 학과별로 사전에 정의된 이미지 경로(`collage_data`)를 기반으로 이미지를 전송합니다.

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
