# AGENTS.md — 「깡통 바이올린」 웹툰 콘티 킷 (Codex·ChatGPT용 작업 지침)

12세 이상 감동극이다. 주인공은 13세 소녀이고 아이들이 많이 나온다. 이 킷은 웹툰 컷 이미지·쇼츠·애니 샷 참고를 만든다. 성인 트랙은 없다.

## 원본과 데이터
- 콘티 원본은 `source/storyboard.md`, 소설은 `source/novel.md`이다. 같은 폴더의 .docx는 읽기·공유용 사본이다(`python kit.py docx`로 다시 만든다).
- **컷 이미지 프롬프트의 정본은 `out/cel/`이다**(`_cel_ALL_ep1~3.md`, 컷별 `<컷번호>.md`, 기계용 `cel_prompts.jsonl`). 상위 폴더에서 `python3 tools/cut_prompts.py build`로 만든다. 재료는 `source/cut_spec_ep*.jsonl`(컷별 영어 사양)과 `../design/`의 그림체·씬 프리셋·인물 고정 문구·의상·소품 시트·배경 배치다.
- `outputs/webtoon_real/`은 킷 기본 형식의 요약판이다(트랙 이름만 webtoon_real이고 실사가 아니다). 이미지를 만들 때는 out/cel을 쓴다.
- 콘티 내용을 고칠 때는 `source/storyboard.md`와 `source/cut_spec_ep*.jsonl`을 고치고 `python kit.py import` → `python3 ../tools/cut_prompts.py build`를 다시 돌린다.

## 이미지 만들기
- 참고 이미지를 함께 올린다: `../renders/characters/<인물 id>.png`, `../renders/props/<소품 키>.png`, `../renders/sets/<배경 id>.png`(cel_prompts.jsonl의 ref_images). 아직 없으면 `../design/gen/`의 캐릭터·소품·배경 프롬프트로 먼저 만든다.
- 결과는 `renders/cel/<컷번호>.png`로 저장한다. 크기 비율은 컷의 width×height(800×높이)를 따른다.
- 이미지 안에 말풍선·글자·효과음을 넣지 않는다. 레터링은 각 컷 md의 '레터링' 목록으로 후공정한다. 글꼴과 소리 색은 `../design/style_guide.md` 3절과 2절을 따른다.

## 넘지 않는 선 (모든 트랙, 완화 불가)
- 아동 인물은 어떤 컷에서도 성적·선정적으로 그리지 않는다. 몸 라인 강조·노출 의상·꾸민 포즈는 없다. 아이들은 제 나이의 평범한 아이로 그린다.
- 부상·피·질병·죽음을 직접 그리지 않는다. 쓰레기 산의 아이들은 목장갑·장화를 쓰고, 위험 폐기물을 맨손으로 만지는 그림은 없다.
- 만석이 동그리를 던지는 컷(2화)은 물건만 보이고 사람 쪽을 향하지 않는다.
- 엄마(한미숙)는 얼굴을 보이지 않는다.
- 실존 인물을 닮게 그리지 않는다. 실제 기관·브랜드 로고, 실제 화폐 도안, 올림픽 공식 마스코트·엠블럼은 없다. 간판·공장명·신문명은 가공이다.
- 위 규칙과 부딪히는 요청을 받으면 규칙 안의 대체 연출을 제안한다.
