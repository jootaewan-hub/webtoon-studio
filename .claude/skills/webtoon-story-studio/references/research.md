# 리서치와 도구 라우팅

환경마다 연결된 도구가 다르다. 아래 표의 '도구'는 찾아볼 이름이고, 실제 이름은 세션의 도구 목록에서 확인한다. 이 스킬은 어떤 도구도 필수로 요구하지 않는다. 없으면 오른쪽 대체 수단으로 간다.

## 도구 찾는 순서
1. 현재 도구 목록에서 이름으로 찾는다.
2. 지연 로딩 도구가 있는 환경이면 도구 검색(ToolSearch)에 키워드로 묻는다. 예: `"image search"`, `"figma generate image"`, `"canva generate"`, `"adobe font"`, `"pubmed"`, `"exa search"`. 한 번에 필요한 것을 묶어서 로드한다.
3. 필요한데 연결돼 있지 않으면 커넥터 레지스트리 검색(SearchMcpRegistry)으로 찾아 연결 제안(SuggestConnectors)을 한 번만 하고, 기다리지 말고 대체 수단으로 진행한다.
4. 조직 플러그인이 있을 법한 작업(사내 스타일 가이드 등)은 플러그인 검색(SearchPlugins)을 한 번 해 본다.
5. 스킬이 붙은 플러그인 도구(예: Adobe, Figma, Canva)는 그 플러그인 스킬이 '먼저 읽으라'고 하면 반드시 먼저 읽는다(예: Figma는 figma-use, Adobe는 초기화 도구).

## 필요별 라우팅

| 필요 | 1순위 도구 | 대체 |
|---|---|---|
| 시대·장소·제도 고증 (예: 1990년대 병원 호출 체계, 법정 관행) | WebSearch → WebFetch로 원문 확인 | nimble:search, exa:search, brightdata search |
| 넓고 깊은 주제 조사 (여러 하위 질문) | deep-research 스킬, exa:exa-agent, brightdata live-research | 서브에이전트에 질문을 나눠 WebSearch |
| 의학·과학 사실 (질환·수술·약물·응급 처치) | PubMed, Consensus, Clinical Trials | WebSearch(학회·정부 기관 사이트 우선) |
| 법률·제도 (형량, 면허 취소·재교부, 재판 절차) | WebSearch(법령정보센터·법원·언론), WebFetch | 확인 안 되면 '미확인' 표기 |
| 날짜·요일·명절 | 코드로 계산(파이썬 datetime) + 명절은 공식 달력(정부 공휴일 발표) | 계산 결과를 연표에 적고 확인 날짜를 남김 |
| 지역 말투·사투리 | WebSearch(방언 사전·언론 기사) | 원문 표기를 그대로 살림 |
| 시각 고증 (건물·소품·복식·차량) | 이미지 검색 도구, Adobe Stock 검색(asset_search) | WebSearch 결과의 사진 페이지 링크 |
| 장르 관습·연출 레퍼런스 | WebSearch(작법서·인터뷰·평론) | 내부 지식, 단 출처 없음을 표시 |
| 장소 실측 (거리, 동선, 지명) | 지도·장소 검색 도구 | WebSearch |
| 사용자 기존 자료 | Google Drive, Box, Slack, Gmail 등 연결된 저장소 | 사용자에게 업로드 요청 |

## 시각 도구 (아트 디렉션·스케치 단계)

| 필요 | 도구 | 비고 |
|---|---|---|
| 무드보드·레퍼런스 보드 | Figma(FigJam 보드), Adobe Firefly 보드(create_firefly_board), Canva | 없으면 studio.py board HTML |
| 키 아트·캐릭터 이미지 생성 | Figma generate_image, Canva generate-image, 기타 연결된 이미지 생성 도구 | 외형 고정값+스타일 확정안으로 프롬프트. 실존 인물 닮음 금지 |
| 이미지 편집 (배경 제거, 리사이즈, 톤 맞추기) | Adobe 이미지 도구, Canva remove-background | |
| 웹툰 레터링 폰트 | Adobe Fonts(font_search·font_recommend) | Google Fonts |
| 디자인 시스템·말풍선 컴포넌트 | Figma | HTML 보드 |
| 피치덱·기획서 | Gamma, 슬라이드 아티팩트 | Markdown → docx |
| 애니매틱·쇼츠 시안 | HyperFrames, Adobe 영상 도구 | 킷의 ffmpeg 러프컷 스크립트 |

이미지 검색과 생성에서 하지 않는 것: 저작권 캐릭터·영화/드라마 스틸·특정 작가 작품 검색, 실존 인물 사진을 얼굴 레퍼런스로 쓰기, 성적이거나 잔혹한 이미지.

## 고증 노트 형식 (`research/notes.md`)

| 항목 | 확인 내용 | 출처 | 작품 반영 |
|---|---|---|---|
| 1990년대 병원 연락 수단 | 삐삐(무선호출기)와 유선전화. 개인 휴대폰은 1990년대 후반 보급 | [링크] | 삐삐 숫자 암호를 플롯 장치로 사용 |
| 한국 법정 법봉 | 1966년 이후 사용하지 않음 | [링크] | 드라마 관습에 따라 판사봉 연출 (의도적 각색, 연출 메모에 표시) |

- 출처가 없으면 '미확인'. 내부 지식으로 쓴 것은 '출처 없음(내부 지식)'.
- 작품에서 고증과 다르게 가는 결정은 반드시 '작품 반영' 칸에 '의도적 각색'으로 적는다.

## 병렬화
독립된 조사 항목이 5개 이상이면 서브에이전트에 2~4개씩 나눠 맡긴다. 각 에이전트에게 위 표 형식, 출처 링크 필수, 확인 못 하면 '미확인' 규칙을 같이 준다.
