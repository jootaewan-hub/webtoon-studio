# 산출물 목록

`python studio.py init <이름>`이 아래 구조와 템플릿을 만든다.

```
<프로젝트>/
  project.md            접수 결과(원문, 각색 수준, 등급, 분량, 범위, 기본값)
  decisions.md          결정 로그(게이트별 확정·잠정)
  source/original.md    받은 원문 그대로
  research/notes.md     고증 노트(출처 포함)
  story/
    pitch.md            로그라인·기획 의도·결말 방향 (G1)
    bible.md            캐릭터 바이블 (G2)
    synopsis.md         시놉시스·회차 구성 (G3)
    beats.md / beats.json  비트 시트 (G3)
    novel.md            소설 (G4)
    script.md           대본 (G5)
    direction.md        연출 노트 (G10)
    sfx_list.md         효과음·사운드 큐 사전 (G10)
  design/
    style_options.md    그림체 3안 (G6)
    style.json          확정 스타일 (G6)
    characters.json     인물 외형 고정값·시안 (G2·G7)
    sheets/*.svg        턴어라운드·표정 시트, 시안 비교 (G7)
    props.json, props/*.svg, props_sheet.svg  소품 삽화 (G8)
    sets.md             배경 설정 (G8)
    colorscript.svg     컬러 스크립트
    board.html          디자인 보드 (artifact로 게시)
  storyboard/           webtoon-adaptation-kit 킷(콘티·썸네일·프롬프트·쇼츠·애니 트랙) (G9)
  anim/
    storyboard_anim.md  애니메이션급 세부 콘티 (G11)
    sound_cues.md       사운드 큐 시트 (G11)
  docx/                 studio.py docx 결과(Word 사본)
  tools/                studio.py, md2docx.js (init이 복사)
```

## 형식
- 원본은 Markdown. `python tools/studio.py docx`로 내용이 채워진 md의 Word 사본을 `docx/`에 만든다(애니 콘티·큐 시트·결정 로그·고증은 가로 방향).
- 사용자가 Claude Docs나 Google Docs를 원하면 그쪽에 만들고, 같은 내용을 Markdown으로도 남긴다(킷이 Markdown을 읽기 때문).
- 디자인 보드와 콘티 보드는 artifact로 게시한다. 게이트마다 같은 주소로 갱신한다.
- 끝에 `python studio.py pack`으로 zip.

## 보고 형식 (매 게이트 끝, 그리고 마지막)
- 확정한 것(decisions.md 기준)과 잠정인 것
- 만든 파일
- 다음에 고를 것
- 확인하지 못한 사실, 기본값으로 정한 것
