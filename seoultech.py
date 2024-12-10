import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View, Select
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import aiohttp
import os

# 봇 설정
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)

# 봇 준비 이벤트
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")

@bot.slash_command(name="도움말",description="봇의 명령어를 알려준다")
async def help_command(interaction: nextcord.Interaction):
    app_commands=bot.get_application_commands()
    embed=nextcord.Embed(
        title="봇 명령어 목록",
        description="아래는 사용 가능한 명령어 목록입니다:",
        color=nextcord.Color.blue()
    )
    for command in app_commands:
        embed.add_field(
            name=f'/{command.name}',
            value=command.description or '설명이 없습니다.',
            inline=False
        )
    await interaction.response.send_message(embed=embed)

@bot.slash_command(name="등록금", description="학과별 등록금을 알려줍니다.")
async def tuition(interaction: nextcord.Interaction):
    # 이미지 파일 경로
    images = ["이미지/등록금1.png", "이미지/등록금2.png"]
    
    # 현재 페이지를 저장할 변수
    current_page = 0

    # 버튼 정의
    async def next_page_callback(interaction: nextcord.Interaction):
        nonlocal current_page
        current_page = (current_page + 1) % len(images)  # 다음 페이지 (순환)
        await interaction.response.edit_message(
            content=f"등록금 정보입니다 (페이지 {current_page + 1}/{len(images)}):",
            files=[nextcord.File(images[current_page])]
        )

    async def prev_page_callback(interaction: nextcord.Interaction):
        nonlocal current_page
        current_page = (current_page - 1) % len(images)  # 이전 페이지 (순환)
        await interaction.response.edit_message(
            content=f"등록금 정보입니다 (페이지 {current_page + 1}/{len(images)}):",
            files=[nextcord.File(images[current_page])]
        )

    # 버튼 생성
    next_button = Button(label="다음", style=nextcord.ButtonStyle.primary)
    prev_button = Button(label="이전", style=nextcord.ButtonStyle.secondary)

    # 버튼 콜백 연결
    next_button.callback = next_page_callback
    prev_button.callback = prev_page_callback

    # 버튼 뷰 생성
    view = View()
    view.add_item(prev_button)
    view.add_item(next_button)

    # 첫 번째 페이지 표시
    await interaction.response.send_message(
        content=f"등록금 정보입니다 (페이지 1/{len(images)}):",
        files=[nextcord.File(images[current_page])],
        view=view
    )

@bot.slash_command(name="캠퍼스지도", description="서울과학기술대학교의 캠퍼스 지도를 보여줍니다.")
async def campus_map(interaction: nextcord.Interaction):
    # 이미지 파일 경로
    file = nextcord.File("이미지/캠퍼스지도.png", filename="캠퍼스지도.png")

    # 메시지 전송
    await interaction.response.send_message(
        content="서울과학기술대학교 캠퍼스 지도입니다:",
        file=file
    )

@bot.slash_command(name="학점비율", description="2025학년 학점 비율을 보여줍니다.")
async def grade_ratio(interaction: nextcord.Interaction):
    # 학점 비율 정보 생성
    embed = nextcord.Embed(
        title="2025학년 학점 비율",
        description="아래는 상대평가 및 절대평가 기준입니다.",
        color=nextcord.Color.green()
    )

    # 상대평가 정보 추가
    embed.add_field(
        name="📘 상대평가",
        value="""
        **A+**: 15%
        **A0**: 30%
        **B+**: 50%
        **B0**: 70%
        """,
        inline=False
    )

    # 절대평가 정보 추가
    embed.add_field(
        name="📗 영어수업",
        value="""
        **A+**: 30%
        **A0**: 40%
        **B+**: 60%
        **B0**: 80%
        """,
        inline=False
    )

    # 주의사항 추가
    embed.add_field(
        name="⚠️ 주의사항",
        value="수업일수의 3분의 2 이상을 출석하여야 성적이 인정됩니다.",
        inline=False
    )

    # 메시지 전송
    await interaction.response.send_message(embed=embed)

@bot.slash_command(name="분과정보", description="분과별 동아리 정보를 보여줍니다.")
async def club_info(interaction: nextcord.Interaction):
    # 분과별 데이터
    pages = [
        {
            "title": "🎤공연분과",
            "clubs": [
                {"name": "IM(아이엠)", "room": "1학생회관 324", "purpose": "방송 댄스를 주로 추는 모임"},
                {"name": "그레이무드", "room": "1학생회관 327", "purpose": "밴드악기를 다루고 팀을 이루어 공연을 하는 모임"},
                {"name": "랩스타", "room": "1학생회관 323-1", "purpose": "힙합 음악을 작곡하고 공연하는 모임"},
                {"name": "세마치", "room": "1학생회관 326", "purpose": "락밴드음악을 정기 콘서트를 통해 발표하는 모임"},
                {"name": "소리사랑", "room": "1학생회관 325", "purpose": "어쿠스틱 보컬 음악을 지향하는 음악인의 모임"},
                {"name": "스누토", "room": "1학생회관 316", "purpose": "오케스트라 합주를 하는 모임"},
                {"name": "어울음", "room": "1학생회관 323", "purpose": "클래식 기타를 통한 정서함향과 친목을 도모하는 모임"},
                {"name": "어의실험극희", "room": "1학생회관 317", "purpose": "창조, 실험정신과 아름답고 신선한 연극을 위한 모임"},
                {"name": "열혈무군", "room": "1학생회관 328", "purpose": "스트리트 댄스를 통한 정신적, 신체적 건강을 지향하는 모임"},
                {"name": "통일아침", "room": "1학생회관 303", "purpose": "기타,베이스,드럼,키보드,미디 등 악기연주 및 밴드 동아리"}
            ],
        },
        {
            "title": "⚔️무예분과",
            "clubs": [
                {"name": "어의검우회", "room": "종합운동장 동아리방 15", "purpose": "검을 통해 도를 닦음으로서 인격수양을 하는 모임"},
                {"name": "유도", "room": "종합운동장 동아리방 14", "purpose": "유도를 통해 자신을 보호하고 체력과 정신력을 기르는 모임"},
                {"name": "어의궁", "room": "1학생회관 315", "purpose": "우리나라 전통 무예인 국궁에 관심있는 사람들이 모여 누구나 활을 배울 수 있는 동아리"},
                {"name": "태권도반", "room": "종합운동장 동아리방 16", "purpose": "태권도를 통해 심신수련과 인격도야를 목적으로 하는 모임"},
                {"name": "주토피아", "room": "1학생회관 202", "purpose": "상대방을 효과적으로 제압하고 자기 몸을 방어하는 주짓수를 하는 동아리"}
            ],
        },
        {
            "title": "🤝사회분과",
            "clubs": [
                {"name": "RCY", "room": "1학생회관 322-1", "purpose": "적십자 활동을 하는 모임"},
                {"name": "새앎터", "room": "1학생회관 305-1", "purpose": "빈민지역에서 활동하고 지역운동에 관여하는 모임"},
                {"name": "서고고", "room": "1학생회관 309", "purpose": "유기고양이 지원 및 동물권인식 확대 모임"}
            ],
        },
        {
            "title": "🎨전시분과",
            "clubs": [
                {"name": "MIST", "room": "1학생회관 312", "purpose": "영화를 사랑하는 학생들이 모여 영화를 제작하고 감상하는 모임"},
                {"name": "그림랑", "room": "1학생회관 311", "purpose": "미술 분야의 한 부분으로 만화를 그리는 모임"},
                {"name": "어의사진반", "room": "1학생회관 308", "purpose": "사진예술의 추구와 사진기술을 습득하는 모임"}
            ],
        },
        {
            "title": "🙏종교분과",
            "clubs": [
                {"name": "CAM", "room": "1학생회관 207", "purpose": "오순절 성령 체험을 통하여 복음을 전파하는 선교공동체 모임"},
                {"name": "CCC", "room": "1학생회관 305", "purpose": "한국대학생선교회, 복음을 전하며 신앙부흥 집회등을 하는 모임"},
                {"name": "I.V.F", "room": "1학생회관 310", "purpose": "한국기독학생회, 문서 사역을 통한 지성사회의 복음화 모임"},
                {"name": "로사리오", "room": "종합운동장 동아리방 11", "purpose": "가톨릭학생회, 성지순례 및 봉사활동으로 서로의 사랑을 나누는 모임"},
                {"name": "예수전도단", "room": "1학생회관 314", "purpose": "참다운 지성의 진리탐구를 향한 그리스도인의 배출을 목적으로 하는 모임"}
            ],
        },
        {
            "title": "⚽체육분과",
            "clubs": [
                {"name": "FC CTRL", "room": "종합운동장 동아리방 17", "purpose": "서울과기대 유일 중앙 축구동아리"},
                {"name": "KOBO(볼링)", "room": "1학생회관 205", "purpose": "볼링을 통한 회원간의 친목을 도모하는 모임"},
                {"name": "SPABA(농구동아리)", "room": "종합운동장 동아리방 3", "purpose": "농구를 통한 스포츠 정신을 함양하는 모임"},
                {"name": "STAB 배드민턴", "room": "1학생회관 227", "purpose": "배드민턴 동아리"},
                {"name": "STRC", "room": "종합운동장 동아리방 8", "purpose": "건강한 러닝 문화를 선도하고 함께 뛰는 즐거움을 나누는 모임"},
                {"name": "TABOTA", "room": "종합운동장 동아리방 9", "purpose": "다양한 보드를 통해 라이딩 하며 친목을 목적으로 한 동아리"},
                {"name": "느티나무 테니스", "room": "테니스장", "purpose": "테니스를 통한 체력증진을 위한 모임"},
                {"name": "보드카", "room": "종합운동장 동아리방 12", "purpose": "보드게임을 통해 친교를 다지는 모임"},
                {"name": "사격반", "room": "1학생회관 319", "purpose": "사격을 통한 심신을 단련하는 모임"},
                {"name": "수중탐사반", "room": "1학생회관 318", "purpose": "잠수기술을 배양하고 수중 자원보호 운동에 앞장서는 모임"},
                {"name": "히어로즈", "room": "1학생회관 216", "purpose": "야구를 통한 체력증진 및 타 대학과의 교류"},
                {"name": "전자오락단(E-sports)", "room": "1학생회관 202", "purpose": "상컴퓨터 게임을 즐기는 모임"},
                {"name": "스키부", "room": "1학생회관 206", "purpose": "겨울을 사랑하는 사람들이 겨울을 사랑하기 위해 모인 서울과학기술대학 스키팀"}
            ],
        },
        {
            "title": "📚학술분과",
            "clubs": [
                {"name": "ATST", "room": "1학생회관 219", "purpose": "소외된 계층 및 기술의 혜택을 받지 못하는 사람들의 삶의 질 향상에 기여할 수 있는 적정기술 개발을 목적을 하는 동아리"},
                {"name": "스트링", "room": "종합운동장 동아리방 5", "purpose": "장르를 가리지 않고 각자 원하는 작곡생활을 하는 모임"},
                {"name": "ECC (영어회화반)", "room": "1학생회관 218", "purpose": "영어 실력배양에 노력하는 모임"},
                {"name": "JCC (일본어회화반)", "room": "1학생회관 203", "purpose": "일본어 실력배양에 노력하는 모임"},
                {"name": "발명개발연구회", "room": "종합운동장 동아리방 7", "purpose": "발명풍토 조성과 지속적인 연구활동을 하는 모임"},
                {"name": "시리우스", "room": "1학생회관 313", "purpose": "밤하늘에 찬란하게 빛나는 별들을 관찰하는 모임"},
                {"name": "st book club", "room": "독서동아리", "purpose": "책이라는 매개체를 통해, 다양한 생각과 지식을 공유하고 나아가 친분을 쌓는 것을 목적으로 하는 동아리"},
                {"name": "푸른동산위전설의도토리군단","room": "","purpose": "환경을 주제로 소모임, 공모전, 대외활동, 견학, 환경 봉사활동 등의 학술활동을 하는 교내 유일 환경 동아리"},
                {"name": "인액터스","room": "","purpose": "사회 문제해결을 위해 비즈니스 프로젝트를 진행하는 창업동아리"}
            ]
        }
    ]

    # 현재 페이지를 관리할 변수
    current_page = 0

    # 페이지를 렌더링하는 함수
    def render_page(page_index):
        page = pages[page_index]
        embed = nextcord.Embed(
            title=f"{page['title']} 동아리 정보",
            description=f"{page['title']}에 속한 동아리 정보를 확인하세요!",
            color=nextcord.Color.blue(),
        )
        for club in page["clubs"]:
            embed.add_field(
                name=f"🔹 {club['name']}",
                value=f"**위치**: {club['room']}\n**목적**: {club['purpose']}",
                inline=False,
            )
        return embed

    # 버튼 콜백 함수 정의
    async def next_page_callback(interaction: nextcord.Interaction):
        nonlocal current_page
        current_page = (current_page + 1) % len(pages)
        embed = render_page(current_page)
        await interaction.response.edit_message(embed=embed, view=view)

    async def prev_page_callback(interaction: nextcord.Interaction):
        nonlocal current_page
        current_page = (current_page - 1) % len(pages)
        embed = render_page(current_page)
        await interaction.response.edit_message(embed=embed, view=view)

    # 버튼 생성
    next_button = Button(label="다음 분과", style=nextcord.ButtonStyle.primary)
    prev_button = Button(label="이전 분과", style=nextcord.ButtonStyle.secondary)

    # 버튼에 콜백 함수 연결
    next_button.callback = next_page_callback
    prev_button.callback = prev_page_callback

    # 버튼 뷰 생성
    view = View()
    view.add_item(prev_button)
    view.add_item(next_button)

    # 초기 페이지 표시
    embed = render_page(current_page)
    await interaction.response.send_message(embed=embed, view=view)

# 공지사항 크롤링 함수
def fetch_notices():
    url = "https://www.seoultech.ac.kr/service/info/notice/"  # 공지사항 URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    notices = []
    rows = soup.select("table tbody tr")  # 테이블 내의 모든 행 선택
    if not rows:
        print("⚠️ 테이블 행을 찾을 수 없습니다.")
        return []

    for i, row in enumerate(rows):
        # 행 0은 건너뜀
        if i == 0:
            continue

        try:
            columns = row.find_all("td")
            if len(columns) < 4:
                continue

            # 제목과 링크 처리
            title_cell = columns[1]
            title = title_cell.text.strip()
            link_tag = title_cell.find("a")
            absolute_link = urljoin(url, link_tag["href"]) if link_tag else "링크 없음"

            # 작성일과 부서 처리
            date = columns[4].text.strip()  # 작성일
            department = columns[3].text.strip()  # 부서

            notices.append({
                "번호": columns[0].text.strip(),
                "제목": title,
                "링크": absolute_link,
                "부서": department,
                "작성일": date
            })

            if len(notices) == 15:  # 최대 15개 공지사항만 가져옴
                break

        except Exception as e:
            print(f"⚠️ 행 {i} 처리 중 오류 발생: {e}")

    return notices

# 공지사항 슬래시 명령어
@bot.slash_command(name="공지사항", description="학교의 최신 공지사항을 보여줍니다.")
async def latest_notices(interaction: nextcord.Interaction):
    notices = fetch_notices()  # 공지사항 크롤링
    if not notices:
        await interaction.response.send_message("현재 공지사항을 가져올 수 없습니다.")
        return

    # 현재 페이지를 관리할 변수
    current_page = 0
    items_per_page = 5  # 페이지당 공지사항 개수
    total_pages = (len(notices) + items_per_page - 1) // items_per_page  # 총 페이지 수

    # 페이지 렌더링 함수
    def render_page(page_index):
        embed = nextcord.Embed(
            title=f"📢 공지사항 (페이지 {page_index + 1}/{total_pages})",
            description="서울과학기술대학교 공지사항입니다.",
            color=nextcord.Color.gold()
        )

        start = page_index * items_per_page
        end = start + items_per_page
        for notice in notices[start:end]:
            embed.add_field(
                name=f"{notice['제목']}",
                value=f"[자세히 보기]({notice['링크']})\n**부서**: {notice['부서']} | **작성일**: {notice['작성일']}",
                inline=False
            )

        return embed

    # 버튼 콜백 함수 정의
    async def next_page_callback(interaction: nextcord.Interaction):
        nonlocal current_page
        current_page = (current_page + 1) % total_pages  # 순환
        embed = render_page(current_page)
        await interaction.response.edit_message(embed=embed, view=view)

    async def prev_page_callback(interaction: nextcord.Interaction):
        nonlocal current_page
        current_page = (current_page - 1) % total_pages  # 순환
        embed = render_page(current_page)
        await interaction.response.edit_message(embed=embed, view=view)

    # 버튼 생성
    next_button = Button(label="다음 페이지", style=nextcord.ButtonStyle.primary)
    prev_button = Button(label="이전 페이지", style=nextcord.ButtonStyle.secondary)

    # 버튼에 콜백 함수 연결
    next_button.callback = next_page_callback
    prev_button.callback = prev_page_callback

    # 버튼 뷰 생성
    view = View()
    view.add_item(prev_button)
    view.add_item(next_button)

    # 첫 번째 페이지 표시
    embed = render_page(current_page)
    await interaction.response.send_message(embed=embed, view=view)

# 단과대학 및 학과 데이터 (학과별 교육 연계도 이미지 경로 포함)
college_data = {
    "공과대학": {
        "기계시스템디자인공학과": "이미지/기계시스템디자인공학과.jpg",
        "기계ㆍ자동차공학과": "이미지/기계자동차공학과.png",
        "안전공학과": "이미지/안전공학과.png",
        "신소재공학과": "이미지/신소재공학과.png",
        "건설시스템공학과": "이미지/건설시스템공학과.png",
        "건축학부(건축공학전공)": "이미지/건축공학전공.png",
        "건축학부(건축학전공)": "이미지/건축학전공.png",
        "[계약학과]건축기계설비공학과": "이미지/건축기계설비공학과.png",
    },
    "에너지바이오대학": {
        "화공생명공학과": "이미지/화공생명공학과.png",
        "환경공학과": "이미지/환경공학과.png",
        "식품생명공학과": "이미지/식품생명공학과.png",
        "정밀화학과": "이미지/정밀화학과.png",
        "스포츠과학과": "이미지/스포츠과학과.png",
        "안경광학과": "이미지/안경과학과.png",
    },
    "정보통신대학": {
        "컴퓨터공학과": "이미지/컴퓨터공학과.png",
        "전기정보공학과": "이미지/전기정보공학과.png",
        "전자공학과": "이미지/전자공학과.png",
        "스마트ICT융합공학과": "이미지/스마트ICT융합공학과.png",
    },
    "조형대학": {
        "디자인학과(산업디자인전공)": "이미지/산업디자인전공.png",
        "디자인학과(시각디자인전공)": "이미지/시각디자인전공.png",
        "도예학과": "이미지/도예학과.png",
        "금속공예디자인학과": "이미지/금속공예디자인학과.png",
        "조형예술학과": "이미지/조형예술학과.png",
    },
    "인문사회대학": {
        "영어영문학과": "이미지/영어영문학과.png",
        "행정학과": "이미지/행정학과.png",
        "문예창작학과": "이미지/문예창작학과.png",
    },
    "기술경영융합대학": {
        "산업정보시스템전공": "이미지/산업정보시스템전공.png",
        "ITM전공": "이미지/ITM.png",
        "MSDE학과": "이미지/MSDE.png",
        "경영학전공": "이미지/경영학전공.png",
        "글로벌테크노경영전공": "이미지/글로벌테크노경영전공.png",
    },
    "미래융합대학": {
        "융합기계공학과": "이미지/융합기계공학과.jpg",
        "건설환경융합공학과": "이미지/건설환경융합공학과.png",
        "헬스피트니스학과": "이미지/헬스피트니스학과.png",
        "영어과": "이미지/영어과.png",
        "벤처경영학과": "이미지/벤처경영학과.png",
        "정보통신융합공학과": "이미지/정보통신융합공학과.png",
    },
    "창의융합대학": {
        "인공지능응용학과": "이미지/인공지능응용학과.png",
        "지능형반도체공학과": "이미지/지능형반도체공학과.png",
        "미래에너지융합학과": "이미지/미래에너지융합학과.png",
    },
}

# 단과대학 명령어
@bot.slash_command(name="단과대학", description="단과대학과 학과 정보를 보여줍니다.")
async def college_info(interaction: nextcord.Interaction):
    # 선택 메뉴 생성
    options = [
        nextcord.SelectOption(label=college, description=f"{college}의 학과를 확인합니다.")
        for college in college_data.keys()
    ]
 
    select_menu = Select(placeholder="단과대학을 선택하세요", options=options)

    async def select_college_callback(interaction: nextcord.Interaction):
        selected_college = select_menu.values[0]
        departments = college_data[selected_college]

        # 학과 선택 메뉴 생성
        department_options = [
            nextcord.SelectOption(label=dept, description=f"{dept}의 교육 연계도를 확인합니다.")
            for dept in departments.keys()
        ]
        department_select_menu = Select(
            placeholder="학과를 선택하세요", options=department_options
        )

        async def select_department_callback(interaction: nextcord.Interaction):
            selected_department = department_select_menu.values[0]
            image_path = departments[selected_department]

            if os.path.exists(image_path):
                file = nextcord.File(image_path, filename=os.path.basename(image_path))
                await interaction.response.send_message(
                    content=f"**{selected_department}**의 교육 연계도입니다:",
                    file=file
                )
            else:
                await interaction.response.send_message(
                    content=f"**{selected_department}**의 교육 연계도를 찾을 수 없습니다."
                )

        department_select_menu.callback = select_department_callback

        # 학과 선택 뷰 생성
        department_view = View()
        department_view.add_item(department_select_menu)

        await interaction.response.send_message(
            content=f"**{selected_college}**의 학과를 선택하세요.", view=department_view
        )

    select_menu.callback = select_college_callback

    # 단과대학 선택 뷰 생성
    view = View()
    view.add_item(select_menu)

    # 초기 메시지 전송
    embed = nextcord.Embed(
        title="단과대학 정보",
        description="단과대학을 선택하면 해당 학과와 교육 연계도를 확인할 수 있습니다.",
        color=nextcord.Color.green()
    )
    await interaction.response.send_message(embed=embed, view=view)

# 봇 실행
# ""안에 자신의 토큰 집어넣기
bot.run("your token number")
